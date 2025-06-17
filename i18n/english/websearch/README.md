---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Web Search Mode

{% hint style="info" %}
Examples of scenarios that require web access:

*   Time-sensitive information: For example, the price of gold futures today/this week/just now.
*   Real-time data: For example, weather, exchange rates, and other dynamic values.
*   Emerging knowledge: For example, new things, new concepts, new technologies, etc...
{% endhint %}

### 1. How to Enable Web Search

In the Cherry Studio question window, click the [Little Globe] icon to enable web search.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Click the globe icon - enable web search</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Indicates - web search is enabled</p></figcaption></figure>

### 2. Special Note: There Are Two Web Search Modes

#### Mode 1: The model provider's large model has a built-in web search function

In this case, after enabling web search, you can use the service directly. It's very simple.

{% hint style="warning" %}
You can quickly determine if a model supports web search by checking for a small globe icon next to the model's name at the top of the chat interface.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

On the model management page, this method also allows you to quickly distinguish which models support web search and which do not.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio currently supports the following model providers with web search capabilities:**</mark>
>
> *   <mark style="color:green;">Google Gemini</mark>
> *   <mark style="color:green;">OpenRouter (all models support web search)</mark>
> *   <mark style="color:green;">Tencent Hunyuan</mark>
> *   <mark style="color:green;">Zhipu AI</mark>
> *   <mark style="color:green;">Alibaba Cloud Bailian, etc.</mark>

{% hint style="danger" %}
Special Note:

There is a special case where a model can access the web even without the small globe icon, as explained in the tutorial below.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Mode 2: The model does not have a built-in web search function; use the Tavily service to enable it

When we use a large model without a built-in web search function (no small globe icon next to its name), but we need it to retrieve real-time information for processing, we need to use the Tavily web search service.

**When using the Tavily service for the first time**, a pop-up will prompt you to configure some settings. Please follow the instructions—it's very simple!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Pop-up window, click: Go to Settings</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Click to get the API key</p></figcaption></figure>

After clicking to get the API key, you will be automatically redirected to the **official Tavily website's** login/registration page. After registering and logging in, create an API key, then copy the key and paste it into Cherry Studio.

{% hint style="danger" %}
If you don't know how to register, refer to the Tavily web search login and registration tutorial in the same directory as this document.
{% endhint %}

**Tavily registration reference document:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

The interface below indicates that the registration was successful.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Copy the key</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Paste the key, and you're all set</p></figcaption></figure>

Let's try again to see the effect. The result shows that the web search is now working correctly, and the number of search results is our default setting: 5.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Note: Tavily has a monthly free usage limit. You will need to pay if you exceed it~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: If you find any errors, please feel free to contact us.