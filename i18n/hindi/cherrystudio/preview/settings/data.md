---
icon: database
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# डेटा सेटिंग

यह इंटरफ़ेस क्लाइंट डेटा की क्लाउड और स्थानीय बैकअप, स्थानीय डेटा डायरेक्टरी क्वेरी और कैशे साफ़ करने जैसे ऑपरेशन करने की सुविधा देता है।

### डेटा बैकअप

वर्तमान में डेटा बैकअप केवल WebDAV के माध्यम से समर्थित है। आप क्लाउड बैकअप के लिए WebDAV समर्थित सेवाओं का चयन कर सकते हैं।

आप `A कंप्यूटर` $$\xrightarrow{\text{बैकअप}}$$ `WebDAV` $$\xrightarrow{\text{पुनर्स्थापना}}$$ `B कंप्यूटर` के माध्यम से मल्टी-डिवाइस डेटा सिंक्रनाइज़ेशन प्राप्त कर सकते हैं।

#### नटस्टोर उदाहरण

1. नटस्टोर में लॉग इन करें, ऊपरी दाएं कोने में उपयोगकर्ता नाम पर क्लिक करें और "खाता जानकारी" चुनें:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. "सुरक्षा विकल्प" चुनें, "एप्लिकेशन जोड़ें" पर क्लिक करें

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. एप्लिकेशन का नाम दर्ज करें, यादृच्छिक पासवर्ड उत्पन्न करें;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. पासवर्ड कॉपी करके सहेजें;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. सर्वर पता, खाता और पासवर्ड प्राप्त करें;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio सेटिंग → डेटा सेटिंग में WebDAV जानकारी दर्ज करें;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. डेटा बैकअप या पुनर्स्थापना का चयन करें, और स्वचालित बैकअप समय अंतराल सेट कर सकते हैं।

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
कम सीमा वाली WebDAV सेवाएँ आमतौर पर क्लाउड ड्राइव हैं:

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/)（सदस्यता आवश्यक）
* [阿里云盘](https://www.alipan.com/)（खरीद आवश्यक）
* [Box](https://www.box.com/) (निःशुल्क 10GB स्थान, 250MB/फ़ाइल सीमा)
* [Dropbox](https://www.dropbox.com/) （निःशुल्क 2GB, मित्रों को आमंत्रित करके 16GB तक बढ़ाया जा सकता है）
* [TeraCloud](https://teracloud.jp/en/) （निःशुल्क 10GB, आमंत्रण से +5GB）
* [Yandex Disk](https://disk.yandex.com/) (निःशुल्क उपयोक्ताओं के लिए 10GB)

स्व-होस्टेड समाधान:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}