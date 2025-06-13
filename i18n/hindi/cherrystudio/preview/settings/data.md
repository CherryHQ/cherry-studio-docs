---
icon: database
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# डेटा सेटिंग्स

इस इंटरफ़ेस के माध्यम से आप क्लाइंट डेटा का क्लाउड और लोकल बैकअप, लोकल डेटा डायरेक्टरी खोज, और कैश साफ़ करने जैसे ऑपरेशन कर सकते हैं।

### डेटा बैकअप

वर्तमान में डेटा बैकअप केवल WebDAV के माध्यम से समर्थित है। आप क्लाउड बैकअप के लिए WebDAV सपोर्ट वाली किसी भी सेवा का चयन कर सकते हैं।

आप `A कंप्यूटर` $$\xrightarrow{\text{बैकअप}}$$ `WebDAV` $$\xrightarrow{\text{पुनर्स्थापित}}$$ `B कंप्यूटर` विधि से कई डिवाइसों के बीच डेटा सिंक्रनाइज़ कर सकते हैं।

#### JianguoYun (Nutstore) उदाहरण

1. Nutstore में लॉग इन करें, शीर्ष-दाएं कोने में यूजरनेम पर क्लिक करें, और "खाता जानकारी" चुनें:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. "सुरक्षा विकल्प" चुनें, "ऐप जोड़ें" पर क्लिक करें:

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. एप्लिकेशन नाम दर्ज करें, यादृच्छिक पासवर्ड उत्पन्न करें:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. पासवर्ड कॉपी करके सहेजें:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. सर्वर पता, खाता और पासवर्ड प्राप्त करें:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio सेटिंग्स > डेटा सेटिंग्स में WebDAV जानकारी दर्ज करें:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. डेटा बैकअप या पुनर्स्थापित करें चुनें, और स्वचालित बैकअप के लिए समय अंतराल सेट करें:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV सर्वर के रूप में उपयोग करने योग्य सामान्य क्लाउड स्टोरेज सेवाएँ:

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/) (मेम्बरशिप आवश्यक)
* [阿里云盘](https://www.alipan.com/) (खरीद आवश्यक)
* [Box](https://www.box.com/) (मुफ़्त 10GB स्थान, 250MB/फ़ाइल सीमा)
* [Dropbox](https://www.dropbox.com/) (मुफ़्त 2GB, 16GB तक मित्र आमंत्रित करके)
* [TeraCloud](https://teracloud.jp/en/) (मुफ़्त 10GB + आमंत्रण द्वारा 5GB अतिरिक्त)
* [Yandex Disk](https://disk.yandex.com/) (मुफ्त 10GB)

स्व-होस्ट किए जाने योग्य विकल्प:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}