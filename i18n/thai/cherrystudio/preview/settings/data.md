---
icon: database
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การตั้งค่าข้อมูล

อินเทอร์เฟซนี้ช่วยให้คุณสามารถสำรองข้อมูลไคลเอนต์ทั้งบนคลาวด์และในเครื่อง ค้นหาไดเรกทอรีข้อมูลท้องถิ่น และล้างแคช

### การสำรองข้อมูล

ปัจจุบันการสำรองข้อมูลรองรับเฉพาะวิธีการ WebDAV คุณสามารถเลือกบริการที่รองรับ WebDAV เพื่อสำรองข้อมูลบนคลาวด์

คุณยังสามารถซิงค์ข้อมูลข้ามอุปกรณ์หลายเครื่องด้วยวิธีการ:  
`คอมพิวเตอร์ A` $$\xrightarrow{\text{สำรอง}}$$ `WebDAV` $$\xrightarrow{\text{กู้คืน}}$$ `คอมพิวเตอร์ B`

#### ตัวอย่างการใช้ JIanguoyun

1. เข้าสู่ระบบ JIanguoyun คลิกชื่อผู้ใช้มุมขวาบน เลือก "账户信息" (ข้อมูลบัญชี):

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. เลือก "安全选项" (ตัวเลือกความปลอดภัย) คลิก "添加应用" (เพิ่มแอปพลิเคชัน):

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. ป้อนชื่อแอปพลิเคชัน ระบบจะสร้างรหัสผ่านแบบสุ่ม:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. คัดลอกและบันทึกรหัสผ่าน:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. รับที่อยู่เซิร์ฟเวอร์ ชื่อบัญชี และรหัสผ่าน:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. ใน Cherry Studio การตั้งค่า → การตั้งค่าข้อมูล ป้อนข้อมูล WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. เลือกสำรองหรือกู้คืนข้อมูล และตั้งค่าช่วงเวลาการสำรองข้อมูลอัตโนมัติ:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
บริการ WebDAV ที่ใช้งานง่ายส่วนใหญ่คือบริการคลาวด์สตอเรจ:

* [JIanguoyun](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (ต้องเป็นสมาชิก)
* [AliCloud Drive](https://www.alipan.com/) (ต้องซื้อบริการ)
* [Box](https://www.box.com/) (พื้นที่ฟรี 10GB, ไฟล์สูงสุด 250MB)
* [Dropbox](https://www.dropbox.com/) (พื้นที่ฟรี 2GB, เชิญเพื่อนเพิ่มได้ถึง 16GB)
* [TeraCloud](https://teracloud.jp/en/) (พื้นที่ฟรี 10GB + รับเพิ่ม 5GB จากการเชิญ)
* [Yandex Disk](https://disk.yandex.com/) (พื้นที่ฟรี 10GB)

หรือบริการที่ต้องติดตั้งเอง:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}