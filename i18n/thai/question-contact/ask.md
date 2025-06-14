---
icon: messages-question
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# วิธีการถามคำถามอย่างมีประสิทธิภาพ

Cherry Studio เป็นโปรเจ็กต์โอเพนซอร์สฟรี และด้วยความเติบโตของโครงการ งานของทีมโครงการก็เพิ่มมากขึ้นด้วย เพื่อลดต้นทุนการสื่อสารและแก้ไขปัญหาของคุณอย่างรวดเร็วและมีประสิทธิภาพ เราขอให้ผู้ใช้ปฏิบัติตามขั้นตอนและวิธีการดังต่อไปนี้ในการแก้ไขปัญหาก่อนที่จะถามคำถาม เพื่อให้ทีมโครงการมีเวลามากขึ้นในการดูแลรักษาและพัฒนาโครงการ ขอบคุณสำหรับความร่วมมือ!

## 1. การตรวจสอบเอกสารและการค้นหา

ปัญหาพื้นฐานส่วนใหญ่สามารถแก้ไขได้ด้วยการตรวจสอบเอกสารอย่างรอบคอบ

* ปัญหาเกี่ยวกับฟังก์ชันการทำงานและการใช้งานซอฟต์แวร์สามารถตรวจสอบได้ที่เอกสาร [功能介绍](../cherrystudio/preview/)
* คำถามที่พบบ่อยถูกรวบรวมไว้ในหน้า [常见问题](questions.md) โปรดตรวจสอบดูว่ามีวิธีแก้ไขหรือไม่ก่อน
* ปัญหาที่ซับซ้อนสามารถแก้ไขได้โดยการค้นหาหรือถามผ่านช่องค้นหา
* โปรดอ่านเนื้อหาในกล่องคำแนะนำของเอกสารทุกฉบับอย่างรอบคอบ จะช่วยหลีกเลี่ยงปัญหามากมาย
* ตรวจสอบหรือค้นหาเกี่ยวกับปัญหาที่คล้ายกันและวิธีแก้ไขที่หน้า [Issue](https://github.com/CherryHQ/cherry-studio/issues) บน GitHub

## 2. การค้นหาทางอินเทอร์เน็ตและการถาม AI

สำหรับปัญหาที่ไม่เกี่ยวข้องกับฟังก์ชันไคลเอ็นต์ เช่น การใช้โมเดล (ข้อผิดพลาดของโมเดล, คำตอบไม่ตรงตามความคาดหวัง, การตั้งค่าพารามิเตอร์) แนะนำให้ค้นหาวิธีแก้ไขในอินเทอร์เน็ตก่อน หรืออธิบายเนื้อหาข้อผิดพลาดและปัญหาให้ AI เพื่อหาวิธีแก้ไข

## 3. ถามในชุมชนทางการหรือเปิด issue บน GitHub

หากสองขั้นตอนข้างต้นไม่พบคำตอบหรือไม่สามารถแก้ไขปัญหาของคุณได้ คุณสามารถไปที่ช่องทางการ [tg频道](https://t.me/CherryStudioAI), [Discord频道](https://discord.com/invite/wez8HtpxqQ), [QQ群 ](#user-content-fn-1)[^1] ([一键进群](https://qm.qq.com/cgi-bin/qm/qr?authKey=xe5nfGVZLMYnlJq%2F%2B4kN03YWcDBB2lnD7tc9rWus2mxS0JHUbOzk79cO7MYuqyGR\&k=UKVgl3YPHmwPaU8qeO1VG03NcUkACKsc\&noverify=0)) เพื่ออธิบายปัญหาโดยละเอียดและขอความช่วยเหลือ

1. หากเป็นข้อผิดพลาดของโมเดล โปรดให้ภาพหน้าจอที่สมบูรณ์และข้อมูลข้อผิดพลาดจากคอนโซล ข้อมูลที่ละเอียดอ่อนสามารถปกปิดได้ แต่ต้องแสดงชื่อโมเดล การตั้งค่าพารามิเตอร์ และเนื้อหาข้อผิดพลาดในภาพหน้าจอ วิธีดูข้อมูลข้อผิดพลาดในคอนโซล [คลิกที่นี่](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)
2. หากเป็นบั๊กซอฟต์แวร์ โปรดให้<mark style="background-color:green;">คำอธิบายข้อผิดพลาดที่เฉพาะเจาะจง</mark>และ<mark style="background-color:green;">ขั้นตอน</mark>[<mark style="background-color:green;">การทำให้เกิดซ้ำ</mark>](#user-content-fn-2)[^2]<mark style="background-color:green;">โดยละเอียด</mark> เพื่อให้นักพัฒนาสามารถดีบักและแก้ไขได้ หากเป็นปัญหาที่เกิดขึ้นเป็นครั้งคราวและไม่สามารถทำให้เกิดซ้ำได้ โปรดอธิบายสถานการณ์ที่เกี่ยวข้อง พื้นหลัง และพารามิเตอร์การตั้งค่าให้ละเอียดที่สุดเท่าที่เป็นไปได้\
   นอกจากนี้ คุณต้องรวม<mark style="background-color:green;">ข้อมูลแพลตฟอร์ม</mark> (Window, Mac หรือ Linux) และ<mark style="background-color:green;">หมายเลขเวอร์ชันซอฟต์แวร์</mark> ในคำอธิบายปัญหาด้วย



{% hint style="success" %}
**ขอเอกสารหรือให้คำแนะนำเกี่ยวกับเอกสาร**

สามารถติดต่อทาง tg channel `@Wangmouuu` หรือ QQ (`1355873789`) หรือส่งอีเมลถึง: `sunrise@cherry-ai.com`
{% endhint %}

[^1]: หมายเลขกลุ่ม: 611659451

[^2]: หมายถึง (ข้อผิดพลาด) เกิดขึ้นอีกครั้ง