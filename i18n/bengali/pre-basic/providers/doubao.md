
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# ByteDance (ডুবাও)

* [ভলকানো ইঞ্জিনে](https://console.volcengine.com/) লগইন করুন
* সরাসরি ক্লিক করুন [এখানে](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### API কী সংগ্রহ করুন

* সাইডবারের নিচে [API কী ব্যবস্থাপনায়](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) ক্লিক করুন
* API কী তৈরি করুন

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* সফলভাবে তৈরি হওয়ার পর, তৈরি করা API কী-এর পাশের 👁️ আইকনে ক্লিক করে দেখুন এবং কপি করুন

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* কপি করা API কী CherryStudio-তে প্রবেশ করান, এবং পরিষেবা প্রদানকারী সুইচটি চালু করুন

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### সক্রিয় করুন এবং মডেল যুক্ত করুন

* আর্ক কনসোল সাইডবারের সর্বনিম্নে [সক্রিয়করণ ব্যবস্থাপনায়](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) ক্লিক করে প্রয়োজনীয় মডেল সক্রিয় করুন। এখানে আপনি প্রয়োজনমতো ডুবাও সিরিজ এবং DeepSeek এর মতো মডেল সক্রিয় করতে পারেন

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* [মডেল তালিকা ডকুমেন্টেশন](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)-এ আপনার প্রয়োজনীয় মডেলের জন্য সংশ্লিষ্ট **মডেল ID** খুঁজুন

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="ভলকানো ইঞ্জিন মডেল ID তালিকার উদাহরণ"><figcaption></figcaption></figure>

* Cherry Studio-এর [মডেল পরিষেবা](../../cherrystudio/preview/settings/providers.md) সেটিংস খুলে ভলকানো ইঞ্জিন খুঁজুন
* "যুক্ত করুন" ক্লিক করুন, পূর্বে প্রাপ্ত **মডেল ID** কপি করে মডেল ID টেক্সট বক্সে পেস্ট করুন

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* এই প্রক্রিয়া অনুসরণ করে মডেলগুলো ক্রমানুসারে যুক্ত করুন

### API এন্ডপয়েন্ট

API এন্ডপয়েন্ট দুভাবে লেখা যায়:

* ক্লায়েন্ট ডিফল্ট: `https://ark.cn-beijing.volces.com/api/v3/`
* বিকল্প: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
দুটি লেখার পদ্ধতির মধ্যে কোন পার্থক্য নেই, ডিফল্ট সংস্করণ ব্যবহার করুন (পরিবর্তনের প্রয়োজন নেই)।

`/` এবং `#` দিয়ে শেষ করার পার্থক্য সংক্রান্ত বিশদ জানতে পরিষেবা প্রদানকারী সেটিংসের API এন্ডপয়েন্ট বিভাগ দেখুন, [এখানে যান](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>অফিসিয়াল ডকুমেন্টেশন cURL উদাহরণ</p></figcaption></figure>