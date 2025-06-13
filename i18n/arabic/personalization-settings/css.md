---
icon: file-code
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# تخصيص CSS

يمكنك تعديل مظهر البرنامج ليناسب ذوقك الخاص باستخدام CSS مخصص، كما في المثال التالي:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>تخصيص CSS</p></figcaption></figure>

```css
:root {
  --color-background: #1a462788;
  --color-background-soft: #1a4627aa;
  --color-background-mute: #1a462766;
  --navbar-background: #1a4627;
  --chat-background: #1a4627;
  --chat-background-user: #28b561;
  --chat-background-assistant: #1a462722;
}

#content-container {
  background-color: #2e5d3a !important;
}
```

### متغيرات مضمنة

```css
:root {
  font-family: "汉仪唐美人" !important; /* نوع الخط */
}

/* لون خط توسيع التفكير العميق */
.ant-collapse-content-box .markdown {
  color: red;
}

/* متغيرات السمة */
:root {
  --color-black-soft: #2a2b2a; /* لون خلفية داكن */
  --color-white-soft: #f8f7f2; /* لون خلفية فاتح */
}

/* سمة داكنة */
body[theme-mode="dark"] {
  /* الألوان */
  --color-background: #2b2b2b; /* لون خلفية داكن */
  --color-background-soft: #303030; /* لون خلفية فاتح */
  --color-background-mute: #282c34; /* لون خلفية محايد */
  --navbar-background: var(-–color-black-soft); /* لون خلفية شريط التنقل */
  --chat-background: var(–-color-black-soft); /* لون خلفية الدردشة */
  --chat-background-user: #323332; /* لون خلفية رسائل المستخدم */
  --chat-background-assistant: #2d2e2d; /* لون خلفية رسائل المساعد */
}

/* أنماط خاصة للسمة الداكنة */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* لون خلفية حاوية المحتوى */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* لون خلفية الرسائل */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* لون خلفية حقل الإدخال */
    border: 1px solid #5e5d5940; /* لون حدود حقل الإدخال */
    border-radius: 8px; /* زوايا دائرية لحدود حقل الإدخال */
  }

  /* أنماط الأكواد */
  code {
    background-color: #e5e5e20d; /* لون خلفية الكود */
    color: #ea928a; /* لون نص الكود */
  }

  pre code {
    color: #abb2bf; /* لون نص الكود في العناوين البرمجية */
  }
}

/* سمة فاتحة */
body[theme-mode="light"] {
  /* الألوان */
  --color-white: #ffffff; /* اللون الأبيض */
  --color-background: #ebe8e2; /* لون خلفية فاتح */
  --color-background-soft: #cbc7be; /* لون خلفية فاتح */
  --color-background-mute: #e4e1d7; /* لون خلفية محايد  */
  --navbar-background: var(-–color-white-soft); /* لون خلفية شريط التنقل */
  --chat-background: var(-–color-white-soft); /* لون خلفية الدردشة */
  --chat-background-user: #f8f7f2; /* لون خلفية رسائل المستخدم */
  --chat-background-assistant: #f6f4ec; /* لون خلفية رسائل المساعد */
}

/* أنماط خاصة للسمة الفاتحة */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* لون خلفية حاوية المحتوى */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* لون خلفية الرسائل */
  }

  .inputbar-container {
    background-color: #ffffff; /* لون خلفية حقل الإدخال */
    border: 1px solid #87867f40; /* لون حدود حقل الإدخال */
    border-radius: 8px; /* زوايا دائرية لحدود حقل الإدخال، يمكن تعديل الحجم حسب التفضيل */
  }

  /* أنماط الأكواد */
  code {
    background-color: #3d39290d; /* لون خلفية الكود */
    color: #7c1b13; /* لون نص الكود */
  }

  pre code {
    color: #000000; /* لون نص الكود في العناوين البرمجية */
  }
}
```

يمكن الرجوع إلى المزيد من متغيرات السمة في الكود المصدري: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### توصيات ذات صلة

مكتبة سُمي Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

مشاركة بعض سُمي Cherry Studio ذات الطابع الصيني: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)