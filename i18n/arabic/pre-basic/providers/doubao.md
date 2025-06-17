
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# بايت دانس (دوباو)

* سجّل الدخول إلى [محرك البركان](https://console.volcengine.com/)
* انقر مباشرةً [هنا للوصول السريع](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### الحصول على مفتاح API

* انقر على [إدارة مفتاح API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) في الشريط الجانبي السفلي
* أنشئ مفتاح API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* بعد الإنشاء بنجاح، انقر على أيقونة العين الصغيرة بجانب مفتاح API الذي تم إنشاؤه لفتحه ونسخه

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* الصق مفتاح API الذي تم نسخه في CherryStudio، ثم شغّل مفتاح موفر الخدمة

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### تفعيل وإضافة النماذج

* في الشريط الجانبي لوحة تحكم سفينة نوح، فعّل النماذج التي تريد استخدامها عبر [إدارة التفعيل](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false). يمكنك تفعيل سلسلة دوباو ونماذج DeepSeek وغيرها حسب الحاجة.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* في [وثيقة قائمة النماذج](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)، ابحث عن معرّف النموذج (Model ID) المقابل للنموذج المطلوب

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="مثال على قائمة معرّفات نماذج محرك البركان"><figcaption></figcaption></figure>

* انتقل إلى إعدادات [خدمة النماذج](../../cherrystudio/preview/settings/providers.md) في Cherry Studio وابحث عن محرك البركان
* انقر على إضافة، ثم الصق معرّف النموذج الذي حصلت عليه في مربع نص معرّف النموذج

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* أضف النماذج بالتسلسل وفقًا لهذه العملية

### عنوان API

هناك طريقتان لكتابة عنوان API

* الطريقة الأولى (الافتراضية للعميل): `https://ark.cn-beijing.volces.com/api/v3/`
* الطريقة الثانية: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
لا فرق بين الطريقتين، يمكنك البقاء على الوضع الافتراضي دون تعديل.

للتعرف على الفرق بين النهايات `/` و `#`، راجع قسم عنوان API في إعدادات موفر الخدمة في الوثائق، [انقر للانتقال](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>مثال cURL في الوثائق الرسمية</p></figcaption></figure>