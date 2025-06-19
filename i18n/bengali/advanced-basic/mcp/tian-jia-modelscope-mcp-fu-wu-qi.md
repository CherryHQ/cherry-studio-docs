
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# ModelScope MCP সার্ভার যোগ করুন

> ModelScope MCP সার্ভার ব্যবহার করতে Cherry Studio v1.2.9 বা তার পরের সংস্করণে আপগ্রেড করতে হবে।

v1.2.9 সংস্করণে, Cherry Studio ModelScope Mofang-এর সাথে আনুষ্ঠানিক সহযোগিতা করেছে, MCP সার্ভার যোগ করার ধাপগুলো উল্লেখযোগ্যভাবে সহজ করে দিয়েছে। এটি কনফিগারেশন ত্রুটি এড়ায় এবং ModelScope কমিউনিটিতে প্রচুর MCP সার্ভার খুঁজে পাওয়া সম্ভব। চলুন Cherry Studio-তে ModelScope-এর MCP সার্ভার সিঙ্ক্রোনাইজ করার ধাপগুলো দেখি।

## অপারেশন ধাপসমূহ

### সিঙ্ক্রোনাইজেশন এন্ট্রি:

সেটিংসে MCP সার্ভার সেটিংস ক্লিক করুন, `সার্ভার সিঙ্ক্রোনাইজ করুন` বেছে নিন

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### MCP সার্ভিস আবিষ্কার করুন:

ModelScope নির্বাচন করুন এবং MCP সার্ভিস ব্রাউজ করুন

<figure><img src="../../.gitbook/assets/image (1) (4).png" alt=""><figcaption></figcaption></figure>

### MCP সার্ভার বিবরণ দেখুন

ModelScope-এ রেজিস্টার ও লগইন করুন এবং MCP সার্ভিসের বিস্তারিত দেখুন;

<figure><img src="../../.gitbook/assets/image (2) (6).png" alt=""><figcaption></figcaption></figure>

### সার্ভারের সাথে সংযোগ করুন

MCP সার্ভিস বিবরণে, "Connect Service" নির্বাচন করুন;

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### API টোকেন আবেদন এবং পেস্ট করুন

Cherry Studio-তে "Get API Token" ক্লিক করুন, ModelScope অফিসিয়াল ওয়েবসাইটে রিডাইরেক্ট হবে, API টোকেন কপি করুন এবং Cherry Studio-তে ফিরে পেস্ট করুন।

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### সফলভাবে সিঙ্ক্রোনাইজ

Cherry Studio-এর MCP সার্ভার তালিকায়, ModelScope-এর সাথে সংযুক্ত MCP সার্ভিস দেখা যাবে এবং কথোপকথনে ব্যবহার করা যাবে।

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### ইনক্রিমেন্টাল আপডেট

পরবর্তীতে ModelScope ওয়েবসাইটে নতুন সংযুক্ত MCP সার্ভারের জন্য শুধু `সার্ভার সিঙ্ক্রোনাইজ করুন` ক্লিক করলেই নতুন MCP সার্ভার যুক্ত হবে।

<figure><img src="../../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

এই ধাপগুলোর মাধ্যমে, আপনি Cherry Studio-তে ModelScope-এর MCP সার্ভার সহজে সিঙ্ক্রোনাইজ করা রপ্ত করেছেন। এই কনফিগারেশন প্রক্রিয়া ম্যানুয়াল সেটআপের জটিলতা এবং সম্ভাব্য ত্রুটি পুরোপুরি এড়ায়, পাশাপাশি ModelScope কমিউনিটির বিপুল MCP সার্ভার রিসোর্স ব্যবহার করা সম্ভব করে তোলে।

এই শক্তিশালী MCP সার্ভিসগুলি এক্সপ্লোর করুন ও ব্যবহার করুন, আপনার Cherry Studio অভিজ্ঞতাকে আরও সুবিধাজনক এবং সম্ভাবনাময় করে তুলুন!