---
icon: database
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# ডেটা সেটিংস

এই ইন্টারফেসে আপনি ক্লায়েন্ট ডেটার ক্লাউড ও লোকাল ব্যাকআপ, লোকাল ডেটা ডিরেক্টরি অনুসন্ধান এবং ক্যাশে পরিষ্কার করার মতো অপারেশন করতে পারবেন।



### ডেটা ব্যাকআপ

বর্তমানে ডেটা ব্যাকআপ শুধুমাত্র WebDAV পদ্ধতিতে সমর্থিত। আপনি WebDAV সমর্থনকারী সার্ভিস ব্যবহার করে ক্লাউড ব্যাকআপ করতে পারেন।

আপনি `কম্পিউটার A` $$\xrightarrow{\text{ব্যাকআপ}}$$ `WebDAV` $$\xrightarrow{\text{পুনরুদ্ধার}}$$ `কম্পিউটার B` পদ্ধতিতে মাল্টি-ডিভাইস ডেটা সিঙ্ক্রোনাইজ করতে পারেন।

#### Nutz Cloud-এর উদাহরণ

1. Nutz Cloud-এ লগইন করুন, উপরের ডান কোণে ব্যবহারকারীর নামে ক্লিক করে "অ্যাকাউন্ট তথ্য" নির্বাচন করুন:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. "সিকিউরিটি অপশনস" নির্বাচন করুন, "অ্যাপ যুক্ত করুন" ক্লিক করুন:

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. অ্যাপের নাম লিখুন, এলোমেলো পাসওয়ার্ড জেনারেট করুন:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. পাসওয়ার্ড কপি করে সংরক্ষণ করুন:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. সার্ভার অ্যাড্রেস, অ্যাকাউন্ট এবং পাসওয়ার্ড সংগ্রহ করুন:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio সেটিংস → ডেটা সেটিংসে WebDAV তথ্য পূরণ করুন:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. ডেটা ব্যাকআপ বা পুনরুদ্ধার নির্বাচন করুন এবং স্বয়ংক্রিয় ব্যাকআপের সময়সূচী সেট করতে পারেন:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
সাধারণত কম থ্রেশহোল্ডের WebDAV পরিষেবাগুলি হলো ক্লাউড স্টোরেজ:

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/) (সদস্যপদ প্রয়োজন)
* [阿里云盘](https://www.alipan.com/) (কিনতে হবে)
* [Box](https://www.box.com/) (বিনামূল্যে স্পেস 10GB, ফাইলের সর্বোচ্চ আকার 250MB)
* [Dropbox](https://www.dropbox.com/) (বিনামূল্যে 2GB, বন্ধু আমন্ত্রণ করে 16GB পর্যন্ত)
* [TeraCloud](https://teracloud.jp/en/) (বিনামূল্যে 10GB, আমন্ত্রণের মাধ্যমে অতিরিক্ত 5GB)
* [Yandex Disk](https://disk.yandex.com/) (বিনামূল্যে 10GB স্পেস)

এছাড়া স্ব-হোস্টেড পরিষেবার বিকল্প:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}