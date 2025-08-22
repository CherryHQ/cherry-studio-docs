# 設定和使用 MCP


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1.  開啟 Cherry Studio 設定。
2.  找到 `MCP 伺服器` 選項。
3.  點擊 `新增伺服器`。
4.  填入 MCP Server 的相關參數（[參考連結](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。可能需要填寫的內容包括：
    *   名稱：自訂名稱，例如 `fetch-server`
    *   類型：選擇 `STDIO`
    *   命令：填寫 `uvx`
    *   參數：填寫 `mcp-server-fetch`
    *   （可能還有其他參數，視具體 Server 而定）
5.  點擊 `儲存`。

{% hint style="success" %}
完成上述設定後，Cherry Studio 會自動下載所需的 MCP Server - `fetch server`。下載完成後即可開始使用！注意：當 mcp-server-fetch 設定不成功時，可嘗試重啟電腦。
{% endhint %}

### 在聊天框中啟用 MCP 服務

<figure><img src="../../.gitbook/assets/MCP-輸入框按鈕範例.png" alt=""><figcaption></figcaption></figure>

*   需在 `MCP 伺服器` 設定中成功新增 MCP 伺服器

<figure><img src="../../.gitbook/assets/MCP伺服器範例.png" alt=""><figcaption></figcaption></figure>

### **使用效果展示**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

由上圖可見，結合 MCP 的 `fetch` 功能後，Cherry Studio 能更準確理解用戶查詢意圖，並從網路獲取相關資訊，提供更精確全面的回答。