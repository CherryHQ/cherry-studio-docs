
{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# एमसीपी की स्वत: स्थापना

> एमसीपी की स्वत: स्थापना के लिए Cherry Studio को v1.1.18 या उच्चतर संस्करण में अपग्रेड करना आवश्यक है।

## सुविधा विवरण

मैन्युअल स्थापना के अतिरिक्त, Cherry Studio में `@mcpmarket/mcp-auto-install` टूल अंतर्निहित है जो एमसीपी सर्वर स्थापित करने का अधिक सुविधाजनक तरीका प्रदान करता है। आपको केवल एमसीपी सपोर्ट करने वाले बड़े मॉडल वार्तालाप में संबंधित आदेश दर्ज करना होगा।

{% hint style="warning" %}
**परीक्षण चरण चेतावनी:**

* `@mcpmarket/mcp-auto-install` वर्तमान में परीक्षण चरण में है
* प्रभाव बड़े मॉडल की "बुद्धिमत्ता" पर निर्भर करता है - कुछ स्वचालित रूप से जोड़े जाते हैं, कुछ में अभी भी **MCP सेटिंग्स में कुछ पैरामीटर मैन्युअल रूप से बदलने की आवश्यकता होती है**
* वर्तमान खोज स्रोत @modelcontextprotocol से किया जाता है, जिसे स्वयं कॉन्फ़िगर किया जा सकता है (नीचे विवरण)
{% endhint %}

## उपयोग निर्देश

उदाहरण के लिए, आप इनपुट कर सकते हैं:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>MCP सर्वर स्थापित करने के लिए आदेश दर्ज करें</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP सर्वर कॉन्फ़िगरेशन इंटरफ़ेस</p></figcaption></figure>

सिस्टम स्वचालित रूप से आपकी आवश्यकता को पहचानेगा और `@mcpmarket/mcp-auto-install` के माध्यम से स्थापना पूरी करेगा। यह टूल विभिन्न प्रकार के एमसीपी सर्वरों का समर्थन करता है, जिनमें शामिल हैं:

* filesystem (फ़ाइल सिस्टम)
* fetch (नेटवर्क अनुरोध)
* sqlite (डेटाबेस)
* आदि...

> MCP_PACKAGE_SCOPES चर MCP सेवा खोज स्रोत अनुकूलित करता है, डिफ़ॉल्ट मान: `@modelcontextprotocol`।

## `@mcpmarket/mcp-auto-install` लाइब्रेरी विवरण

{% hint style="info" %}
**डिफ़ॉल्ट कॉन्फ़िगरेशन संदर्भ:**

```json
// `axun-uUpaWEdMEMU8C61K` सेवा ID है, कस्टमाइज़ करें
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "स्वचालित रूप से MCP सेवाएँ स्थापित करें (बीटा संस्करण)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "विवरण के लिए देखें https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` एक ओपन-सोर्स npm पैकेज है। इसका विस्तृत विवरण और उपयोग दस्तावेज़ [npm आधिकारिक रिपॉजिटरी](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) पर देखा जा सकता है। `@mcpmarket` Cherry Studio का आधिकारिक MCP सेवा संग्रह है।
{% endhint %}