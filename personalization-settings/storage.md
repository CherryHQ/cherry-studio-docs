---
icon: floppy-disk
---

# 默认存储位置

Cherry Studio 数据存储遵循系统规范，数据会自动放在用户目录下，具体目录位置如下：

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

也可以在以下位置查看：
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# 修改存储位置（供参考）

方法一：

可以通过创建软连接的方式来实现。将软件退出，将数据移动到你希望保存的位置，然后在原位置创建一个链接指向移动后的位置即可。

具体操作步骤可以参考：[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

方法二：
基于 Electron 应用特点、通过配置启动参数进行存储位置修改。

> --user-data-dir
> 如: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

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
@title CherryStudio 初始化
@echo off

set current_path_dir=%~dp0
@echo 当前路径:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio 数据路径:%user_data_dir%

@echo 查找当前路径下 Cherry-Studio-*-portable.exe
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do (
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo 找到文件: %target_file%
) else (
    echo 未找到匹配文件，退出该脚本
    pause
    exit
)

@echo 确认请继续
pause

@echo 启动 CherryStudio
start %target_file% --user-data-dir="%user_data_dir%"

@echo 操作结束
@echo on
exit
```

> 目录 user-data-dir 初始化后结构：

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
