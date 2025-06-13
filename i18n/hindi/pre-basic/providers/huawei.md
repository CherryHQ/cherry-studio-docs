
{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# Huawei Cloud

### 1. [हुवाई क्लाउड](https://auth.huaweicloud.com/authui/login) पर अकाउंट बनाकर लॉग इन करें

### 2. [इस लिंक](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) पर क्लिक करके MaaS कंसोल में जाएँ

### 3. अथॉराइज़ेशन

<details>

<summary>अथॉराइज़ेशन चरण (पहले से अथॉराइज़्ड होने पर छोड़ें)</summary>

1. चरण (2) का लिंक खोलने के बाद, प्रॉम्प्ट के अनुसार अथॉराइज़ेशन पेज पर जाएँ (IAM सब-यूजर → नया ट्रस्ट जोड़ें → नॉर्मल यूजर)

![](<../../.gitbook/assets/image (49).png>)

2. क्रिएट पर क्लिक करने के बाद चरण (2) के लिंक पेज पर वापस जाएँ
3. एक्सेस परमिशन न होने का प्रॉम्प्ट दिखेगा, प्रॉम्प्ट में "यहाँ क्लिक करें" पर क्लिक करें
4. एग्जिस्टिंग अथॉराइज़ेशन ऐड करें और कन्फर्म करें

![](<../../.gitbook/assets/image (50).png>)

ध्यान दें: यह विधि शुरुआती लोगों के लिए है, बहुत कॉन्टेंट पढ़ने की ज़रूरत नहीं है, सिर्फ प्रॉम्प्ट के अनुसार क्लिक करें। अगर आप एक बार में अथॉराइज़ कर सकते हैं तो अपने तरीके से करें।

</details>

### 4. साइडबार में Authentication Management पर क्लिक करें, API Key (सीक्रेट) क्रिएट करें और कॉपी करें

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

अब CherryStudio में न्यू प्रोवाइडर क्रिएट करें

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

क्रिएट होने के बाद सीक्रेट को फील में डालें

### 5. साइडबार में Model Deployment पर क्लिक करें, सभी को कलेक्ट करें

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

### 6. Call पर क्लिक करें

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

जगह ① का एड्रेस कॉपी करें और CherryStudio प्रोवाइडर एड्रेस में पेस्ट करें, अंत में "#" जोड़ें  
अंत में "#" जोड़ें  
अंत में "#" जोड़ें  
अंत में "#" जोड़ें  
अंत में "#" जोड़ें

क्यों "#" जोड़ें? [यहाँ देखें](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> आप उस पेज को नहीं देख सकते हैं, तो सीधे ट्यूटोरियल के अनुसार करें;  
> v1/chat/completions को डिलीट करके भी भर सकते हैं, अगर पता है तो अपने तरीके से करें, नहीं पता तो ट्यूटोरियल फॉलो करें।

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

फिर जगह ② का मॉडल नाम कॉपी करें और CherryStudio में "+ऐड" बटन पर क्लिक करके न्यू मॉडल क्रिएट करें

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

मॉडल नाम डालें, कोई एक्स्ट्रा शब्द न जोड़ें, कोई कोट्स न डालें, जैसे उदाहरण में है वैसा ही कॉपी करें

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

ऐड मॉडल बटन पर क्लिक करें, मॉडल ऐड हो जाएगा।

{% hint style="info" %}
हुवाई क्लाउड में हर मॉडल का एड्रेस अलग होता है, इसलिए हर मॉडल के लिए नया प्रोवाइडर क्रिएट करें। ऊपर के चरणों को रिपीट करें।
{% endhint %}