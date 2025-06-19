---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# Vertex AI

## টিউটোরিয়ালের সংক্ষিপ্ত বিবরণ

### ১. API কী সংগ্রহ করুন

* Gemini-এর API কী সংগ্রহের আগে, আপনার একটি Google Cloud প্রকল্প থাকা দরকার (যদি আপনার থাকে তবে এই প্রক্রিয়াটি এড়িয়ে যেতে পারেন)
* [Google Cloud](https://console.cloud.google.com/projectcreate)-এ যান, একটি প্রকল্প তৈরি করুন, প্রকল্পের নাম লিখুন এবং 'প্রকল্প তৈরি' ক্লিক করুন

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI কনসোল](https://console.cloud.google.com/vertex-ai)-এ যান
* তৈরি করা প্রকল্পে [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) চালু করুন

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## ২. API অ্যাক্সেস অনুমতি সেট আপ করুন

* [সার্ভিস অ্যাকাউন্ট](https://console.cloud.google.com/iam-admin/serviceaccounts) অনুমতি ইন্টারফেস খুলুন, একটি সার্ভিস অ্যাকাউন্ট তৈরি করুন

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* সার্ভিস অ্যাকাউন্ট ম্যানেজমেন্ট পৃষ্ঠায় 방금 তৈরি করা সার্ভিস অ্যাকাউন্টটি খুঁজুন, `কী` ক্লিক করুন এবং একটি নতুন JSON ফরম্যাট কী তৈরি করুন

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* সফলভাবে তৈরি হওয়ার পর, কী ফাইলটি JSON ফাইলের ফরম্যাটে আপনার কম্পিউটারে স্বয়ংক্রিয়ভাবে সংরক্ষণ করা হবে, অনুগ্রহ করে **সাবধানে সংরক্ষণ করুন**

## ৩. Cherry Studio-এ Vertex AI কনফিগার করুন

* Vertex AI পরিষেবা প্রদানকারী নির্বাচন করুন
* JSON ফাইলের সংশ্লিষ্ট ক্ষেত্রগুলি পূরণ করুন

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[মডেল](https://console.cloud.google.com/vertex-ai/model-garden) যোগ করতে ক্লিক করুন, এবং আনন্দের সাথে ব্যবহার শুরু করুন!