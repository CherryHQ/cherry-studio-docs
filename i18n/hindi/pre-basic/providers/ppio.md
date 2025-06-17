
{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# PPIO

## Cherry Studio में PPIO LLM API को इंटीग्रेट करें

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)ट्यूटोरियल अवलोकन <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio एक मल्टी-मॉडल डेस्कटॉप क्लाइंट है, जो वर्तमान में सपोर्ट करता है: Windows, Linux, MacOS सिस्टम के लिए इंस्टॉलेशन पैकेज। यह मुख्य LLM मॉडल्स को एकीकृत करता है और बहुउद्देशीय सहायता प्रदान करता है। उपयोगकर्ता स्मार्ट कन्वर्सेशन मैनेजमेंट, ओपन-सोर्स कस्टमाइजेशन और मल्टी-थीम इंटरफेस के माध्यम से अपनी कार्य दक्षता बढ़ा सकते हैं।

Cherry Studio अब **PPIO हाई-परफॉर्मेंस API चैनल** के साथ पूरी तरह अनुकूलित है—एंटरप्राइज-ग्रेड कंप्यूटिंग पावर के माध्यम से **DeepSeek-R1/V3 हाई-स्पीड रिस्पॉन्स** और **99.9% सर्विस अवेलेबिलिटी** प्रदान करता है, जो आपको तेज और सुचारु अनुभव देता है।

नीचे दिया गया ट्यूटोरियल पूर्ण इंटीग्रेशन सॉल्यूशन (API कुंजी कॉन्फ़िगरेशन सहित) शामिल करता है, जिससे आप **3 मिनट** में "Cherry Studio इंटेलिजेंट स्केड्यूलिंग + PPIO हाई-परफॉर्मेंस API" एडवांस मोड एक्टिवेट कर सकते हैं।

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. CherryStudio में "PPIO" को मॉडल प्रोवाइडर के रूप में जोड़ें <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

सबसे पहले ऑफिसियल वेबसाइट से Cherry Studio डाउनलोड करें: [https://cherry-ai.com/download](https://cherry-ai.com/download) (यदि एक्सेस नहीं होता है, तो नीचे दिए गए Quark नेटडिस्क लिंक से अपने सिस्टम के अनुसार वर्जन डाउनलोड करें: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) सबसे पहले निचले बाएँ कोने में सेटिंग पर क्लिक करें, प्रोवाइडर नाम कस्टमाइज़ करें: `PPIO`, फिर "OK" पर क्लिक करें

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) [PPIO कंप्यूटिंग क्लाउड API कुंजी मैनेजमेंट](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio) पर जाएँ, 【यूज़र आइकन】—【API कुंजी प्रबंधन】 पर क्लिक कर कंट्रोल पैनल में प्रवेश करें

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

【+ बनाएँ】 बटन पर क्लिक कर नई API कुंजी जेनरेट करें। एक कस्टम नाम दर्ज करें, **जेनरेट कुंजी केवल क्रिएशन समय पर दिखाई देती है, कृपया इसे कॉपी करके सेव करें ताकि बाद में उपयोग प्रभावित न हो**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) CherryStudio में कुंजी डालें सेटिंग पर क्लिक करें, 【PPIO】 चुनें, जेनरेट की गई API कुंजी इनपुट करें, और अंत में 【जाँचें】 पर क्लिक करें

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) मॉडल चुनें: उदाहरण के लिए deepseek/deepseek-r1/community. यदि अन्य मॉडल अपडेट करना चाहते हैं, तो सीधे बदल सकते हैं।

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 और V3 कम्युनिटी वर्जन सिर्फ़ ट्रायल के लिए हैं, ये फुल-पैरामीटर मॉडल हैं जिनकी स्थिरता और परफॉर्मेंस में कोई अंतर नहीं है। यदि बड़े पैमाने पर उपयोग करना है, तो **रिचार्ज करके नॉन-कम्युनिटी वर्जन पर स्विच करें**।

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. मॉडल उपयोग कॉन्फ़िगरेशन <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) 【जाँचें】 पर क्लिक करने के बाद कनेक्शन सफल दिखने पर सामान्य उपयोग शुरू कर सकते हैं

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) अंत में 【@】 पर क्लिक कर PPIO प्रोवाइडर के अंतर्गत जोड़े गए DeepSeek R1 मॉडल को चुनें, और चैट शुरू करें\~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【कुछ सामग्री स्रोत: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. PPIO×Cherry Studio वीडियो उपयोग गाइड <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

यदि आप विज़ुअल लर्निंग पसंद करते हैं, तो हमने Bilibili पर वीडियो ट्यूटोरियल तैयार किया है। स्टेप-बाय-स्टेप गाइड के माध्यम से, आप "PPIO API + Cherry Studio" कॉन्फ़िगरेशन तेज़ी से सीख सकते हैं। नीचे दिए गए लिंक पर क्लिक करके वीडियो देखें और सुचारु अनुभव शुरू करें → [《Still irritated by DeepSeek's endless loading? PPIO + DeepSeek full version =? No more congestion, take off instantly》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【वीडियो सामग्री स्रोत: sola】