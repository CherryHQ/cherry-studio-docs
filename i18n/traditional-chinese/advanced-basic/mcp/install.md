# MCP 環境安裝


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




**MCP(Model Context Protocol)** 是一種開源協議，旨在以標準化的方式向大語言模型（LLM）提供上下文資訊。更多關於 MCP 的介紹請見 [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## 在 Cherry Studio 中使用 MCP

下面以 `fetch` 功能為例，演示如何在 Cherry Studio 中使用 MCP，可以在 [文件](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 中查找詳情。

### **準備工作：安裝 uv、bun**

{% hint style="warning" %}
Cherry Studio 目前只使用內建的 [uv](https://github.com/astral-sh/uv) 和 [bun](https://github.com/oven-sh/bun)，**不會復用**系統中已經安裝的 uv 和 bun。
{% endhint %}

在 `設定 - MCP 伺服器` 中，點擊 `安裝` 按鈕，即可自動下載並安裝。因為是直接從 GitHub 上下載，速度可能會比較慢，且有較大可能失敗。安裝成功與否，以下文提到的資料夾內是否有檔案為準。

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**可執行程序安裝目錄：**

Windows: `C:\Users\使用者名稱\.cherrystudio\bin`

macOS、Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_資料夾.png" alt=""><figcaption><p>bin 目錄</p></figcaption></figure>

**無法正常安裝的情況下：**

可將系統中的相對應命令使用軟連結的方式連結到這裡，如果沒有對應目錄，需要手動建立。也可以手動下載可執行檔案放到這個目錄下面：

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)