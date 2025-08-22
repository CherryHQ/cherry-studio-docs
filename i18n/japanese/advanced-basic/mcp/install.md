# MCP 環境インストール


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




**MCP(Model Context Protocol)** は、大規模言語モデル（LLM）に標準化された方法でコンテキスト情報を提供するためのオープンソースプロトコルです。MCPの詳細は [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention") を参照してください。

## Cherry Studio での MCP の使用

以下では `fetch` 機能を例に、Cherry Studio で MCP を使用する方法を説明します。詳細は [ドキュメント](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) で確認できます。

### **事前準備：uv・bun のインストール**

{% hint style="warning" %}
Cherry Studio は現在、組み込みの [uv](https://github.com/astral-sh/uv) と [bun](https://github.com/oven-sh/bun) **のみ**を使用しており、システムにインストール済みの uv や bun を**再利用しません**。
{% endhint %}

`設定 - MCP サーバー` で `インストール` ボタンをクリックすると、自動的にダウンロードとインストールが行われます。GitHub から直接ダウンロードするため、速度が遅く失敗する可能性が高いです。インストールが成功したかは、後述のフォルダ内にファイルがあるかで確認してください。

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

**実行ファイルのインストールディレクトリ:**

Windows: `C:\Users\ユーザー名\.cherrystudio\bin`

macOS・Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_フォルダ.png" alt=""><figcaption><p>bin ディレクトリ</p></figcaption></figure>

**正常にインストールできない場合:**

システム内の対応コマンドをシンボリックリンクでこのディレクトリにリンクできます（該当ディレクトリがない場合は手動で作成）。または実行ファイルを手動でダウンロードし、このディレクトリに配置してください：

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)