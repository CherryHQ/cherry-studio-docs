import os
import re
import hashlib
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_file_hash(file_path):
    """
    计算文件的MD5哈希值
    """
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for {file_path}: {e}")
        return None

def update_download_version():
    """
    更新 cherrystudio/download.md 文件中的版本号。
    """
    file_path = 'cherrystudio/download.md'
    new_version_with_v = os.environ.get('NEW_VERSION') # e.g., v1.4.2
    
    if not new_version_with_v:
        logging.error("NEW_VERSION environment variable not found.")
        return False

    # 移除 'v' 前缀，得到纯版本号
    new_version_without_v = new_version_with_v.lstrip('v') # e.g., 1.4.2

    logging.info(f"Attempting to update version to: {new_version_with_v} (with 'v') and {new_version_without_v} (without 'v') in {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 替换文档顶部的版本提示：当前最新正式版：vX.Y.Z
        updated_content = re.sub(r'(当前最新正式版：)v\d+\.\d+\.\d+', r'\g<1>' + new_version_with_v, content)

        # 替换 /releases/download/vX.Y.Z/ 中的 vX.Y.Z
        # 确保只替换 GitHub 下载链接中的版本号
        updated_content = re.sub(r'(https://github\.com/CherryHQ/cherry-studio/releases/download/)v\d+\.\d+\.\d+(?=/Cherry-Studio-\d+\.\d+\.\d+)', r'\g<1>' + new_version_with_v, updated_content)
        
        # 替换 Cherry-Studio-X.Y.Z- 或 Cherry-Studio-X.Y.Z. 中的 X.Y.Z
        # 确保只替换 Cherry-Studio- 后面的版本号
        updated_content = re.sub(r'(Cherry-Studio-)\d+\.\d+\.\d+(?=[-\.])', r'\g<1>' + new_version_without_v, updated_content)

        current_hash = get_file_hash(file_path)
        new_hash = hashlib.md5(updated_content.encode('utf-8')).hexdigest()

        if current_hash == new_hash:
            logging.info('No changes detected. Skipping file write.')
            return False
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            logging.info(f'Successfully updated {file_path}')
            return True

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    if update_download_version():
        exit(0)
    else:
        exit(1)