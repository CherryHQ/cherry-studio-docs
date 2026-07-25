---
icon: download
---

# クライアントのダウンロード

Cherry Studio では、Windows、macOS、Linux 用のインストールパッケージを提供しています。ダウンロードページに記載したバージョン番号が古くならないように、このページでは長期的に利用できる公式リンクだけを紹介します。ダウンロードページを開いたら、最新の安定版と、お使いのシステムアーキテクチャに合うファイルを選択してください。

## 公式ダウンロードリンク

* [Cherry Studio 公式ダウンロードページ](https://cherry-ai.com/download)
* [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases)
* [GitHub 最新安定版](https://github.com/CherryHQ/cherry-studio/releases/latest)

{% hint style="warning" %}
インストールパッケージは、Cherry Studio 公式サイト、公式の `CherryHQ/cherry-studio` リポジトリ、またはダウンロードページに明記されたミラーからのみ入手してください。提供元が不明なもの、再パッケージされたもの、セキュリティソフトの無効化を求めるインストーラーは実行しないでください。
{% endhint %}

## 安定版とプレビュー版の選び方

| 種類 | 見分け方 | 適したユーザー |
| :--- | :--- | :--- |
| 安定版 | GitHub Releases で **Latest** と表示され、通常はバージョン番号に `alpha`、`beta`、`rc` が含まれない | 日常利用向け。推奨 |
| プレリリース版 | **Pre-release** と表示され、バージョン番号に `alpha`、`beta`、`rc` が含まれる場合がある | 新機能を早期に試したいユーザー |
| デイリープレビュー版 | 公式の [V2 Daily Preview Build](https://github.com/CherryHQ/cherry-studio/actions/workflows/v2-daily-preview-build.yml) から取得する | 開発、テスト、問題の再現 |

プレビュー版には、未完了のデータ移行、UI、互換性に関する変更が含まれる場合があります。インストール前にバックアップを作成し、重要なデータを扱う環境では安定版を優先してください。

## Windows

### アーキテクチャを選ぶ

**設定 → システム → バージョン情報**を開き、「システムの種類」を確認します。

* `x64` または「x64 ベース プロセッサ」と表示される場合：`x64` をダウンロードします。
* `ARM64` または「ARM ベース プロセッサ」と表示される場合：`arm64` をダウンロードします。

Intel または AMD を搭載する一般的な PC の多くは `x64` を使用します。`arm64` を使用するのは、Windows on ARM デバイスだけです。

### インストールパッケージを選ぶ

| ファイル形式 | 説明 |
| :--- | :--- |
| `*-x64-setup.exe` / `*-arm64-setup.exe` | インストール版。インストール先を選択し、ショートカットを作成できる |
| `*-x64-portable.exe` / `*-arm64-portable.exe` | ポータブル版。インストール処理を行いたくない場合に適している |

{% hint style="warning" %}
Cherry Studio は Windows 7 に対応していません。サポート対象の Windows バージョンにインストールしてください。
{% endhint %}

インストール手順とシステムのセキュリティ警告については、[Windows インストールガイド](../pre-basic/installation/windows.md)を参照してください。

## macOS

**Apple メニュー → この Mac について**を開き、「チップ」または「プロセッサ」を確認します。

* Apple M シリーズのチップが表示される場合：`arm64` をダウンロードします。
* Intel プロセッサが表示される場合：`x64` をダウンロードします。

| ファイル形式 | 説明 |
| :--- | :--- |
| `*-arm64.dmg` / `*-x64.dmg` | 推奨のグラフィカルインストールパッケージ |
| `*-arm64.zip` / `*-x64.zip` | 圧縮ファイル版 |

Apple Silicon パッケージは、M1、M2、M3、M4 などの Apple チップに対応しています。アーキテクチャを間違えると、アプリを開けないか、互換レイヤーを通じてしか動作しない場合があります。

インストール手順と「開発元を検証できません」などの警告については、[macOS インストールガイド](../pre-basic/installation/macos.md)を参照してください。

## Linux

ターミナルで次のコマンドを実行します。

```bash
uname -m
```

* 出力が `x86_64` の場合：`x86_64` または `amd64` を選択します。
* 出力が `aarch64` / `arm64` の場合：`arm64` / `aarch64` を選択します。

公式 Release では通常、次の形式が提供されます。

| ファイル形式 | 適した用途 |
| :--- | :--- |
| `.AppImage` | ディストリビューションを問わず直接実行する |
| `.deb` | Debian、Ubuntu、およびその派生ディストリビューション |
| `.rpm` | Fedora、RHEL、Rocky Linux などの RPM 系ディストリビューション |

形式によってアーキテクチャの表記が異なる場合があります。たとえば、x64 は `.deb` のファイル名では通常 `amd64`、AppImage では `x86_64` と表記されます。

## ダウンロード後の確認

1. ファイルの提供元が公式ドメインまたは `github.com/CherryHQ/cherry-studio` であることを確認します。
2. OS、アーキテクチャ、インストールパッケージの形式をもう一度確認します。
3. Release ページに SHA-256 ダイジェストが掲載されている場合は、実行前にローカルファイルのダイジェストと比較します。
4. 更新またはプレビュー版のテスト前に、Cherry Studio のデータをバックアップします。

### SHA-256 を計算する

{% tabs %}
{% tab title="Windows PowerShell" %}
```powershell
Get-FileHash .\Cherry-Studio-インストーラーファイル名 -Algorithm SHA256
```
{% endtab %}

{% tab title="macOS" %}
```bash
shasum -a 256 ~/Downloads/Cherry-Studio-インストーラーファイル名
```
{% endtab %}

{% tab title="Linux" %}
```bash
sha256sum ~/Downloads/Cherry-Studio-インストーラーファイル名
```
{% endtab %}
{% endtabs %}

出力は、公式 Release に記載された該当ファイルの SHA-256 と完全に一致する必要があります。一致しない場合はファイルを実行せず、公式リンクからダウンロードし直してください。

## 次のステップ

* [インストールガイド](../pre-basic/installation/)
* [モデルサービスの設定](../pre-basic/providers/)
* [会話画面](preview/chat.md)
