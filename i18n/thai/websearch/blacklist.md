---
icon: ban
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การกำหนดค่าบัญชีดำการค้นหาทางอินเทอร์เน็ต

Cherry Studio รองรับการกำหนดค่าบัญชีดำได้สองวิธี: ด้วยตนเองและการเพิ่มแหล่งข้อมูลสมัครสมาชิก กฎการกำหนดค่าอ้างอิง [ublacklist](https://github.com/iorate/ublacklist)

## การกำหนดค่าด้วยตนเอง

คุณสามารถเพิ่มกฎสำหรับผลการค้นหาหรือคลิกไอคอนบนแถบเครื่องมือเพื่อบล็อกเว็บไซต์ที่ระบุ กฎสามารถระบุได้โดยใช้ [รูปแบบการจับคู่](https://developer.mozilla.org/zh-CN/docs/mozilla/add-ons/webextensions/match_patterns) (ตัวอย่าง: `*://*.example.com/*`) หรือใช้ [regular expression](https://developer.mozilla.org/zh-CN/docs/web/javascript/guide/regular_expressions) (ตัวอย่าง: `/example\.(net|org)/`).

## การกำหนดค่าแหล่งข้อมูลสมัครสมาชิก

คุณยังสามารถสมัครสมาชิกชุดกฎสาธารณะได้ เว็บไซต์นี้แสดงรายการการสมัครสมาชิกบางส่วน:\
https://iorate.github.io/ublacklist/subscriptions

以下是一些比较推荐的订阅源链接：

| ชื่อ                                                                                                    | ลิงก์                                                                                                   | ประเภท   |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| [uBlacklist subscription compilation](https://github.com/eallion/uBlacklist-subscription-compilation) | https://git.io/ublacklist                                                                            | จีน   |
| [uBlockOrigin-HUGE-AI-Blocklist](https://github.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist)         | https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/list\_uBlacklist.txt | สร้างโดย AI |

<figure><img src="../.gitbook/assets/blacklist1.jpg" alt=""><figcaption><p>การกำหนดค่าแหล่งข้อมูลสมัครสมาชิก</p></figcaption></figure>