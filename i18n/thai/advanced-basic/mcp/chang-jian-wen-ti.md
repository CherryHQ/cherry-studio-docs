---
icon: hexagon-exclamation
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# คำถามที่พบบ่อย

### 1. mcp-server-time

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6068931438453048569-y.jpg" alt=""><figcaption><p>ภาพหน้าจอแสดงข้อผิดพลาด</p></figcaption></figure>

**วิธีการแก้ไข**  

กรอกข้อมูลในคอลัมน์ "พารามิเตอร์":

```
mcp-server-time
--local-timezone
<เขตเวลามาตรฐานของคุณ ตัวอย่างเช่น Asia/Shanghai>
```