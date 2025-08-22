---
icon: cloud-check
---
# 模型服務設置


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




當前頁面僅做介面功能的介紹，配置教學可以參考基礎教學中的 [服務商設定](../../../pre-basic/providers/) 教學。

{% hint style="info" %}
* 使用內建服務商時只需填寫對應的秘鑰即可。
* 不同服務商對秘鑰的稱呼可能有所不同，秘鑰、Key、API Key、令牌等均指同一種憑證。
{% endhint %}

### API 秘鑰

在 Cherry Studio 中，單個服務商支援多 Key 輪詢使用，輪詢方式為從前到後的列表循環模式。

* 多個 Key 需用英文逗號隔開添加。範例如下：

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
必須使用 **英文** 逗號。
{% endhint %}

### API 地址

使用內建服務商時通常不需要填寫 API 地址，如需修改請嚴格按照對應的官方文件地址填寫。

> 若服務商提供的地址格式為 <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>，僅需填寫根地址部分（<mark style="background-color:red;">https://xxx.xxx.com</mark>）即可。
>
> Cherry Studio 會自動拼接剩餘路徑（<mark style="background-color:green;">/v1/chat/completions</mark>），未按要求填寫可能導致功能異常。

{% hint style="info" %}
說明：多數服務商的大型語言模型路由是統一的，通常無需以下操作。若服務商的API路徑為v2、v3/chat/completions或其他版本時，可在地址欄手動輸入對應版本並以"`/`"結尾；當服務商請求路由非標準<mark style="background-color:green;">/v1/chat/completions</mark>時，使用服務商提供的完整地址並以 `#` 結尾。

規則：
* API地址以 `/` 結尾時，僅拼接"<mark style="background-color:green;">chat/completions</mark>"
* API地址以 `#` 結尾時，不執行拼接操作，直接使用填入的地址

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### 添加模型

通常點擊服務商設定頁面左下角的 `管理` 按鈕會自動取得該服務商所有支援調用的模型，從彈出列表中點擊模型右側的 `+` 號即可添加至模型列表。

{% hint style="info" %}
點擊管理按鈕時彈窗內的模型不會自動全部添加，需點擊模型右側的 `+` 號添加至服務商設定頁面的模型列表，方可在模型選擇列表中顯示。
{% endhint %}

### 連通性檢查

點擊API秘鑰輸入框後的檢查按鈕即可測試是否設定成功。

{% hint style="info" %}
模型檢查預設使用模型列表中已添加的最後一個對話模型，若檢查失敗請確認模型列表中是否存在錯誤或不支援的模型。
{% endhint %}

{% hint style="danger" %}
設定成功後務必開啟右上角開關，否則該服務商仍處於停用狀態，無法在模型列表中找到對應模型。
{% endhint %}