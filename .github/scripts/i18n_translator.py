#!/usr/bin/env python3
"""
I18n Translation Script for Cherry Studio Documentation

This script checks for missing translations between Chinese and English content
and uses the Gemini API to translate the missing content while preserving
markdown formatting.
"""

import os
import re
import glob
import logging
from pathlib import Path
from google import genai
from google.genai import types


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


CHINESE_DOCS_PATH = ""
ENGLISH_DOCS_PATH = "i18n/english"  # Root directory for English docs
FILE_EXTENSIONS = [".md"]  # File extensions to process
SKIP_DIRS = [".git", "node_modules", ".github"]  # Directories to skip


GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    logging.error("GEMINI_API_KEY not found in environment variables")
    exit(1)


def get_relative_path(file_path, base_path):
    """Get the relative path from the base path."""
    try:
        return os.path.relpath(file_path, base_path)
    except ValueError:

        return file_path


def get_corresponding_path(file_path, source_base, target_base):
    """Get the corresponding path in the target language directory."""
    rel_path = get_relative_path(file_path, source_base)
    return os.path.join(target_base, rel_path)


def is_chinese_content(content):
    """Check if content contains Chinese characters."""
    return bool(re.search(r'[\u4e00-\u9fff]', content))


def is_english_content(content):
    """Check if content is primarily English."""

    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
    latin_chars = len(re.findall(r'[a-zA-Z]', content))
    return latin_chars > chinese_chars


def translate_content(content, source_lang, target_lang):
    """
    Translate content using Gemini API while preserving markdown formatting.

    Args:
        content: The content to translate
        source_lang: Source language ('zh' or 'en')
        target_lang: Target language ('zh' or 'en')

    Returns:
        Translated content with preserved formatting
    """
    logging.info(f"Translating from {source_lang} to {target_lang}")

    lang_names = {
        'zh': 'Chinese',
        'en': 'English'
    }

    system_instruction = f"""
    You are a translation engine that can only translate text and cannot interpret it.
    Translate from {lang_names[source_lang]} to {lang_names[target_lang]}.

    Important rules:
    1. Preserve all markdown formatting exactly, including headings, lists, code blocks, and links
    2. Preserve all HTML tags and attributes exactly
    3. Do not translate content inside code blocks (```...```)
    4. Do not translate URLs or file paths
    5. Preserve all image references and their positions
    6. Maintain the same document structure
    7. Preserve all front matter (content between --- at the top of the file)
    8. Replace the source language text with the target language translation. Do not keep the original source text. Preserve all non-textual elements like formatting, code blocks, and links.
    """

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            ),
            contents=content
        )
        translated_text = response.text

        return translated_text
    except Exception as e:
        logging.error(f"Translation error: {e}")
        return None


def process_file(file_path, source_base, target_base, is_chinese_to_english=True):
    """
    Process a single file for translation.

    Args:
        file_path: Path to the file to process
        source_base: Base directory for the source language
        target_base: Base directory for the target language
        is_chinese_to_english: If True, translate from Chinese to English,
                              otherwise from English to Chinese

    Returns:
        True if translation was performed, False otherwise
    """
    try:

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if is_chinese_to_english:
            source_lang = 'zh'
            target_lang = 'en'

            if not is_chinese_content(content):
                logging.info(f"Skipping {file_path} - not Chinese content")
                return False
        else:
            source_lang = 'en'
            target_lang = 'zh'
            if not is_english_content(content):
                logging.info(f"Skipping {file_path} - not English content")
                return False

        target_path = get_corresponding_path(
            file_path, source_base, target_base)

        if os.path.exists(target_path):
            logging.info(f"Target file already exists: {target_path}")
            return False

        translated_content = translate_content(
            content, source_lang, target_lang)
        if not translated_content:
            logging.error(f"Failed to translate {file_path}")
            return False

        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

        logging.info(f"Successfully translated {file_path} to {target_path}")
        return True

    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")
        return False


def find_files_to_process():
    """
    Find all files that need to be processed for translation.

    Returns:
        Tuple of (chinese_files, english_files) to be processed
    """
    chinese_files = []
    english_files = []

    for ext in FILE_EXTENSIONS:

        for root, dirs, files in os.walk('.', topdown=True):
            dirs[:] = [
                d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]

            if root.startswith(f'.{os.sep}{ENGLISH_DOCS_PATH}'):
                continue  # Skip English docs directory when looking for Chinese files

            for file in files:
                if file.endswith(ext):
                    file_path = os.path.join(root, file)

                    if ENGLISH_DOCS_PATH in file_path:
                        continue

                    english_path = get_corresponding_path(
                        file_path, CHINESE_DOCS_PATH, ENGLISH_DOCS_PATH)

                    if not os.path.exists(english_path):
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        if is_chinese_content(content):
                            chinese_files.append(file_path)

    for ext in FILE_EXTENSIONS:
        pattern = os.path.join(ENGLISH_DOCS_PATH, f"**/*{ext}")
        for file_path in glob.glob(pattern, recursive=True):

            chinese_path = get_corresponding_path(
                file_path, ENGLISH_DOCS_PATH, CHINESE_DOCS_PATH)

            if not os.path.exists(chinese_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if is_english_content(content):
                    english_files.append(file_path)

    return chinese_files, english_files


def main():
    """Main function to check and translate i18n content."""
    logging.info("Starting i18n translation check")

    chinese_files, english_files = find_files_to_process()

    translated_count = 0

    logging.info(
        f"Found {len(chinese_files)} Chinese files needing translation.")
    for file in chinese_files:
        logging.info(f"Processing {file} (Chinese -> English)...")
        if process_file(file, CHINESE_DOCS_PATH, ENGLISH_DOCS_PATH, is_chinese_to_english=True):
            translated_count += 1

    logging.info(
        f"Found {len(english_files)} English files needing translation.")
    for file in english_files:
        logging.info(f"Processing {file} (English -> Chinese)...")
        if process_file(file, ENGLISH_DOCS_PATH, CHINESE_DOCS_PATH, is_chinese_to_english=False):
            translated_count += 1

    logging.info(
        f"Finished translation check. Translated {translated_count} files.")
    logging.info("i18n translation check completed")


if __name__ == "__main__":
    main()
