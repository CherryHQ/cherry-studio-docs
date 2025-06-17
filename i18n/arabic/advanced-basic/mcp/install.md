
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# تثبيت بيئة MCP

**MCP (بروتوكول سياق النموذج)** هو بروتوكول مفتوح المصدر يهدف إلى توفير معلومات السياق لنماذج اللغة الكبيرة (LLM) بطريقة موحدة. لمزيد من التفاصيل حول MCP، راجع [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## استخدام MCP في Cherry Studio

دعنا نأخذ وظيفة `fetch` كمثال لإظهار كيفية استخدام MCP في Cherry Studio. يمكنك العثور على التفاصيل في [المستندات](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **التحضير: تثبيت uv وbun**

{% hint style="warning" %}
يستخدم Cherry Studio حاليًا [uv](https://github.com/astral-sh/uv) و [bun](https://github.com/oven-sh/bun) المدمجين فقط، **ولن يعيد استخدام** نسخ uv وbun المثبتة مسبقًا على النظام.
{% endhint %}

في `الإعدادات - خادم MCP`، انقر على زر `تثبيت` لتنزيله وتثبيته تلقائيًا. نظرًا لأنه يتم التحميل مباشرة من GitHub، فقد تكون السرعة بطيئة واحتمال الفشل مرتفعًا. يعتمد نجاح التثبيت على وجود الملفات في المجلدات المذكورة أدناه.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**دليل تثبيت الملفات القابلة للتنفيذ:**  
Windows: `C:\Users\用户名\.cherrystudio\bin`  
macOS وLinux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>دليل bin</p></figcaption></figure>

**في حالة فشل التثبيت:**  
يمكنك إنشاء روابط رمزية للأوامر المقابلة من النظام إلى هذا الدليل. إذا لم يكن الدليل موجودًا، قم بإنشائه يدويًا. بدلاً من ذلك، يمكنك تنزيل الملفات القابلة للتنفيذ يدويًا ووضعها في هذا الدليل:  
Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)  
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)