
{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# बाइटडांस (डौबाओ)

*   [वोल्कन इंजन](https://console.volcengine.com/) पर लॉग इन करें
*   सीधे [यहाँ क्लिक करें](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### API कुंजी प्राप्त करें

*   साइडबार के नीचे [API कुंजी प्रबंधन](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) पर क्लिक करें
*   API कुंजी बनाएं

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   सफलतापूर्वक बनाने के बाद, बनाई गई API कुंजी के आगे छोटी आँख पर क्लिक करके दिखाएँ और कॉपी करें

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   कॉपी की गई API कुंजी CherryStudio में भरें, फिर सेवा प्रदाता स्विच चालू करें।

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### मॉडल सक्रिय करें और जोड़ें

*   आर्क कंसोल के साइडबार के सबसे नीचे [सक्रियण प्रबंधन](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) में जाकर आवश्यक मॉडल सक्रिय करें, यहाँ आप डौबाओ सीरीज़ और DeepSeek जैसे मॉडल आवश्यकता अनुसार सक्रिय कर सकते हैं।

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   [मॉडल सूची दस्तावेज़](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90) में, आवश्यक मॉडल के संगत मॉडल ID ढूँढें।

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="वोल्कन इंजन मॉडल ID सूची उदाहरण"><figcaption></figcaption></figure>

*   Cherry Studio की [मॉडल सेवा](../../cherrystudio/preview/settings/providers.md) सेटिंग्स खोलें और वोल्कन इंजन ढूँढें
*   जोड़ें पर क्लिक करें, पहले प्राप्त मॉडल ID को मॉडल ID टेक्स्ट बॉक्स में कॉपी करें

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   इस प्रक्रिया के अनुसार क्रमिक रूप से मॉडल जोड़ें

### API पता

API पते के दो लिखने के तरीके हैं:

*   पहला क्लाइंट डिफ़ॉल्ट है: `https://ark.cn-beijing.volces.com/api/v3/`
*   दूसरा तरीका: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
दोनों तरीकों में कोई अंतर नहीं है, डिफ़ॉल्ट रखें, बदलने की आवश्यकता नहीं।

`/` और `#` से समाप्त होने वाले अंतर के बारे में सेवा प्रदाता सेटिंग्स के API पते अनुभाग में देखें, [यहाँ जाएँ](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>आधिकारिक दस्तावेज़ cURL उदाहरण</p></figcaption></figure>