---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การเชื่อมต่อ Volcano Engine เข้ากับเครือข่าย

### 1. เข้าสู่ระบบหรือลงทะเบียนบัญชี Volcano Engine <a href="#rclz7" id="rclz7"></a>

เยี่ยมชมเว็บไซต์ทางการ: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>เว็บไซต์หลักของ Volcano Engine</p></figcaption></figure>

### 2. สร้าง "แอปพลิเคชันของฉัน" ที่ "สามารถเชื่อมต่อเครือข่ายได้" <a href="#gvzaa" id="gvzaa"></a>

2.1. เข้าสู่ระบบ Volcano Engine แล้วไปที่หน้า "Volcano Ark" โดยตรง: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **คลิกตามลำดับ:** <mark style="color:red;">**"แอปพลิเคชันของฉัน" → "สร้างแอปพลิเคชัน" → "Zero-code" → "แชทเดี่ยว"**</mark>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. กรอกข้อมูลและเผยแพร่แอปพลิเคชัน <a href="#zzdfe" id="zzdfe"></a>

**ชื่อแอปพลิเคชัน**: ตั้งชื่อตามต้องการ (เฉพาะช่องที่มี <mark style="color:red;">**\* จำเป็นต้องกรอก**</mark> ส่วนอื่นไม่ต้องกรอกก็ได้)

<mark style="color:red;">**ประเด็นสำคัญ: ต้องเปิดปลั๊กอินเครือข่าย (ต้องเปิดใช้งานก่อน)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. เปิดใช้งานฟังก์ชันปลั๊กอินเครือข่าย (โปรดทราบค่าบริการและจำนวนครั้งฟรี) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>คลิก "ซื้อทันที" แล้วดำเนินการตามขั้นตอนจนแสดงหน้าต่างด้านล่าง แสดงว่าการเปิดใช้งานสำเร็จ</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>ตรวจสอบสถานะ เมื่อถึงขั้นตอนนี้แสดงว่าการเปิดใช้งานสำเร็จ</p></figcaption></figure>

กลับไปที่หน้ากรอกข้อมูลแอปพลิเคชันเพื่อดำเนินการต่อ

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. คำอธิบายการตั้งค่าขั้นสูง "การค้นหาทางอินเทอร์เน็ต" <a href="#sp6uz" id="sp6uz"></a>

เลือกตามความต้องการจริง:

* หากต้องการควบคุมอินพุต/เอาต์พุตอย่างแม่นยำ ให้ใช้ "**การเรียกใช้งานแบบกำหนดเอง**"
* หากไม่ต้องการยุ่งยาก สามารถใช้ "**การเรียกอัตโนมัติ**" - ค่าเริ่มต้น
* หากไม่กังวลเรื่องงบประมาณ และต้องการข้อมูลทันสมัยสูงสุด สามารถเลือก "**บังคับเปิด**"

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. เผยแพร่แอปพลิเคชัน <a href="#fe1gf" id="fe1gf"></a>

คลิกปุ่ม "เผยแพร่" ที่มุมขวาบน เพื่อสร้างแอปพลิเคชันสำเร็จ

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. รับ API Key <a href="#jtqlu" id="jtqlu"></a>

คลิกตามลำดับ: **"คู่มือเรียกใช้งาน API" → "เลือก API Key แล้วคัดลอก" → "ดูและเลือก"**

คัดลอก API Key มาเก็บไว้ก่อน แล้วไปวางใน Cherry Studio (รายละเอียดการดำเนินการดูในหน้าจอด้านล่าง)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

หมายเหตุ: หากไม่มี API Key ให้คลิก "**สร้าง API Key**" ที่มุมขวาบนของป๊อปอัพ แล้วคัดลอก API Key

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. ใช้ API Key ใน Cherry Studio เพื่อเชื่อมต่อ DeepSeek-R1 ผ่านเครือข่าย <a href="#lrefj" id="lrefj"></a>

#### 5.1. เปิด Cherry Studio → "การตั้งค่า" → "ตั้งชื่อตามต้องการ" → "ประเภทเป็น: OpenAI" <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. กำหนดค่า URL และ Key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">หมายเหตุ: หากไม่พบที่อยู่หรือโหนดที่ไม่ใช่ปักกิ่ง สามารถหาที่อยู่ที่แน่นอนได้ในส่วนนี้ อย่าลืมเครื่องหมาย "/":</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. เพิ่มชื่อโมเดล <a href="#qmh3i" id="qmh3i"></a>

**ต้องคัดลอกชื่อโมเดลจากข้อความขนาดเล็กด้านล่างเท่านั้น** มิฉะนั้นจะเกิดข้อผิดพลาด

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. แสดงตัวอย่างผลลัพธ์ <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>