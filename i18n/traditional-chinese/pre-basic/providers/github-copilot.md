
{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# GitHub Copilot

使用 GitHub Copilot 需要先擁有一個 GitHub 帳號，並訂閱 GitHub Copilot 服務，free 版本的訂閱也可以，但 free 版本不支援最新的 Claude 3.7 模型，具體請參考 [GitHub Copilot 官網](https://github.com/features/copilot)。

## 獲取 Device Code

點擊「登入 GitHub」，獲取 Device Code 並複製。

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="獲取 Device Code 範例圖片"><figcaption><p>獲取 Device Code</p></figcaption></figure>

## 在瀏覽器中填寫 Device Code 並授權

成功獲取 Device Code 後，點擊連結打開瀏覽器，在瀏覽器中登入 GitHub 帳號，輸入 Device Code 並授權。

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="GitHub授權.png 範例圖片"><figcaption><p>GitHub 授權</p></figcaption></figure>

授權成功後，返回 Cherry Studio，點擊「連接 GitHub」，成功後會顯示 GitHub 使用者名稱和頭像。

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="GitHub連接成功範例圖片"><figcaption><p>GitHub 連接成功</p></figcaption></figure>

## 點擊「管理」獲取模型列表

點擊下方的「管理」按鈕，會自動聯網獲取當前支援的模型列表。

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="管理按鈕獲取模型列表示範圖片"><figcaption><p>獲取模型列表</p></figcaption></figure>

## 常見問題

### 獲取 Device Code 失敗，請重試

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="獲取 Device Code 失敗範例圖片"><figcaption><p>獲取 Device Code 失敗</p></figcaption></figure>

目前使用 Axios 構建請求，Axios 不支援 socks 代理，請使用系統代理或 HTTP 代理，或者直接不在 CherryStudio 中設定代理，使用全域代理。首先請確保您的網路連線正常，以避免獲取 Device Code 失敗的情況。