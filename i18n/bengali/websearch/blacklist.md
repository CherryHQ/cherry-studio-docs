---
icon: ban
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# ওয়েব অনুসন্ধান কালোতালিকা কনফিগারেশন

Cherry Studio কালোতালিকা কনফিগার করতে ম্যানুয়াল এবং সাবস্ক্রিপশন ফিড যোগ করার দুটি পদ্ধতি সমর্থন করে। কনফিগারেশন নিয়মের জন্য [ublacklist](https://github.com/iorate/ublacklist) রেফারেন্স করুন।

## ম্যানুয়াল কনফিগারেশন

আপনি সার্চ রেজাল্টের জন্য রুল যোগ করতে পারেন অথবা টুলবার আইকনে ক্লিক করে নির্দিষ্ট ওয়েবসাইট ব্লক করতে পারেন। নিম্নলিখিত পদ্ধতিতে রুল স্পেসিফাই করা যাবে: [ম্যাচিং প্যাটার্ন](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (উদাহরণ: `*://*.example.com/*`) অথবা [রেগুলার এক্সপ্রেশন](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) ব্যবহার করে (উদাহরণ: `/example\.(net|org)/`)।

## সাবস্ক্রিপশন ফিড কনফিগারেশন

আপনি পাবলিক রুল সেট সাবস্ক্রাইব করতে পারেন। এই ওয়েবসাইট কিছু সাবস্ক্রিপশন তালিকাভুক্ত করেছে:\
https://iorate.github.io/ublacklist/subscriptions

এখানে কিছু সুপারিশকৃত সাবস্ক্রিপশন লিঙ্ক দেওয়া হল:

| নাম                                                                                                   | লিঙ্ক                                                                                                                               | প্রকার   |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                                                           | চীনা    |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt                               | এআই উৎপন্ন |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>সাবস্ক্রিপশন ফিড কনফিগারেশন</p></figcaption></figure>