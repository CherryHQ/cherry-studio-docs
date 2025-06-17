
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 自動インストール MCP

> 自動インストールには、Cherry Studio を v1.1.18 以上にアップグレードする必要があります。

## 機能概要

手動インストールに加え、Cherry Studio にはより便利な `@mcpmarket/mcp-auto-install` ツールが組み込まれており、MCP サーバーを簡単にインストールできます。MCP サービス対応の大規模言語モデル対話で適切なコマンドを入力するだけで設定可能です。

{% hint style="warning" %}
**テスト段階に関する注意:**

* `@mcpmarket/mcp-auto-install` は現在ベータテスト中です
* 動作は大規模モデルの「知能レベル」に依存し、自動追加される場合もありますが、**一部設定はMCP設定で手動調整が必要**な場合があります
* 現在の検索ソースは @modelcontextprotocol から取得しています（カスタマイズ方法は下記説明）
{% endhint %}

## 使用方法

例えば、次のコマンドを入力：

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>MCP サーバーインストールコマンド入力画面</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP サーバー設定インターフェース</p></figcaption></figure>

システムが自動的に要求を認識し、`@mcpmarket/mcp-auto-install` でインストールを完了します。このツールは次のような様々なタイプの MCP サーバーに対応しています：

* filesystem（ファイルシステム）
* fetch（ネットワークリクエスト）
* sqlite（データベース）
* など...

> MCP_PACKAGE_SCOPES 変数で MCP サービスの検索ソースをカスタマイズ可能（デフォルト値：`@modelcontextprotocol`）。

## `@mcpmarket/mcp-auto-install` ライブラリ概要

{% hint style="info" %}
**デフォルト設定例:**

```json
// `axun-uUpaWEdMEMU8C61K` はサービスID（任意の値に設定可）
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "詳細はhttps://www.npmjs.com/package/@mcpmarket/mcp-auto-installを参照"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` はオープンソースの npm パッケージです。詳細な情報と使用方法は [npm 公式リポジトリ](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) で確認できます。`@mcpmarket` は Cherry Studio 公式の MCP サービスコレクションです。
{% endhint %}