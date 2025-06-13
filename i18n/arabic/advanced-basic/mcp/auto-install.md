
{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# التثبيت التلقائي لـ MCP

> يتطلب التثبيت التلقائي لـ MCP تحديث Cherry Studio إلى الإصدار v1.1.18 أو أحدث.

## نبذة عن الميزة

بالإضافة إلى التثبيت اليدوي، يحتوي Cherry Studio على أداة `@mcpmarket/mcp-auto-install` المدمجة، وهي طريقة أكثر سهولة لتثبيت خادم MCP. كل ما عليك هو إدخال الأمر المناسب في حوار النموذج الكبير الذي يدعم خدمة MCP.

{% hint style="warning" %}
**تذكير بمرحلة الاختبار:**

* `@mcpmarket/mcp-auto-install` لا يزال في مرحلة الاختبار.
* يعتمد التأثير على "ذكاء" النموذج الكبير، فالبعض يضيف تلقائيًا، والبعض الآخر **لا يزال يحتاج إلى تغيير بعض المعلمات يدويًا في إعدادات MCP**.
* حاليًا، يتم البحث في المصدر من @modelcontextprotocol، ويمكن تكوينه بشكل مستقل (انظر الشرح أدناه).
{% endhint %}

## تعليمات الاستخدام

على سبيل المثال، يمكنك إدخال:

```
ساعدني في تثبيت خادم filesystem mcp
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>إدخال أمر لتثبيت خادم MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>واجهة تكوين خادم MCP</p></figcaption></figure>

سيتعرف النظام تلقائيًا على احتياجاتك ويكمل التثبيت عبر `@mcpmarket/mcp-auto-install`. تدعم هذه الأداة أنواعًا متعددة من خوادم MCP، بما في ذلك على سبيل المثال لا الحصر:

* filesystem (نظام الملفات)
* fetch (طلب الشبكة)
* sqlite (قاعدة البيانات)
* إلخ...

> يمكن تخصيص متغير MCP_PACKAGE_SCOPES لمصدر بحث خدمة MCP، والقيمة الافتراضية هي: `@modelcontextprotocol`، ويمكن تكوينها حسب الحاجة.

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
    "MCP_REGISTRY_PATH": "للتفاصيل، راجع https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` هي حزمة npm مفتوحة المصدر، يمكنك الاطلاع على التفاصيل ووثائق الاستخدام في [npm official repository](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` هو مجموعة خدمات MCP الرسمية لـ Cherry Studio.
{% endhint %}