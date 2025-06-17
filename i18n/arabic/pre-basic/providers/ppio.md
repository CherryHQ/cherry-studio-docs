
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# PPIO | بايو ستوديو

## دمج Cherry Studio مع منصة بايو الـ API للذكاء الاصطناعي

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%D9%86%D8%B8%D8%B1%D8%A9-%D8%B9%D8%A7%D9%85%D8%A9-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D8%AF%D8%B1%D8%B3)نظرة عامة على الدروس <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio هو عميل سطح مكتب متعدد النماذج، يدعم حاليًا: حزم تثبيت لأنظمة Windows وLinux وMacOS. يجمع بين نماذج الذكاء الاصطناعي الرائدة، ويوفر مساعدًا متعدد الاستخدامات. يمكن للمستخدمين تحسين الإنتاجية من خلال إدارة المحادثات الذكية والتخصيص مفتوح المصدر والواجهات متعددة السمات.

تم دمج Cherry Studio بشكل كامل مع **قنوات API عالية الأداء من PPIO** - حيث يضمن قوة الحوسبة على مستوى المؤسسات، **استجابة فائقة السرعة لـ DeepSeek-R1/V3** و **توفر خدمة بنسبة 99.9%**، مما يمنحك تجربة سلسة.

يغطي الدرج التالي خطة دمج كاملة (بما في ذلك تكوين المفاتيح)، مما يمكنك من تمكين "الجدولة الذكية لـ Cherry Studio + قنوات API عالية الأداء من PPIO" خلال 3 دقائق.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%D8%A5%D8%B6%D8%A7%D9%81%D8%A9-ppio-%D9%83%D9%85%D9%88%D8%B1%D9%91%D8%B6-%D9%86%D9%85%D8%A7%D8%B0%D8%AC)1. إضافة PPIO كمورّد للنماذج <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

انتقل أولاً إلى الموقع الرسمي لتنزيل Cherry Studio: [https://cherry-ai.com/download](https://cherry-ai.com/download) (إذا لم يعمل الرابط، يمكنك استخدام رابط تخزين Quark: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) انقر على "الإعدادات" في الزاوية اليسرى السفلية، وحدد اسم المورّد كـ `PPIO`، ثم انقر على "موافق"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) انتقل إلى [إدارة مفاتيح API في منصة بايو](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio)، ثم انقر على [صورة المستخدم] → [إدارة مفاتيح API] للوصول إلى لوحة التحكم

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

انقر فوق [ + إنشاء ] لإنشاء مفتاح API جديد. قم بتخصيص اسم للمفتاح. **يظهر المفتاح عند الإنشاء فقط - يرجى نسخه وحفظه في مستند لتجنب مشاكل الاستخدام لاحقًا**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) في CherryStudio، أدخل المفتاح: انتقل إلى الإعدادات → اختر [PPIO | بايو] → أدخل مفتاح API المنشأ على الموقع الرسمي → انقر أخيرًا على [فحص]

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) اختيار النموذج: مثال deepseek/deepseek-r1/community. لتغيير النموذج، يمكنك التحديد مباشرة.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></>

نسخة DeepSeek R1 وV3 community مخصصة للاختبار، وهي نسخة كاملة المعالم. للأداء والاستقرار نفس الإصدارات الأخرى، ولكن للاستخدام المكثف، يجب **الشحن والتبديل إلى النسخة غير community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%D8%AA%D9%83%D9%88%D9%8A%D9%86-%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D8%A7%D9%84%D9%86%D9%85%D8%A7%D8%B0%D8%AC)2. تكوين استخدام النموذج <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) بعد النقر على [فحص] وظهور "اتصال ناجح"، يمكنك البدء في الاستخدام الطبيعي

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) أخيرًا، انقر على [@] واختر نموذج DeepSeek R1 المضافة حديثًا تحت مورّد PPIO، وابدأ المحادثة بنجاح

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

[مصدر جزئي: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)]

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D9%8A-ppio--cherry-studio)3. فيديو تعليمي: تكامل PPIO مع Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

إذا كنت تفضل التعلم المرئي، فقد أعددنا درسًا مرئيًا على Bilibili. يساعدك البرنامج التعليمي التفاعلي على إتقان تكوين "PPIO API + Cherry Studio" بسرعة، انقر على الرابط التالي لتشغيل الفيديو مباشرة → [【هل تشعر بالإحباط بسبب بطء DeepSeek؟】 منصة بايو + نسخة كاملة من DeepSeek =؟ لا ازدحام، سرعة فورية](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

[مصدر الفيديو: sola]