---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# Vulkan Engine-এ ইন্টারনেট সংযোগ সম্পাদন

### 1. "Vulkan Engine" অ্যাকাউন্টে <a href="#rclz7" id="rclz7"></a> **লগইন/নিবন্ধন করুন**

অফিসিয়াল ওয়েবসাইটে ভিজিট করুন: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Vulkan Engine-এর অফিসিয়াল ওয়েবসাইট</p></figcaption></figure>

### 2. **"ইন্টারনেট-সক্ষম" "আমার অ্যাপ্লিকেশন"** <a href="#gvzaa" id="gvzaa"></a> **তৈরি করুন**

2.1. Vulkan Engine-এ লগ ইন করুন, "**Volcano Ark**" পৃষ্ঠায় যান: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **ধাপে ধাপে ক্লিক করুন:** <mark style="color:red;">**"আমার অ্যাপ্লিকেশন" → "অ্যাপ্লিকেশন তৈরি করুন" → "জিরো কোড" → "ওয়ান-টু-ওয়ান চ্যাট"**</mark>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. **তথ্য পূরণ করে অ্যাপ্লিকেশন প্রকাশ করুন** <a href="#zzdfe" id="zzdfe"></a>

**অ্যাপ্লিকেশনের নাম**: প্রয়োজন অনুযায়ী যে কোনো নাম দিতে পারেন। (কেবল <mark style="color:red;">**\* চিহ্নিত আবশ্যক ফিল্ড**</mark> পূরণ করুন, বাকিগুলো খালি রাখতে পারেন)

<mark style="color:red;">**গুরুত্বপূর্ণ: ইন্টারনেট প্লাগইন সক্রিয় করতে হবে (প্রথমে সক্রিয় করুন)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. **ইন্টারনেট প্লাগইন কার্যকারিতা সক্রিয় করুন** <a href="#mwn38" id="mwn38"></a> (খরচ ও ফ্রীমিয়াদ সম্পর্কে সতর্ক থাকুন)

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>"অবিলম্বে ক্রয় করুন" ক্লিক করুন। নিচের স্ক্রিনটি দেখানো পর্যন্ত ধাপগুলি অনুসরণ করুন — সফলভাবে সক্রিয় হয়েছে।</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>স্থিতি লক্ষ্য করুন — সক্রিয়করণ সফল হয়েছে</p></figcaption></figure>

এরপর পূর্বের "অ্যাপ্লিকেশন তথ্য পূরণ করুন" পৃষ্ঠায় ফিরে যান।

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. **অ্যাডভান্সড কনফিগারেশনের জন্য ইন্টারনেট অনুসন্ধান নির্দেশনা** <a href="#sp6uz" id="sp6uz"></a>

ব্যক্তিগত পরামর্শ:

* ইনপুট/আউটপুট নিয়ন্ত্রণ করতে চাইলে "**কাস্টমাইজড কল**" ব্যবহার করুন;
* সহজ করতে "**অটো কল**" (ডিফল্ট) অবিকল রাখুন;
* বাজেট সীমিত না হলে বা রিয়েল-টাইম ডেটা প্রয়োজন হলে "**ফোর্স এনাবল**" করুন।

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. **অ্যাপ্লিকেশন প্রকাশ করুন** <a href="#fe1gf" id="fe1gf"></a>

উপরের ডানদিকের "**প্রকাশ করুন**" বাটনে ক্লিক করুন — অ্যাপ্লিকেশন তৈরি সফল হয়েছে।

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. **API কী প্রাপ্তি** <a href="#jtqlu" id="jtqlu"></a>

ধাপে ধাপে: **"API কল নির্দেশিকা" → "API কী নির্বাচন এবং কপি করুন" → "দেখুন এবং নির্বাচন করুন"**

API কী অনুলিপি করুন। এরপর Cherry Studio-তে এটি ব্যবহার করব। (বিস্তারিত নিচের স্ক্রিনশটে)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

**নোট:** API কী না থাকলে পপ-আপের ডানদিকে "**API কী তৈরি করুন**" ক্লিক করে তা অনুলিপি করুন।

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. **deepseek-R1-এ ইন্টারনেট অ্যাক্সেসের জন্য Cherry Studio-তে API কী ব্যবহার** <a href="#lrefj" id="lrefj"></a>

#### 5.1. Cherry Studio খুলুন → **"সেটিংস" → "যেকোনো নাম লিখুন" → "টাইপ: OpenAI"** <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. **URL এবং কী কনফিগার করুন** <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">নোট: এন্ডপয়েন্ট খুঁজে না পেলে বা বেইজিং নোড না হলে এখানে সঠিক এন্ডপয়েন্ট খুঁজুন ("/" ভুলবেন না):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. **মডেলের নাম যুক্ত করুন** <a href="#qmh3i" id="qmh3i"></a>

**সতর্কতা:** ছোট হরফে লেখা মডেলের নাম অনুলিপি করুন, অন্যথায় ত্রুটি দেখা দেবে।

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. **প্রভাব পূর্বরূপ** <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>