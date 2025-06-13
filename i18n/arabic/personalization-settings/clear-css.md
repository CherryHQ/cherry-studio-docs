---
icon: trash-xmark
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# مسح إعدادات CSS

{% hint style="warning" %}
استخدم هذه الطريقة عند تعيين CSS خاطئ أو عند عدم القدرة على الدخول إلى واجهة الإعدادات بعد تعيين CSS.
{% endhint %}

* افتح وحدة التحكم (Console)، انقر على نافذة CherryStudio، ثم اضغط على الاختصار <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (لنظام MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>).
* في نافذة وحدة التحكم التي ستظهر، انقر على علامة تبويب `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* اكتب يدويًا الأمر `document.getElementById('user-defined-custom-css').remove()` (النسخ واللصغ غالبًا لن ينفذ الأمر).
* اضغط على زر الإدخال (Enter) بعد كتابة الأمر لمسح إعدادات CSS، ثم عد إلى إعدادات العرض في CherryStudio واحذف كود CSS المُعطل.