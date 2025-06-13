---
icon: trash-xmark
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# CSS সেটিংস ক্লিয়ার করুন

{% hint style="warning" %}
যখন ভুল CSS সেট করা হয়েছে অথবা CSS সেট করার পর সেটিংস ইন্টারফেইসে প্রবেশ করা সম্ভব হচ্ছে না, তখন এই পদ্ধতিটি ব্যবহার করে CSS সেটিংস ক্লিয়ার করুন।
{% endhint %}

* কনসোল খুলুন, CherryStudio উইন্ডোতে ক্লিক করুন এবং শর্টকাট <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> চাপুন (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>)।
* খোলা কনসোল উইন্ডোতে, `Console` ট্যাবে ক্লিক করুন

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* তারপর ম্যানুয়ালি `document.getElementById('user-defined-custom-css').remove()` লিখুন - কপি-পেস্ট করলে সাধারণত কার্যকর হবে না।
* লিখা শেষে এন্টার চেপে নিশ্চিত করুন, CSS সেটিংস ক্লিয়ার হবে। এরপর CherryStudio-এর ডিসপ্লে সেটিংসে আবার প্রবেশ করুন এবং সমস্যাযুক্ত CSS কোড মুছে দিন।