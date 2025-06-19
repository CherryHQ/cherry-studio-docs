---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# Vertex AI

## টিউটোরিয়াল ওভারভিউ

### 1. API কী সংগ্রহ করুন

* Gemini-র API কী পাওয়ার আগে, আপনার একটি Google Cloud প্রজেক্ট থাকতে হবে (যদি আপনার ইতিমধ্যেই থাকে তবে এই ধাপটি ছাড়া যেতে পারেন)
* [Google Cloud](https://console.cloud.google.com/projectcreate)-এ গিয়ে প্রজেক্ট তৈরি করুন, প্রজেক্টের নাম লিখুন এবং "প্রজেক্ট তৈরি করুন" ক্লিক করুন

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* [Vertex AI কনসোল](https://console.cloud.google.com/vertex-ai)-এ প্রবেশ করুন
* তৈরি করা প্রজেক্টে [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) সক্রিয় করুন

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API প্রবেশাধিকার সেট আপ করুন

* [সার্ভিস অ্যাকাউন্ট](https://console.cloud.google.com/iam-admin/serviceaccounts) অনুমতি পেজ খুলুন, একটি সার্ভিস অ্যাকাউন্ট তৈরি করুন

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* সার্ভিস অ্যাকাউন্ট ম্যানেজমেন্ট পেজে নতুন তৈরি করা সার্ভিস অ্যাকাউন্ট খুঁজে `কী` ক্লিক করুন এবং একটি নতুন JSON ফরম্যাট কী তৈরি করুন

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* সফলভাবে তৈরি হওয়ার পর, কী ফাইলটি আপনার কম্পিউটারে JSON ফাইলের আকারে স্বয়ংক্রিয়ভাবে সংরক্ষিত হবে, অনুগ্রহ করে **সাবধানে সংরক্ষণ করুন**

## 3. Cherry Studio-তে Vertex AI কনফিগার করুন

* Vertex AI সার্ভিস প্রোভাইডার নির্বাচন করুন
* JSON ফাইলের প্রাসঙ্গিক ক্ষেত্রগুলি পূরণ করুন

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

[মডেল](https://console.cloud.google.com/vertex-ai/model-garden) যোগ করতে ক্লিক করুন, তারপর আনন্দের সাথে ব্যবহার শুরু করুন!\