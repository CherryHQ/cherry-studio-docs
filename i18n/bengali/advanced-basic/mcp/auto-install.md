
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# স্বয়ংক্রিয়ভাবে MCP ইন্সটল করুন

> স্বয়ংক্রিয় MCP ইন্সটলেশনের জন্য Cherry Studio v1.1.18 বা উচ্চতর সংস্করণে আপগ্রেড করতে হবে।

## ফিচার ওভারভিউ

ম্যানুয়াল ইন্সটলেশন ছাড়াও, Cherry Studio এ `@mcpmarket/mcp-auto-install` টুলটি অন্তর্ভুক্ত রয়েছে - এটি একটি সহজ MCP সার্ভার ইন্সটলেশন পদ্ধতি। আপনাকে MCP-সক্ষম লার্জ ল্যাঙ্গুয়েজ মডেল কনভার্সেশনে সংশ্লিষ্ট কমান্ড ইনপুট করতে হবে।

{% hint style="warning" %}
**টেস্টিং ফেজ রিমাইন্ডার:**

* `@mcpmarket/mcp-auto-install` বর্তমানে বেটা পর্যায়ে রয়েছে
* কার্যকারিতা LLM-এর "ইন্টেলিজেন্স"-এর উপর নির্ভরশীল, কিছু স্বয়ংক্রিয়ভাবে যোগ হবে, কিছু ক্ষেত্রে **MCP সেটিংসে ম্যানুয়ালি প্যারামিটার পরিবর্তন করতে হবে**
* বর্তমানে সার্চ সোর্স @modelcontextprotocol থেকে নেওয়া হয়, যা কাস্টমাইজ করা যাবে (নিচে বিস্তারিত)
{% endhint %}

## ব্যবহার নির্দেশিকা

উদাহরণস্বরূপ, আপনি ইনপুট করতে পারেন:

```
আমাকে একটি filesystem MCP সার্ভার ইন্সটল করতে সাহায্য করুন
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>MCP সার্ভার ইন্সটল করার জন্য কমান্ড ইনপুট করুন</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP সার্ভার কনফিগারেশন ইন্টারফেস</p></figcaption></figure>

সিস্টেম স্বয়ংক্রিয়ভাবে আপনার প্রয়োজন শনাক্ত করবে এবং `@mcpmarket/mcp-auto-install` এর মাধ্যমে ইন্সটলেশন সম্পন্ন করবে। এই টুল নিম্নলিখিত ধরনের MCP সার্ভার সাপোর্ট করে:
* filesystem (ফাইল সিস্টেম)
* fetch (নেটওয়ার্ক রিকোয়েস্ট)
* sqlite (ডাটাবেস)
* ইত্যাদি...

> MCP_PACKAGE_SCOPES পরিবর্তনশীল দিয়ে MCP সার্ভিস সার্চ সোর্স কাস্টমাইজ করা যায়, ডিফল্ট মান: `@modelcontextprotocol`।

## `@mcpmarket/mcp-auto-install` লাইব্রেরি পরিচিতি

{% hint style="info" %}
**ডিফল্ট কনফিগারেশন রেফারেন্স:**

```json
// `axun-uUpaWEdMEMU8C61K` সার্ভিস আইডি হিসেবে, যেকোনো কাস্টম স্ট্রিং কাজ করবে
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "অটো ইন্সটল MCP সার্ভিস (বেটা সংস্করণ)",
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
    "MCP_REGISTRY_PATH": "বিস্তারিত দেখুন https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` একটি ওপেন-সোর্স npm প্যাকেজ, বিস্তারিত এবং ব্যবহার নির্দেশিকা [npm অফিসিয়াল রিপোজিটরিতে](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) পাওয়া যাবে। `@mcpmarket` Cherry Studio-এর অফিসিয়াল MCP সার্ভিস কালেকশন।
{% endhint %}