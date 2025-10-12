---
icon: robot
---
# Cherry Agent使用教程


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




Cherry Studio v1.7.0.alpha版本引入了Agent，可以在Cherry Studio中使用Claude Code。本教程將引導您完成設置和啟動的完整流程。

### 1. 創建Anthropic類型的供應商

&#x20;任意支援Anthropic端點的服務商都可以使用，以CherryIn為例，創建一個新的Agent服務商，填寫好密鑰和地址，添加任意模型即可。(⚠️Agent模式消耗token量很大，請注意token使用)

> 訂閱了Claude Code的用戶也可以將key和url地址填入獲取到模型

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.26.35@2x.png" alt=""><figcaption></figcaption></figure>

### 2. 開啟API 伺服器

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 19.56.22@2x.png" alt=""><figcaption></figcaption></figure>

### 3. 創建一個Agent

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.24.43@2x.png" alt=""><figcaption></figcaption></figure>

右鍵Agent可以進入編輯界面，編輯Agent的權限和可以使用的工具/mcp服務。

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.25.10@2x (1).png" alt=""><figcaption></figcaption></figure>

### 結果展示

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.30.26@2x (1).png" alt=""><figcaption></figcaption></figure>