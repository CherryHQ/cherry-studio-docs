import sys
import json
import os
import logging

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    if len(sys.argv) < 2:
        logging.error("Usage: python summarize_translation.py <path_to_status_files_directory>")
        sys.exit(1)

    status_files_dir = sys.argv[1]
    
    translation_results = {}
    successful_languages = []
    failed_languages = []

    # 遍历目录及其子目录下的所有 JSON 文件
    for root, _, files in os.walk(status_files_dir):
        for filename in files:
            if filename.startswith("status_") and filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        lang_code = data.get("lang_code")
                        status = data.get("status")
                        if lang_code and status:
                            translation_results[lang_code] = status
                        else:
                            logging.warning(f"Malformed status file {file_path}. Skipping.")
                except json.JSONDecodeError:
                    logging.error(f"Invalid JSON in file {file_path}. Skipping.")
                except Exception as e:
                    logging.error(f"Error reading file {file_path}: {e}. Skipping.")

    if not translation_results:
        logging.error("No translation status files found or parsed successfully.")
        sys.exit(1)

    logging.info("--- 翻译结果总结 ---")

    for lang_code, status in translation_results.items():
        if status == "success":
            successful_languages.append(lang_code)
        else:
            failed_languages.append(lang_code)

    if not failed_languages:
        logging.info("所有语言的文档翻译和同步均已成功完成！")
        logging.info(f"成功翻译的语言: {', '.join(successful_languages)}")
    else:
        logging.warning("部分语言的文档翻译或同步操作失败。")
        logging.info(f"成功翻译的语言: {', '.join(successful_languages) if successful_languages else '无'}")
        logging.error(f"失败的语言: {', '.join(failed_languages)}")
        sys.exit(1)
    
    logging.info("--------------------")

if __name__ == "__main__":
    main()