---
icon: database
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# إعدادات البيانات

تتيح هذه الواجهة إجراء عمليات النسخ الاحتياطي للبيانات على السحابة ومحلياً، والاستعلام عن دليل البيانات المحلي، ومسح ذاكرة التخزين المؤقت، وغير ذلك من العمليات.

### النسخ الاحتياطي للبيانات

حالياً، يدعم النسخ الاحتياطي للبيانات فقط طريقة WebDAV. يمكنك اختيار خدمة تدعم WebDAV لإجراء النسخ الاحتياطي على السحابة.

يمكنك أيضاً تحقيق مزامنة البيانات عبر أجهزة متعددة عبر:  
`جهاز A` $$\xrightarrow{\text{نسخ احتياطي}}$$ `WebDAV` $$\xrightarrow{\text{استعادة}}$$ `جهاز B`

#### مثال باستخدام Jianguoyun

1. سجل الدخول إلى Jianguoyun، انقر على اسم المستخدم في الزاوية اليمنى العليا، واختر "معلومات الحساب":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. اختر "خيارات الأمان"، وانقر على "إضافة تطبيق"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. أدخل اسم التطبيق، وقم بإنشاء كلمة مرور عشوائية;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. انسخ كلمة المرور واحفظها;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. احصل على عنوان الخادم، واسم المستخدم، وكلمة المرور;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. في إعدادات Cherry Studio - إعدادات البيانات، املأ معلومات WebDAV;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. اختر نسخ احتياطي أو استعادة البيانات، ويمكنك تعيين فترة النسخ الاحتياطي التلقائي.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
خدمات WebDAV ذات المتطلبات المنخفضة هي عادةً خدمات التخزين السحابي:

* [Jianguoyun](https://www.jianguoyun.com/)
* [123 Pan](https://www.123pan.com/) (يتطلب عضوية)
* [Aliyun Drive](https://www.alipan.com/) (يتطلب شراء)
* [Box](https://www.box.com/) (المساحة المجانية 10GB، حد حجم الملف الواحد 250MB.)
* [Dropbox](https://www.dropbox.com/) (المساحة المجانية 2GB، يمكن توسيعها إلى 16GB بدعوة الأصدقاء.)
* [TeraCloud](https://teracloud.jp/en/) (المساحة المجانية 10GB، دعوة صديق تضيف 5GB إضافية.)
* [Yandex Disk](https://disk.yandex.com/) (المساحة المجانية 10GB للمستخدمين.)

الخدمات الأخرى تتطلب نشراً ذاتياً للخادم:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}