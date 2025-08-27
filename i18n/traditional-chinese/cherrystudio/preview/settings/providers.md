---
icon: cloud-check
---
# 模型服務設置


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




當前頁面僅做介面功能的介紹，配置教程可以參考基礎教程中的[服務商配置](../../../pre-basic/providers/)教學。

{% hint style="info" %}
* 使用內建服務商時只需填寫對應的密鑰即可。
* 不同服務商對密鑰的稱呼可能不同，如密鑰、Key、API Key、令牌等，均指同一項設定。
{% endhint %}

### API 密鑰

在 Cherry Studio 中，單個服務商支援多組 Key 輪流使用，輪詢方式依列表順序循環執行。

* 多組 Key 需以**英文逗號**分隔輸入。範例如下：

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
必須使用**英文**逗號分隔。
{% endhint %}

### API 地址

使用內建服務商時通常不需填寫 API 地址，若需修改請嚴格按照對應官方文件提供的地址填寫。

> 若服務商提供的地址格式為 <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>，只需填寫根地址部分（<mark style="background-color:red;">https://xxx.xxx.com</mark>）。
>
> Cherry Studio 會自動拼接後續路徑（<mark style="background-color:green;">/v1/chat/completions</mark>），未按規範填寫可能導致功能異常。

{% hint style="info" %}
說明：多數服務商的大型語言模型路由是統一的，通常無需額外設定。若服務商的 API 路徑為 v2、v3/chat/completions 或其他版本時，可在地址欄手動輸入對應版本並以「`/`」結尾；當請求路由非標準 <mark style="background-color:green;">/v1/chat/completions</mark> 時，請直接用「`#`」結尾填入完整地址。

規則如下：
* API 地址以 `/` 結尾時，自動拼接「<mark style="background-color:green;">chat/completions</mark>」
* API 地址以 `#` 結尾時，直接使用完整地址不拼接

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### 新增模型

點擊服務商配置頁面左下角的 `管理` 按鈕，通常會自動獲取該服務商所有支援調用的模型，從彈出清單中點擊模型右側的 `+` 即可添加至模型列表。

{% hint style="info" %}
管理清單中的模型不會自動全部添加，需手動點擊 `+` 才能將模型加入服務商配置頁面，後續才可在模型選擇清單中使用。
{% endhint %}

### 連通性檢查

點擊 API 密鑰輸入框旁的檢查按鈕，即可測試配置是否成功。

{% hint style="info" %}
模型檢查時預設使用模型清單中最後一個對話模型。若檢查失敗，請確認模型清單是否有錯誤或不支援的模型。
{% endhint %}

{% hint style="danger" %}
配置完成後**務必開啟**右上角的開關，否則服務商將處於未啟用狀態，無法在模型清單中顯示對應模型。
{% endhint %}