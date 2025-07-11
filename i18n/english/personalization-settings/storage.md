---
icon: floppy-disk
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Default Storage Location

Cherry Studio data storage follows system specifications. Data is automatically placed in the user directory at the following locations:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

You can also view it at:
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# Changing Storage Location (For Reference)

Method 1:

This can be achieved by creating a symbolic link. Exit the application, move the data to your desired location, then create a link at the original location pointing to the new path.

For detailed steps, refer to:  
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

Method 2:  
Based on Electron application characteristics, modify the storage location by configuring launch parameters.

> --user-data-dir  
> Example: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> Example:

```shell
PS D:\CherryStudio> dir


    目录: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (encoding: ANSI)

```bash
@title CherryStudio Initialization
@echo off

set current_path_dir=%~dp0
@echo Current path: %current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio data path: %user_data_dir%

@echo Searching for Cherry-Studio-*-portable.exe in current directory
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( # Compatible with GitHub and official releases. Modify for other versions
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo Found file: %target_file%
) else (
    echo No matching files found. Exiting script
    pause
    exit
)

@echo Press any key to continue...
pause

@echo Launching CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo Operation completed
@echo on
exit
```

> Initial structure of user-data-dir:

```shell
PS D:\CherryStudio> dir .\user-data-dir\


    目录: D:\CherryStudio\user-data-dir


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