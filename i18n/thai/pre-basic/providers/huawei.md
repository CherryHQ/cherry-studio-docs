
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# Huawei Cloud

## ขั้นตอนที่ 1: สร้างบัญชีผู้ใช้
ไปที่ [Huawei Cloud](https://auth.huaweicloud.com/authui/login) เพื่อสร้างบัญชีและเข้าสู่ระบบ

## ขั้นตอนที่ 2: เข้าสู่คอนโซล ModelArts
คลิก [ลิงก์นี้](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) เพื่อเข้าสู่คอนโซล ModelArts

## ขั้นตอนที่ 3: การมอบสิทธิ์

<details>

<summary>ขั้นตอนการมอบสิทธิ์ (หากมอบสิทธิ์แล้ว ข้ามขั้นตอนนี้)</summary>

1. หลังจากเข้าสู่หน้าจากขั้นตอนที่ 2 ตามคำแนะนำให้ไปที่หน้าการมอบสิทธิ์ (คลิก IAM ผู้ใช้ย่อย → เพิ่มผู้มอบหมาย → ผู้ใช้ทั่วไป)

![](<../../.gitbook/assets/image (49).png>)

2. หลังจากคลิกสร้างแล้ว ให้กลับไปที่ลิงก์ในขั้นตอนที่ 2
3. จะปรากฏข้อความแจ้งว่าสิทธิ์การเข้าถึงไม่เพียงพอ ให้คลิก "คลิกที่นี่" ในข้อความแจ้งนั้น
4. เพิ่มการมอบสิทธิ์ที่มีอยู่และยืนยัน

![](<../../.gitbook/assets/image (50).png>)

หมายเหตุ: วิธีนี้เหมาะสำหรับผู้เริ่มต้น ไม่จำเป็นต้องดูเนื้อหามากมาย เพียงคลิกตามคำแนะนำ หากคุณสามารถมอบสิทธิ์สำเร็จในครั้งเดียวก็สามารถทำตามวิธีของคุณเองได้

</details>

## ขั้นตอนที่ 4: สร้าง API Key
คลิกการจัดการการตรวจสอบสิทธิ์ (Authentication Management) ในแถบด้านข้าง สร้าง API Key (คีย์ลับ) และคัดลอก

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

จากนั้นใน CherryStudio ให้สร้างผู้ให้บริการใหม่

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

หลังจากสร้างเสร็จแล้ว ให้ป้อนคีย์ลับ

## ขั้นตอนที่ 5: รับแบบจำลองทั้งหมด
คลิกการปรับใช้แบบจำลอง (Model Deployment) ในแถบด้านข้าง แล้วคลิก "รับทั้งหมด"

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

## ขั้นตอนที่ 6: เรียกใช้งาน
<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

คัดลอกที่อยู่จากจุด ① แล้ววางในช่องที่อยู่ผู้ให้บริการของ CherryStudio และเติมเครื่องหมาย "#" ต่อท้าย

และเติมเครื่องหมาย "#" ต่อท้าย

และเติมเครื่องหมาย "#" ต่อท้าย

และเติมเครื่องหมาย "#" ต่อท้าย

และเติมเครื่องหมาย "#" ต่อท้าย

เหตุผลที่ต้องเติม "#" [ดูที่นี่](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> คุณสามารถทำตามบทช่วยสอนนี้ได้เลยโดยไม่ต้องดูลิงก์ดังกล่าว
> หรือคุณสามารถใช้วิธีลบ v1/chat/completions ในการกรอกก็ได้ ตราบใดที่คุณเข้าใจวิธีการกรอก แต่ถ้าไม่เข้าใจ โปรดทำตามบทช่วยสอนนี้อย่างเคร่งครัด



<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

คัดลอกชื่อแบบจำลองจากจุด ② ใน CherryStudio แล้วคลิกปุ่ม "+เพิ่ม" เพื่อสร้างแบบจำลองใหม่

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

ป้อนชื่อแบบจำลองตามตัวอย่าง โดยไม่เพิ่มหรือลดเนื้อหาใดๆ และไม่ใส่เครื่องหมายคำพูด

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

คลิกปุ่มเพิ่มแบบจำลองเพื่อดำเนินการให้เสร็จสิ้น

{% hint style="info" %}
ใน Huawei Cloud เนื่องจากแต่ละแบบจำลองมีที่อยู่ต่างกัน จึงจำเป็นต้องสร้างผู้ให้บริการใหม่สำหรับแต่ละแบบจำลอง โดยทำซ้ำขั้นตอนข้างต้น
{% endhint %}