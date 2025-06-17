
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# GitHub Copilot

لستخدام GitHub Copilot، يجب أولاً امتلاك حساب GitHub والاشتراك في خدمة GitHub Copilot. يمكن استخدام نسخة الاشتراك المجانية أيضًا، لكن النسخة المجانية لا تدعم أحدث نموذج Claude 3.7. يُرجى مراجعة [الموقع الرسمي لـ GitHub Copilot](https://github.com/features/copilot) للحصول على التفاصيل.

## الحصول على كود الجهاز

انقر على "تسجيل الدخول إلى GitHub"، ثم احصل على Device Code وانسخه.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="صورة توضيحية للحصول على Device Code"><figcaption><p>الحصول على Device Code</p></figcaption></figure>

## املأ كود الجهاز في المتصفح وقم بالتفويض

بعد الحصول على Device Code بنجاح، انقر على الرابط لفتح المتصفح، سجّل الدخول إلى حساب GitHub في المتصفح، أدخل Device Code ووافق على التفويض.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="صورة توضيحية لتفويض GitHub"><figcaption><p>تفويض GitHub</p></figcaption></figure>

بعد التفويض بنجاح، عد إلى Cherry Studio، انقر على "الاتصال بـ GitHub"، وعند نجاح الاتصال سيعرض اسم المستخدم والصورة الشخصية لحساب GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="صورة توضيحية لنجاح الاتصال بـ GitHub"><figcaption><p>اتصال GitHub ناجح</p></figcaption></figure>

## انقر على "إدارة" للحصول على قائمة النماذج

انقر على زر "إدارة" الموجود أدناه، وسيقوم تلقائيًا بالحصول على قائمة النماذج المدعومة حاليًا عبر الإنترنت.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="صورة توضيحية للحصول على قائمة النماذج"><figcaption><p>الحصول على قائمة النماذج</p></figcaption></figure>

## الأسئلة الشائعة

### فشل الحصول على Device Code، يرجى إعادة المحاولة

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="صورة توضيحية لفشل الحصول على Device Code"><figcaption><p>فشل الحصول على Device Code</p></figcaption></figure>

يتم حاليًا بناء الطلبات باستخدام Axios، ولا يدعم Axios وكيل socks. يُرجى استخدام وكيل النظام أو وكيل HTTP، أو عدم ضبط الوكيل في CherryStudio واستخدام الوكيل العام بدلاً من ذلك. أولاً، تأكد من أن اتصالك بالشبكة يعمل بشكل طبيعي لتجنب فشل الحصول على Device Code.