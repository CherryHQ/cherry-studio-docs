
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# MCP環境のインストール

**MCP(Model Context Protocol)** は、大規模言語モデル（LLM）にコンテキスト情報を標準化された方法で提供することを目的としたオープンソースプロトコルです。MCPの詳細については [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention") をご参照ください。

## Cherry StudioでのMCPの使用方法

`fetch`機能を例に、Cherry StudioでMCPを使用する方法を説明します。詳細は[ドキュメント](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)でご確認ください。

### **準備作業: uvとbunのインストール**

{% hint style="warning" %}
Cherry Studioは現在、組み込みの[uv](https://github.com/astral-sh/uv)と[bun](https://github.com/oven-sh/bun)のみを使用しており、システムにインストール済みのuvやbunを**再利用しません**。
{% endhint %}

`設定 > MCP サーバー`で`インストール`ボタンをクリックすると、自動的にダウンロード・インストールが行われます。GitHubから直接ダウンロードするため速度が遅く、失敗する可能性があります。インストールの成功は、後述のフォルダにファイルが存在するかで確認してください。

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**実行ファイルのインストールディレクトリ:**

Windows: `C:\Users\ユーザー名\.cherrystudio\bin`

macOS、Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>binディレクトリ</p></figcaption></figure>

**正常にインストールできない場合:**

システム内の対応するコマンドをシンボリックリンクでリンクすることができます。ディレクトリが存在しない場合は手動で作成してください。または実行ファイルを手動でダウンロードしてこのディレクトリに配置することも可能です:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)