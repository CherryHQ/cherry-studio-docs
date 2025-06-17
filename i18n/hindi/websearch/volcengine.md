---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# वोल्क इंजन नेटवर्क एक्सेस सेटअप

### 1. "वोल्क इंजन" अकाउंट में लॉग इन/रजिस्टर करें <a href="#rclz7" id="rclz7"></a>

ऑफिशियल वेबसाइट पर जाएँ: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>वोल्क इंजन ऑफिशियल वेबसाइट</p></figcaption></figure>

### 2. "इंटरनेट-सक्षम" "मेरा ऐप्लिकेशन" बनाएँ <a href="#gvzaa" id="gvzaa"></a>

2.1. वोल्क इंजन में लॉग इन करके "वोल्क आर्क" पेज पर जाएँ: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **इनका क्रमबद्ध तरीके से पालन करें:**<mark style="color:red;">**「मेरा ऐप्लिकेशन」 → 「ऐप्लिकेशन बनाएँ」 → 「ज़ीरो-कोड」 → 「सिंगल चैट」**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. जानकारी भरें और ऐप्लिकेशन पब्लिश करें <a href="#zzdfe" id="zzdfe"></a>

**ऐप्लिकेशन नाम**: आवश्यकतानुसार कोई भी नाम (<mark style="color:red;">**\*अनिवार्य**</mark>, अन्य फ़ील्ड छोड़े जा सकते हैं)

<mark style="color:red;">**कुंजी बिंदु: नेटवर्क प्लगइन सक्षम करें (पहले सक्रिय करना आवश्यक)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. नेटवर्क प्लगइन सुविधा सक्रिय करें (लागत और फ्री उपयोग सीमा का ध्यान रखें) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>"अभी खरीदें" पर क्लिक करके स्टेप-बाय-स्टेप निर्देशों का पालन करें। यह स्क्रीन दिखने पर सक्रियण सफल माना जाएगा।</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>वर्तमान स्थिति नोट करें - इस चरण में सक्रियण पूर्ण हो चुका है</p></figcaption></figure>

"जानकारी भरें" इंटरफ़ेस पर वापस जाकर प्रक्रिया जारी रखें।

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. नेटवर्क खोज "एडवांस्ड कॉन्फ़िगरेशन" व्याख्या <a href="#sp6uz" id="sp6uz"></a>

व्यक्तिगत सुझाव के अनुसार विकल्प चुनें:

* इनपुट/आउटपुट सटीकता नियंत्रित करने हेतु **"कस्टम कॉल"** का उपयोग करें
* सरलता के लिए **"ऑटोमेटिक कॉल"** (डिफ़ॉल्ट) छोड़ें
* उच्च टाइमलीनस की आवश्यकता हो तो **"फोर्स ऑन"** चुनें

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. ऐप्लिकेशन पब्लिश करें <a href="#fe1gf" id="fe1gf"></a>

ऊपरी-दाएँ "पब्लिश करें" बटन दबाएँ। ऐप्लिकेशन सफलतापूर्वक बन जाएगा।

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. API Key प्राप्त करें <a href="#jtqlu" id="jtqlu"></a>

क्रम से क्लिक करें: **「API कॉल गाइड」 → 「API Key चुनें और कॉपी करें」 → 「व्यू एंड सेलेक्ट」**

API Key को कॉपी कर लें और cherry studio में पेस्ट करें (नीचे चित्रानुसार):

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

टिप: यदि API Key दिखाई न दे तो पॉपअप के ऊपर-दाएँ कोने में **"API Key बनाएँ"** पर क्लिक कर बनाकर कॉपी कर लें।

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. cherry studio में API Key द्वारा deepseek-R1 नेटवर्क एक्सेस <a href="#lrefj" id="lrefj"></a>

#### 5.1. cherry studio खोलें → "सेटिंग्स" → "कोई भी नाम" → "टाइप: openAI" <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. URL और KEY कॉन्फ़िगर करें <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">नोट: यदि URL न मिले या बीजिंग नोड न हो, तो यहाँ सटीक पता देखें ("/" अक्षर न भूलें):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. मॉडल नाम जोड़ें <a href="#qmh3i" id="qmh3i"></a>

नोट: छोटे अक्षरों वाला मॉडल नाम कॉपी करें (इग्नोर करने पर एरर आएगा)

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. प्रभाव पूर्वावलोकन <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>