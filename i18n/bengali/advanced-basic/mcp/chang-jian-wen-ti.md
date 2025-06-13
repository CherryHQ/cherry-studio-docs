---
icon: hexagon-exclamation
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# সাধারণ সমস্যাসমূহ

### 1. mcp-server-time

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6068931438453048569-y.jpg" alt=""><figcaption><p>ত্রুটির স্ক্রিনশট</p></figcaption></figure>

**সমাধান**  
"প্যারামিটার" কলামে নিম্নলিখিতগুলি লিখুন:

```
mcp-server-time
--local-timezone
<আপনার স্ট্যান্ডার্ড সময় অঞ্চল, উদাহরণ: Asia/Shanghai>
```