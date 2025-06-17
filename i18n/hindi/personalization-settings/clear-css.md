---
icon: trash-xmark
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# सीएसएस सेटिंग्स साफ़ करें

{% hint style="warning" %}
गलत सीएसएस सेट होने पर, या सीएसएस सेट करने के बाद सेटिंग इंटरफेस में प्रवेश करने में असमर्थ होने पर, इस विधि का उपयोग करें।
{% endhint %}

* कंसोल खोलें, CherryStudio विंडो पर क्लिक करें, और शॉर्टकट <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> दबाएँ (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>)।
* पॉप-अप कंसोल विंडो में, `Console` टैब पर क्लिक करें

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* फिर मैन्युअल रूप से `document.getElementById('user-defined-custom-css').remove()` दर्ज करें (कॉपी-पेस्ट करने पर अक्सर निष्पादित नहीं होता)।
* एंटर दबाकर पुष्टि करने पर सीएसएस सेटिंग्स साफ़ हो जाएंगी। अब CherryStudio की डिस्प्ले सेटिंग्स में जाकर समस्याग्रस्त सीएसएस कोड हटा दें।