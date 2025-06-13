---
icon: cloud-check
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 服務商設置

當前頁面僅做介面功能的介紹，配置教學可以參考基礎教學中的 [服務商配置](../../../pre-basic/providers/) 教學。

{% hint style="info" %}
* 使用內建服務商時只需要填寫對應的秘鑰即可。
* 不同服務商對秘鑰的叫法可能有所不同，秘鑰、Key、API Key、令牌等都指的是同一個東西。
{% endhint %}

### API 秘鑰

在 Cherry Studio 當中，單個服務商支援多 Key 輪詢使用，輪詢方式為從前到後列表循環的方式。

* 多 Key 用英文逗號隔開添加。如以下示例方式：

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
必須使用 **英文** 逗號。
{% endhint %}

### API 地址

使用內建服務商時一般不需要填寫 API 地址，如果需要修改請嚴格按照對應的官方文件給的地址填寫。

> 如果服務商給的地址為 <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> 這種格式，只需要填寫根地址部分（<mark style="background-color:red;">https://xxx.xxx.com</mark>）即可。
>
> Cherry Studio 會自動拼接剩餘的路徑（<mark style="background-color:green;">/v1/chat/completions</mark>），未按要求填寫可能導致無法正常使用。

{% hint style="info" %}
說明：大多數服務商的大型語言模型路由是統一的，一般情況下不需要進行如下操作。如果服務商的API路徑是v2、v3/chat/completions或其他版本時，可在地址欄手動輸入對應版本並以"`/`"結尾；當服務商請求路由不是常規的<mark style="background-color:green;">/v1/chat/completions</mark>時使用服務商提供的完整地址，並以 `#`結尾。

即：
* API地址使用 `/` 結尾時只拼接"<mark style="background-color:green;">chat/completions</mark>"
* API地址使用 `#` 結尾時不執行拼接操作，只使用填入的地址。

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### 添加模型

一般情況下點擊服務商配置頁面最左下角的 `管理` 按鈕會自動獲取該服務商所有支援呼叫的模型，從獲取列表中點擊 `+` 號添加到模型列表即可。

{% hint style="info" %}
點擊管理按鈕時彈窗列表裡的模型不會全部添加，需要點擊模型右側的 `+` ，添加到服務商配置頁面的模型列表才可以在模型選擇列表中出現。
{% endhint %}

### 連通性檢查

點擊API 秘鑰輸入框後的檢查按鈕即可測試是否成功配置。

{% hint style="info" %}
模型檢查時預設使用模型列表已添加模型的最後一個對話模型，如果檢查時有失敗的情況請檢查模型列表是否有錯誤的或不支援的模型。
{% endhint %}

{% hint style="danger" %}
配置成功後務必打開右上角的開關，否則該服務商仍處於未啟用狀態，無法在模型列表中找到對應模型。
{% endhint %}