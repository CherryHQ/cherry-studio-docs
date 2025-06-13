---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# इंटरनेट मोड

{% hint style="info" %}
इंटरनेट की आवश्यकता वाले परिदृश्यों के उदाहरण:

* समय-संवेदी जानकारी: जैसे आज/इस सप्ताह/अभी-अभी सोने के भाव आदि।
* वास्तविक समय डेटा: जैसे मौसम, विनिमय दरें जैसे गतिशील मूल्य।
* नवीनतम ज्ञान: जैसे नई चीजें, नई अवधारणाएँ, नई तकनीकें आदि...
{% endhint %}

### 1. इंटरनेट कैसे सक्षम करें

Cherry Studio के प्रश्न विंडो में, 【पृथ्वी आइकन】 पर क्लिक करके इंटरनेट सक्षम करें।

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>पृथ्वी आइकन पर क्लिक करें - इंटरनेट सक्षम करें</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>इंगित करता है - इंटरनेट कार्यक्षमता सक्रिय है</p></figcaption></figure>

### 2. विशेष ध्यान दें: इंटरनेट के दो मोड हैं

#### मोड 1: मॉडल प्रदाता के बड़े मॉडल में अंतर्निहित इंटरनेट क्षमता

इस स्थिति में, इंटरनेट सक्षम करने के बाद, सीधे इंटरनेट सेवा का उपयोग किया जा सकता है, यह बहुत सरल है।

{% hint style="warning" %}
प्रश्नोत्तर इंटरफ़ेस के शीर्ष पर मॉडल नाम के बाद छोटा ग्लोब आइकन देखकर तुरंत पहचाना जा सकता है कि मॉडल इंटरनेट का समर्थन करता है या नहीं।
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

मॉडल प्रबंधन पृष्ठ पर, यह विधि आपको तेज़ी से पहचानने में सहायक होगी कि कौन से मॉडल इंटरनेट का समर्थन करते हैं और कौन से नहीं।

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio द्वारा वर्तमान में समर्थित इंटरनेट-सक्षम मॉडल प्रदाता**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (सभी मॉडल इंटरनेट का समर्थन करते हैं)</mark>
> * <mark style="color:green;">टेनसेंट हुनयुआन</mark>
> * <mark style="color:green;">ज़हिपू AI</mark>
> * <mark style="color:green;">अलीबाबा क्लाउड बेलियन आदि</mark>

{% hint style="danger" %}
विशेष ध्यान दें:

एक विशेष स्थिति होती है जहाँ मॉडल पर ग्लोब आइकन न होने के बावजूद यह इंटरनेट सक्षम हो सकता है, जैसा कि निम्नलिखित गाइड में बताया गया है।
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### मोड 2: Tavily सेवा का उपयोग कर इंटरनेट क्षमता

जब हम ऐसे मॉडल का उपयोग करते हैं जिसमें इंटरनेट क्षमता नहीं होती (नाम के बाद ग्लोब आइकन नहीं होता), लेकिन हमें कुछ वास्तविक समय जानकारी प्राप्त करने की आवश्यकता होती है, तब हमें Tavily वेब खोज सेवा की आवश्यकता होती है।

**Tavily सेवा का पहली बार उपयोग** करने पर, एक पॉपअप दिखाई देगा जहाँ आपको कुछ जानकारी सेट करनी होगी। निर्देशों का पालन करें - यह बहुत सरल है!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>पॉपअप, क्लिक करें: सेटिंग पर जाएँ</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>API कुंजी प्राप्त करें पर क्लिक करें</p></figcaption></figure>

API कुंजी प्राप्त करने पर आप **tavily की वेबसाइट** पर लॉगिन/पंजीकरण पृष्ठ पर स्वतः पहुँच जाएँगे। पंजीकरण और लॉगिन के बाद, API कुंजी बनाएँ और उसे Cherry Studio में कॉपी करें।

{% hint style="danger" %}
पंजीकरण में समस्या होने पर इसी निर्देशिका में Tavily पंजीकरण गाइड देखें।
{% endhint %}

**Tavily पंजीकरण संदर्भ दस्तावेज़:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

निम्न स्क्रीन पंजीकरण सफलता को दर्शाती है।

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>कुंजी कॉपी करें</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>कुंजी पेस्ट करें, सफलतापूर्वक पूर्ण</p></figcaption></figure>

परिणाम जाँचने के लिए पुनः प्रयास करें। परिणाम दर्शाते हैं कि इंटरनेट खोज सामान्य रूप से कार्य कर रही है, और खोज परिणामों की संख्या हमारी डिफ़ॉल्ट सेटिंग (5) है।

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
ध्यान दें: Tavily मासिक मुफ्त उपयोग सीमा प्रदान करता है, जिसके अधिक होने पर शुल्क लगेगा
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: कोई त्रुटि मिलने पर कृपया बिना झिझक संपर्क करें।