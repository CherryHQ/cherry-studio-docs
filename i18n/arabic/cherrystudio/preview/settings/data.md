---
icon: database
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# إعدادات البيانات

تتيح هذه الواجهة إجراء نسخ احتياطي للبيانات في السحابة أو محليًا، والاستعلام عن دليل البيانات المحلي، ومسح الذاكرة المؤقتة، وغيرها من العمليات.

### النسخ الاحتياطي للبيانات

حاليًا، يدعم النسخ الاحتياطي للبيانات فقط طريقة WebDAV. يمكنك اختيار خدمات تدعم WebDAV لإنشاء نسخ احتياطية سحابية.

يمكنك أيضًا تحقيق مزامنة البيانات بين أجهزة متعددة من خلال طريقة: `الحاسوب A` $$\xrightarrow{\text{نسخ احتياطي}}$$ `WebDAV` $$\xrightarrow{\text{استعادة}}$$ `الحاسوب B`.

#### مثال على نوت يونتين (Jianguoyun)

1. سجّل الدخول إلى نوت يونتين، انقر على اسم المستخدم في الزاوية اليمنى العليا، واختر "معلومات الحساب":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. اختر "خيارات الأمان"، ثم انقر على "إضافة تطبيق"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. أدخل اسم التطبيق، ثم قم بتوليد كلمة مرور عشوائية؛

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. انسخ كلمة المرور المسجلة؛

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. احصل على عنوان الخادم، والحساب، وكلمة المرور؛

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. في إعدادات Cherry Studio - إعدادات البيانات، املأ معلومات WebDAV؛

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. اختر نسخ البيانات احتياطيًا أو استعادتها، ويمكنك ضبط الفترة الزمنية للنسخ الاحتياطي التلقائي.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
تتضمن خدمات WebDAV منخفضة العتبة عادةً خدمات التخزين السحابي:

* [نوت يونتين (Jianguoyun)](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/) (يتطلب عضوية)
* [علي باين (AliPan)](https://www.alipan.com/) (يتطلب الشراء)
* [Box](https://www.box.com/) (تقدم مساحة مجانية 10 جيجابايت، بحد أقصى للفرد 250 ميجابايت)
* [Dropbox](https://www.dropbox.com/) (2 جيجابايت مجانًا، يمكن زيادة السعة إلى 16 جيجابايت بدعوة الأصدقاء)
* [TeraCloud](https://teracloud.jp/en/) (مساحة مجانية 10 جيجابايت، يمكن الحصول على 5 جيجابايت إضافية بدعوة)
* [Yandex Disk](https://disk.yandex.com/) (تقدم 10 جيجابايت للمستخدمين المجانيين)

تتضمن الخيارات الأخرى خدمات تتطلب نشرًا ذاتيًا:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}