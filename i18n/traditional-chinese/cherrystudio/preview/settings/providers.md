---
icon: cloud-check
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 服務商設定

目前頁面僅用於介紹介面功能，設定教學可參考基礎教學中的 [服務商設定](../../../pre-basic/providers/) 教學。

{% hint style="info" %}
* 使用內建服務商時，只需填寫對應的祕鑰即可。
* 不同服務商對祕鑰的稱呼可能有所不同，祕鑰、Key、API Key、令牌等均指同一種憑證。
{% endhint %}

### API 祕鑰

在 Cherry Studio 中，單一服務商支援多 Key 輪詢使用，輪詢方式為從前到後依序循環。

* 多組 Key 需以英文逗號分隔新增。如下方範例：

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
必須使用 **英文** 逗號。
{% endhint %}

### API 網址

使用內建服務商時通常不需填寫 API 網址，如需要修改請嚴格按照對應官方文件提供的網址填寫。

> 若服務商提供 <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> 格式的網址，只需填寫根網址部分（<mark style="background-color:red;">https://xxx.xxx.com</mark>）。
>
> Cherry Studio 會自動拼接剩餘路徑（<mark style="background-color:green;">/v1/chat/completions</mark>），未按要求填寫可能導致功能異常。

{% hint style="info" %}
說明：大多數服務商的大型語言模型路由是統一的，通常不需以下操作。若服務商 API 路徑為 v2、v3/chat/completions 或其他版本，請在網址欄手動輸入對應版本並以"`/`"結尾；當服務商請求路由非常規的<mark style="background-color:green;">/v1/chat/completions</mark>時，請使用服務商提供的完整網址，並以 `#`結尾。

即：
* API 網址以 `/` 結尾時，只拼接"<mark style="background-color:green;">chat/completions</mark>"
* API 網址以 `#` 結尾時，不執行拼接操作，直接使用輸入的網址。

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### 新增模型

通常點擊服務商設定頁面左下角的 `管理` 按鈕，系統會自動取得該服務商所有可調用模型，從列表中點擊 `+` 按鈕即可新增至模型清單。

{% hint style="info" %}
點擊管理按鈕時，彈出視窗中的模型不會全部自動新增，需點擊模型右側的 `+` 按鈕新增至服務商設定頁面的模型清單後，才會出現在模型選擇清單中。
{% endhint %}

### 連線檢查

點擊 API 祕鑰輸入框後方的檢查按鈕，即可測試設定是否成功。

{% hint style="info" %}
模型檢查預設使用已新增模型清單中的最後一個對話模型。若檢查失敗，請確認模型清單中是否有錯誤或不支援的模型。
{% endhint %}

{% hint style="danger" %}
設定完成後務必開啟右上角的開關，否則該服務商仍處於未啟用狀態，無法在模型清單中找到對應模型。
{% endhint %}