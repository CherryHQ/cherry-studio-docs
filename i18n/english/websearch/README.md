---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---
# Network Access


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




{% hint style="info" %}
Examples of scenarios requiring network access:

*   Time-sensitive information: such as today's/this week's/just now's gold futures prices.
*   Real-time data: such as dynamic values for weather, exchange rates.
*   Emerging knowledge: such as new things, new concepts, new technologies, etc.
{% endhint %}

### I. How to enable network access

In Cherry Studio's prompt window, click the "globe" icon to enable network access.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Click the globe icon - Enable network access</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Indicates - Network access function is enabled</p></figcaption></figure>

### II. Special attention: There are two modes for network access

#### Mode 1: Large models from model service providers come with network access

In this case, once network access is enabled, you can directly use the network service, which is very simple.

{% hint style="warning" %}
You can quickly determine if a model supports network access by checking if there's a small map icon next to the model name above the chat interface.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

On the model management page, this method also allows you to quickly distinguish which models support network access and which do not.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Currently supported network-enabled model service providers in Cherry Studio include**</mark>
>
> *   <mark style="color:green;">Google Gemini</mark>
> *   <mark style="color:green;">OpenRouter (All models support network access)</mark>
> *   <mark style="color:green;">Tencent Hunyuan</mark>
> *   <mark style="color:green;">Zhipu AI</mark>
> *   <mark style="color:green;">Alibaba Cloud BaiLian, etc.</mark>

{% hint style="danger" %}
Special note:

There is a special case where a model can still achieve network access even if it doesn't have a small globe icon, as explained in the tutorial below.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Mode 2: Models without network access use Tavily service to achieve network access

When we use a large model that does not have network access (no small globe icon next to its name), but we need it to retrieve and process some real-time information, then the Tavily web search service is needed.

**When using Tavily service for the first time**, a pop-up will prompt you to set up some information. Please follow the instructions - it's very simple!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Pop-up, click: Go to Settings</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Click to get API key</p></figcaption></figure>

After clicking to get the API key, it will automatically jump to **Tavily's official website** login and registration page. After registering and logging in, create an API key, then copy the key to Cherry Studio.

{% hint style="danger" %}
If you don't know how to register, refer to the Tavily network access login and registration tutorial in the same directory as this document.
{% endhint %}

**Tavily registration reference document:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

The following interface indicates successful registration.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Copy key</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Paste key, job done!</p></figcaption></figure>

Let's try it again to see the effect. The results show that network search is normal, and the number of search results is our default value: 5.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Note: Tavily has a free tier limit per month, exceeding it requires payment~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: If you find any errors, please feel free to contact us.