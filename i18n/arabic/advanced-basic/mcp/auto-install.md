
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# التثبيت التلقائي لـ MCP

> يتطلب التثبيت التلقائي لـ MCP ترقية Cherry Studio إلى الإصدار v1.1.18 أو أعلى.

## مقدمة عن الميزة

بالإضافة إلى التثبيت اليدوي، يحتوي Cherry Studio على أداة `@mcpmarket/mcp-auto-install` مدمجة، وهي طريقة أكثر سهولة لتثبيت خادم MCP. كل ما عليك فعله هو إدخال الأمر المناسب في محادثة النموذج اللغوي الكبير الذي يدعم خدمة MCP.

{% hint style="warning" %}
**تذكير بمرحلة الاختبار:**
* `@mcpmarket/mcp-auto-install` لا يزال في مرحلة الاختبار
* يعتمد الأداء على "ذكاء" النموذج اللغوي الكبير - فبعضها يضيف التكوين تلقائيًا بينما يتطلب البعض **تعديل بعض المعلمات يدويًا في إعدادات MCP**
* حاليًا يتم البحث في المصادر من خلال @modelcontextprotocol، ويمكن تكوينه يدويًا (كما هو موضح أدناه)
{% endhint %}

## تعليمات الاستخدام

على سبيل المثال، يمكنك إدخال:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>إدخال أمر لتثبيت خادم MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>واجهة تكوين خادم MCP</p></figcaption></figure>

سيتعرف النظام تلقائيًا على طلبك ويقوم بالتثبيت باستخدام `@mcpmarket/mcp-auto-install`. تدعم هذه الأداة أنواعًا متعددة من خوادم MCP، تشمل:

* filesystem (نظام الملفات)
* fetch (جلب البيانات)
* sqlite (قاعدة بيانات)
* وغيرها...

> يمكن تخصيص مصادر بحث خدمة MCP عبر متغير MCP_PACKAGE_SCOPES، حيث تكون القيمة الافتراضية: `@modelcontextprotocol`.

## مقدمة عن مكتبة `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**مرجع الإعداد الافتراضي:**

```json
// `axun-uUpaWEdMEMU8C61K` هو معرف الخدمة، يمكن تخصيصه
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "详情见https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` عبارة عن حزمة npm مفتوحة المصدر. يمكنك الاطلاع على التفاصيل والوثائق في [المستودع الرسمي لـ npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). يُعتبر `@mcpmarket` المجموعة الرسمية لخدمات MCP من Cherry Studio.
{% endhint %}