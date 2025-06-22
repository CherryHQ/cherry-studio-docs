---
icon: floppy-disk
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# デフォルトの保存場所

Cherry Studio のデータ保存はシステム仕様に従い、データはユーザーディレクトリ下に自動的に保存されます。具体的なディレクトリの場所は以下の通りです：

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

以下の場所でも確認できます：
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# 保存場所の変更（参考用）

方法1：

シンボリックリンクを作成することで実現できます。ソフトウェアを終了し、データを保存したい場所に移動した後、元の場所に移動先を指すリンクを作成します。

具体的な操作手順はこちらを参照してください：[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

方法2：
Electron アプリの特性を利用し、起動パラメータの設定で保存場所を変更します。

> --user-data-dir
> 例: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> 実行例:

```shell
PS D:\CherryStudio> dir


    ディレクトリ: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (encoding: ANSI)

```bash
@title CherryStudio 初期化
@echo off

set current_path_dir=%~dp0
@echo 現在のパス:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio データパス:%user_data_dir%

@echo カレントパスで Cherry-Studio-*-portable.exe を検索中
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( #このコードは、GitHubおよび公式サイトからダウンロードしたバージョンに適応します。その他の場合はご自身で修正してください
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo ファイルを検出: %target_file%
) else (
    echo 該当ファイルが見つかりません、スクリプトを終了します
    pause
    exit
)

@echo 続行するには確認してください
pause

@echo CherryStudio を起動します
start %target_file% --user-data-dir="%user_data_dir%"

@echo 操作が完了しました
@echo on
exit
```

> user-data-dir ディレクトリの初期化後構造:

```shell
PS D:\CherryStudio> dir .\user-data-dir\


    ディレクトリ: D:\CherryStudio\user-data-dir


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