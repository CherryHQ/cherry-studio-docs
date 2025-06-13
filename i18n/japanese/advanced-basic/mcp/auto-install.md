
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# MCPの自動インストール

> MCPの自動インストールには、Cherry Studioをv1.1.18以降にアップグレードする必要があります。

## 機能概要

手動インストールに加え、Cherry Studioはより便利なMCPサーバーインストール方法として`@mcpmarket/mcp-auto-install`ツールを組み込んでいます。MCPサービスをサポートする大規模言語モデルとの対話で、対応するコマンドを入力するだけで利用できます。

{% hint style="warning" %}
**テスト段階の注意点：**

* `@mcpmarket/mcp-auto-install`は現在ベータ版です
* 効果は大規模言語モデルの「知能」に依存し、自動追加される場合もあれば、**MCP設定で一部パラメータを手動調整する必要がある場合もあります**
* 現在の検索ソースは@modelcontextprotocolから取得しており、カスタム設定が可能です（後述）
{% endhint %}

## 使用説明

例えば、次のように入力できます：

```
filesystem mcp serverをインストールしてください
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>MCPサーバーインストールコマンド入力</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCPサーバー設定画面</p></figcaption></figure>

システムは自動的に要求を認識し、`@mcpmarket/mcp-auto-install`を介してインストールを完了します。このツールは以下を含む様々なタイプのMCPサーバーをサポートしています：

* filesystem（ファイルシステム）
* fetch（ネットワークリクエスト）
* sqlite（データベース）
* など...

> MCP_PACKAGE_SCOPES変数でMCPサービスの検索ソースをカスタマイズ可能です。デフォルト値は`@modelcontextprotocol`です。

## `@mcpmarket/mcp-auto-install`ライブラリの紹介

{% hint style="info" %}
**デフォルト設定例：**

```json
// `axun-uUpaWEdMEMU8C61K`はサービスID（任意設定可）
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

`@mcpmarket/mcp-auto-install`はオープンソースのnpmパッケージです。詳細情報と使用ドキュメントは[npm公式リポジトリ](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install)で確認できます。`@mcpmarket`はCherry Studio公式のMCPサービスコレクションです。
{% endhint %}