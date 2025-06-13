---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 網路模式

{% hint style="info" %}
需要連網的場景舉例：

* 時效性資訊：例如今日/本週/即時黃金期貨價格等。
* 即時數據：例如天氣、匯率等動態數值。
* 新興知識：例如新事物、新概念、新技術等等...
{% endhint %}

### 一、如何開啟連網

在Cherry Studio的提問視窗，點擊【小地球】圖示即可開啟連網功能。

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>點擊地球圖示 - 開啟連網</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>表示 - 已開啟連網功能</p></figcaption></figure>

### 二、特別注意：連網有兩種模式

#### 模式1：模型服務商的大模型自帶連網功能

這種情況下，開啟連網後，直接就可以使用連網服務，非常簡單。

{% hint style="warning" %}
可通過問答介面上方，模型名稱後方是否帶有小地圖標記，快速判斷該模型是否支援連網。
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

在模型管理頁面，此方法也可讓你快速分辨哪些模型支援連網。

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio 目前已支援的連網模型服務商**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter（全部模型支援連網）</mark>
> * <mark style="color:green;">騰訊混元</mark>
> * <mark style="color:green;">智譜AI</mark>
> * <mark style="color:green;">阿里雲百煉等</mark>

{% hint style="danger" %}
特別注意：
存在特殊情況，即使模型未帶小地球標記，仍可能實現連網功能，例如下方攻略說明的情況。
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### 模式2：模型不具連網功能，需透過Tavily服務實現連網

當使用不具連網功能的大模型（名稱後無小地球圖示），又需獲取即時資訊時，需使用Tavily網路搜尋服務。

**初次使用Tavily服務**，會彈出視窗提示設定相關資訊，請依照指引操作 - 非常簡單！

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>彈出視窗，點選：前往設定</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>點擊獲取金鑰</p></figcaption></figure>

點擊獲取金鑰後，將自動跳轉至**tavily官網**登入頁面，註冊登入後建立APIkey，將金鑰複製回Cherry Studio即可。

{% hint style="danger" %}
若需註冊指引，請參閱本文件同目錄下的tavily註冊教學。
{% endhint %}

**Tavily註冊參考文件：**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

顯示下方介面表示註冊成功。

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>複製金鑰</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>貼上金鑰，設定完成</p></figcaption></figure>

再次測試連網效果。結果顯示已成功搜尋，搜尋結果數量為預設值：5筆。

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
注意：Tavily每月有免費額度限制，超出需付費～
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> 備註：若發現錯誤，歡迎隨時聯繫回報。