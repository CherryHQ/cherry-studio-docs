---
icon: cloud-check
---
# 模型服務設置


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




當前頁面僅做介面功能的介紹，配置教學可以參考基礎教學中的 [服務商配置](../../../pre-basic/providers/) 教學。

{% hint style="info" %}
* 在使用內建服務商時只需要填寫對應的密鑰即可。
* 不同服務商對密鑰的叫法可能有所不同，密鑰、Key、API Key、令牌等都指的是同一個東西。
{% endhint %}

### API 密鑰

在 Cherry Studio 當中，單個服務商支援多 Key 輪詢使用，輪詢方式為從前到後列表循環的方式。

* 多 Key 用英文逗號隔開新增。如以下範例方式：

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
必須使用 **英文** 逗號。
{% endhint %}

### API 地址

在使用內建服務商時一般不需要填寫 API 地址，如果需要修改請嚴格按照對應的官方文件給的地址填寫。

> 如果服務商給的地址為 <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> 這種格式，只需要填寫根地址部分（<mark style="background-color:red;">https://xxx.xxx.com</mark>）即可。
>
> Cherry Studio 會自動拼接剩餘的路徑（<mark style="background-color:green;">/v1/chat/completions</mark>），未按要求填寫可能會導致無法正常使用。

{% hint style="info" %}
說明：大多數服務商的大語言模型路由是統一的，一般情況下不需要進行如下操作。如果服務商的API路徑是v2、v3/chat/completions或者其他版本時，可在地址欄手動輸入對應版本以"`/`"結尾；當服務商請求路由不是常規的<mark style="background-color:green;">/v1/chat/completions</mark>時使用服務商提供的完整地址，並以 `#`結尾。

即：
* API地址使用 `/` 結尾時只拼接"<mark style="background-color:green;">chat/completions</mark>"
* API地址使用 `#` 結尾時不執行拼接操作，只使用填入的地址。

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### 新增模型

一般情況下點擊服務商配置頁面最左下角的 `管理` 按鈕會自動取得該服務商所有支援調用的模型，從取得列表中點擊 `+` 號新增到模型列表即可。

{% hint style="info" %}
點擊管理按鈕時彈窗列表裡的模型不會全部新增，需要點擊模型右側的 `+` ，新增到服務商配置頁面的模型列表才可以在模型選擇列表中出現。
{% endhint %}

### 連通性檢查

點擊API 密鑰輸入框後的檢查按鈕即可測試是否成功配置。

{% hint style="info" %}
模型檢查時預設使用模型列表已新增模型的最後一個對話模型，如果檢查時有失敗的情況請檢查模型列表是否有錯誤的或不支援的模型。
{% endhint %}

{% hint style="danger" %}
配置成功後務必開啟右上角的開關，否則該服務商仍處於未啟用狀態，無法在模型列表中找到對應模型。
{% endhint %}