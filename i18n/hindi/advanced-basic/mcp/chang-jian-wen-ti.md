---
icon: hexagon-exclamation
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# आम समस्याएँ (Common Problems)

### 1. mcp-server-time

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6068931438453048569-y.jpg" alt=""><figcaption><p>त्रुटि स्क्रीनशॉट (Error Screenshot)</p></figcaption></figure>

**समाधान (Solution)**&#x20;

"पैरामीटर्स (Parameters)" सेक्शन में निम्न भरें:

```
mcp-server-time
--local-timezone
<आपका स्टैंडर्ड टाइमज़ोन, उदाहरण: Asia/Shanghai>
```