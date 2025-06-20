---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# Vertex AI

## ภาพรวมบทแนะนำ

### 1. ขั้นตอนการขอคีย์ API

* ก่อนที่จะขอคีย์ API ของ Gemini คุณต้องมีโปรเจ็กต์ Google Cloud ก่อน (ถ้ามีแล้ว ข้ามขั้นตอนนี้ได้)
* เข้าไปที่ [Google Cloud](https://console.cloud.google.com/projectcreate) เพื่อสร้างโปรเจ็กต์ กรอกชื่อโปรเจ็กต์ แล้วคลิกสร้างโปรเจ็กต์

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* เข้าไปที่ [คอนโซล Vertex AI](https://console.cloud.google.com/vertex-ai)
* ในโปรเจ็กต์ที่สร้างแล้ว ให้เปิดใช้งาน [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. การตั้งค่าสิทธิ์การเข้าถึง API

* เปิดหน้า [บัญชีผู้ใช้บริการ](https://console.cloud.google.com/iam-admin/serviceaccounts) เพื่อสร้างบัญชีผู้ใช้บริการ

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* ในหน้าจัดการบัญชีผู้ใช้บริการ ให้ค้นหาบัญชีผู้ใช้บริการที่เพิ่งสร้าง คลิกที่ `คีย์` แล้วสร้างคีย์รูปแบบ JSON ใหม่

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* หลังจากสร้างคีย์สำเร็จแล้ว ไฟล์คีย์จะถูกบันทึกลงเครื่องคอมพิวเตอร์ของคุณในรูปแบบไฟล์ JSON กรุณา **เก็บรักษาให้ดี**

## 3. การกำหนดค่า Vertex AI ใน Cherry Studio

* เลือกผู้ให้บริการ Vertex AI
* กรอกข้อมูลในฟิลด์ที่เกี่ยวข้องจากไฟล์ JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

คลิกเพิ่ม [โมเดล](https://console.cloud.google.com/vertex-ai/model-garden) แล้วก็สามารถเริ่มใช้ได้อย่างสนุกสนาน!