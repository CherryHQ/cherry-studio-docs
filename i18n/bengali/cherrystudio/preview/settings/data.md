---
icon: database
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# ডেটা সেটিংস

এই ইন্টারফেসের মাধ্যমে ক্লায়েন্ট ডেটার ক্লাউড ও লোকাল ব্যাকআপ, স্থানীয় ডেটা ডিরেক্টরি অনুসন্ধান এবং ক্যাশে পরিষ্কার করার মতো অপারেশন করা যায়।

### ডেটা ব্যাকআপ

বর্তমানে ডেটা ব্যাকআপ শুধুমাত্র WebDAV পদ্ধতিতে সমর্থিত। আপনি WebDAV সমর্থন করে এমন পরিষেবা নির্বাচন করে ক্লাউড ব্যাকআপ করতে পারেন।

আপনি `A কম্পিউটার` $$\xrightarrow{\text{ব্যাকআপ}}$$ `WebDAV` $$\xrightarrow{\text{পুনরুদ্ধার}}$$ `B কম্পিউটার` পদ্ধতিতে একাধিক ডিভাইসে ডেটা সিঙ্ক্রোনাইজ করতে পারেন।

#### Jianguoyun উদাহরণ

1. Jianguoyun-এ লগ ইন করুন, উপরে ডানদিকে ব্যবহারকারীর নামে ক্লিক করে "অ্যাকাউন্ট তথ্য" নির্বাচন করুন:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. "সুরক্ষা বিকল্পগুলি" নির্বাচন করুন, "অ্যাপ যুক্ত করুন" এ ক্লিক করুন:

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. অ্যাপ্লিকেশনের নাম লিখুন, এলোমেলো পাসওয়ার্ড তৈরি করুন:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. পাসওয়ার্ড কপি করে সংরক্ষণ করুন:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. সার্ভারের ঠিকানা, অ্যাকাউন্ট এবং পাসওয়ার্ড পেতে:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio সেটিংস - ডেটা সেটিংসে WebDAV তথ্য পূরণ করুন:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. ডেটা ব্যাকআপ বা পুনরুদ্ধার নির্বাচন করুন এবং স্বয়ংক্রিয় ব্যাকআপের সময়সীমা সেট করতে পারেন:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
সাধারণত WebDAV পরিষেবার জন্য কম থ্রেশহোল্ডের ডিস্ক স্টোরেজ ব্যবহৃত হয়:

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/) (সদস্যতা প্রয়োজন)
* [阿里云盘](https://www.alipan.com/) (ক্রয় করতে হবে)
* [Box](https://www.box.com/) (বিনামূল্যে 10GB স্থান, একক ফাইলের আকার 250MB-এ সীমিত)
* [Dropbox](https://www.dropbox.com/) (বিনামূল্যে 2GB, বন্ধু আমন্ত্রণ করে 16GB পর্যন্ত বৃদ্ধি করা যায়)
* [TeraCloud](https://teracloud.jp/en/) (বিনামূল্যে 10GB, আমন্ত্রণের মাধ্যমে অতিরিক্ত 5GB পাওয়া যায়)
* [Yandex Disk](https://disk.yandex.com/) (বিনামূল্যে 10GB স্থান)

এছাড়াও কিছু নিজস্ব স্টোরেজ পরিচালনার পরিষেবা:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}