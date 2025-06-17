
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# অটো MCP ইন্সটলেশন

> অটো MCP ইন্সটলের জন্য Cherry Studio কে v1.1.18 বা তার চেয়ে নতুন সংস্করণে আপগ্রেড করতে হবে।

## বৈশিষ্ট্য সংক্ষেপ

হাতে কলমে ইন্সটল করার পাশাপাশি, Cherry Studio তে `@mcpmarket/mcp-auto-install` টুল অন্তর্ভুক্ত রয়েছে, যা MCP সার্ভার ইন্সটল করার আরও সহজ উপায়। আপনাকে শুধু MCP সাপোর্ট করে এমন বড় মডেল কনভারসেশনে প্রাসঙ্গিক কমান্ড লিখতে হবে।

{% hint style="warning" %}
**টেস্টিং পর্যায়ে সতর্কতা:**

* `@mcpmarket/mcp-auto-install` বর্তমানে টেস্টিং পর্যায়ে আছে
* কার্যকারিতা নির্ভর করে মডেলের "বুদ্ধিমত্তার" উপর, কিছু স্বয়ংক্রিয়ভাবে যোগ করতে পারে, আবার কিছু ক্ষেত্রে **MCP সেটিংসে ম্যানুয়ালি প্যারামিটার পরিবর্তন করতে হতে পারে**
* বর্তমানে সোর্স সার্চ হয় @modelcontextprotocol থেকে, আপনি নিজে কনফিগার করতে পারেন (নীচে বর্ণিত)
{% endhint %}

## ব্যবহার নির্দেশিকা

উদাহরণস্বরূপ, আপনি লিখতে পারেন:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>MCP সার্ভার ইন্সটল করতে কমান্ড লিখুন</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP সার্ভার কনফিগারেশন ইন্টারফেস</p></figcaption></figure>

সিস্টেম স্বয়ংক্রিয়ভাবে আপনার প্রয়োজনে বুঝবে এবং `@mcpmarket/mcp-auto-install` এর মাধ্যমে ইন্সটলেশন সম্পন্ন করবে। এই টুল নিম্নলিখিত ধরনের MCP সার্ভার সাপোর্ট করে:

* filesystem (ফাইল সিস্টেম)
* fetch (নেটওয়ার্ক রিকোয়েস্ট)
* sqlite (ডাটাবেস)
* ইত্যাদি...

> MCP_PACKAGE_SCOPES ভেরিয়েবল দ্বারা MCP সার্ভিস অনুসন্ধানের উৎস কাস্টমাইজ করা যায়, ডিফল্ট মান: `@modelcontextprotocol`, কাস্টম কনফিগারেশন করা যেতে পারে।

## `@mcpmarket/mcp-auto-install` লাইব্রেরি পরিচিতি

{% hint style="info" %}
**ডিফল্ট কনফিগারেশন রেফারেন্স:**

```json
// `axun-uUpaWEdMEMU8C61K` হল সার্ভিস আইডি, কাস্টমাইজ করা যায়
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
    "MCP_REGISTRY_PATH": "ডিটেইলসের জন্য দেখুন https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` হল একটি ওপেন-সোর্স npm প্যাকেজ, আপনি [npm অফিসিয়াল রিপোজিটরি](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) এ বিস্তারিত তথ্য ও ডকুমেন্টেশন দেখতে পারেন। `@mcpmarket` হল Cherry Studio এর অফিসিয়াল MCP সার্ভিস সংগ্রহ।
{% endhint %}