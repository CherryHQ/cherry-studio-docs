---
icon: ban
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# वेब खोज ब्लैकलिस्ट कॉन्फ़िगरेशन

Cherry Studio ब्लैकलिस्ट कॉन्फ़िगर करने के लिए मैन्युअल और फ़ीड सब्सक्रिप्शन दोनों तरीकों का समर्थन करता है। कॉन्फ़िगरेशन नियम [ublacklist](https://github.com/iorate/ublacklist) का संदर्भ लें

## मैन्युअल कॉन्फ़िगरेशन

आप खोज परिणामों के लिए नियम जोड़ सकते हैं या टूलबार आइकन पर क्लिक करके विशिष्ट वेबसाइटों को ब्लॉक कर सकते हैं। नियम निम्नलिखित तरीकों से निर्दिष्ट किए जा सकते हैं: [मिलान पैटर्न](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (उदाहरण: `*://*.example.com/*`) या [रेगुलर एक्सप्रेशन](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (उदाहरण: `/example\.(net|org)/`) का उपयोग करके।

## फ़ीड सब्सक्रिप्शन

आप सार्वजनिक नियम सेट की सदस्यता भी ले सकते हैं। यह वेबसाइट कुछ सदस्यता सूचियाँ प्रदान करती है:\
https://iorate.github.io/ublacklist/subscriptions

यहाँ कुछ अनुशंसित सब्सक्रिप्शन फ़ीड लिंक दिए गए हैं:

| नाम                                                                                                    | लिंक                                                                                                   | प्रकार   |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | चीनी   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | AI-जनित |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>फ़ीड सब्सक्रिप्शन कॉन्फ़िगरेशन</p></figcaption></figure>