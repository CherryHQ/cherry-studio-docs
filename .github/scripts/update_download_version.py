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

【Cherry Studio 官网 <sup>1</sup> [<sup>1</sup>](https://cherry-ai.com/download)】 【GitHub <sup>2</sup> [<sup>2</sup>](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-setup.exe)】

备用线路：

【线路1 <sup>3</sup> [<sup>3</sup>](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-setup.exe)】 【线路2 <sup>4</sup> [<sup>4</sup>](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-setup.exe)】 【线路3 <sup>5</sup> [<sup>5</sup>](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-setup.exe)】

</details>

<details>

<summary>ARM64 版本</summary>

主线路：

【Cherry Studio 官网 <sup>1</sup> [<sup>1</sup>](https://cherry-ai.com/download)】 【GitHub <sup>6</sup> [<sup>6</sup>](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-setup.exe)】

备用线路：

【线路1 <sup>7</sup> [<sup>7</sup>](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-setup.exe)】 【线路2 <sup>8</sup> [<sup>8</sup>](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-setup.exe)】 【线路3 <sup>9</sup> [<sup>9</sup>](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-setup.exe)】

</details>

#### 便携版（Portable）

<details>

<summary>x64 版本</summary>

主线路：

【Cherry Studio 官网 <sup>1</sup> [<sup>1</sup>](https://cherry-ai.com/download)】 【GitHub <sup>10</sup> [<sup>10</sup>](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-portable.exe)】

备用线路：

【线路1 <sup>11</sup> [<sup>11</sup>](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-portable.exe)】 【线路2 <sup>12</sup> [<sup>12</sup>](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-portable.exe)】 【线路3 <sup>13</sup> [<sup>13</sup>](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64-portable.exe)】

</details>

<details>

<summary>ARM64 版本</summary>

主线路：

【Cherry Studio 官网 <sup>1</sup> [<sup>1</sup>](https://cherry-ai.com/download)】 【GitHub <sup>14</sup> [<sup>14</sup>](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-portable.exe)】

备用线路：

【线路1 <sup>15</sup> [<sup>15</sup>](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-portable.exe)】 【线路2 <sup>16</sup> [<sup>16</sup>](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-portable.exe)】 【线路3 <sup>17</sup> [<sup>17</sup>](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-portable.exe)】

</details>

***

### macOS 版本

<details>

<summary>Intel 芯片版本（x64）</summary>

主线路：

【Cherry Studio 官网 <sup>1</sup> [<sup>1</sup>](https://cherry-ai.com/download)】 【GitHub <sup>18</sup> [<sup>18</sup>](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64.dmg)】

备用线路：

【线路1 <sup>19</sup> [<sup>19</sup>](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}.dmg)】 【线路2 <sup>20</sup> [<sup>20</sup>](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64.dmg)】 【线路3 <sup>21</sup> [<sup>21</sup>](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x64.dmg)】

</details>

<details>

<summary>Apple Silicon 版本（ARM64，M 系列芯片）</summary>

主线路：

【Cherry Studio 官网 <sup>1</sup> [<sup>1</sup>](https://cherry-ai.com/download)】 【GitHub <sup>22</sup> [<sup>22</sup>](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.dmg)】

备用线路：

【线路1 <sup>23</sup> [<sup>23</sup>](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.dmg)】 【线路2 <sup>24</sup> [<sup>24</sup>](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.dmg)】 【线路3 <sup>25</sup> [<sup>25</sup>](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.dmg)】

</details>

***

### Linux 版本

<details>

<summary>x86_64 版本</summary>

主线路：

【Cherry Studio 官网 <sup>1</sup> [<sup>1</sup>](https://cherry-ai.com/download)】 【GitHub <sup>26</sup> [<sup>26</sup>](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x86_64.AppImage)】

备用线路：

【线路1 <sup>27</sup> [<sup>27</sup>](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x86_64.AppImage)】 【线路2 <sup>28</sup> [<sup>28</sup>](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x86_64.AppImage)】 【线路3 <sup>29</sup> [<sup>29</sup>](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-x86_64.AppImage)】

</details>

<details>

<summary>ARM64 版本</summary>

主线路：

【Cherry Studio 官网 <sup>1</sup> [<sup>1</sup>](https://cherry-ai.com/download)】 【GitHub <sup>30</sup> [<sup>30</sup>](https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.AppImage)】

备用线路：

【线路1 <sup>31</sup> [<sup>31</sup>](https://download-cf.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.AppImage)】 【线路2 <sup>32</sup> [<sup>32</sup>](https://download.ocoolai.com/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64.AppImage)】 【线路3 <sup>33</sup> [<sup>33</sup>](https://download.ocoolai.online/https://github.com/CherryHQ/cherry-studio/releases/download/v{version}/Cherry-Studio-{version}-arm64-AppImage)】

</details>

***

## 网盘下载

夸克 <sup>34</sup> [<sup>34</sup>](https://pan.quark.cn/s/4044324d0ecd#/list/share)
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
