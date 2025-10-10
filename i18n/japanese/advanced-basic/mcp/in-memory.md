# 内蔵MCP設定


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




### @cherry/mcp-auto-install

MCPサービスの自動インストール（ベータ版）

### @cherry/memory

ローカルナレッジグラフに基づく永続的メモリの基盤実装。これによりモデルは異なる対話間でユーザーの関連情報を記憶できます。

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

構造化思考プロセスを通じた動的・内省的問題解決ツールを提供するMCPサーバー実装。

### @cherry/brave-search

Brave検索APIを統合したMCPサーバー実装で、ウェブ検索とローカル検索のデュアル機能を提供します。

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

URLのウェブコンコンテンンツを取得するためのMCPサーサーバー。

### @cherry/filesystem

ファイルシステム操作を実装するモデルコンコンテキストプロトコル（MCP）のNode.jsサーバー。