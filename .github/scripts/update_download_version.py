import os
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
    if os.path.exists(file_path):
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            logging.error(f"Error calculating hash for {file_path}: {e}")
    return None

def update_download_version():
    """
    根据硬编码模板生成 download.md 文件，仅替换版本号。
    """
    file_path = 'cherrystudio/download.md'
    version_with_v = os.environ.get('NEW_VERSION')
    
    if not version_with_v:
        logging.error("NEW_VERSION environment variable not found.")
        return False

    # 移除 'v' 前缀，得到纯版本号
    version = version_with_v.lstrip('v')
    
    # 确保版本号不为空
    if not version:
        logging.error("Invalid version format. Version cannot be empty.")
        return False

    logging.info(f"Generating new download.md with version: {version_with_v} (v{version})")

    # 硬编码的文档模板，只包含版本号占位符
    # 特殊字符如 {% %} 需要使用双花括号 {{ }} 进行转义
    template = """---
icon: download
---

# 客户端下载

{% hint style="info" %}
当前最新正式版：v{version}
{% endhint %}

## 直链下载

### Windows 版本

{% hint style="warning" %}
注意：Windows 7 系统不支持安装 Cherry Studio。
{% endhint %}

#### 安装版（Setup）

<details>

<summary>x64 版本</summary>

主线路：

【[Cherry Studio 官网](https://cherry-ai.com/download)】 【[GitHub](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-setup.exe)】

备用线路：

【[线路1](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-setup.exe)】 【[线路2](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-setup.exe)】 【[线路3](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-setup.exe)】

</details>

<details>

<summary>ARM64 版本</summary>

主线路：

【[Cherry Studio 官网](https://cherry-ai.com/download)】 【[GitHub](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-setup.exe)】

备用线路：

【[线路1](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-setup.exe)】 【[线路2](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-setup.exe)】 【[线路3](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-setup.exe)】

</details>

#### 便携版（Portable）

<details>

<summary>x64 版本</summary>

主线路：

【[Cherry Studio 官网](https://cherry-ai.com/download)】 【[GitHub](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-portable.exe)】

备用线路：

【[线路1](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-portable.exe)】 【[线路2](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-portable.exe)】 【[线路3](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-portable.exe)】

</details>

<details>

<summary>ARM64 版本</summary>

主线路：

【[Cherry Studio 官网](https://cherry-ai.com/download)】 【[GitHub](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-portable.exe)】

备用线路：

【[线路1](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-portable.exe)】 【[线路2](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-portable.exe)】 【[线路3](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-portable.exe)】

</details>

***

### macOS 版本

<details>

<summary>Intel 芯片版本（x64）</summary>

主线路：

【[Cherry Studio 官网](https://cherry-ai.com/download)】 【[GitHub](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64.dmg)】

备用线路：

【[线路1](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}.dmg)】 【[线路2](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64.dmg)】 【[线路3](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64.dmg)】

</details>

<details>

<summary>Apple Silicon 版本（ARM64，M 系列芯片）</summary>

主线路：

【[Cherry Studio 官网](https://cherry-ai.com/download)】 【[GitHub](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.dmg)】

备用线路：

【[线路1](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.dmg)】 【[线路2](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.dmg)】 【[线路3](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.dmg)】

</details>

***

### Linux 版本

<details>

<summary>x86_64 版本</summary>

主线路：

【[Cherry Studio 官网](https://cherry-ai.com/download)】 【[GitHub](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x86_64.AppImage)】

备用线路：

【[线路1](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x86_64.AppImage)】 【[线路2](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x86_64.AppImage)】 【[线路3](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x86_64.AppImage)】

</details>

<details>

<summary>ARM64 版本</summary>

主线路：

【[Cherry Studio 官网](https://cherry-ai.com/download)】 【[GitHub](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.AppImage)】

备用线路：

【[线路1](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.AppImage)】 【[线路2](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.AppImage)】 【[线路3](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.AppImage)】

</details>

***

## 网盘下载

[夸克](https://pan.quark.cn/s/4044324d0ecd#/list/share)
"""

    # 用实际版本号替换模板中的占位符
    updated_content = template.format(version=version)

    # 检查是否需要更新文件
    current_hash = get_file_hash(file_path)
    new_hash = hashlib.md5(updated_content.encode('utf-8')).hexdigest()

    if current_hash == new_hash:
        logging.info('No changes detected. Skipping file write.')
        return False
    else:
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        logging.info(f'Successfully generated {file_path} with version v{version}')
        return True

if __name__ == "__main__":
    if update_download_version():
        exit(0)
    else:
        exit(1)
