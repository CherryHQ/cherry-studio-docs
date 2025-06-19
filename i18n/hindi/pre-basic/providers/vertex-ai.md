---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# Vertex AI

## ट्यूटोरियल अवलोकन

### 1. APIKey प्राप्त करें

* Gemini का API key प्राप्त करने से पहले, आपके पास एक Google Cloud प्रोजेक्ट होना चाहिए (यदि आपके पास पहले से है तो इस चरण को छोड़ सकते हैं)
* [Google Cloud](https://console.cloud.google.com/projectcreate) पर जाकर प्रोजेक्ट बनाएँ, प्रोजेक्ट का नाम भरें और "प्रोजेक्ट बनाएँ" पर क्लिक करें

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI कंसोल](https://console.cloud.google.com/vertex-ai) पर जाएँ
* बनाए गए प्रोजेक्ट में Vertex AI API सक्षम करें ([https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA))

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>