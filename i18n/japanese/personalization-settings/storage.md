---
icon: floppy-disk
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# デフォルト保存場所

Cherry Studioのデータ保存はシステム仕様に準拠しており、データは自動的にユーザーディレクトリに保存されます。具体的なディレクトリの場所は以下の通りです：

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

> Linux: /home/username/.config/CherryStudio

以下の場所でも確認できます：
<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>



# 保存場所変更（参考用）

**方法1：**

シンボリックリンクを作成することで変更できます。ソフトウェアを終了し、データを保存したい場所に移動後、元の場所に移動先を指すリンクを作成してください。

具体的な操作手順は以下を参照：
[https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)

**方法2：**
Electronアプリケーションの特性を利用し、起動パラメータを設定して保存場所を変更します。

> --user-data-dir
> 例: Cherry-Studio-*-x64-portable.exe --user-data-dir="%user_data_dir%"

> 例:

```shell
PS D:\CherryStudio> dir


    ディレクトリ: D:\CherryStudio


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/4/18     14:05                user-data-dir
-a----         2025/4/14     23:05       94987175 Cherry-Studio-1.2.4-x64-portable.exe
-a----         2025/4/18     14:05            701 init_cherry_studio.bat
```

> init_cherry_studio.bat (エンコード: ANSI)

```bash
@title CherryStudio初期化
@echo off

set current_path_dir=%~dp0
@echo カレントパス:%current_path_dir%
set user_data_dir=%current_path_dir%user-data-dir
@echo CherryStudioデータパス:%user_data_dir%

@echo カレントパス下のCherry-Studio-*-portable.exeを検索中
setlocal enabledelayedexpansion

for /f "delims=" %%F in ('dir /b /a-d "Cherry-Studio-*-portable*.exe" 2^>nul') do ( #このコードはGitHubと公式サイトからダウンロードしたバージョンに対応しています。その他の場合はご自身で変更してください
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

@echo 確認後、続行してください
pause

@echo CherryStudioを起動中
start %target_file% --user-data-dir="%user_data_dir%"

@echo 操作完了
@echo on
exit
```

> ディレクトリuser-data-dirの初期化後の構造：

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