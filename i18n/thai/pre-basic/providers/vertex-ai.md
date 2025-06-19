---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# Vertex AI

## ภาพรวมของบทสอน

### 1. รับคีย์ API

* ก่อนที่จะรับคีย์ API ของ Gemini คุณจำเป็นต้องมีโปรเจ็กต์ Google Cloud (หากมีอยู่แล้วสามารถข้ามขั้นตอนนี้ได้)
* เข้าไปที่ [Google Cloud](https://console.cloud.google.com/projectcreate) เพื่อสร้างโปรเจ็กต์ กรอกชื่อโปรเจ็กต์แล้วคลิก "สร้างโปรเจ็กต์"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* เข้าไปที่ [คอนโซล Vertex AI](https://console.cloud.google.com/vertex-ai)
* เปิดใช้งาน Vertex AI API ในโปรเจ็กต์ที่สร้างขึ้น ([https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA))

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>