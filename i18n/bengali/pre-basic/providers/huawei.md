
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# হুয়াওয়ে ক্লাউড

১. [হুয়াওয়ে ক্লাউড](https://auth.huaweicloud.com/authui/login)-এ অ্যাকাউন্ট তৈরি করে লগইন করুন

২. [এই লিঙ্কে](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) ক্লিক করে MaaS কনসোলে প্রবেশ করুন

৩. অনুমোদন

<details>

<summary>অনুমোদন প্রক্রিয়া (ইতিমধ্যে অনুমোদিত হলে এড়িয়ে যান)</summary>

১. (২) নং লিঙ্কের পৃষ্ঠায় প্রবেশের পর, নির্দেশনা অনুসারে অনুমোদন পৃষ্ঠায় যান (IAM সাব-ইউজার → নতুন অ্যাসাইনমেন্ট → নিয়মিত ব্যবহারকারী)

![](<../../.gitbook/assets/image (49).png>)

২. তৈরি ক্লিক করার পর (২) নং লিঙ্কের পৃষ্ঠায় ফিরে যান
৩. অ্যাক্সেস স্বল্পতার বিষয়ে সতর্কতা দেখাবে, সতর্কতায় "এখানে ক্লিক করুন" বোতামে ক্লিক করুন
৪. বিদ্যমান অনুমোদনে সংযোজন করুন এবং নিশ্চিত করুন

![](<../../.gitbook/assets/image (50).png>)

দ্রষ্টব্য: এই পদ্ধতিটি নবীনদের জন্য উপযোগী, অতিরিক্ত বিষয়বস্তু দেখার প্রয়োজন নেই, শুধু নির্দেশনা অনুযায়ী ক্লিক করুন। একবারে সফলভাবে অনুমোদন করতে পারলে নিজের পদ্ধতিতে এগোনো যেতে পারে।

</details>

৪. সাইডবারের Authentication Management-এ ক্লিক করুন, API Key তৈরি করুন এবং কপি করুন

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

তারপর CherryStudio-তে নতুন প্রদানকারী তৈরি করুন

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

তৈরি সম্পন্ন হলে API Key ইনপুট করুন

৫. সাইডবারের Model Deployment-এ ক্লিক করুন, সমস্ত রিসোর্স দাবি করুন (Claim All)

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

৬. Deploy-এ ক্লিক করুন

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

① চিহ্নিত ঠিকানাটি কপি করুন, CherryStudio-র প্রদানকারী ঠিকানায় পেস্ট করুন এবং শেষে "#" যোগ করুন

এবং শেষে "#" যোগ করুন

এবং শেষে "#" যোগ করুন

এবং শেষে "#" যোগ করুন

এবং শেষে "#" যোগ করুন

কেন "#" যোগ করবেন? [এখানে দেখুন](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> অবশ্যই সেখানে না দেখে সরাসরি টিউটোরিয়াল অনুসরণ করতে পারেন;
>
> অথবা v1/chat/completions ডিলিট করে পূরণ করতে পারেন, নিজের পদ্ধতিতে পূরণ করতে পারলে তাই করুন। না পারলে অবশ্যই টিউটোরিয়াল অনুসরণ করুন।

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

② চিহ্নিত মডেলের নাম কপি করুন, CherryStudio-তে "+Add" বোতাম ক্লিক করে নতুন মডেল তৈরি করুন

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

মডেলের নাম ইনপুট করুন, অতিরিক্ত কিছু যোগ করবেন না, উদ্ধৃতি চিহ্ন দেবেন না, উদাহরণে যেমন দেখানো হয়েছে হুবহু লিখুন

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Add Model বোতামে ক্লিক করে মডেল যুক্ত করা সম্পন্ন করুন।

{% hint style="info" %}
হুয়াওয়ে ক্লাউডে প্রতিটি মডেলের ঠিকানা ভিন্ন হওয়ায়, প্রতিটি মডেলের জন্য আলাদা প্রদানকারী তৈরি করতে হবে। উপরের ধাপগুলি পুনরাবৃত্তি করুন।
{% endhint %}