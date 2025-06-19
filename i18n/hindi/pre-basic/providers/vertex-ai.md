---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# Vertex AI

## ट्यूटोरियल अवलोकन

### 1. API कुंजी प्राप्त करें

* जेमिनी की API कुंजी प्राप्त करने से पहले, आपके पास एक Google Cloud प्रोजेक्ट होना चाहिए (यदि आपके पास पहले से है तो इस चरण को छोड़ सकते हैं)
* [Google Cloud](https://console.cloud.google.com/projectcreate) पर जाएँ और प्रोजेक्ट बनाएँ, प्रोजेक्ट नाम भरें और "बनाएँ" पर क्लिक करें

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI कंसोल](https://console.cloud.google.com/vertex-ai) में जाएँ
* निर्मित प्रोजेक्ट में [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) सक्षम करें

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API एक्सेस अनुमतियाँ सेट करें

* [सर्विस खाता](https://console.cloud.google.com/iam-admin/serviceaccounts) अनुमति इंटरफ़ेस खोलें और एक सर्विस खाता बनाएँ

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* सर्विस खाता प्रबंधन पृष्ठ पर अभी बनाया गया सर्विस खाता ढूँढें, `कुंजी` पर क्लिक करें और एक नई JSON प्रारूप की कुंजी बनाएँ

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* सफलतापूर्वक बनाने के बाद, कुंजी फ़ाइल स्वचालित रूप से JSON फ़ाइल प्रारूप में आपके कंप्यूटर पर सहेजी जाएगी, कृपया **इसे सावधानी से सुरक्षित रखें**

## 3. Cherry Studio में Vertex AI कॉन्फ़िगर करें

* Vertex AI सेवा प्रदाता चुनें
* JSON फ़ाइल के संबंधित फ़ील्ड भरें

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[मॉडल](https://console.cloud.google.com/vertex-ai/model-garden) जोड़ने पर क्लिक करें, और आप खुशी-खुशी उपयोग शुरू कर सकते हैं!