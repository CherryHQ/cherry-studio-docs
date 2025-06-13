---
icon: floppy-disk
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# デフォルトの保存場所

Cherry Studioのデータ保存はシステムの仕様に従い、データはユーザーディレクトリ下に自動的に保存されます。具体的なディレクトリの場所は次の通りです：

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

以下の場所でも確認できます：
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

# 保存場所の変更（参考情報）

方法１：

シンボリックリンクを作成することで実現できます。ソフトウェアを終了し、データを希望の保存場所に移動した後、元の場所に移動先を指すリンクを作成します。

具体的な操作手順はこちらを参照してください：[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

方法２：
Electronアプリケーションの特性を活用し、起動パラメータを設定して保存場所を変更します。

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

> init_cherry_studio.bat (エンコーディング: ANSI)

```bash
@title CherryStudio 初期設定
@echo off

set current_path_dir=%~dp0
@echo 現在のパス:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudio データパス:%user_data_dir%

@echo 現在のパスでCherry-Studio-*-portable.exeを検索
setlocal enabledelayedexpansion
for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable.exe" 2^>nul') do ( #実際のダウンロードファイル名に変更してください。公式サイトとGithubのダウンロードでは名前が異なります
    set "target_file=!cd!\%%F"
    goto :break
)
:break
if defined target_file (
    echo ファイル発見: %target_file%
) else (
    echo 一致するファイルが見つかりません。スクリプトを終了します
    pause
    exit
)

@echo 続行する場合は確認してください
pause

@echo CherryStudioを起動
start %target_file% --user-data-dir="%user_data_dir%"

@echo 操作完了
@echo on
exit
```

> ディレクトリ user-data-dir 初期化後の構造：

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