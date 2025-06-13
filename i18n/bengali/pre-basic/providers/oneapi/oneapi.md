
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# OneAPI

* লগইন করুন এবং টোকেন পৃষ্ঠায় যান

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

* নতুন টোকেন তৈরি করুন (অথবা সরাসরি ডিফল্ট টোকেন↑ ব্যবহার করুন)

<figure><img src="../../../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

* টোকেন কপি করুন

<figure><img src="../../../.gitbook/assets/image (24).png" alt="" width="563"><figcaption></figcaption></figure>

* CherryStudio-এর সার্ভিস প্রোভাইডার সেটিংসে যান, সার্ভিস প্রোভাইডার তালিকার নীচে `যুক্ত করুন` ক্লিক করুন
* একটি রিমার্ক নাম লিখুন, প্রোভাইডার হিসাবে OpenAI নির্বাচন করুন, এবং 'ঠিক আছে' ক্লিক করুন

<figure><img src="../../../.gitbook/assets/image (25).png" alt="" width="291"><figcaption></figcaption></figure>

* কপি করা কী পেস্ট করুন
* API কী পাওয়ার পৃষ্ঠায় ফিরে যান, সংশ্লিষ্ট ব্রাউজারের অ্যাড্রেস বারে রুট অ্যাড্রেস কপি করুন, উদাহরণ:

<figure><img src="../../../.gitbook/assets/image (26).png" alt="" width="563"><figcaption><p><strong>শুধুমাত্র https://xxx.xxx.com কপি করুন, "/" এবং তার পরের অংশ প্রয়োজন নেই</strong></p></figcaption></figure>

{% hint style="info" %}
* যখন অ্যাড্রেসটি IP+পোর্ট হয়, তখন http://IP:পোর্ট লিখুন, যেমন: http://127.0.0.1:3000
* `http` এবং `https` এর মধ্যে কঠোর পার্থক্য করুন, SSL চালু না থাকলে https লিখবেন না
{% endhint %}

* মডেল যুক্ত করুন (ম্যানেজ ক্লিক করে স্বয়ংক্রিয়ভাবে পাবেন বা ম্যানুয়ালি ইনপুট করুন) এবং উপরের ডানদিকের সুইচ চালু করুন

{% hint style="success" %}
OneAPI-এর অন্যান্য থিমের ইন্টারফেস আলাদা হতে পারে, তবে যোগ করার পদ্ধতি উপরের প্রক্রিয়ার অনুরূপ
{% endhint %}