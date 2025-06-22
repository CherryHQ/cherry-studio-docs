---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Internet Mode

{% hint style="info" %}
Examples of scenarios that require internet access:

* Time-sensitive information: such as today's/this week's/just now's gold futures prices.
* Real-time data: such as weather, exchange rates, and other dynamic values.
* Emerging knowledge: such as new things, new concepts, new technologies, etc.
{% endhint %}

### How to Enable Internet Access

In the Cherry Studio question window, click the 【Globe】 icon to enable internet access.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Click the globe icon - Enable internet</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Indicates - Internet function is enabled</p></figcaption></figure>

### Important Note: Two Modes for Internet Access

#### Mode 1: Models with built-in internet function from providers

When using such models, enabling internet access requires no extra steps - it's straightforward.

{% hint style="warning" %}
Quickly identify internet-enabled models by checking for a small globe icon next to the model name above the chat interface.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

This method also helps quickly distinguish internet-enabled models in the Model Management page.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio currently supports internet-enabled models from**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (all models support internet)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Bailian, etc.</mark>

{% hint style="danger" %}
Important note:

Special cases exist where models may access internet without the globe icon, as explained in the tutorial below.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Mode 2: Models without internet function use Tavily service

When using models without built-in internet (no globe icon), use Tavily search service to process real-time information.

**First-time Tavily setup** triggers a setup prompt - simply follow the instructions!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Popup window, click: Go to settings</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Click to get API key</p></figcaption></figure>

After clicking, you'll be redirected to **Tavily's website** to register/login. Create and copy your API key back to Cherry Studio.

{% hint style="danger" %}
Registration guide available in Tavily tutorial within this documentation directory.
{% endhint %}

**Tavily registration reference:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

The following interface confirms successful registration.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Copy API key</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Paste key - setup complete!</p></figcaption></figure>

Test again for results: shows normal internet search with default result count (5).

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Note: Tavily has monthly free tier limits - exceeding requires payment~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Please report any issues you encounter.