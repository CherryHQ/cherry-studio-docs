
{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# GitHub Copilot

GitHub Copilot का उपयोग करने के लिए, आपके पास पहले से GitHub खाता होना चाहिए और GitHub Copilot सेवा की सदस्यता लेनी होगी। निःशुल्क (free) संस्करण भी उपयोग कर सकते हैं, लेकिन यह नवीनतम Claude 3.7 मॉडल का समर्थन नहीं करता है। विस्तृत जानकारी के लिए [GitHub Copilot आधिकारिक वेबसाइट](https://github.com/features/copilot) देखें।

## Device Code प्राप्त करें

"लॉग इन GitHub" पर क्लिक करें, Device Code प्राप्त करें और उसे कॉपी करें।

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Device Code प्राप्त करने की उदाहरण छवि"><figcaption><p>Device Code प्राप्त करना</p></figcaption></figure>

## ब्राउज़र में Device Code भरें और अधिकृत करें

Device Code सफलतापूर्वक प्राप्त करने के बाद, लिंक पर क्लिक करके ब्राउज़र खोलें, GitHub खाते में लॉग इन करें, Device Code दर्ज करें और अधिकृत करें।

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="GitHub अधिकृति उदाहरण छवि"><figcaption><p>GitHub अधिकृति</p></figcaption></figure>

अधिकृति सफल होने के बाद, Cherry Studio पर वापस जाएँ और "GitHub से कनेक्ट करें" पर क्लिक करें। सफल होने पर GitHub उपयोगकर्ता नाम और प्रोफ़ाइल चित्र दिखाई देगा।

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="GitHub कनेक्शन सफलता की उदाहरण छवि"><figcaption><p>GitHub कनेक्शन सफल</p></figcaption></figure>

## मॉडल सूची प्राप्त करने के लिए "प्रबंधन" क्लिक करें

निचले "प्रबंधन" बटन पर क्लिक करें। यह स्वचालित रूप से वर्तमान में समर्थित मॉडलों की सूची प्राप्त करेगा।

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="प्रबंधन बटन द्वारा मॉडल सूची प्राप्त करने की उदाहरण छवि"><figcaption><p>मॉडल सूची प्राप्त करना</p></figcaption></figure>

## सामान्य समस्याएँ

### Device Code प्राप्त करने में विफल, कृपया पुनः प्रयास करें

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Device Code प्राप्त करने में विफलता की उदाहरण छवि"><figcaption><p>Device Code प्राप्त करने में विफल</p></figcaption></figure>

वर्तमान में अनुरोध बनाने के लिए Axios का उपयोग किया जाता है जो SOCKS प्रॉक्सी का समर्थन नहीं करता। कृपया सिस्टम प्रॉक्सी या HTTP प्रॉक्सी का उपयोग करें, या CherryStudio में प्रॉक्सी सेटिंग बिल्कुल न करके सीधे वैश्विक प्रॉक्सी का उपयोग करें। सुनिश्चित करें कि आपका नेटवर्क कनेक्शन सामान्य है ताकि Device Code प्राप्त करने में विफलता से बचा जा सके।