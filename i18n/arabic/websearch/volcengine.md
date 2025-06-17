---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# التكامل مع محرك بركاني للوصول للإنترنت

### 1. تسجيل الدخول/إنشاء حساب في "محرك بركاني" <a href="#rclz7" id="rclz7"></a>

اذهب للموقع الرسمي: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>الموقع الرسمي لمحرك بركاني</p></figcaption></figure>

### 2. إنشاء "تطبيقي" "بإمكانه الاتصال بالإنترنت" <a href="#gvzaa" id="gvzaa"></a>

2.1. سجّل الدخول إلى محرك بركاني، ثم انتقل لصفحة "سفينة نوح": [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **انقر تباعاً على:** <mark style="color:red;">**"تطبيقاتي" → "إنشاء تطبيق" → "بدون كود" → "محادثة فردية"**</mark> 

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. تعبئة المعلومات ونشر التطبيق <a href="#zzdfe" id="zzdfe"></a>

**اسم التطبيق**: اختر أي اسم تريده (الحقول <mark style="color:red;">**المميزة بعلامة * إلزامية**</mark>، باقي الحقول اختيارية).

<mark style="color:red;">**النقطة الأساسية: تفعيل إضافة الاتصال بالإنترنت (يجب تفعيلها أولاً)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. تفعيل ميزة الاتصال بالإنترنت (لاحظ التكلفة وعدد المرات المجانية) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>انقر على "اشتري الآن" واتبع الخطوات حتى تظهر الواجهة التالية، مما يعني أن التفعيل نجح.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>لاحظ حالة التفعيل - نجحت العملية هنا</p></figcaption></figure>

عد بعدها لواجهة "تعبئة معلومات التطبيق" واكمل العملية.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. إعدادات متقدمة للبحث عبر الإنترنت <a href="#sp6uz" id="sp6uz"></a>

اختار بناءً على احتياجاتك:

* للتحكم الدقيق بالإدخال/الإخراج: استخدم "**استدعاء مخصص**".
* للتبسيط: استخدم "**استدعاء تلقائي**" (القيمة الافتراضية).
* لتحديث المعلومات الفوري (تكلفة أعلى): "**التفعيل الإلزامي**".

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. نشر التطبيق <a href="#fe1gf" id="fe1gf"></a>

انقر على زر "نشر" في الزاوية العلوية اليمنى لإنهاء إنشاء التطبيق.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. الحصول على API Key <a href="#jtqlu" id="jtqlu"></a>

انقر تباعاً على: **"دليل استدعاء API" → "حدد API Key وانسخه" → "عرض واختيار"**

انسخ API Key، ثم الصقه في cherry studio (انظر التفاصيل أدناه)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

ملاحظة: إن لم يكن هناك API Key، انقر على "**إنشاء API Key**" في الزاوية العلوية للنافذة، ثم انسخه.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. استخدام API Key في cherry studio للوصول إلى deepseek-R1 عبر الإنترنت <a href="#lrefj" id="lrefj"></a>

#### 5.1. افتح cherry studio → "إعدادات" → "أي اسم" → "النوع: openAI" <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. إعداد URL و key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">ملاحظة: إن لم تجد العنوان أو لم يكن لخادم بكين، يمكنك العثور عليه هنا (لا تنسَ "/"):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. إضافة اسم النموذج <a href="#qmh3i" id="qmh3i"></a>

انسخ الاسم الموجود في النص الصغير أسفل الصفحة، وإلا سيظهر خطأ.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. معاينة النتيجة <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>