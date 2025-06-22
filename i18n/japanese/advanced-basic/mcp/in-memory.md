
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 組み込みMCP設定

### @cherry/mcp-auto-install

MCPサービスの自動インストール（ベータ版）

### @cherry/memory

ローカルナレッジグラフベースの持続的メモリ基盤の実装。これにより、モデルは異なる会話間でユーザーの関連情報を記憶できます。

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

構造化された思考プロセスを通じて動的かつ反射的な問題解決を可能にするツールを提供するMCPサーバーの実装。

### @cherry/brave-search

Brave検索APIを統合したMCPサーバーの実装で、ウェブ検索とローカル検索の両機能を提供します。

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

URLのウェブコンテンツを取得するためのMCPサーバー。

### @cherry/filesystem

ファイルシステム操作を実装するモデルコンテキストプロトコル（MCP）のNode.jsサーバー。