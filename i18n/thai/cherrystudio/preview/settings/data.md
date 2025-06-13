---
icon: database
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การตั้งค่าข้อมูล

อินเทอร์เฟซนี้ช่วยให้คุณสามารถสำรองข้อมูลไคลเอ็นต์บนระบบคลาวด์หรือเครื่องท้องถิ่น ค้นหาไดเรกทอรีข้อมูลท้องถิ่น และล้างแคชได้

### การสำรองข้อมูล

ปัจจุบันการสำรองข้อมูลรองรับเฉพาะวิธีการผ่าน WebDAV เท่านั้น คุณสามารถเลือกใช้บริการที่รองรับ WebDAV เพื่อสำรองข้อมูลบนระบบคลาวด์

คุณยังสามารถซิงโครไนซ์ข้อมูลข้ามอุปกรณ์หลายเครื่องได้ด้วยวิธีการ:  
`คอมพิวเตอร์ A` $$\xrightarrow{\text{สำรอง}}$$ `WebDAV` $$\xrightarrow{\text{กู้คืน}}$$ `คอมพิวเตอร์ B`

#### ตัวอย่างการใช้งาน Nutstore

1. ลงชื่อเข้าใช้ Nutstore คลิกที่ชื่อผู้ใช้มุมขวาบน แล้วเลือก "账户信息":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. เลือก "安全选项" แล้วคลิก "添加应用"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. ป้อนชื่อแอปพลิเคชัน เพื่อสร้างรหัสผ่านแบบสุ่ม:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. คัดลอกและบันทึกรหัสผ่าน:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. รับข้อมูลเซิร์ฟเวอร์: ที่อยู่ บัญชีผู้ใช้ และรหัสผ่าน:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. ในการตั้งค่า Cherry Studio > การตั้งค่าข้อมูล: กรอกข้อมูล WebDAV

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. เลือกสำรองหรือกู้คืนข้อมูล และตั้งค่าช่วงเวลาการสำรองอัตโนมัติได้

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
บริการ WebDAV ที่ใช้งานง่ายส่วนใหญ่คือคลาวด์สตอเรจ:

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/) (ต้องเป็นสมาชิก)
* [阿里云盘](https://www.alipan.com/) (ต้องซื้อบริการ)
* [Box](https://www.box.com/) (พื้นที่ฟรี 10GB, จำกัดขนาดไฟล์เดียวที่ 250MB)
* [Dropbox](https://www.dropbox.com/) (ฟรี 2GB, เชิญเพื่อนเพิ่มพื้นที่ได้สูงสุด 16GB)
* [TeraCloud](https://teracloud.jp/en/) (พื้นที่ฟรี 10GB, เชิญเพื่อนรับพื้นที่เพิ่ม 5GB)
* [Yandex Disk](https://disk.yandex.com/) (พื้นที่ฟรี 10GB)

หรือบริการที่ต้องติดตั้งเอง:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}