#!/usr/bin/env python3
"""
Test script for the i18n translation functionality.
This script can be run locally to test the translation without triggering the GitHub workflow.
"""

import os
import sys
import logging
import tempfile
import shutil
from pathlib import Path
from i18n_translator import translate_content, process_file, get_corresponding_path


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def test_translation():
    """Test the translation functionality with a sample markdown text."""

    if not os.environ.get("GEMINI_API_KEY"):
        logging.error("GEMINI_API_KEY not found in environment variables")
        logging.error(
            "Please set the GEMINI_API_KEY environment variable before running this script")
        sys.exit(1)

    chinese_text = """---
icon: language
---

# 翻译

Cherry Studio 的翻译功能为您提供快速、准确的文本翻译服务，支持多种语言之间的互译。

### 界面概览

<figure><img src="../../.gitbook/assets/翻译.png" alt=""><figcaption></figcaption></figure>

翻译界面主要由以下几个部分组成：

1. **源语言选择区**：
   * 任意语言：Cherry Studio 会自动识别源语言并进行翻译。
2. **目标语言选择区**：
   * 下拉菜单：选择您希望将文本翻译成的语言。
3. **设置按钮**：
   * 点击后将跳转到 [默认模型设置](settings/default-models.md)。

### 使用步骤

1. **选择目标语言**：
   * 在目标语言选择区选择您希望翻译成的语言。
2. **输入或粘贴文本**：
   * 在左侧的文本输入框中输入或粘贴您要翻译的文本。
3. **开始翻译**：
   * 点击 `翻译` 按钮。

```python
# 这是一段代码，不应该被翻译
def hello_world():
    print("你好，世界！")
```
"""

    # Translate from Chinese to English
    logging.info("Testing Chinese to English translation...")
    english_text = translate_content(chinese_text, 'zh', 'en')

    if english_text:
        logging.info("Translation successful!")
        logging.info("\nTranslated text:\n")
        print(english_text)
    else:
        logging.error("Translation failed!")

    # Sample markdown text in English
    english_sample = """---
icon: book
---

# Documentation

This is a sample English text for testing translation to Chinese.

## Features

* Feature 1: This is the first feature
* Feature 2: This is the second feature

### Code Example

```javascript
// This code should not be translated
function sayHello() {
    console.log("Hello, world!");
}
```

Please refer to the [documentation](docs/readme.md) for more information.

<figure><img src="image.png" alt="Sample image"><figcaption>This is a caption</figcaption></figure>
"""

    logging.info("\nTesting English to Chinese translation...")
    chinese_result = translate_content(english_sample, 'en', 'zh')

    if chinese_result:
        logging.info("Translation successful!")
        logging.info("\nTranslated text:\n")
        print(chinese_result)
    else:
        logging.error("Translation failed!")


def test_file_placement():
    """Test if translated files are correctly placed in their corresponding locations."""

    if not os.environ.get("GEMINI_API_KEY"):
        logging.error("GEMINI_API_KEY not found in environment variables")
        logging.error(
            "Please set the GEMINI_API_KEY environment variable before running this script")
        sys.exit(1)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        chinese_docs = temp_path
        english_docs = temp_path / "i18n" / "english"
        os.makedirs(english_docs, exist_ok=True)

        test_zh_file = chinese_docs / "test_translation.md"
        with open(test_zh_file, 'w', encoding='utf-8') as f:
            f.write("# 测试文档\n\n这是一个测试文档，用于测试翻译功能。")

        test_en_file = english_docs / "test_english.md"
        with open(test_en_file, 'w', encoding='utf-8') as f:
            f.write("# Hello World")

        logging.info("Testing Chinese to English file placement...")

        en_path = get_corresponding_path(
            str(test_zh_file), str(chinese_docs), str(english_docs))
        logging.info(f"Chinese file: {test_zh_file}")
        logging.info(f"Expected English file: {en_path}")

        result = process_file(
            str(test_zh_file),
            source_base=str(chinese_docs),
            target_base=str(english_docs),
            is_chinese_to_english=True
        )
        if result:
            logging.info(f"Processing result for {test_zh_file}: Success")
        else:
            logging.warning(
                f"Processing result for {test_zh_file}: Failed or Skipped")

        if os.path.exists(en_path):
            logging.info("✅ English file was created successfully!")
            with open(en_path, 'r', encoding='utf-8') as f:
                content = f.read()
            logging.info(f"Translated content:\n{content}")
        else:
            logging.error("❌ English file was not created!")

        logging.info("\nTesting English to Chinese file placement...")

        zh_path = get_corresponding_path(
            str(test_en_file), str(english_docs), str(chinese_docs))
        logging.info(f"English file: {test_en_file}")
        logging.info(f"Expected Chinese file: {zh_path}")

        result = process_file(
            str(test_en_file),
            source_base=str(english_docs),
            target_base=str(chinese_docs),
            is_chinese_to_english=False
        )
        if result:
            logging.info(f"Processing result for {test_en_file}: Success")
        else:
            logging.warning(
                f"Processing result for {test_en_file}: Failed or Skipped")

        if os.path.exists(zh_path):
            logging.info("✅ Chinese file was created successfully!")
            with open(zh_path, 'r', encoding='utf-8') as f:
                content = f.read()
            logging.info(f"Translated content:\n{content}")
        else:
            logging.error("❌ Chinese file was not created!")


if __name__ == "__main__":
    # test_translation()
    test_file_placement()
