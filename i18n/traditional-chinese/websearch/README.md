---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 連網模式

{% hint style="info" %}
需要連網的場景舉例：

* 時效性訊息：比如今天/本週/剛剛 黃金期貨價格等。
* 即時數據：比如天氣，匯率等動態數值。
* 新興知識：比如新事物，新概念，新技術等等...
{% endhint %}

### 一、如何開啟連網

在 Cherry Studio 的提問視窗，點擊 【小地球】 圖示即可開啟連網。

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>點擊地球圖示 - 開啟連網</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>表示 - 已開啟連網功能</p></figcaption></figure>

### 二、特別注意：連網有兩種模式

#### 模式1：模型服務商的大模型自帶連網功能

這種情況下，開啟連網後，直接就可以使用連網服務了，非常簡單。

{% hint style="warning" %}
可以透過問答介面上方，模型名字後面是否帶有小地圖標記，迅速判斷該模型是否支援連網。
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

在模型管理頁面，這個方法也可以讓你快速分辨出哪些模型支援連網，哪些不支援。

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio 目前已支援的連網模型服務商有**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter（全部模型支援連網）</mark>
> * <mark style="color:green;">騰訊混元</mark>
> * <mark style="color:green;">智譜AI</mark>
> * <mark style="color:green;">阿里雲百煉等</mark>

{% hint style="danger" %}
特別注意：

存在一種特殊的情況，即便模型上沒帶小地球標記，但是它也能實現連網，比如下面這個攻略教學解釋的情況。
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### 模式2：模型不帶連網功能，使用 Tavily服務 實現連網功能

當我們使用一個不帶連網功能的大模型時（名字後面沒有小地球圖示），而我們又需要它獲取一些即時性的訊息進行處理，此時就需要用到Tavily網絡搜尋服務。

**初次使用Tavily服務**，會彈窗提示去設定一些資訊，請根據指引操作即可-非常簡單！

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>彈窗，點擊：去設定</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>點擊獲取密鑰</p></figcaption></figure>

點擊獲取密鑰後，會自動跳轉到**tavily的官網**登入註冊頁面，註冊並登入後，建立APIkey，然後複製key到Cherry Studio即可。

{% hint style="danger" %}
不會註冊，參考本文檔同目錄下tavily連網登入註冊教學。
{% endhint %}

**tavily註冊參考文件：**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

顯示下面的介面表示註冊成功。

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>複製key</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>貼上key，大功告成</p></figcaption></figure>

再來試一次看看效果。結果表明，已經正常連網搜尋了，並且搜尋結果數是我們設定的預設值：5個。

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
注意：tavily 每個月有免費限制，超過了要付費~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS：如果發現錯誤，歡迎大家隨時聯絡。