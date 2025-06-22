---
icon: floppy-disk
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 預設儲存位置

Cherry Studio 資料儲存遵循系統規範，資料會自動放置在使用者目錄下，具體目錄位置如下：

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

也可以在以下位置查看：
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# 修改儲存位置（參考用）

方法一：

可以透過建立軟連結的方式實現。先退出軟體，將資料移動到您希望儲存的位置，然後在原位置建立一個指向新位置的連結即可。

具體操作步驟請參考：[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

方法二：
基於 Electron 應用特性，透過設定啟動參數修改儲存位置。

> --user-data-dir
> 如: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> 範例:

```shell
PS D:\CherryStudio> dir


    目錄: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (編碼格式: ANSI)

```bash
@title CherryStudio 初始化
@echo off

set current_path_dir=%~dp0
@echo 目前路徑:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio 資料路徑:%user_data_dir%

@echo 搜尋目前路徑下的 Cherry-Studio-*-portable.exe
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( #此程式碼適用於 GitHub 和官網下載版本，其他版本請自行修改
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo 找到檔案: %target_file%
) else (
    echo 未找到符合檔案，結束腳本執行
    pause
    exit
)

@echo 確認執行請繼續
pause

@echo 啟動 CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo 操作完成
@echo on
exit
```

> 目錄 user-data-dir 初始化後的結構：

```shell
PS D:\CherryStudio> dir .\user-data-dir\


    目錄: D:\CherryStudio\user-data-dir


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:29                blob_storage
d-----         2025/4/18     14:07                Cache
d-----         2025/4/18     14:07                Code Cache
d-----         2025/4/18     14:07                Data
d-----         2025/4/18     14:07                DawnGraphiteCache
d-----         2025/4/18     14:07                DawnWebGPUCache
d-----         2025/4/18     14:07                Dictionaries
d-----         2025/4/18     14:07                GPUCache
d-----         2025/4/18     14:07                IndexedDB
d-----         2025/4/18     14:07                Local Storage
d-----         2025/4/18     14:07                logs
d-----         2025/4/18     14:30                Network
d-----         2025/4/18     14:07                Partitions
d-----         2025/4/18     14:29                Session Storage
d-----         2025/4/18     14:07                Shared Dictionary
d-----         2025/4/18     14:07                WebStorage
-a----         2025/4/18     14:07             36 .updaterId
-a----         2025/4/18     14:29             20 config.json
-a----         2025/4/18     14:07            434 Local State
-a----         2025/4/18     14:29             57 Preferences
-a----         2025/4/18     14:09           4096 SharedStorage
-a----         2025/4/18     14:30            140 window-state.json
```