
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# تكوين واستخدام MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1.  افتح إعدادات Cherry Studio.
2.  ابحث عن خيار `MCP 服务器`.
3.  انقر على `添加服务器`.
4.  املأ المعلمات ذات الصلة لخادم MCP ([رابط مرجعي](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). قد تشمل المحتويات التي تحتاج إلى ملئها:
    *   الاسم: اسم مخصص مثل `fetch-server`
    *   النوع: اختر `STDIO`
    *   الأمر: املأ `uvx`
    *   المعلمات: املأ `mcp-server-fetch`
    *   (قد تكون هناك معلمات أخرى حسب الخادم المحدد)
5.  انقر على `保存`.

{% hint style="success" %}
بعد إكمال التكوين أعلاه، سيقوم Cherry Studio تلقائيًا بتنزيل خادم MCP المطلوب - `fetch server`. بعد اكتمال التنزيل، يمكننا البدء في استخدامه! ملاحظة: عند عدم تكوين mcp-server-fetch بنجاح، يمكنك محاولة إعادة تشغيل الكمبيوتر.
{% endhint %}

### تمكين خدمة MCP في مربع الدردشة

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

*   تمت إضافة خادم MCP بنجاح في إعدادات `MCP 服务器`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **عرض تأثير الاستخدام**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

كما يتضح من الصورة أعلاه، بعد دمج وظيفة `fetch` في MCP، أصبح Cherry Studio قادرًا على:
- فهم نية استعلام المستخدم بشكل أفضل
- الحصول على المعلومات ذات الصلة من الإنترنت
- تقديم إجابات أكثر دقة وشمولاً.