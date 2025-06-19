
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# เพิ่มเซิร์ฟเวอร์ ModelScope MCP

> การใช้เซิร์ฟเวอร์ ModelScope MCP จำเป็นต้องอัปเกรด Cherry Studio เป็นเวอร์ชัน v1.2.9 หรือสูงกว่า

ในเวอร์ชัน v1.2.9 Cherry Studio ได้ร่วมมืออย่างเป็นทางการกับ ModelScope 魔搭 เพื่อลดขั้นตอนการเพิ่มเซิร์ฟเวอร์ MCP อย่างมาก ป้องกันข้อผิดพลาดระหว่างการตั้งค่า และช่วยให้คุณสามารถค้นพบเซิร์ฟเวอร์ MCP จำนวนมหาศาลในชุมชน ModelScope ได้ ต่อไปนี้เป็นขั้นตอนการทำงานเพื่อดูวิธีซิงโครไนซ์เซิร์ฟเวอร์ MCP จาก ModelScope ใน Cherry Studio

## ขั้นตอนการดำเนินงาน

### จุดเริ่มต้นการซิงโครไนนซ์:
คลิกการตั้งค่าเซิร์ฟเวอร์ MCP ใน Settings แล้วเลือก `ซิงโครไนซ์เซิร์ฟเวอร์`

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### ค้นพบบริการ MCP:
เลือก ModelScope และเรียกดูเพื่อค้นพบบริการ MCP

<figure><img src="../../.gitbook/assets/image (1) (4).png" alt=""><figcaption></figcaption></figure>

### ดูรายละเอียดเซิร์ฟเวอร์ MCP
ลงทะเบียน/เข้าสู่ระบบ ModelScope และตรวจสอบรายละเอียดบริการ MCP

<figure><img src="../../.gitbook/assets/image (2) (6).png" alt=""><figcaption></figcaption></figure>

### เชื่อมต่อเซิร์ฟเวอร์
ในหน้าดูรายละเอียดบริการ MCP ให้เลือกเชื่อมต่อบริการ

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### ขอและคัดลอก api token
คลิก "รับ api token" ใน Cherry Studio เพื่อไปยังเว็บไซต์ ModelScope คัดลอก api token แล้วกลับมาใส่ใน Cherry Studio

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### ซิงโครไนซ์สำเร็จ
ในรายการเซิร์ฟเวอร์ MCP ของ Cherry Studio คุณจะเห็นบริการ MCP จาก ModelScope ที่เชื่อมต่อแล้วและสามารถใช้งานได้ในการสนทนา

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### อัปเดตแบบเพิ่มส่วน (Incremental Update)
สำหรับเซิร์ฟเวอร์ MCP ที่เชื่อมต่อใหม่ผ่านเว็บ ModelScope ในภายหลัง เพียงคลิก `ซิงโครไนซ์เซิร์ฟเวอร์` เพื่อเพิ่มเซิร์ฟเวอร์ MCP แบบเพิ่มส่วน

<figure><img src="../../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

ผ่านขั้นตอนเหล่านี้ คุณได้เรียนรู้วิธีซิงโครไนซ์เซิร์ฟเวอร์ MCP จาก ModelScope ใน Cherry Studio อย่างง่ายดาย โดยกระบวนการตั้งค่านั้นถูกทำให้ง่ายขึ้นอย่างมาก ช่วยหลีกเลี่ยงความซับซ้อนและข้อผิดพลาดจากการตั้งค่าด้วยตนเอง และยังช่วยให้คุณสามารถเข้าถึงทรัพยากรเซิร์ฟเวอร์ MCP จำนวนมหาศาลที่ชุมชน ModelScope มอบให้ได้อย่างง่ายดาย

เริ่มสำรวจและใช้บริการ MCP ที่ทรงพลังเหล่านี้ เพื่อมอบความสะดวกสบายและความเป็นไปได้ใหม่ๆ ให้กับประสบการณ์การใช้งาน Cherry Studio ของคุณกันเถอะ!