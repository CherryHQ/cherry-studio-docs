---
icon: file-code
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# कस्टम CSS

कस्टम CSS के माध्यम से, आप सॉफ्टवेयर की उपस्थिति को अपनी पसंद के अनुसार बदल सकते हैं, उदाहरण के लिए:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>कस्टम CSS</p></figcaption></figure>

```css
:root {
  --color-background: #1a462788;
  --color-background-soft: #1a4627aa;
  --color-background-mute: #1a462766;
  --navbar-background: #1a4627;
  --chat-background: #1a4627;
  --chat-background-user: #28b561;
  --chat-background-assistant: #1a462722;
}

#content-container {
  background-color: #2e5d3a !important;
}
```

### अंतर्निहित वेरिएबल्स

```css
:root {
  font-family: "汉仪唐美人" !important; /* फ़ॉन्ट */
}

/* गहरी सोच के विस्तार का फ़ॉन्ट रंग */
.ant-collapse-content-box .markdown {
  color: red;
}

/* थीम वेरिएबल्स */
:root {
  --color-black-soft: #2a2b2a; /* गहरे रंग की पृष्ठभूमि */
  --color-white-soft: #f8f7f2; /* हल्के रंग की पृष्ठभूमि */
}

/* डार्क थीम */
body[theme-mode="dark"] {
  /* रंग */
  --color-background: #2b2b2b; /* गहरे रंग की पृष्ठभूमि */
  --color-background-soft: #303030; /* हल्के रंग की पृष्ठभूमि */
  --color-background-mute: #282c34; /* तटस्थ पृष्ठभूमि */
  --navbar-background: var(-–color-black-soft); /* नेविगेशन बार पृष्ठभूमि */
  --chat-background: var(–-color-black-soft); /* चैट पृष्ठभूमि */
  --chat-background-user: #323332; /* उपयोगकर्ता चैट पृष्ठभूमि */
  --chat-background-assistant: #2d2e2d; /* असिस्टेंट चैट पृष्ठभूमि */
}

/* डार्क थीम विशिष्ट शैलियाँ */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* सामग्री कंटेनर पृष्ठभूमि */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* संदेश पृष्ठभूमि */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* इनपुट बार पृष्ठभूमि */
    border: 1px solid #5e5d5940; /* इनपुट बार बॉर्डर रंग */
    border-radius: 8px; /* इनपुट बार बॉर्डर गोलाई */
  }

  /* कोड शैलियाँ */
  code {
    background-color: #e5e5e20d; /* कोड पृष्ठभूमि */
    color: #ea928a; /* कोड टेक्स्ट रंग */
  }

  pre code {
    color: #abb2bf; /* फ़ॉर्मेटेड कोड टेक्स्ट रंग */
  }
}

/* लाइट थीम */
body[theme-mode="light"] {
  /* रंग */
  --color-white: #ffffff; /* सफेद */
  --color-background: #ebe8e2; /* हल्की पृष्ठभूमि */
  --color-background-soft: #cbc7be; /* हल्की पृष्ठभूमि */
  --color-background-mute: #e4e1d7; /* तटस्थ पृष्ठभूमि */
  --navbar-background: var(-–color-white-soft); /* नेविगेशन बार पृष्ठभूमि */
  --chat-background: var(-–color-white-soft); /* चैट पृष्ठभूमि */
  --chat-background-user: #f8f7f2; /* उपयोगकर्ता चैट पृष्ठभूमि */
  --chat-background-assistant: #f6f4ec; /* असिस्टेंट चैट पृष्ठभूमि */
}

/* लाइट थीम विशिष्ट शैलियाँ */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* सामग्री कंटेनर पृष्ठभूमि */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* संदेश पृष्ठभूमि */
  }

  .inputbar-container {
    background-color: #ffffff; /* इनपुट बार पृष्ठभूमि */
    border: 1px solid #87867f40; /* इनपुट बार बॉर्डर रंग */
    border-radius: 8px; /* इनपुट बार बॉर्डर गोलाई (अपनी पसंद के अनुसार) */
  }

  /* कोड शैलियाँ */
  code {
    background-color: #3d39290d; /* कोड पृष्ठभूमि */
    color: #7c1b13; /* कोड टेक्स्ट रंग */
  }

  pre code {
    color: #000000; /* फ़ॉर्मेटेड कोड टेक्स्ट रंग */
  }
}
```

अधिक थीम वेरिएबल्स के लिए कृपया स्रोत कोड देखें: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### संबंधित सिफारिशें

Cherry Studio थीम लाइब्रेरी: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

कुछ चीनी शैली के Cherry Studio थीम स्किन साझा करें: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)