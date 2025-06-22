
{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 內建 MCP 配置

### @cherry/mcp-auto-install

自動安裝 MCP 服務（測試版）

### @cherry/memory

基於本體知識圖譜的持久性記憶基礎實現。這使得模型能夠在不同對話間記住用戶的相關資訊。

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

一個 MCP 伺服器實現，提供了透過結構化思維過程進行動態和反思性問題解決的工具。

### @cherry/brave-search

一個整合了 Brave 搜尋 API 的 MCP 伺服器實現，提供網頁與本地搜尋雙重功能。

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

用於取得 URL 網頁內容的 MCP 伺服器。

### @cherry/filesystem

實現檔案系統操作的模型上下文協議（MCP）的 Node.js 伺服器。