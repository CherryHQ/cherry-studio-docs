
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# PPIO পাইও ক্লাউড

## Cherry Studio-এ PPIO LLM API সংযোগ

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)টিউটোরিয়াল সংক্ষেপ <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio হলো একটি মাল্টি-মডেল ডেস্কটপ ক্লায়েন্ট, বর্তমানে সমর্থন করে: Windows, Linux, এবং MacOS সিস্টেমের জন্য ইনস্টলেশন প্যাকেজ। এটি প্রধান LLM মডেলগুলিকে একত্রিত করে, বহু-পরিস্থিতিতে সহায়তা প্রদান করে। ব্যবহারকারীরা বুদ্ধিমান সংলাপ ব্যবস্থাপনা, ওপেন সোর্স কাস্টমাইজেশন, এবং মাল্টি-থিম ইন্টারফেসের মাধ্যমে কাজের উৎপাদনশীলতা বাড়াতে পারেন।

Cherry Studio এখন **PPIO হাই-পারফরমেন্স API চ্যানেলের** সাথে গভীরভাবে সংযুক্ত—এন্টারপ্রাইজ-গ্রেড কম্পিউটিং শক্তির মাধ্যমে **DeepSeek-R1/V3 উচ্চ গতির প্রতিক্রিয়া** এবং **99.9% পরিষেবা প্রাপ্যতা** নিশ্চিত করে, আপনাকে দ্রুত ও নিরবিচ্ছিন্ন অভিজ্ঞতা প্রদান করে।

নীচের টিউটোরিয়ালে সম্পূর্ণ সংযোগ সমাধান (API কী কনফিগারেশন সহ) রয়েছে, মাত্র ৩ মিনিটে "Cherry Studio ইন্টেলিজেন্ট শিডিউলিং + PPIO হাই-পারফরমেন্স API" এর উন্নত মোড চালু করুন।

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)১. CherryStudio-তে প্রবেশ করুন, "PPIO" কে মডেল প্রদানকারী হিসাবে যোগ করুন <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

প্রথমে অফিসিয়াল ওয়েবসাইট থেকে Cherry Studio ডাউনলোড করুন: [ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) (যদি প্রবেশ করতে সমস্যা হয়, নীচের Quark ড্রাইভ লিঙ্ক থেকে আপনার প্রয়োজনীয় সংস্করণ ডাউনলোড করুন: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(১) প্রথমে নিচের বাম দিকের সেটিংসে ক্লিক করুন, কাস্টম প্রদানকারীর নাম লিখুন: `PPIO`, তারপর "নিশ্চিত করুন" ক্লিক করুন

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(২) [পাইও কম্পিউটিং ক্লাউড API কী ম্যানেজমেন্টে](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio) যান, 【ব্যবহারকারী আইকন】—【API কী ব্যবস্থাপনা】 এ ক্লিক করে কন্ট্রোল প্যানেলে প্রবেশ করুন

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

নতুন API কী তৈরি করতে 【+ তৈরি】 বোতামে ক্লিক করুন। একটি কাস্টম কী নাম লিখুন, **তৈরি করার সময় শুধুমাত্র একবার দেখানো হবে, অনুগ্রহ করে অনুলিপি করে ডকুমেন্টে সংরক্ষণ করুন, যাতে পরবর্তী ব্যবহারে ব্যাঘাত না ঘটে**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(৩) CherryStudio-তে কী পেস্ট করুন সেটিংসে ক্লিক করুন, 【PPIO পাইও ক্লাউড】 নির্বাচন করুন, ওয়েবসাইটে তৈরি করা API কী লিখুন, শেষে 【পরীক্ষা করুন】 ক্লিক করুন

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(৪) মডেল নির্বাচন করুন: উদাহরণস্বরূপ deepseek/deepseek-r1/community, অন্যান্য মডেলে পরিবর্তন করতে সরাসরি সুইচ করতে পারেন।

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 এবং V3 community সংস্করণ শুধুমাত্র স্বাদ নেওয়ার জন্য, এগুলি পূর্ণ প্যারামিটার সংস্করণ, স্থিতিশীলতা এবং কার্যকারণ অপরিবর্তিত। বড় পরিমাণে ব্যবহারের জন্য অবশ্যই **রিচার্জ করুন এবং non-community সংস্করণে স্যুইচ করুন**।

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)২. মডেল ব্যবহার কনফিগারেশন <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(১) 【পরীক্ষা করুন】 এ ক্লিক করার পর সংযোগ সফলভাবে দেখানো হলে নিয়মিত ব্যবহার শুরু করুন

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(২) শেষে 【@】 ক্লিক করে PPIO প্রদানকারীর অধীনে সদ্য যোগ করা DeepSeek R1 মডেল নির্বাচন করুন, তারপর চ্যাট শুরু করুন\~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【কিছু উপাদান সূত্র: [ চেন এন ](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)৩. PPIO×Cherry Studio ভিডিও ব্যবহার টিউটোরিয়াল <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

আপনি যদি ভিজ্যুয়াল শিখতে পছন্দ করেন, আমরা Bilibili-তে ভিডিও টিউটোরিয়াল প্রস্তুত করেছি। ধাপে ধাপে নির্দেশনার মাধ্যমে, দ্রুত "PPIO API+Cherry Studio" কনফিগারেশন শিখুন, নীচের লিঙ্কে ক্লিক করে সরাসরি ভিডিও দেখুন, নিরবিচ্ছিন্ন ডেভেলপমেন্ট অভিজ্ঞতা শুরু করুন → [《 【আপনি কি DeepSeek-এর ক্রমাগত লোডিং দেখে বিরক্ত?】পাইও ক্লাউড+DeepSeek ফুল প্যারামিটার ভার্সন =? কোন ব্যান্ডউইথ সীমাবদ্ধতা নয়, অবিলম্বে শুরু করুন》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【ভিডিও উপাদান সূত্র: sola】