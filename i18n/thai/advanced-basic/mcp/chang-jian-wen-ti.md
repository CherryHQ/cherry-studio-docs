---
icon: hexagon-exclamation
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# คำถามที่พบบ่อย

### 1. mcp-server-time

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6068931438453048569-y.jpg" alt=""><figcaption><p>ภาพหน้าจอแสดงข้อผิดพลาด</p></figcaption></figure>

**แนวทางแก้ไข**&#x20;

กรอกข้อมูลในคอลัมน์ "พารามิเตอร์" ดังนี้:

```
mcp-server-time
--local-timezone
<เขตเวลามาตรฐานของคุณ เช่น Asia/Shanghai>
```