
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 組み込みMCP設定

### @cherry/mcp-auto-install

MCPサービス自動インストーラー（ベータ版）

### @cherry/memory

ローカル知識グラフに基づく持続性記憶の基盤実装。これによりモデルは異なる会話間でユーザーの関連情報を記憶可能になります。

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

構造化思考プロセスを通じた動的・反省的問題解決ツールを提供するMCPサーバー実装。

### @cherry/brave-search

Brave検索APIを統合したMCPサーバー実装。ウェブ検索とローカル検索の二重機能を提供します。

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

URLウェブページコンテンツ取得用MCPサーバー。

### @cherry/filesystem

ファイルシステム操作を実装するModel Context Protocol（MCP）用Node.jsサーバー。