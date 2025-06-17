---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# โหมดเชื่อมต่ออินเทอร์เน็ต

{% hint style="info" %}
ตัวอย่างสถานการณ์ที่ต้องการการเชื่อมต่ออินเทอร์เน็ต:

* ข้อมูลที่เน้นความทันสมัย: เช่น ราคาทองคำล่าสุดวันนี้/สัปดาห์นี้
* ข้อมูลเรียลไทม์: เช่น สภาพอากาศ อัตราแลกเปลี่ยน ค่าตัวเลขเปลี่ยนแปลง
* ความรู้ใหม่ๆ: เช่น สิ่งใหม่ แนวคิดใหม่ เทคโนโลยีใหม่ ฯลฯ
{% endhint %}

### 1. วิธีเปิดใช้งานการเชื่อมต่ออินเทอร์เน็ต

ในช่องถามคำถามของ Cherry Studio ให้คลิกไอคอน 【ลูกโลก】 เพื่อเปิดใช้งานการเชื่อมต่ออินเทอร์เน็ต

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>คลิกไอคอนลูกโลก - เปิดการเชื่อมต่อ</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>สัญลักษณ์แสดงว่าเปิดใช้งานแล้ว</p></figcaption></figure>

### 2. ข้อควรระวัง: มีโหมดเชื่อมต่อ 2 แบบ

#### แบบที่ 1: รุ่นโมเดลพื้นฐานจากผู้ให้บริการที่มีฟีเจอร์เชื่อมต่อในตัว

ในกรณีนี้ เมื่อเปิดใช้งานการเชื่อมต่อ คุณสามารถใช้บริการอินเทอร์เน็ตได้ทันทีโดยไม่ต้องตั้งค่าเพิ่มเติม

{% hint style="warning" %}
คุณสามารถตรวจสอบว่าโมเดลนั้นรองรับการเชื่อมต่อหรือไม่ โดยดูที่สัญลักษณ์ลูกโลกเล็กๆ หลังชื่อโมเดลในส่วนบนของอินเทอร์เฟซ
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

ในหน้าจัดการโมเดล วิธีนี้ช่วยให้คุณแยกแยะโมเดลที่รองรับการเชื่อมต่อได้อย่างรวดเร็ว

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**ผู้ให้บริการโมเดลที่ Cherry Studio รองรับการเชื่อมต่อในปัจจุบัน**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (รองรับทุกรุ่น)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian เป็นต้น</mark>

{% hint style="danger" %}
กรณีพิเศษ:
แม้ว่าโมเดลจะไม่มีสัญลักษณ์ลูกโลก แต่บางครั้งอาจใช้งานการเชื่อมต่อได้ เช่น กรณีที่อธิบายในบทความ攻略นี้
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### แบบที่ 2: ใช้บริการ Tavily เมื่อโมเดลไม่รองรับการเชื่อมต่อในตัว

เมื่อเราใช้โมเดลพื้นฐานที่ไม่รองรับการเชื่อมต่อ (ไม่มีไอคอนลูกโลกหลังชื่อ) แต่ต้องการให้ประมวลผลข้อมูลเรียลไทม์ เราจำเป็นต้องใช้บริการค้นหาทางอินเทอร์เน็ตของ Tavily

**ครั้งแรกที่ใช้บริการ Tavily**: จะมีป็อปอัพแจ้งให้ตั้งค่าข้อมูล กรุณาดำเนินการตามคำแนะนำ - ง่ายมาก!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>คลิก "ไปตั้งค่า" ในป็อปอัพ</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>คลิก "รับคีย์ลับ"</p></figcaption></figure>

หลังจากคลิกรับคีย์ลับ ระบบจะเปลี่ยนไปยังหน้า **ลงทะเบียน/เข้าสู่ระบบเว็บไซต์ Tavily** ลงทะเบียนและเข้าสู่ระบบ จากนั้นสร้าง API key แล้วคัดลอก key มาใส่ใน Cherry Studio

{% hint style="danger" %}
หากไม่ทราบวิธีลงทะเบียน อ้างอิงเอกสารสอนการลงทะเบียน Tavily ในไดเรกทอรีเดียวกันนี้
{% endhint %}

**เอกสารอ้างอิงการลงทะเบียน Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

อินเทอร์เฟซด้านล่างแสดงว่าลงทะเบียนสำเร็จ

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>คัดลอกคีย์</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>วางคีย์ - เสร็จสิ้น</p></figcaption></figure>

ลองทดสอบอีกครั้ง ผลลัพธ์แสดงว่าสามารถค้นหาทางอินเทอร์เน็ตได้ปกติ โดยจำนวนผลการค้นหาเป็นค่าเริ่มต้นที่เราตั้งไว้: 5 ผลลัพธ์

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
หมายเหตุ: บริการ Tavily มีขีดจำกัดฟรีรายเดือน หากเกินต้องชำระเงิน~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> หมายเหตุ: หากพบข้อผิดพลาด ยินดีรับฟังคำติชม隨時