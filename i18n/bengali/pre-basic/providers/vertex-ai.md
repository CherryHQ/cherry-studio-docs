---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# Vertex AI

## টিউটোরিয়াল ওভারভিউ

### 1. API কী প্রাপ্তি

* Gemini-এর জন্য API কী প্রাপ্তির আগে, আপনার একটি Google Cloud প্রকল্প থাকা প্রয়োজন (যদি ইতোমধ্যে থাকে তবে এই পদক্ষেপটি এড়িয়ে যেতে পারেন)
* [Google Cloud](https://console.cloud.google.com/projectcreate)-এ গিয়ে প্রকল্প তৈরি করুন, প্রকল্পের নাম লিখুন এবং "প্রকল্প তৈরি" ক্লিক করুন

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI কনসোল](https://console.cloud.google.com/vertex-ai)-এ প্রবেশ করুন
* তৈরি করা প্রকল্পে [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) চালু করুন

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API অ্যাক্সেস অনুমতি কনফিগারেশন

* [সার্ভিস অ্যাকাউন্ট](https://console.cloud.google.com/iam-admin/serviceaccounts) অনুমতি পৃষ্ঠায় একটি নতুন সার্ভিস অ্যাকাউন্ট তৈরি করুন

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* সার্ভিস অ্যাকাউন্ট পরিচালনা পৃষ্ঠায় নতুন তৈরি করা সার্ভিস অ্যাকাউন্ট খুঁজুন, `কী` ক্লিক করুন এবং একটি নতুন JSON ফরম্যাট কী তৈরি করুন

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* সফলভাবে তৈরি হলে, কী ফাইলটি JSON ফরম্যাটে স্বয়ংক্রিয়ভাবে আপনার কম্পিউটারে সংরক্ষিত হবে, অনুগ্রহ করে **সতর্কতার সাথে সংরক্ষণ করুন**

## 3. Cherry Studio-তে Vertex AI কনফিগার করুন

* Vertex AI পরিষেবা প্রদানকারী নির্বাচন করুন
* JSON ফাইলের সংশ্লিষ্ট ক্ষেত্রগুলি পূরণ করুন

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[মডেল](https://console.cloud.google.com/vertex-ai/model-garden) যোগ করতে ক্লিক করুন, তারপর আনন্দের সাথে ব্যবহার শুরু করতে পারেন!