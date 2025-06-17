
{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# MCP का कॉन्फ़िगरेशन और उपयोग

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Cherry Studio सेटिंग्स खोलें।
2. `MCP सर्वर` विकल्प ढूँढें।
3. `सर्वर जोड़ें` पर क्लिक करें।
4. MCP सर्वर के संबंधित पैरामीटर्स भरें ([संदर्भ लिंक](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch))। निम्नलिखित जानकारी भरनी पड़ सकती है:
   * नाम: कोई कस्टम नाम, जैसे `fetch-server`
   * प्रकार: `STDIO` चुनें
   * कमांड: `uvx` भरें
   * पैरामीटर्स: `mcp-server-fetch` भरें
   *(अन्य पैरामीटर्स हो सकते हैं, जो विशिष्ट सर्वर पर निर्भर करता है)*
5. `सेव` पर क्लिक करें।

{% hint style="success" %}
उपरोक्त कॉन्फ़िगरेशन पूरा होने पर, Cherry Studio स्वचालित रूप से आवश्यक MCP सर्वर - `fetch सर्वर` डाउनलोड करेगा। डाउनलोड पूरा होने के बाद आप उपयोग शुरू कर सकते हैं! नोट: जब mcp-server-fetch कॉन्फ़िगरेशन सफल न हो, तो कंप्यूटर को पुनरारंभ करने का प्रयास करें।
{% endhint %}

### चैट बॉक्स में MCP सेवा सक्षम करें

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* `MCP सर्वर` सेटिंग्स में MCP सर्वर सफलतापूर्वक जोड़ा गया है

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **उपयोग परिणाम प्रदर्शन**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

उपरोक्त छवि से देखा जा सकता है कि MCP के `fetch` कार्य से संयुक्त होने पर, Cherry Studio उपयोगकर्ता की क्वेरी इरादे को बेहतर समझ सकता है और इंटरनेट से प्रासंगिक जानकारी प्राप्त करके अधिक सटीक और विस्तृत उत्तर प्रदान कर सकता है।