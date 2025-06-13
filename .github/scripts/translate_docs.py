import os
import hashlib
import logging
import shutil
import subprocess
import time
from pathlib import Path
import sys # 新增导入
import json # 新增导入
from google import genai
from google.genai import types
import openai
import frontmatter
import re # 新增导入

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_file_hash(file_path):
    """
    计算文件的MD5哈希值。
    用于检查文件内容是否发生变化，避免不必要的写入操作。
    """
    if not os.path.exists(file_path):
        logging.debug(f"File not found for hash calculation: {file_path}")
        return None
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
            return hashlib.md5(file_content).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for {file_path}: {e}")
        return None

def run_git_command(command):
    """
    执行git命令并返回输出。
    封装subprocess.run，处理常见的错误并记录日志。
    """
    try:
        # 确保命令是列表形式，以便subprocess.run正确处理
        cmd_list = command if isinstance(command, list) else command.split()
        result = subprocess.run(
            cmd_list,
            capture_output=True,
            text=True,
            check=True,
            shell=False, # 避免shell注入风险，直接传递列表
            encoding='utf-8'
        )
        # 记录执行的Git命令，避免记录敏感信息或过长的输出
        logging.debug(f"Executing git command: {' '.join(cmd_list)}")
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        logging.error(f"Git command failed with exit code {e.returncode}. Command: {e.cmd}")
        logging.error(f"Git Stderr: {e.stderr.strip()}")
        # 仅在调试模式下打印 stdout，避免生产环境日志冗余
        logging.debug(f"Git Stdout: {e.stdout.strip()}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error running git command: {e}")
        return []

def get_changed_files():
    """
    获取自上次提交以来发生更改的Markdown和GitBook相关文件。
    根据GitHub Actions事件类型和用户提供的git命令获取文件列表。
    同时处理文件的添加、修改和删除。
    """
    files_to_process = set()
    files_to_delete = set()
    event_name = os.environ.get('GITHUB_EVENT_NAME')
    
    logging.info(f"Workflow triggered by event: '{event_name}'")

    if event_name == 'workflow_dispatch':
        logging.info("Workflow manually triggered. Performing a full repository scan for relevant files.")
        files_to_process.update(_get_all_relevant_files())
        logging.info(f"Found {len(files_to_process)} files for processing during workflow_dispatch.")

    elif event_name == 'push':
        logging.info("Workflow triggered by push event. Determining changed files using git diff.")
        
        before_sha = os.environ.get('PUSH_BEFORE_SHA')
        current_sha = os.environ.get('PUSH_AFTER_SHA')

        if not before_sha or not current_sha:
            logging.error("GITHUB_EVENT_BEFORE or GITHUB_SHA environment variables not found for push event. This might indicate a shallow clone or an unusual push event.")
            logging.warning("Falling back to full repository scan for relevant files. This may increase processing time.")
            files_to_process.update(_get_all_relevant_files())
            return files_to_process, files_to_delete

        logging.info(f"Push event details: before_sha={before_sha}, current_sha={current_sha}")

        if before_sha == "0000000000000000000000000000000000000000":
            logging.info("This is the first push to the branch. Listing all relevant files in HEAD.")
            raw_output = run_git_command("git ls-tree --name-only -r HEAD")
            logging.info(f"Git ls-tree command returned {len(raw_output)} lines.")
        else:
            logging.info(f"Comparing changes between {before_sha} and {current_sha} using git diff --name-status.")
            raw_output = run_git_command(f"git diff --name-status {before_sha} {current_sha}")
            logging.info(f"Git diff command returned {len(raw_output)} lines.")
        
        for line in raw_output:
            parts = line.strip().split('\t')
            if len(parts) < 2:
                logging.debug(f"Skipping malformed git diff line: {line}")
                continue
            status = parts[0]
            file_path_str = parts[1]
            
            if file_path_str.endswith('.md') or '.gitbook/' in file_path_str:
                file_path = Path(file_path_str)
                if status == 'D':
                    files_to_delete.add(file_path)
                    logging.info(f"Identified for deletion: {file_path}")
                else: # A (Added), M (Modified), R (Renamed), C (Copied)
                    files_to_process.add(file_path)
                    logging.info(f"Identified for processing (added/modified): {file_path}")
    else:
        logging.warning(f"Unsupported event type: '{event_name}'. Falling back to full repository scan.")
        files_to_process.update(_get_all_relevant_files())
        logging.info(f"Found {len(files_to_process)} files for processing after unsupported event fallback.")

    # 过滤掉i18n目录下的文件，因为它们是翻译目标，不是源文件
    files_to_process = {f for f in files_to_process if not str(f).startswith('i18n/')}
    files_to_delete = {f for f in files_to_delete if not str(f).startswith('i18n/')}
    
    logging.info(f"Final list of {len(files_to_process)} files to process (after i18n filter): {files_to_process}")
    logging.info(f"Final list of {len(files_to_delete)} files to delete (after i18n filter): {files_to_delete}")
    
    return files_to_process, files_to_delete

def _get_all_relevant_files():
    """
    扫描整个仓库，获取所有相关的Markdown和GitBook文件。
    """
    relevant_files = set()
    base_path = Path('.')
    for root, _, files in os.walk(base_path):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix == '.md' or '.gitbook' in str(file_path):
                relevant_files.add(file_path)
    return relevant_files

# 配置API密钥
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY')

if not GEMINI_API_KEY:
    logging.error("GEMINI_API_KEY environment variable not found. Please set it.")
    exit(1)
if not DEEPSEEK_API_KEY:
    logging.error("DEEPSEEK_API_KEY environment variable not found. Please set it.")
    exit(1)

# 系统提示词
SYSTEM_INSTRUCTIONS = """
You are a professional document translation assistant specialized in GitHub content. Your task is to fluently translate Chinese documents into the target language.

## Translation Rules:
1.  **Translate only the textual content that will be displayed to the user.**
2.  **Strictly preserve all Markdown formatting and structural elements:** This includes headings (#), lists (-, *, +), code blocks (```), blockquotes (>), bold (**), italics (*), links ([text](link)), images (![alt text](image path)), tables, etc. The Markdown syntax itself should NOT be translated.
3.  **Translate comments within code blocks:** For example, comments inside code blocks (```) should be translated, as they are intended for user understanding and guidance. However, the code, commands, file names, URLs, version numbers, and other technical syntax within code blocks or other parts of the document should remain untranslated.
4.  **Preserve links and image paths unchanged:** For instance, `cherrystudio/preview/chat.md` in `[对话界面](cherrystudio/preview/chat.md)` and the image path in `![alt text](image path)` should not be translated or modified.
5.  **Maintain GitBook-style hint block structure:** Content within `{% hint style="warning" %}` and `{% endhint %}` tags needs to be translated, but the tags themselves must remain unchanged.
6.  **Keep Frontmatter (YAML header) content unchanged:** For example, the `--- icon: cherries ---` section should not be translated or modified.
7.  **Do not add any extra explanations, prefaces, postscripts, or summaries.** Return only the translated document content.
8.  **For table of contents files (e.g., SUMMARY.md), translate only the title names, keeping links unchanged.**
9.  **Preserve all GitHub-specific terminology** (e.g., pull request, fork, commit, repository) in its original form.
10. **Preserve all URLs, file paths, and version numbers** exactly as in the original.
11. **Maintain the original document structure and paragraph breaks.**
"""

# 警告语模板
WARNING_HINT_TEMPLATE = """
{% hint style="warning" %}
（警告语）
{% endhint %}
"""

# 目标语言配置
LANG_CONFIG = {
    "en": {
        "dir": "english",
        "name": "English",
        "model": "gemini",
        "warning_text": "This document was translated from Chinese by AI and has not yet been reviewed."
    },
    "es": {
        "dir": "spanish",
        "name": "Spanish",
        "model": "deepseek",
        "warning_text": "Este documento ha sido traducido del chino por IA y aún no ha sido revisado."
    },
    "fr": {
        "dir": "french",
        "name": "French",
        "model": "deepseek",
        "warning_text": "Ce document a été traducido del chino por IA y aún no ha sido revisado."
    },
    "de": {
        "dir": "german",
        "name": "German",
        "model": "deepseek",
        "warning_text": "Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden."
    },
    "ja": {
        "dir": "japanese",
        "name": "Japanese",
        "model": "deepseek",
        "warning_text": "このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。"
    },
    "ko": {
        "dir": "korean",
        "name": "Korean",
        "model": "deepseek",
        "warning_text": "이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。"
    },
    "ru": {
        "dir": "russian",
        "name": "Russian",
        "model": "deepseek",
        "warning_text": "Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен."
    },
    "pt": {
        "dir": "portuguese",
        "name": "Portuguese",
        "model": "deepseek",
        "warning_text": "Este documento foi traduzido do chinês por IA e ainda não foi revisado."
    },
    "it": {
        "dir": "italian",
        "name": "Italian",
        "model": "deepseek",
        "warning_text": "Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato."
    },
    "ar": {
        "dir": "arabic",
        "name": "Arabic",
        "model": "deepseek",
        "warning_text": "تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد."
    },
    "hi": {
        "dir": "hindi",
        "name": "Hindi",
        "model": "deepseek",
        "warning_text": "यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।"
    },
    "bn": {
        "dir": "bengali",
        "name": "Bengali",
        "model": "deepseek",
        "warning_text": "এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।"
    },
    "id": {
        "dir": "indonesian",
        "name": "Indonesian",
        "model": "deepseek",
        "warning_text": "Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau."
    },
    "th": {
        "dir": "thai",
        "name": "Thai",
        "model": "deepseek",
        "warning_text": "เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ"
    },
    "vi": {
        "dir": "vietnamese",
        "name": "Vietnamese",
        "model": "deepseek",
        "warning_text": "Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét."
    },
    "tr": {
        "dir": "turkish",
        "name": "Turkish",
        "model": "deepseek",
        "warning_text": "Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir."
    },
    "pl": {
        "dir": "polish",
        "name": "Polish",
        "model": "deepseek",
        "warning_text": "Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany."
    },
    "nl": {
        "dir": "dutch",
        "name": "Dutch",
        "model": "deepseek",
        "warning_text": "Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld."
    },
    "zh-tw": {
        "dir": "traditional-chinese",
        "name": "繁體中文",
        "model": "deepseek",
        "warning_text": "此文件由 AI 從中文翻譯而來，尚未經過審閱。"
    }
}
# 示例中文 README.md 内容，用于 Few-shot 翻译
EXAMPLE_CHINESE_README = """---
icon: cherries
---

# 项目简介

{% hint style="warning" %}
此文档由中文AI翻译而来，目前暂未经过审核。
我会尽量逐一查看文档，检查翻译是否合理。
{% endhint %}

<figure><img src=".gitbook/assets/docs-readme-banner1.png" alt=""><figcaption></figcaption></figure>

Cherry Studio 是一款集多模型对话、知识库管理、AI 绘画、翻译等功能于一体的全能 AI 助手平台。

### Star History

![Star History](https://urlscan.io/liveshot/?width=1300&height=620&url=https://cherrystarhistory.ocool.online/)

## 关注我们的社交账号

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">小红书</a></td><td><a href=".gitbook/assets/1.png">1.png</a></td><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link</a></td></tr></tbody></table>
"""

# 示例英文 README.md 翻译，用于 Few-shot 翻译
EXAMPLE_ENGLISH_README = """---
icon: cherries
---

{% hint style="warning" %}
This document is translated from Chinese by AI and has not yet been reviewed. I will try to check the document one by one to ensure the translation is reasonable.
{% endhint %}

# Project Introduction

<figure><img src=".gitbook/assets/docs-readme-banner1.png" alt=""><figcaption></figcaption></figure>

Cherry Studio is an all-in-one AI assistant platform integrating multi-model conversations, knowledge base management, AI painting, translation, and more.

### Star History

![Star History](https://urlscan.io/liveshot/?width=1300&height=620&url=https://cherrystarhistory.ocool.online/)

## Follow Our Social Accounts

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">Xiaohongshu</a></td><td><a href=".gitbook/assets/1.png">1.png</a></td><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link</a></td></tr></tbody></table>
"""

def translate_text(text, target_lang_code):
    """
    调用Gemini或DeepSeek API翻译文本。
    """
    if not text.strip():
        return ""

    lang_config = LANG_CONFIG.get(target_lang_code)
    if not lang_config:
        logging.error(f"Unsupported target language code: {target_lang_code}")
        return None

    target_language_name = lang_config["name"]
    model_type = lang_config["model"]

    # 精简后的 README.md 中文原文（作为示例输入）
    # 精简后的 README.md 英文翻译（作为示例输出）

    if model_type == "gemini":
        client = genai.Client(
            api_key=GEMINI_API_KEY,
            http_options={"base_url": "https://aihubmix.com/gemini"},
        )
        model_name = "gemini-2.5-pro-preview-06-05"

        contents = [
            types.Content(role="user", parts=[types.Part.from_text(text=f"请将以下中文内容翻译成English：\n\n{EXAMPLE_CHINESE_README}")]),
            types.Content(role="model", parts=[types.Part.from_text(text=EXAMPLE_ENGLISH_README)]),
            types.Content(role="user", parts=[types.Part.from_text(text=f"请将以下中文内容翻译成{target_language_name}：\n\n{text}")]),
        ]

        generate_content_config = types.GenerateContentConfig(
            temperature=1,
            candidate_count=1,
            response_mime_type="text/plain",
            system_instruction=[types.Part.from_text(text=SYSTEM_INSTRUCTIONS)],
            safety_settings=[
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ]
        )

        translated_content_parts = []
        try:
            for chunk in client.models.generate_content_stream(
                model=model_name,
                contents=contents,
                config=generate_content_config,
            ):
                translated_content_parts.append(chunk.text)
            translated_content = "".join(translated_content_parts)
            return translated_content
        except Exception as e:
            logging.error(f"Error translating text with Gemini: {e}")
            return None

    elif model_type == "deepseek":
        client = openai.OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url="https://api.ppinfra.com/v3/openai",
        )
        model_name = "deepseek/deepseek-r1-0528"

        messages = [
            {"role": "system", "content": SYSTEM_INSTRUCTIONS},
            {"role": "user", "content": f"请将以下中文内容翻译成English：\n\n{EXAMPLE_CHINESE_README}"},
            {"role": "assistant", "content": EXAMPLE_ENGLISH_README},
            {"role": "user", "content": f"请将以下中文内容翻译成{target_language_name}：\n\n{text}"}
        ]

        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=1,
                stream=True,
            )
            translated_content_parts = []
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    translated_content_parts.append(chunk.choices[0].delta.content)
            
            translated_content = "".join(translated_content_parts)
            
            # 使用正则表达式移除 <think>...</think> 标签及其内容
            # re.DOTALL 允许 . 匹配换行符
            translated_content = re.sub(r'<think>.*?</think>', '', translated_content, flags=re.DOTALL)
            
            translated_content = translated_content.strip() # 移除首尾空白，包括可能的换行
            return translated_content
        except Exception as e:
            logging.error(f"Error translating text with DeepSeek: {e}")
            return None
    else:
        logging.error(f"Unknown model type: {model_type} for language {target_lang_code}")
        return None

def process_markdown_file(source_path, target_lang_code):
    """
    处理Markdown文件，进行翻译并保存。
    """
    logging.info(f"Attempting to translate Markdown file: {source_path}")
    logging.info(f"Target language code: {target_lang_code}")
    
    target_dir = Path('i18n') / LANG_CONFIG[target_lang_code]["dir"]
    target_path = target_dir / source_path
    logging.info(f"Target path for translated file: {target_path}")

    os.makedirs(target_path.parent, exist_ok=True)

    try:
        logging.info(f"Reading source file: {source_path}")
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        logging.info(f"Successfully read {len(content)} characters from {source_path}.")

        # 解析frontmatter（YAML头部）和Markdown内容
        post = frontmatter.loads(content)
        markdown_content = post.content
        frontmatter_data = post.metadata

        # 根据目标语言配置添加警告语
        warning_hint = WARNING_HINT_TEMPLATE.replace("（警告语）", LANG_CONFIG[target_lang_code]["warning_text"])
        
        # 调用Gemini API翻译Markdown内容
        logging.info(f"Calling translate_text for {source_path} to {target_lang_code}")
        translated_markdown_content = translate_text(markdown_content, target_lang_code)
        if translated_markdown_content is None:
            logging.error(f"Failed to translate content for '{source_path}' to '{LANG_CONFIG[target_lang_code]['name']}'. Skipping this file.")
            return False
        logging.info(f"Translation successful for {source_path}. Translated content length: {len(translated_markdown_content)}.")

        # 重新组合frontmatter和翻译后的内容
        final_content = ""
        if frontmatter_data:
            final_content += "---\n"
            for key, value in frontmatter_data.items():
                final_content += f"{key}: {value}\n"
            final_content += "---\n"
        
        # 将警告语插入到frontmatter之后，翻译内容之前
        final_content += warning_hint + "\n" + translated_markdown_content

        # 检查文件是否实际有变化，避免不必要的Git提交
        current_hash = get_file_hash(target_path)
        new_hash = hashlib.md5(final_content.encode('utf-8')).hexdigest()
        logging.info(f"Comparing hashes for {target_path}: current={current_hash}, new={new_hash}")

        if current_hash == new_hash:
            logging.info(f"No content changes detected for {target_path}. Skipping file write.")
            return False
        else:
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            logging.info(f"Successfully translated and saved: '{target_path}'. Hash changed from {current_hash} to {new_hash}.")
            return True

    except Exception as e:
        logging.error(f"An unexpected error occurred while processing {source_path}: {e}")
        return False

def sync_gitbook_assets(target_lang_code):
    """
    同步.gitbook/assets/目录下的图片和其他资产到i18n对应语言目录。
    此函数会检查文件哈希值，只复制发生变化的文件，以优化性能和Git历史。
    返回 True 表示成功，False 表示失败。
    """
    logging.info(f"Starting asset synchronization for '.gitbook/assets/' to '{LANG_CONFIG[target_lang_code]['dir']}' directory.")
    source_assets_dir = Path('.gitbook') / 'assets'
    target_assets_dir = Path('i18n') / LANG_CONFIG[target_lang_code]["dir"] / '.gitbook' / 'assets'
    
    sync_success = True # 新增：跟踪同步状态

    if not source_assets_dir.exists():
        logging.warning(f"Source assets directory not found: '{source_assets_dir}'. Skipping asset synchronization.")
        return sync_success # 此时仍为 True，因为没有需要同步的源

    # 确保目标目录存在，如果不存在则创建
    try:
        os.makedirs(target_assets_dir, exist_ok=True)
    except Exception as e:
        logging.error(f"Error creating target assets directory '{target_assets_dir}': {e}")
        return False # 创建目录失败

    # 遍历源目录下的所有文件和子目录
    for item in os.listdir(source_assets_dir):
        s = source_assets_dir / item
        d = target_assets_dir / item
        try:
            if s.is_file():
                # 检查文件哈希值，如果不同则复制
                current_hash = get_file_hash(d)
                source_hash = get_file_hash(s)
                if current_hash != source_hash:
                    shutil.copy2(s, d)
                    logging.info(f"Copied asset: '{s}' to '{d}'")
                else:
                    logging.debug(f"Asset unchanged: {s}")
            elif s.is_dir():
                # 递归复制目录，逐个文件同步，避免不必要的Git历史更改
                logging.info(f"Recursively syncing directory: '{s}' to '{d}'.")
                for root, _, files in os.walk(s):
                    for file in files:
                        source_file_path = Path(root) / file
                        relative_file_path = source_file_path.relative_to(source_assets_dir)
                        target_file_path = target_assets_dir / relative_file_path
                        
                        # 确保目标子目录存在
                        os.makedirs(target_file_path.parent, exist_ok=True)
                        
                        current_hash = get_file_hash(target_file_path)
                        source_hash = get_file_hash(source_file_path)
                        if current_hash != source_hash:
                            shutil.copy2(source_file_path, target_file_path)
                            logging.info(f"Copied asset: '{source_file_path}' to '{target_file_path}'.")
                        else:
                            logging.debug(f"Asset unchanged: '{source_file_path}'.")
        except Exception as e:
            logging.error(f"Error syncing asset '{s}' to '{d}': {e}")
            sync_success = False # 任何一个文件同步失败都算失败
    return sync_success

def main():
    """
    主函数：协调文件更改检测、翻译和资产同步。
    """
    # 从命令行参数获取语言代码
    if len(sys.argv) < 2:
        logging.error("Usage: python translate_docs.py <language_code>")
        exit(1)
    
    target_lang_code = sys.argv[1]
    if target_lang_code not in LANG_CONFIG:
        logging.error(f"Unsupported language code provided: {target_lang_code}")
        exit(1)

    overall_translation_status = True # 新增：跟踪当前语言的整体翻译状态
    
    files_to_process, files_to_delete = get_changed_files()
    logging.info(f"Files identified for processing: {files_to_process}")
    logging.info(f"Files identified for deletion: {files_to_delete}")
    
    md_files_to_translate = {f for f in files_to_process if f.suffix == '.md'}
    gitbook_assets_to_sync = {f for f in files_to_process if '.gitbook' in str(f) and f.suffix != '.md'}
    logging.info(f"Markdown files to translate: {md_files_to_translate}")
    logging.info(f"GitBook assets to sync: {gitbook_assets_to_sync}")
    gitbook_dirs_to_delete = {f for f in files_to_delete if '.gitbook' in str(f) and f.is_dir()}
    logging.info(f"GitBook directories to delete: {gitbook_dirs_to_delete}")
    
    # 只处理当前 matrix job 对应的语言
    lang_code = target_lang_code
    config = LANG_CONFIG[lang_code]

    logging.info(f"--- Initiating translation and synchronization process for language: '{config['name']}' ({lang_code}) ---")
    
    target_lang_dir = Path('i18n') / config["dir"]

    # 处理需要删除的文件和目录
    if files_to_delete:
        logging.info(f"Processing {len(files_to_delete)} files/directories marked for deletion for language '{lang_code}'.")
    for deleted_file_path in files_to_delete:
        target_path = target_lang_dir / deleted_file_path
        logging.info(f"Attempting to delete: '{target_path}'")
        if target_path.exists():
            try:
                if target_path.is_file():
                    os.remove(target_path)
                    logging.info(f"Successfully deleted translated file: '{target_path}'.")
                elif target_path.is_dir():
                    shutil.rmtree(target_path)
                    logging.info(f"Successfully deleted translated directory: '{target_path}'.")
            except Exception as e:
                logging.error(f"Error deleting '{target_path}': {e}")
                overall_translation_status = False # 删除失败也算失败
        else:
            logging.info(f"Target file/directory not found, skipping deletion: '{target_path}'.")

    # 翻译Markdown文件
    if md_files_to_translate:
        logging.info(f"Translating {len(md_files_to_translate)} Markdown files for language '{lang_code}'.")
        for md_file in md_files_to_translate:
            success = process_markdown_file(md_file, lang_code)
            if not success:
                logging.warning(f"Translation failed for '{md_file}'. This file might need manual review or retry.")
                overall_translation_status = False # 翻译失败
        
    # 同步GitBook资产
    # 如果有GitBook资产需要同步，或者有GitBook目录被删除，则触发整个assets目录的同步
    if gitbook_assets_to_sync or gitbook_dirs_to_delete:
        logging.info(f"Triggering GitBook assets synchronization for language '{lang_code}'.")
        sync_success = sync_gitbook_assets(lang_code) # 捕获同步结果
        if not sync_success:
            overall_translation_status = False # 同步失败
    else:
        logging.info(f"No GitBook assets or directories detected for synchronization for language '{lang_code}'.")
    
    final_status_message = "成功" if overall_translation_status else "失败"
    logging.info(f"--- Completed translation and synchronization for language: '{config['name']}' ({lang_code}). Status: {final_status_message} ---")

    # 输出翻译状态和语言目录名，供 GitHub Actions 使用 (推荐方式)
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f"translation_status={'success' if overall_translation_status else 'failure'}\n")
        f.write(f"lang_dir={config['dir']}\n")

    # 将翻译状态写入 JSON 文件，供后续 job 汇总
    status_output_dir = Path('translation_status_output')
    status_output_dir.mkdir(exist_ok=True)
    status_file_path = status_output_dir / f"status_{target_lang_code}.json"
    
    status_data = {
        "lang_code": target_lang_code,
        "status": "success" if overall_translation_status else "failure"
    }
    with open(status_file_path, 'w', encoding='utf-8') as f:
        json.dump(status_data, f, ensure_ascii=False, indent=2)
    logging.info(f"Translation status for {target_lang_code} saved to {status_file_path}")

if __name__ == "__main__":
    main()