---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# Vertex AI

## अवलोकन

### 1. API कुंजी प्राप्त करें

* Gemini की API कुंजी प्राप्त करने से पहले, आपके पास एक Google Cloud प्रोजेक्ट होना चाहिए (यदि आपके पास पहले से है तो इस चरण को छोड़ सकते हैं)
* प्रोजेक्ट बनाने के लिए [Google Cloud](https://console.cloud.google.com/projectcreate) पर जाएँ, प्रोजेक्ट का नाम भरें और "प्रोजेक्ट बनाएँ" पर क्लिक करें

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI कंसोल](https://console.cloud.google.com/vertex-ai) में जाएँ
* बनाए गए प्रोजेक्ट में [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) सक्षम करें

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API पहुंच अनुमतियाँ सेट करें

* [सेवा खाता](https://console.cloud.google.com/iam-admin/serviceaccounts) अनुमति पृष्ठ पर जाकर एक सेवा खाता बनाएँ

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* सेवा खाता प्रबंधन पृष्ठ पर अभी बनाए गए खाते को ढूंढें, `कुंजी` पर क्लिक करें और एक नया JSON प्रारूप की कुंजी बनाएँ

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* सफलतापूर्वक बनाने पर, कुंजी फ़ाइल JSON फ़ॉर्मेट में आपके कंप्यूटर पर स्वचालित रूप से डाउनलोड हो जाएगी, कृपया **सावधानीपूर्वक सहेजें**

## 3. Cherry Studio में Vertex AI कॉन्फ़िगर करें

* Vertex AI सेवा प्रदाता चुनें
* JSON फ़ाइल के संबंधित फ़ील्ड भरें

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[मॉडल](https://console.cloud.google.com/vertex-ai/model-garden) जोड़ने के लिए क्लिक करें, और आप उपयोग करना शुरू कर सकते हैं!