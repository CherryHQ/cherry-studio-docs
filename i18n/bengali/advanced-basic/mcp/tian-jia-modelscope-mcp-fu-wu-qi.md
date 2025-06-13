
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# ModelScope MCP সার্ভার যোগ করুন

> ModelScope MCP সার্ভার ব্যবহার করতে Cherry Studio v1.2.9 বা তার পরবর্তী সংস্করণে আপগ্রেড করতে হবে।

v1.2.9 সংস্করণে, Cherry Studio এবং ModelScope MoDa এর মধ্যে অফিসিয়াল অংশীদারিত্ব গড়ে উঠেছে যা MCP সার্ভার যোগ করার প্রক্রিয়াকে যথেষ্ট সরলীকৃত করেছে, কনফিগারেশনে ত্রুটি এড়াতে সহায়তা করে এবং ModelScope কমিউনিটিতে প্রচুর MCP সার্ভার আবিষ্কার করতে সক্ষম করে। নিচের ধাপগুলি অনুসরণ করে Cherry Studio-তে কিভাবে ModelScope-এর MCP সার্ভার সিঙ্ক্রোনাইজ করতে হয় তা দেখুন।

## কাজের ধাপ

### সিঙ্ক্রোনাইজেশন এন্ট্রি

সেটিংসে MCP সার্ভার সেটিংসে ক্লিক করুন, `সিঙ্ক্রোনাইজ সার্ভার` নির্বাচন করুন

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### MCP সার্ভিস আবিষ্কার করুন

ModelScope নির্বাচন করুন এবং MCP সার্ভিস ব্রাউজ করুন

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### MCP সার্ভারের বিবরণ দেখুন

ModelScope-এ রেজিস্টার/লগইন করুন এবং MCP সার্ভিসের বিবরণ দেখুন

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### সার্ভারের সাথে সংযোগ স্থাপন করুন

MCP সার্ভিস বিবরণে, সার্ভিস কানেক্ট করুন নির্বাচন করুন

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### API টোকেন অনুরোধ করুন এবং কপি-পেস্ট করুন

Cherry Studio-তে "API টোকেন পান" ক্লিক করুন, ModelScope ওয়েবসাইটে রিডাইরেক্ট হোন, API টোকেন কপি করুন এবং Cherry Studio-তে ফিরে এসে পেস্ট করুন

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### সফল সিঙ্ক্রোনাইজেশন

Cherry Studio-এর MCP সার্ভার তালিকায় ModelScope-এ সংযুক্ত MCP সার্ভিস দেখা যাবে এবং সংলাপে ব্যবহার করা যাবে

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### ইনক্রিমেন্টাল আপডেট

পরবর্তীতে ModelScope ওয়েবসাইটে নতুন সংযুক্ত MCP সার্ভারগুলির জন্য, `সিঙ্ক্রোনাইজ সার্ভার` ক্লিক করলেই ইনক্রিমেন্টাল MCP সার্ভার যোগ হয়ে যাবে

<figure><img src="../../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

উপরের ধাপগুলি অনুসরণ করে, Cherry Studio-তে ModelScope-এর MCP সার্ভার সিঙ্ক্রোনাইজ করার পদ্ধতি আপনি সফলভাবে আয়ত্ত করেছেন। এই কনফিগারেশন প্রক্রিয়া কেবল সরলীকৃত নয়, ম্যানুয়াল কনফিগারেশনের জটিলতা এবং ত্রুটির সম্ভাবনাও দূর করে, এর পাশাপাশি ModelScope কমিউনিটির বিপুল পরিমাণ MCP সার্ভার রিসোর্স ব্যবহারের সুবিধাও এনে দেয়।

এই শক্তিশালী MCP সার্ভিসগুলি অন্বেষণ এবং ব্যবহার করে আপনার Cherry Studio অভিজ্ঞতায় আরও সুবিধা ও সম্ভাবনা নিয়ে আসুন!