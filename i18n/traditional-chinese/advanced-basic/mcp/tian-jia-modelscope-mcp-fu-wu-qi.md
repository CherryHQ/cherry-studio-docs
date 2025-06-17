
{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 新增 ModelScope MCP 伺服器

> ModelScope MCP 伺服器需要將 Cherry Studio 升級至 v1.2.9 或更高版本。

在 v1.2.9 版本中，Cherry Studio 與 ModelScope 魔搭達成官方合作，大幅簡化了 MCP 伺服器新增的操作步驟，避免配置過程出錯，而且可以在 ModelScope 社群發現海量 MCP 伺服器。接下來跟隨操作步驟，一起看下如何在 Cherry Studio 中同步 ModelScope 的 MCP 伺服器。

## 操作步驟

### 同步入口：

點擊設定中的 MCP 伺服器設定，選 `同步服务器`

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### 發現 MCP 服務：

選擇 ModelScope，並瀏覽發現 MCP 服務

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### 查看 MCP 伺服器詳情

註冊登入 ModelScope，並查看 MCP 服務詳情；

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### 連接伺服器

在 MCP 服務詳情中，選擇連接服務；

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### 申請並複製貼上 api 令牌

點擊 Cherry Studio 中的「獲取api」令牌，跳轉 ModelScope 官網，複製 api 令牌，並回到 Cherry Studio 中貼上。

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### 成功同步

在 Cherry Studio 的 MCP 伺服器清單中，可以看到 ModelScope 連接的 MCP 服務並在對話中調用。

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### 增量更新

在後續 ModelScope 網頁新連接的 MCP 伺服器，直接點擊 `同步服务器` 就可以實現增量的 MCP 伺服器新增。

<figure><img src="../../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

通過以上步驟，你已經成功掌握了如何在 Cherry Studio 中便捷地同步 ModelScope 上的 MCP 伺服器，整個配置過程不僅大大簡化，有效避免了手動配置的繁瑣和潛在錯誤，更讓你能夠輕鬆接入 ModelScope 社群提供的海量 MCP 伺服器資源。

開始探索和使用這些強大的 MCP 服務，為你的 Cherry Studio 使用體驗帶來更多便利和可能性吧！