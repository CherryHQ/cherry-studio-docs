# 配置和使用 MCP


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. 開啟 Cherry Studio 設定。
2. 找到 `MCP 伺服器` 選項。
3. 點擊 `新增伺服器`。
4. 將 MCP Server 的相關參數填入（[參考連結](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)）。可能需要填寫的內容包括：
   * 名稱：自訂一個名稱，例如 `fetch-server`
   * 類型：選擇 `STDIO`
   * 命令：填寫 `uvx`
   * 參數：填寫 `mcp-server-fetch`
   * （可能還有其他參數，視具體 Server 而定）
5. 點擊 `儲存`。

{% hint style="success" %}
完成上述配置後，Cherry Studio 會自動下載所需的 MCP Server - `fetch server`。下載完成後，我們就可以開始使用了！注意：當 mcp-server-fetch 配置不成功時，可以嘗試重啟電腦。
{% endhint %}

### 在聊天框中啟用 MCP 服務

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt="MCP-輸入框按鈕範例"><figcaption></figcaption></figure>

* 在 `MCP 伺服器` 設定成功新增 MCP 伺服器

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt="MCP伺服器範例"><figcaption></figcaption></figure>

### **使用效果展示**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="使用效果展示"><figcaption></figcaption></figure>

從上圖可以看出，結合了 MCP 的 `fetch` 功能後，Cherry Studio 能夠更好地理解使用者的查詢意圖，並從網路上獲取相關資訊，給出更準確、更全面的回答。