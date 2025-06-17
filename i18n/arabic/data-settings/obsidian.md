---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# دليل إعداد Obsidian

يدعم Cherry Studio التكامل مع Obsidian، مما يتيح لك تصدير المحادثات الكاملة أو الرسائل المفردة إلى مكتبة Obsidian.

{% hint style="warning" %}
لا تتطلب هذه العملية تثبيت أي إضافات إضافية لـ Obsidian. نظرًا لأن مبدأ الاستيراد من Cherry Studio إلى Obsidian مشابه لـ Obsidian Web Clipper، يُنصح المستخدمون بتحديث Obsidian إلى أحدث إصدار (يجب أن يكون الإصدار الحالي على الأقل **1.7.2** أو أعلى) لتجنب [فشل الاستيراد في حال كانت المحادثات طويلة جدًا](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## أحدث دليل

{% hint style="info" %}
مقارنة بالإصدار السابق لتصدير المحادثات إلى Obsidian، يمكن للوظيفة الجديدة تحديد مسار المكتبة تلقائيًا دون الحاجة لإدخال اسم المكتبة أو المجلد يدويًا.
{% endhint %}

### الخطوة الأولى: تهيئة Cherry Studio

افتح في Cherry Studio: _الإعدادات_ → _إعدادات البيانات_ → قائمة _إعداد Obsidian_، ستظهر أسماء مكتبات Obsidian المفتوحة محليًا تلقائيًا في القائمة المنسدلة. اختر مكتبة Obsidian الهدف:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### الخطوة الثانية: تصدير المحادثة

#### تصدير محادثة كاملة

ارجع إلى واجهة المحادثة في Cherry Studio، انقر بزر الماوس الأيمن على المحادثة، اختر _تصدير_، ثم انقر على _تصدير إلى Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

ستظهر نافذة لتعديل **خصائص (Properties)** الملاحظة التي ستُصدَر إلى Obsidian، و**موقع المجلد** في Obsidian، و**طريقة المعالجة** عند التصدير:

* **المكتبة (Vault)**: اختر من القائمة المنسدلة مكتبات Obsidian الأخرى
* **المسار (Path)**: اختر المجلد لحفظ ملاحظات المحادثة المصدرة
* خصائص ملاحظة Obsidian (Properties):
  * الوسوم (tags)
  * وقت الإنشاء (created)
  * المصدر (source)
* **طرق المعالجة** عند التصدير إلى Obsidian:
  * **جديد (استبدال إذا كان موجودًا)**: إنشاء ملاحظة محادثة جديدة في المجلد المحدد في **المسار**، مع استبدال الملاحظة القدية إذا وجدت واحدة بنفس الاسم
  * **إضافة في البداية**: إضافة محتوى المحادثة المحدد إلى بداية الملاحظة عند وجود ملاحظة بنفس الاسم
  * **إضافة في النهاية**: إضافة محتوى المحادثة المحدد إلى نهاية الملاحظة عند وجود ملاحظة بنفس الاسم

{% hint style="info" %}
تُضاف خصائص (Properties) فقط مع الطريقة الأولى، ولا تضاف مع الطريقتين الأخريتين.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>تهيئة خصائص الملاحظة</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>اختيار المسار</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>اختيار طريقة المعالجة</p></figcaption></figure>

بعد تحديد جميع الخيارات، انقر على موافقة لتصدير المحادثة الكاملة إلى المجلد المناسب في مكتبة Obsidian المحددة.

#### تصدير رسالة مفردة

لتصدير رسالة مفردة، انقر على _قائمة الثلاثة شرطات_ أسفل الرسالة، اختر _تصدير_، ثم انقر على _تصدير إلى Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>تصدير رسالة مفردة</p></figcaption></figure>

ستظهر نفس النافذة التي تظهر عند تصدير محادثة كاملة، حيث يمكنك تكوين **خصائص الملاحظة** و**طريقة معالجة الملاحظة**، اتبع نفس [الخطوات السابقة](obsidian.md#dao-chu-wan-zheng-dui-hua).

### اكتمال التصدير بنجاح

🎉 تهانينا! لقد أكملت جميع إعدادات التكامل بين Cherry Studio وObsidian، ومررت عبر عملية التصدير بالكامل، استمتع!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>التصدير إلى Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>مشاهدة نتيجة التصدير</p></figcaption></figure>



***

## الدليل القديم (لإصدار Cherry Studio < v1.1.13)

### الخطوة الأولى: إعداد Obsidian

افتح مكتبة Obsidian، وأنشئ مجلدًا لحفظ المحادثات المصدرة (مثال: مجلد Cherry Studio):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

احفظ النص المحاط في الزاوية السفلى اليسرى، حيث يمثل اسم `مكتبتك`.

### الخطوة الثانية: تهيئة Cherry Studio

في Cherry Studio: _الإعدادات_ → _إعدادات البيانات_ → قائمة _إعداد Obsidian_، أدخل اسم `المكتبة` و`المجلد` الذي حصلت عليه في [الخطوة الأولى](obsidian.md#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

اختياريًا: يمكنك في حقل `الوسوم العامة` تعيين وسوم لجميع المحادثات المصدرة في Obsidian حسب الحاجة.

### الخطوة الثالثة: تصدير المحادثة

#### تصدير محادثة كاملة

ارجع إلى واجهة المحادثة في Cherry Studio، انقر بزر الماوس الأيمن على المحادثة، اختر _تصدير_، ثم انقر على _تصدير إلى Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>تصدير محادثة كاملة</p></figcaption></figure>

ستظهر نافذة لتعديل **خصائص (Properties)** الملاحظة، و**طريقة المعالجة**. تتضمن طرق المعالجة:

* **جديد (استبدال إذا كان موجودًا)**: إنشاء ملاحظة جديدة في `المجلد` الذي تم تعيينه في [الخطوة الثانية](obsidian.md#di-er-bu)
* **إضافة في البداية**: إضافة محتوى المحادثة المحدد إلى بداية ملاحظة موجودة
* **إضافة في النهاية**: إضافة محتوى المحادثة المحدد إلى نهاية ملاحظة موجودة

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>تهيئة خصائص الملاحظة</p></figcaption></figure>

{% hint style="info" %}
تُضاف خصائص (Properties) فقط مع الطريقة الأولى، ولا تضاف مع الطريقتين الأخريتين.
{% endhint %}

#### تصدير رسالة مفردة

لتصدير رسالة مفردة، انقر على _قائمة الثلاثة شرطات_ أسفل الرسالة، اختر _تصدير_، ثم انقر على _تصدير إلى Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>تصدير رسالة مفردة</p></figcaption></figure>

ستظهر نفس نافذة التهيئة المستخدمة لتصدير محادثة كاملة، اتبع [الخطوات السابقة](obsidian.md#dao-chu-wan-zheng-dui-hua).

### اكتمال التصدير بنجاح

🎉 تهانينا! لقد أكملت جميع إعدادات التكامل بين Cherry Studio وObsidian، ومررت عبر عملية التصدير بالكامل، استمتع!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>التصدير إلى Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>مشاهدة نتيجة التصدير</p></figcaption></figure>