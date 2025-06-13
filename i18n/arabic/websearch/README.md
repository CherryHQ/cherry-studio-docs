---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# وضع الاتصال بالإنترنت

{% hint style="info" %}
أمثلة على الحالات التي تتطلب الاتصال بالإنترنت:

* معلومات زمنية محددة: مثل أسعار العقود الآجلة للذهب اليوم/هذا الأسبوع/للتو.
* بيانات حية: مثل الطقس، أسعار الصرف، وغيرها من القيم الديناميكية.
* معرفة مستجدة: مثل الأشياء الجديدة، المفاهيم الحديثة، التقنيات المستحدثة، إلخ...
{% endhint %}

### أولاً: كيفية تفعيل الاتصال بالإنترنت

في نافذة الأسئلة بـCherry Studio، انقر على أيقونة 【الكرة الأرضية الصغيرة】 لتفعيل الاتصال بالإنترنت.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>انقر على أيقونة الكرة الأرضية - تفعيل الاتصال</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>المؤشر يدل على تفعيل ميزة الاتصال</p></figcaption></figure>

### ثانياً: ملاحظة هامة: هناك وضعان للاتصال

#### الوضع 1: النماذج الكبيرة من موفري الخدمة مع دعم مدمج للاتصال

في هذه الحالة، بعد تفعيل الاتصال، يمكنك استخدام الخدمة مباشرةً بكل بساطة.

{% hint style="warning" %}
يمكنك التحقق سريعاً مما إذا كان النموذج يدعم الاتصال من خلال وجود علامة الكرة الأرضية بجوار اسم النموذج في واجهة الأسئلة.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

في صفحة إدارة النماذج، تتيح لك هذه الطريقة أيضاً التمييز بسرعة بين النماذج المدعومة للاتصال وتلك غير المدعومة.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**موفرو خدمات النماذج المدعومة حالياً في Cherry Studio للاتصال هم**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (جميع النماذج مدعومة للاتصال)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian وغيرها</mark>

{% hint style="danger" %}
ملاحظة هامة:
هناك حالة خاصة حيث قد يعمل النموذج مع الاتصال بالإنترنت رغم عدم وجود علامة الكرة الأرضية، كما هو موضح في البرنامج التعليمي التالي.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### الوضع 2: نماذج بدون دعم اتصال، باستخدام خدمة Tavily للاتصال

عند استخدام نموذج كبير غير مدعوم للاتصال (بدون علامة الكرة الأرضية)، ونحتاج منه معالجة معلومات حية، نلجأ لخدمة البحث على الإنترنت Tavily.

**عند الاستخدام الأول لخدمة Tavily**، ستظهر نافذة لإدخال معلومات الإعدادات. اتبع الإرشادات - الأمر بسيط!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>النافذة المنبثقة، انقر: الذهاب للإعدادات</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>انقر للحصول على المفتاح</p></figcaption></figure>

بعد النقر على "الحصول على المفتاح"، ستنتقل تلقائياً لصفحة **تسجيل الدخول/التسجيل** في موقع tavily. بعد التسجيل وتسجيل الدخول، أنشئ مفتاح API ثم انسخه إلى Cherry Studio.

{% hint style="danger" %}
إذا واجهت صعوبة في التسجيل، راجع دليل التسجيل للاتصال عبر Tavily في نفس مجلد هذا المستند.
{% endhint %}

**مرجع تسجيل Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

هذه الواجهة تشير إلى نجاح التسجيل:

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>انسخ المفتاح</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>الصق المفتاح، تم الانتهاء!</p></figcaption></figure>

لنجرب مرة أخرى. النتيجة تظهر أن البحث عبر الإنترنت يعمل بشكل طبيعي، وعدد نتائج البحث هو القيمة الافتراضية (5).

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
ملاحظة: خدمة tavily لها حد شهري مجاني، ويتطلب الاستخدام الزائد دفع رسوم~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> ملحوظة: إذا اكتشفت خطأ، يرجى التواصل معنا في أي وقت.