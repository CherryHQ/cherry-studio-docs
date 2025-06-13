import sys
import json
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python summarize_translation.py <path_to_status_files_directory>")
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
                            print(f"Warning: Malformed status file {file_path}. Skipping.")
                except json.JSONDecodeError:
                    print(f"Error: Invalid JSON in file {file_path}. Skipping.")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}. Skipping.")

    if not translation_results:
        print("Error: No translation status files found or parsed successfully.")
        sys.exit(1)

    for lang_code, status in translation_results.items():
        if status == "success":
            successful_languages.append(lang_code)
        else:
            failed_languages.append(lang_code)

    print("********************************************************************")
    print("******************** 翻译结果总结 **********************************")
    print("********************************************************************")

    if not failed_languages:
        print("所有语言的文档翻译和同步均已成功完成！")
        print(f"成功翻译的语言: {', '.join(successful_languages)}")
    else:
        print("部分语言的文档翻译或同步操作失败。")
        print(f"成功翻译的语言: {', '.join(successful_languages) if successful_languages else '无'}")
        print(f"失败的语言: {', '.join(failed_languages)}")
        # 如果有失败的语言，设置一个非零退出码，以便 GitHub Actions 标记为失败
        sys.exit(1) 
    
    print("********************************************************************")
    print("********************************************************************")

if __name__ == "__main__":
    main()