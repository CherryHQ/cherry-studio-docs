---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# Vertex AI

## ภาพรวมของบทเรียน

### 1. รับคีย์ API

* ก่อนรับคีย์ API ของ Gemini คุณต้องมีโปรเจกต์ Google Cloud (หากมีอยู่แล้ว สามารถข้ามขั้นตอนนี้ได้)
* ไปที่ [Google Cloud](https://console.cloud.google.com/projectcreate) สร้างโปรเจกต์ กรอกชื่อโปรเจกต์และคลิก "สร้างโครงการ"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* ไปที่ [คอนโซล Vertex AI](https://console.cloud.google.com/vertex-ai)
* ในโปรเจกต์ที่สร้างขึ้น เปิดใช้งาน [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. ตั้งค่าสิทธิ์การเข้าถึง API

* เปิดหน้า [บัญชีบริการ](https://console.cloud.google.com/iam-admin/serviceaccounts) สร้างบัญชีบริการ

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* ในหน้าจัดการบัญชีบริการ ค้นหาบัญชีบริการที่เพิ่งสร้าง คลิก `คีย์` และสร้างคีย์แบบ JSON ใหม่

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* หลังสร้างสำเร็จ ไฟล์คีย์จะถูกบันทึกลงคอมพิวเตอร์คุณในรูปแบบ JSON โปรด**เก็บรักษาไว้อย่างดี**

## 3. กำหนดค่า Vertex AI ใน Cherry Studio

* เลือกผู้ให้บริการ Vertex AI
* กรอกข้อมูลในฟิลด์ที่เกี่ยวข้องจากไฟล์ JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

คลิกเพิ่ม [โมเดล](https://console.cloud.google.com/vertex-ai/model-garden) แล้วก็สามารถเริ่มต้นใช้งานได้ทันที!