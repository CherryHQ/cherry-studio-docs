
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# Google Gemini

## รับคีย์ API

* ก่อนรับคีย์ API ของ Gemini คุณต้องมีโปรเจ็กต์ Google Cloud (หากคุณมีอยู่แล้ว ข้ามขั้นตอนนี้ได้)
* ไปที่ [Google Cloud](https://console.cloud.google.com/projectcreate) เพื่อสร้างโปรเจ็กต์ กรอกชื่อโปรเจ็กต์แล้วคลิกสร้างโปรเจ็กต์

<figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

* ในหน้า [API Key อย่างเป็นทางการ](https://aistudio.google.com/app/apikey?hl=zh-cn) คลิก `สร้างคีย์ API`

<figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

* คัดลอกคีย์ที่สร้างมา จากนั้นเปิด [การตั้งค่าผู้ให้บริการ](broken-reference) ของ CherryStudio
* ค้นหาผู้ให้บริการ Gemini แล้ววางคีย์ที่เพิ่งได้รับ

<figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

* คลิกจัดการหรือเพิ่มที่ด้านล่างสุด เพิ่มโมเดลที่รองรับ แล้วเปิดสวิตช์ผู้ให้บริการด้านขวาบนเพื่อเริ่มใช้ได้

{% hint style="info" %}
- ในประเทศจีน ยกเว้นไต้หวัน ไม่สามารถใช้บริการ Google Gemini โดยตรงได้ ต้องจัดการปัญหา proxy ด้วยตนเอง
{% endhint %}