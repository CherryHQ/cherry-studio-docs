---
icon: robot
---
# Cherry Agent 使用教學


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




Cherry Studio v1.7.0.alpha 版本引入了 Agent，可以在 Cherry Studio 中使用 Cherry Agent。本教學將引導您完成設定和啟動的完整流程。

### 1. 創建 Anthropic 類型的供應商

&#x20;任何支援 Anthropic 端點的服務商皆可使用，以 CherryIn 為例，創建一個新的 Agent 服務商，填寫好金鑰和位址，新增任何模型即可。

{% hint style="warning" %}
Agent 模式消耗大量 token，請注意 token 使用
{% endhint %}

{% hint style="info" %}
已訂閱 Claude Code 的用戶亦可將 key 和 url 位址填入以獲取模型
{% endhint %}

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.26.35@2x.png" alt=""><figcaption></figcaption></figure>

### 2. 開啟 API 伺服器

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 19.56.22@2x.png" alt=""><figcaption></figcaption></figure>

### 3. 創建一個 Agent

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.24.43@2x.png" alt=""><figcaption></figcaption></figure>

右鍵 Agent 可進入編輯介面，編輯 Agent 的權限和可使用的工具或 mcp 服務。

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.25.10@2x (1).png" alt=""><figcaption></figcaption></figure>

### 結果展示

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.30.26@2x (1).png" alt=""><figcaption></figcaption></figure>