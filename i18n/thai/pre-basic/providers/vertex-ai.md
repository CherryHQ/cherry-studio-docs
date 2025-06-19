---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# Vertex AI

## ภาพรวมของบทเรียน

### 1. รับ API Key

* ก่อนรับ API Key ของ Gemini คุณต้องมีโครงการ Google Cloud (หากคุณมีอยู่แล้ว สามารถข้ามขั้นตอนนี้ได้)
* เข้าสู่ [Google Cloud](https://console.cloud.google.com/projectcreate) เพื่อสร้างโครงการ กรอกชื่อโครงการและคลิก "สร้างโครงการ"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* เข้าสู่ [คอนโซล Vertex AI](https://console.cloud.google.com/vertex-ai)
* เปิดใช้งาน [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) ในโครงการที่สร้างขึ้น

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. ตั้งค่าการเข้าถึง API

* เปิดหน้าการ[อนุญาตบัญชีบริการ](https://console.cloud.google.com/iam-admin/serviceaccounts) และสร้างบัญชีบริการ

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* ในหน้าการจัดการบัญชีบริการ ค้นหาบัญชีบริการที่เพิ่งสร้าง คลิก `คีย์` และสร้างคีย์รูปแบบ JSON ใหม่

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* หลังจากการสร้างสำเร็จ ไฟล์คีย์จะถูกบันทึกไว้ในคอมพิวเตอร์ของคุณในรูปแบบไฟล์ JSON โปรด**เก็บรักษาไว้เป็นอย่างดี**

## 3. กำหนดค่า Vertex AI ใน Cherry Studio

* เลือกผู้ให้บริการ Vertex AI
* กรอกข้อมูลในฟิลด์ที่เกี่ยวข้องของไฟล์ JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

คลิกเพิ่ม[โมเดล](https://console.cloud.google.com/vertex-ai/model-garden) แล้วคุณก็สามารถเริ่มใช้ได้อย่างสนุกสนาน!