---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# Vertex AI

## ट्यूटोरियल अवलोकन

### 1. APIKey प्राप्त करना

* Gemini का API key प्राप्त करने से पहले, आपके पास एक Google Cloud प्रोजेक्ट होना आवश्यक है (यदि पहले से है तो छोड़ें)
* प्रोजेक्ट बनाने के लिए [Google Cloud](https://console.cloud.google.com/projectcreate) पर जाएं, प्रोजेक्ट नाम भरें और "प्रोजेक्ट बनाएं" क्लिक करें

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI कंसोल](https://console.cloud.google.com/vertex-ai) पर जाएं
* बनाए गए प्रोजेक्ट में [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) सक्षम करें

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API एक्सेस अनुमतियाँ सेट करना

* [सर्विस अकाउंट](https://console.cloud.google.com/iam-admin/serviceaccounts) अनुमतियों वाले पेज पर जाकर नया सर्विस अकाउंट बनाएं

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* सर्विस अकाउंट प्रबंधन पेज पर नए बनाए गए सर्विस अकाउंट में `कुंजी` पर क्लिक कर JSON फॉर्मेट में नई कुंजी बनाएं

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* सफलतापूर्वक बनने पर कुंजी फाइल JSON फॉर्मेट में आपके कंप्यूटर पर स्वतः सेव हो जाएगी, कृपया **इसे सुरक्षित रखें**

## 3. Cherry Studio में Vertex AI कॉन्फ़िगर करना

* Vertex AI प्रदाता चुनें
* JSON फाइल के संबंधित फ़ील्ड भरें

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[मॉडल](https://console.cloud.google.com/vertex-ai/model-garden) जोड़ने पर क्लिक करें, और फिर आप बढ़िया उपयोग शुरू कर सकते हैं!\