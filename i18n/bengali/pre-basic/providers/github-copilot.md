
{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# GitHub Copilot

GitHub Copilot ব্যবহার করতে প্রথমে আপনার একটি GitHub অ্যাকাউন্ট এবং GitHub Copilot সেবার সাবস্ক্রিপশন প্রয়োজন। ফ্রী সংস্করণও কাজ করে, তবে ফ্রী সংস্করণে নতুন Claude 3.7 মডেল সাপোর্ট করে না। বিস্তারিত জানতে [GitHub Copilot অফিসিয়াল সাইট](https://github.com/features/copilot) দেখুন।

## Device Code পাওয়ার পদ্ধতি

"GitHub-এ লগইন করুন" এ ক্লিক করে Device Code পান এবং কপি করুন।

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Device Code পাওয়ার উদাহরণ ছবি"><figcaption><p>Device Code পাওয়া</p></figcaption></figure>

## ব্রাউজারে Device Code দিয়ে অনুমোদন

Device Code পাওয়ার পর লিংকে ক্লিক করে ব্রাউজার খুলুন, GitHub অ্যাকাউন্টে লগইন করুন, Device Code ইনপুট দিন এবং অনুমোদন দিন।

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="GitHub অনুমোদনের উদাহরণ ছবি"><figcaption><p>GitHub অনুমোদন</p></figcaption></figure>

অনুমোদন সফল হলে Cherry Studio-তে ফিরে "GitHub-এর সাথে সংযোগ করুন" ক্লিক করুন। সফল হলে আপনার GitHub ব্যবহারকারী নাম ও প্রোফাইল ছবি দেখা যাবে।

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="GitHub সংযোগ সফল উদাহরণ ছবি"><figcaption><p>GitHub সংযোগ সফল</p></figcaption></figure>

## "ব্যবস্থাপনা" ক্লিক করে মডেল তালিকা পান

নিচে থাকা "ব্যবস্থাপনা" বাটনে ক্লিক করলে স্বয়ংক্রিয়ভাবে ইন্টারনেট থেকে বর্তমানে সাপোর্ট করা মডেলের তালিকা লোড হবে।

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="মডেল তালিকা পাওয়ার উদাহরণ ছবি"><figcaption><p>মডেল তালিকা পাওয়া</p></figcaption></figure>

## সাধারণ সমস্যা

### Device Code পেতে ব্যর্থ, আবার চেষ্টা করুন

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Device Code পাওয়ায় ব্যর্থতার উদাহরণ ছবি"><figcaption><p>Device Code পাওয়ায় ব্যর্থ</p></figcaption></figure>

বর্তমানে Axios দিয়ে রিকোয়েস্ট তৈরি করা হয় যা socks প্রক্সি সাপোর্ট করে না। দয়া করে সিস্টেম প্রক্সি বা HTTP প্রক্সি ব্যবহার করুন, অথবা সরাসরি CherryStudio-তে প্রক্সি সেট না করে গ্লোবাল প্রক্সি ব্যবহার করুন। Device Code পেতে ব্যর্থ হওয়া এড়াতে প্রথমে নিশ্চিত হোন আপনার ইন্টারনেট সংযোগ সঠিকভাবে কাজ করছে।