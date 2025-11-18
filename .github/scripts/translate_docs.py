import os
import hashlib
import logging
import shutil
import subprocess
import time
from pathlib import Path
import sys
import json
from google import genai
from google.genai import types
import openai
import frontmatter
import re

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
        cmd_list = command if isinstance(command, list) else command.split()
        result = subprocess.run(
            cmd_list,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        logging.debug(f"Executing git command: {' '.join(cmd_list)}")
        # 返回按行分割的输出列表，并过滤掉空行
        return [line for line in result.stdout.strip().split('\n') if line]
    except subprocess.CalledProcessError as e:
        logging.error(f"Git command failed with exit code {e.returncode}. Command: {e.cmd}")
        logging.error(f"Git Stderr: {e.stderr.strip()}")
        logging.debug(f"Git Stdout: {e.stdout.strip()}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error running git command: {e}")
        return []

def get_changed_files():
    """
    获取自 'last-translated' 标签以来发生更改的Markdown和GitBook相关文件。
    此函数通过比较 'last-translated' 标签与当前 HEAD 的差异，来确保所有累积的变更都被包含。
    """
    files_to_process = set()
    files_to_delete = set()
    
    logging.info("Determining changed files based on 'last-translated' tag.")
    
    # 1. 确保本地仓库拥有所有最新的标签信息
    run_git_command("git fetch --tags")

    # 2. 查找 'last-translated' 标签
    existing_tags = run_git_command("git tag -l last-translated")

    before_sha = None
    if existing_tags:
        # 3a. 如果标签存在，获取它指向的 commit SHA
        tag_sha_list = run_git_command(f"git rev-list -n 1 last-translated")
        if tag_sha_list:
            before_sha = tag_sha_list[0]
            logging.info(f"Found 'last-translated' tag pointing to commit: {before_sha}")
        else:
            logging.error("Could not find commit for tag 'last-translated'.")
            raise RuntimeError("Failed to get commit from tag.")
    else:
        # 3b. 如果标签不存在（首次运行），找到仓库的第一个 commit
        # 这将导致翻译仓库中所有相关文件
        initial_commit_list = run_git_command("git rev-list --max-parents=0 HEAD")
        if initial_commit_list:
            before_sha = initial_commit_list[0]
            logging.info("'last-translated' tag not found. Comparing against the first commit of the repository: {before_sha}")
        else:
            logging.error("Could not find the initial commit of the repository.")
            raise RuntimeError("Failed to get initial commit.")
            
    # 4. after_sha 永远是当前工作流检出的那个 commit
    current_sha = os.environ.get('GITHUB_SHA')
    if not current_sha:
        logging.error("GITHUB_SHA environment variable is not set.")
        raise RuntimeError("Missing GITHUB_SHA.")
    logging.info(f"Current HEAD commit for comparison is: {current_sha}")

    # 5. 如果 before_sha 和 current_sha 相同，说明没有新变更
    if before_sha == current_sha:
        logging.info("No new commits since last translation. Nothing to do.")
        return set(), set()

    # 6. 比较两个 commit 之间的差异来获取文件列表
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

    # 7. 过滤掉i18n和.github目录下的文件
    files_to_process = {f for f in files_to_process if not str(f).startswith('i18n/') and not str(f).startswith('.github/')}
    files_to_delete = {f for f in files_to_delete if not str(f).startswith('i18n/') and not str(f).startswith('.github/')}
    
    logging.info(f"Final list of {len(files_to_process)} files to process: {files_to_process}")
    logging.info(f"Final list of {len(files_to_delete)} files to delete: {files_to_delete}")
    
    return files_to_process, files_to_delete

# --- 从这里开始，下面的所有代码与您原始文件中的保持一致，无需任何修改 ---

def _get_all_relevant_files():
    """
    扫描整个仓库，获取所有相关的Markdown和GitBook文件，并排除i18n和.github目录。
    注意：这个函数在新逻辑下不会被 get_changed_files 调用，但可以保留以备手动触发等用途。
    """
    relevant_files = set()
    base_path = Path('.')
    for root, _, files in os.walk(base_path):
        # 排除i18n和.github目录
        if str(Path(root)).startswith('i18n/') or str(Path(root)).startswith('.github/'):
            continue
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix == '.md' or '.gitbook' in str(file_path):
                relevant_files.add(file_path)
    return relevant_files

# 配置API密钥
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
PPIO_API_KEY = os.environ.get('PPIO_API_KEY')

if not GEMINI_API_KEY:
    logging.error("GEMINI_API_KEY environment variable not found. Please set it.")
    exit(1)
if not PPIO_API_KEY:
    logging.error("PPIO_API_KEY environment variable not found. Please set it.")
    exit(1)

# 系统提示词
SYSTEM_INSTRUCTIONS = """
You are a professional document translation assistant specialized in GitHub content. Your task is to fluently translate Chinese documents into the target language.

## Translation Rules:
1. **Translate only user-facing textual content.** Do not translate structural elements, metadata, or technical syntax that are not intended for end-user consumption.

2. **Strictly preserve all Markdown formatting and structural elements:** This includes headings (#), lists (-, *, +), code blocks (```), blockquotes (>), bold (**), italics (*), links <sup>1</sup> [<sup>1</sup>](link), images (!alt text <sup>2</sup> [<sup>2</sup>](image path)), tables, etc. The Markdown syntax itself must remain untranslated.

3. **Translate comments within code blocks:** Comments inside code blocks (```) should be translated as they serve user understanding. However, preserve all code, commands, file names, technical identifiers, programming syntax, and variables in their original form.

4. **Preserve all resource references unchanged:** Links, image paths, file paths, and directory structures (e.g., `cherrystudio/preview/chat.md` in `User Interface <sup>3</sup> [<sup>3</sup>](cherrystudio/preview/chat.md)`) must remain in their original form without translation or modification.

5. **Maintain specialized documentation structures:** Content within `{% hint style="warning" %}` and `{% endhint %}` tags should be translated, but the tags themselves and their attributes must remain unchanged.

6. **Keep Frontmatter (YAML header) content intact:** All content between `---` delimiters, including metadata like `icon: cherries`, must remain untranslated.

7. **Provide translation only—no additional content:** Return only the translated document content without adding explanations, prefaces, postscripts, summaries, or any extraneous text.

8. **Handle table of contents files appropriately:** For SUMMARY.md or files beginning with `# Table of contents` followed by `## Cherry Studio`, translate only the displayed title text while preserving all links. Specifically, do not translate `# Table of contents` and `## Cherry Studio` headers.

9. **Preserve domain-specific terminology:** Maintain all platform-specific terms (e.g., pull request, fork, commit, repository for GitHub; merge request for GitLab) in their original form.

10. **Retain all technical identifiers:** Preserve URLs, file paths, version numbers, package names, API endpoints, and command-line syntax exactly as they appear in the source.

11. **Maintain original document structure:** Keep the same paragraph breaks, section organization, and overall document structure as the source material.

12. **Complete translation without omissions:** Translate the entire document in full regardless of length. Never omit, summarize, or skip content. Avoid phrases indicating brevity (e.g., "omitted", "summarized", "...") or their equivalents in the target language.

13. **Preserve repetitive content:** Translate all repeated sections fully without collapsing or removing duplicates, while maintaining the original structure.

14. **Maintain untranslatable content in original form:** Preserve in their original language all legal documents (including open-source licenses like MIT, GPL, Apache), proper nouns (brand names, product names, company names, personal names, place names), technical terms with established industry usage, and any content where translation would compromise legal, technical, or contextual accuracy.
"""

# 警告语模板
WARNING_HINT_TEMPLATE = """
{% hint style="warning" %}
（警告语）
{% endhint %}
"""

# 找到第一个标题的正则表达式
first_heading_pattern = re.compile(r"^(#+ .*)$", re.MULTILINE)

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
        "model": "qwen",
        "warning_text": "Este documento ha sido traducido del chino por IA y aún no ha sido revisado."
    },
    "fr": {
        "dir": "french",
        "name": "French",
        "model": "qwen",
        "warning_text": "Ce document a été traducido del chino por IA y aún no ha sido revisado."
    },
    "de": {
        "dir": "german",
        "name": "German",
        "model": "qwen",
        "warning_text": "Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden."
    },
    "ja": {
        "dir": "japanese",
        "name": "Japanese",
        "model": "qwen",
        "warning_text": "このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。"
    },
    "ko": {
        "dir": "korean",
        "name": "Korean",
        "model": "qwen",
        "warning_text": "이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。"
    },
    "ru": {
        "dir": "russian",
        "name": "Russian",
        "model": "qwen",
        "warning_text": "Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен."
    },
    "pt": {
        "dir": "portuguese",
        "name": "Portuguese",
        "model": "qwen",
        "warning_text": "Este documento foi traduzido do chinês por IA e ainda não foi revisado."
    },
    "it": {
        "dir": "italian",
        "name": "Italian",
        "model": "qwen",
        "warning_text": "Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato."
    },
    "ar": {
        "dir": "arabic",
        "name": "Arabic",
        "model": "qwen",
        "warning_text": "تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد."
    },
    "hi": {
        "dir": "hindi",
        "name": "Hindi",
        "model": "qwen",
        "warning_text": "यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।"
    },
    "bn": {
        "dir": "bengali",
        "name": "Bengali",
        "model": "qwen",
        "warning_text": "এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।"
    },
    "id": {
        "dir": "indonesian",
        "name": "Indonesian",
        "model": "qwen",
        "warning_text": "Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau."
    },
    "th": {
        "dir": "thai",
        "name": "Thai",
        "model": "qwen",
        "warning_text": "เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ"
    },
    "vi": {
        "dir": "vietnamese",
        "name": "Vietnamese",
        "model": "qwen",
        "warning_text": "Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét."
    },
    "tr": {
        "dir": "turkish",
        "name": "Turkish",
        "model": "qwen",
        "warning_text": "Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir."
    },
    "pl": {
        "dir": "polish",
        "name": "Polish",
        "model": "qwen",
        "warning_text": "Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany."
    },
    "nl": {
        "dir": "dutch",
        "name": "Dutch",
        "model": "qwen",
        "warning_text": "Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld."
    },
    "zh-tw": {
        "dir": "traditional-chinese",
        "name": "繁體中文",
        "model": "qwen",
        "warning_text": "此文件由 AI 從中文翻譯而來，尚未經過審閱。"
    },
    "el": {
        "dir": "greek",
        "name": "Ελληνικά",
        "model": "qwen",
        "warning_text": "Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί."
    }
}
# 示例中文 README.md 内容，用于 Few-shot 翻译
EXAMPLE_CHINESE_README = """# 项目简介

{% hint style="warning" %}
此文档由中文AI翻译而来，目前暂未经过审核。
我会尽量逐一查看文档，检查翻译是否合理。
{% endhint %}

<figure><img src=".gitbook/assets/docs-readme-banner1.png" alt=""><figcaption></figcaption></figure>

Cherry Studio 是一款集多模型对话、知识库管理、AI 绘画、翻译等功能于一体的全能 AI 助手平台。

### Star History

!Star History [<sup>4</sup>](https://urlscan.io/liveshot/?width=1300&height=620&url=https://cherrystarhistory.ocool.online/)

## 关注我们的社交账号

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">小红书</a></td><td><a href=".gitbook/assets/1.png">1.png</a></td><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link</a></td></tr></tbody></table>
"""

# 示例英文 README.md 翻译，用于 Few-shot 翻译
EXAMPLE_ENGLISH_README = """# Project Introduction

{% hint style="warning" %}
This document is translated from Chinese by AI and has not yet been reviewed. I will try to check the document one by one to ensure the translation is reasonable.
{% endhint %}

<figure><img src=".gitbook/assets/docs-readme-banner1.png" alt=""><figcaption></figcaption></figure>

Cherry Studio is an all-in-one AI assistant platform integrating multi-model conversations, knowledge base management, AI painting, translation, and more.

### Star History

!Star History [<sup>4</sup>](https://urlscan.io/liveshot/?width=1300&height=620&url=https://cherrystarhistory.ocool.online/)

## Follow Our Social Accounts

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">Xiaohongshu</a></td><td><a href=".gitbook/assets/1.png">1.png</a></td><td><a href="https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link">https://www.xiaohongshu.com/user/profile/662b6853000000000b031d9a?xsec_token=YB_1nKvlH4r5hPYVVbbsNHF8Y6n6AKlm5-DaggPCtd2DQ%3D&#x26;xsec_source=app_share&#x26;xhsshare=CopyLink&#x26;appuid=662b6853000000000b031d9a&#x26;apptime=1738627324&#x26;share_id=ace5db41b5954fab8d98a2a7865a62bc&#x26;share_channel=copy_link</a></td></tr></tbody></table>
"""

def translate_text(text, target_lang_code):
    """
    调用Gemini或DeepSeek API翻译文本，并增加了自动重试机制。
    """
    if not text.strip():
        return ""

    lang_config = LANG_CONFIG.get(target_lang_code)
    if not lang_config:
        logging.error(f"Unsupported target language code: {target_lang_code}")
        return None

    target_language_name = lang_config["name"]
    model_type = lang_config["model"]

    max_attempts = 3
    # 定义每次重试前的等待时间（秒）
    retry_wait_times = [60, 120]

    for attempt in range(max_attempts):
        try:
            translated_content = None
            translated_content_parts = []
            
            logging.info(f"Attempt {attempt + 1}/{max_attempts} to translate to {target_language_name} using {model_type} model.")

            if model_type == "gemini":
                client = genai.Client(
                    api_key=GEMINI_API_KEY,
                    http_options={"base_url": "https://aihubmix.com/gemini"},
                )
                model_name = "gemini-1.5-flash"

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

                for chunk in client.models.generate_content_stream(
                    model=model_name,
                    contents=contents,
                    config=generate_content_config,
                ):
                    translated_content_parts.append(chunk.text)
                translated_content = "".join(translated_content_parts)

            elif model_type in ["qwen", "deepseek"]:
                client = openai.OpenAI(
                    api_key=PPIO_API_KEY,
                    base_url="https://api.ppinfra.com/v1",
                )
                model_name = "qwen/qwen2-72b-instruct" if model_type == "qwen" else "deepseek/deepseek-v2"
                
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
                    for chunk in response:
                        if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                            translated_content_parts.append(chunk.choices[0].delta.content)
                    translated_content = "".join(translated_content_parts)
                    if not translated_content.strip():
                        raise ValueError("Streaming returned empty content, attempting non-streaming fallback.")
                except Exception as stream_error:
                    logging.warning(f"Streaming failed with error: {stream_error}. Falling back to non-streaming.")
                    resp = client.chat.completions.create(
                        model=model_name,
                        messages=messages,
                        temperature=1,
                        stream=False,
                    )
                    if resp.choices and resp.choices[0].message:
                        translated_content = resp.choices[0].message.content or ""
                    else:
                        translated_content = ""

            else:
                # 这是一个配置错误，不需要重试
                logging.error(f"Unknown model type: {model_type} for language {target_lang_code}")
                return None

            # 如果成功获取到非空翻译内容，则返回结果
            if translated_content and translated_content.strip():
                logging.info(f"Translation successful on attempt {attempt + 1}.")
                return translated_content
            else:
                # 如果API调用成功但返回空内容，也视为一次失败
                raise ValueError("API returned empty content.")

        except Exception as e:
            logging.error(f"Attempt {attempt + 1}/{max_attempts} failed with error: {e}")
            # 如果不是最后一次尝试，则等待后重试
            if attempt < max_attempts - 1:
                wait_time = retry_wait_times[attempt]
                logging.info(f"Waiting for {wait_time} seconds before retrying...")
                time.sleep(wait_time)
            else:
                # 所有重试都失败了
                logging.error(f"All {max_attempts} translation attempts have failed for language {target_lang_code}.")
                return None
    
    # 理论上不会执行到这里，但作为保障
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
        
        # 将警告语插入到大标题与正文之间，而不是icon和大标题之间
        # 检查文件路径是否在 .gitbook/includes/ 目录下或是否为 SUMMARY.md，如果是则不添加警告语
        if ".gitbook/includes/" not in str(source_path) and source_path != Path('SUMMARY.md'):
            # 定义一个函数，用于在匹配到的标题后插入警告语
            def insert_warning_after_heading(match):
                return match.group(0) + "\n\n" + warning_hint + "\n\n"

            # 尝试在第一个标题后插入警告语。re.sub 的 count=1 确保只处理第一个匹配项。
            # 如果没有找到标题，translated_markdown_content 将保持不变。
            processed_markdown_content = first_heading_pattern.sub(insert_warning_after_heading, translated_markdown_content, count=1)
            
            if processed_markdown_content == translated_markdown_content:
                # 如果没有找到标题（即 processed_markdown_content 没有变化），
                # 则在翻译内容的开头（Frontmatter之后）插入警告语。
                final_content += warning_hint + "\n\n"
                final_content += translated_markdown_content
            else:
                # 如果找到了标题并成功插入，则使用处理后的内容
                final_content += processed_markdown_content
        else:
            # 如果是 .gitbook/includes/ 目录下的文件或 SUMMARY.md，不添加警告语
            final_content += translated_markdown_content

        # 检查文件是否实际有变化，避免不必要的Git提交
        current_hash = get_file_hash(target_path)
        new_hash = hashlib.md5(final_content.encode('utf-8')).hexdigest()
        logging.info(f"Comparing hashes for {target_path}: current={current_hash}, new={new_hash}")

        if current_hash == new_hash:
            logging.info(f"No content changes detected for {target_path}. Skipping file write.")
            return True
        else:
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            logging.info(f"Successfully translated and saved: '{target_path}'. Hash changed from {current_hash} to {new_hash}.")
            return True

    except Exception as e:
        logging.error(f"An unexpected error occurred while processing {source_path}: {e}")
        return False

def sync_gitbook_assets_full(target_lang_code):
    """
    执行.gitbook/assets/目录的全量同步。
    此函数会先删除目标语言中的旧.gitbook/assets目录，然后将整个源.gitbook/assets目录复制过去。
    这种“先删后拷”的策略确保了最终状态的完全一致。
    """
    lang_dir = LANG_CONFIG[target_lang_code]['dir']
    logging.info(f"Starting full synchronization for '.gitbook/assets/' to '{lang_dir}' directory.")
    
    source_assets_dir = Path('.gitbook') / 'assets'
    target_assets_dir = Path('i18n') / lang_dir / '.gitbook' / 'assets'
    
    if not source_assets_dir.is_dir():
        logging.warning(f"Source directory '{source_assets_dir}' not found. Skipping synchronization.")
        return True # 源目录不存在，无需同步，视为成功

    try:
        # 1. 如果目标目录存在，则先删除
        if target_assets_dir.exists():
            logging.info(f"Removing existing target directory: '{target_assets_dir}'")
            shutil.rmtree(target_assets_dir)
        
        # 2. 完整地复制源目录到目标位置
        logging.info(f"Copying '{source_assets_dir}' to '{target_assets_dir}'")
        shutil.copytree(source_assets_dir, target_assets_dir)
        
        logging.info(f"Successfully synced '.gitbook/assets' directory for language '{lang_dir}'.")
        return True
    except Exception as e:
        logging.error(f"Error during full sync of '.gitbook/assets' for language '{lang_dir}': {e}")
        return False

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

    overall_translation_status = True
    
    try:
        files_to_process, files_to_delete = get_changed_files()
    except Exception as e:
        logging.error(f"Failed to determine changed files: {e}")
        exit(1)
    logging.info(f"Files identified for processing: {files_to_process}")
    logging.info(f"Files identified for deletion: {files_to_delete}")
    
    lang_code = target_lang_code
    config = LANG_CONFIG[lang_code]
    target_lang_dir = Path('i18n') / config["dir"]

    logging.info(f"--- Initiating translation and synchronization for language: '{config['name']}' ({lang_code}) ---")

    # 1. 判断并执行 .gitbook/assets/ 目录的全量同步
    gitbook_assets_changed = any('.gitbook/assets/' in str(p) for p in files_to_process.union(files_to_delete))
    if gitbook_assets_changed:
        logging.info("Changes detected in '.gitbook/assets/' directory. Triggering full synchronization.")
        if not sync_gitbook_assets_full(lang_code):
            overall_translation_status = False
        
        # 从待处理/待删除列表中移除已同步的.gitbook/assets文件
        files_to_process = {f for f in files_to_process if not str(f).startswith('.gitbook/assets/')}
        files_to_delete = {f for f in files_to_delete if not str(f).startswith('.gitbook/assets/')}
        logging.info(f"After .gitbook/assets sync, remaining files to process: {files_to_process}")
        logging.info(f"After .gitbook/assets sync, remaining files to delete: {files_to_delete}")
    else:
        logging.info("No changes detected in '.gitbook/assets/' directory. Skipping full synchronization.")

    # 2. 处理剩余的需要删除的文件
    if files_to_delete:
        logging.info(f"Processing {len(files_to_delete)} remaining files for deletion.")
    for deleted_path in files_to_delete:
        target_path = target_lang_dir / deleted_path
        if target_path.exists() and target_path.is_file():
            try:
                os.remove(target_path)
                logging.info(f"Successfully deleted file: '{target_path}'.")
            except Exception as e:
                logging.error(f"Error deleting '{target_path}': {e}")
                overall_translation_status = False
        else:
            logging.info(f"Target file not found or is a directory, skipping deletion: '{target_path}'.")

    # 3. 翻译剩余的 Markdown 文件 (包括 .gitbook/includes/*.md)
    md_files_to_translate = {f for f in files_to_process if f.suffix == '.md'}
    if md_files_to_translate:
        logging.info(f"Translating {len(md_files_to_translate)} Markdown files.")
        for md_file in md_files_to_translate:
            if not process_markdown_file(md_file, lang_code):
                logging.warning(f"Translation failed for '{md_file}'.")
                overall_translation_status = False
    else:
        logging.info("No Markdown files to translate.")
            
    final_status_message = "成功" if overall_translation_status else "失败"
    logging.info(f"--- Completed translation and synchronization for language: '{config['name']}' ({lang_code}). Status: {final_status_message} ---")

    # 输出翻译状态和语言目录名，供 GitHub Actions 使用
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
