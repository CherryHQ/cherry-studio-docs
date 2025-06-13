
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# OneAPI

* เข้าสู่ระบบและไปที่หน้ารายการโทเค็น

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

* สร้างโทเค็นใหม่ (หรือใช้โทเค็น default ด้านบนได้โดยตรง↑)

<figure><img src="../../../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

* คัดลอกโทเค็น

<figure><img src="../../../.gitbook/assets/image (24).png" alt="" width="563"><figcaption></figcaption></figure>

* เปิดการตั้งค่าผู้ให้บริการของ CherryStudio แล้วคลิกที่ `เพิ่ม` ด้านล่างสุดของรายการผู้ให้บริการ
* ใส่ชื่อหมายเหตุ เลือกผู้ให้บริการเป็น OpenAI แล้วคลิกตกลง

<figure><img src="../../../.gitbook/assets/image (25).png" alt="" width="291"><figcaption></figcaption></figure>

* ใส่คีย์ที่เพิ่งคัดลอกมา
* กลับไปที่หน้าคีย์ API แล้วคัดลอกที่อยู่รูทจากแถบที่อยู่ของเบราว์เซอร์ ตัวอย่างเช่น:

<figure><img src="../../../.gitbook/assets/image (26).png" alt="" width="563"><figcaption><p><strong>คัดลอกแค่ https://xxx.xxx.com เท่านั้น ไม่จำเป็นต้องมี "/" และเนื้อหาหลังจากนั้น</strong></p></figcaption></figure>

{% hint style="info" %}
* เมื่อที่อยู่เป็น IP+พอร์ต ให้กรอก http://IP:พอร์ต เช่น: http://127.0.0.1:3000
* ระวังความแตกต่างระหว่าง `http` และ `https` หากไม่ได้เปิด SSL อย่าใส่ https
{% endhint %}

* เพิ่มโมเดล (คลิกจัดการเพื่อรับโดยอัตโนมัติหรือป้อนด้วยตนเอง) เปิดสวิตช์มุมขวาบนเพื่อใช้งาน

{% hint style="success" %}
ธีมอื่นของ OneAPI อาจมีอินเทอร์เฟซที่แตกต่างกัน แต่วิธีการเพิ่มจะเหมือนกับขั้นตอนการดำเนินการข้างต้น
{% endhint %}