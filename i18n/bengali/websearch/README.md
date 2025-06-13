---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

```bengali
---
icon: cherries
---

# ইন্টারনেট সংযোগ মোড

{% hint style="info" %}
যেসব ক্ষেত্রে ইন্টারনেট সংযোগ প্রয়োজন তার উদাহরণ:

* সময়সাপেক্ষ তথ্য: যেমন আজ/এই সপ্তাহে/এইমাত্র সোনার ভবিষ্যৎ মূল্য ইত্যাদি।
* রিয়েল-টাইম ডেটা: যেমন আবহাওয়া, মুদ্রা বিনিময় হার ইত্যাদি গতিশীল সংখ্যাসূচক মান।
* সাম্প্রতিক জ্ঞান: যেমন নতুন বিষয়, নতুন ধারণা, নতুন প্রযুক্তি ইত্যাদি...
{% endhint %}

### এক、ইন্টারনেট সংযোগ কীভাবে চালু করবেন

Cherry Studio-র প্রশ্ন উইন্ডোতে, 【ছোট গ্লোব】 আইকনে ক্লিক করলেই ইন্টারনেট সংযোগ চালু হয়ে যাবে।

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>গ্লোব আইকনে ক্লিক করুন - ইন্টারনেট সংযোগ চালু করুন</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>নির্দেশ করে - ইন্টারনেট সংযোগ সক্রিয় করা হয়েছে</p></figcaption></figure>

### দুই、বিশেষভাবে লক্ষণীয়: ইন্টারনেট সংযোগের দুইটি মোড রয়েছে

#### মোড ১: মডেল সার্ভিস প্রোভাইডারের বড় মডেলে অন্তর্নির্মিত ইন্টারনেট সংযোগ

এই ক্ষেত্রে, ইন্টারনেট সংযোগ চালু করলেই সরাসরি ব্যবহার করা যাবে, অত্যন্ত সহজ।

{% hint style="warning" %}
প্রশ্নোত্তর ইন্টারফেসের উপরে, মডেল নামের পাশে ছোট গ্লোব আইকন আছে কি না দেখে দ্রুত বিচার করতে পারেন যে মডেলটি ইন্টারনেট সংযোগ সমর্থন করে কিনা।
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

মডেল ম্যানেজমেন্ট পেজেও, এই পদ্ধতিতে আপনি সহজেই চিনতে পারবেন কোন মডেলগুলো ইন্টারনেট সংযোগ সমর্থন করে আর কোনগুলো করে না।

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Cherry Studio বর্তমানে যেসব ইন্টারনেট-সক্ষম মডেল সার্ভিস প্রোভাইডার সমর্থন করে**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (সমস্ত মডেল ইন্টারনেট সংযোগ সমর্থন করে)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">ZHIPU AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian ইত্যাদি</mark>

{% hint style="danger" %}
বিশেষভাবে লক্ষণীয়:

একটি বিশেষ পরিস্থিতি রয়েছে, এমনকি মডেলে ছোট গ্লোব আইকন না থাকলেও এটি ইন্টারনেট সংযোগ করতে পারে, যেমন নিচের টিউটোরিয়ালে ব্যাখ্যা করা হয়েছে।
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***



#### মোড ২: মডেল ইন্টারনেট সংযোগ সমর্থন করে না, Tavily সার্ভিস ব্যবহার করে ইন্টারনেট সংযোগ সক্রিয় করা

যখন আমরা এমন একটি বড় মডেল ব্যবহার করি যা ইন্টারনেট সংযোগ সমর্থন করে না (নামের পাশে ছোট গ্লোব আইকন নেই), এবং আমাদের রিয়েল-টাইম তথ্য প্রক্রিয়া করার প্রয়োজন হয়, তখন Tavily ওয়েব সার্চ সার্ভিস ব্যবহার করতে হবে।

**প্রথমবার Tavily সার্ভিস ব্যবহার করলে**, একটি পপআপ উইন্ডো দেখা যাবে কিছু তথ্য সেট আপ করতে, নির্দেশিকা অনুসরণ করুন-অত্যন্ত সহজ!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>পপআপ, ক্লিক করুন: সেটিংসে যান</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>এপিআই কী নিন</p></figcaption></figure>

এপিআই কী নিতে ক্লিক করলে স্বয়ংক্রিয়ভাবে **tavily-এর অফিসিয়াল ওয়েবসাইটের** লগইন/রেজিস্ট্রেশন পেজে যাবে, রেজিস্ট্রেশন করে লগইন করার পর এপিআইকি তৈরি করুন, তারপর কীটি Cherry Studio-তে কপি করুন।

{% hint style="danger" %}
রেজিস্ট্রেশন করতে সমস্যা হলে, এই ডকুমেন্টের একই ডিরেক্টরির অধীনে "tavily ইন্টারনেট লগইন রেজিস্ট্রেশন টিউটোরিয়াল" রেফারেন্স করুন।
{% endhint %}

**tavily রেজিস্ট্রেশন রেফারেন্স ডকুমেন্ট:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

নিচের ইন্টারফেসটি দেখালে বুঝবেন রেজিস্ট্রেশন সফল হয়েছে।

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>কী কপি করুন</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>কী পেস্ট করুন, সব সম্পন্ন!</p></figcaption></figure>

আবার একবার চেষ্টা করে ফলাফল দেখুন। ফলাফল থেকে বোঝা যাচ্ছে, ইন্টারনেট সফলভাবে সার্চ হয়েছে, এবং সার্চ ফলাফলের সংখ্যা আমাদের সেট করা ডিফল্ট মান: ৫টি।

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
লক্ষণীয়: tavily প্রতি মাসে সীমিত ফ্রি কোটা দেয়, কোটা অতিক্রম করলে পেমেন্ট করতে হবে\~\~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> পিএস: কোনো ভুল পেলে, আমাদের অবহিত করতে দ্বিধা করবেন না। 
```