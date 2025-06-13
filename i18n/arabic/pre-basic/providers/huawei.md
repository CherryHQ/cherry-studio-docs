
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# سحابة هواوي (Huawei Cloud)

1. انتقل إلى [سحابة هواوي](https://auth.huaweicloud.com/authui/login) لإنشاء حساب وتسجيل الدخول
2. انقر على [هذا الرابط](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) للدخول إلى لوحة تحكم Maa S
3. التفويض (Authorization)

<details>

<summary>خطوات التفويض (تخطي إذا تم التفويض مسبقاً)</summary>

1. بعد الدخول إلى صفحة الرابط (2)، اتبع الإرشادات للدخول إلى صفحة التفويض (انقر IAM子用户 → 新增委托 → 普通用户)

![](<../../.gitbook/assets/image (49).png>)

2. بعد النقر فوق إنشاء، ارجع إلى صفحة الرابط (2)
3. ستظهر رسالة تفيد بأن أذونات الوصول غير كافية، انقر على "انقر هنا" في الرسالة
4. أضف التفويض الحالي وحدد موافق

![](<../../.gitbook/assets/image (50).png>)

ملاحظة: هذه الطريقة مناسبة للمبتدئين، لا حاجة لقراءة الكثير من المحتوى، فقط انقر وفقاً للإرشادات.

</details>

4. انقر على إدارة المصادقة في الشريط الجانبي، أنشئ مفتاح API (سري) وانسخه

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

ثم في CherryStudio، أنشئ موفر خدمة جديد

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

بعد الإنشاء، املأ المفتاح السري

5. انقر على نشر النموذج في الشريط الجانبي، وقم بالمطالبة بالكل (Claim All)

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6. انقر على استدعاء (Invoke)

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

انسخ العنوان عند ①، والصقه في عنوان موفر الخدمة في CherryStudio وأضف علامة "#" في النهاية

أضف "#" في النهاية  
أضف "#" في النهاية  
أضف "#" في النهاية  
أضف "#" في النهاية

لماذا نضيف "#"؟ [انظر هنا](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> يمكنك التخطي والمتابعة مباشرة وفقاً للبرنامج التعليمي؛  
> أو استخدام طريقة حذف v1/chat/completions للتعبيئة.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

ثم انسخ اسم النموذج عند ②، واذهب إلى CherryStudio وانقر على زر "+添加" لإنشاء نموذج جديد

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

أدخل اسم النموذج، لا تقم بإضافات أو علامات اقتباس، اكتب كما في المثال.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

انقر على زر إضافة النموذج لإكمال الإضافة.

{% hint style="info" %}
في سحابة هواوي، نظراً لاختلاف عنوان كل نموذج، يحتاج كل نموذج إلى موفر خدمة جديد. كرر الخطوات أعلاه لكل نموذج.
{% endhint %}