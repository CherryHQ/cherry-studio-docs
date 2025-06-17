---
icon: trash-xmark
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# ล้างการตั้งค่า CSS

{% hint style="warning" %}
ใช้วิธีนี้เมื่อตั้งค่า CSS ผิดพลาด หรือไม่สามารถเข้าหน้าตั้งค่าหลังจากกำหนด CSS ได้  
{% endhint %}

* เปิดคอนโซล: คลิกที่หน้าต่าง CherryStudio แล้วกดปุ่มลัด  
<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (MacOS: <kbd>command</kbd>+<kbd>option</kbd>+<kbd>I</kbd>)
* ในหน้าต่างคอนโซลที่ปรากฏขึ้น ให้คลิกแท็บ `Console`

<figure><img src="../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

* พิมพ์คำสั่งด้วยมือ: `document.getElementById('user-defined-custom-css').remove()`  
**หมายเหตุ:** การคัดลอกและวางคำสั่งมีแนวโน้มจะไม่ทำงาน
* กด <kbd>Enter</kbd> เพื่อยืนยันการล้างการตั้งค่า CSS  
* เข้าไปที่การตั้งค่าการแสดงผลของ CherryStudio อีกครั้ง แล้วลบโค้ด CSS ที่มีปัญหาออก

---

### รายละเอียดการแปล:
1. รักษาโครงสร้าง Markdown, shortcuts (<kbd>), และ paths ของรูปภาพ (.gitbook/assets/image (126).png) ตามต้นฉบับ
2. แปลข้อความใน hint block โดยคงรูปแบบ {% hint %}...{% endhint %}
3. ปรับคำศัพท์เทคนิค:  
   - "控制台" → คอนโซล  
   - "快捷键" → ปุ่มลัด  
   - "回车确认" → กด Enter เพื่อยืนยัน
4. รูปแบบไวยากรณ์ไทย:  
   - ใช้ "เมื่อ...หรือ..." แทนเงื่อนไข  
   - เพิ่ม **หมายเหตุ** สำหรับข้อควรระวัง  
   - ใช้เครื่องหมาย » สำหรับลำดับขั้นตอน
5. รักษาชื่อเฉพาะ: CherryStudio, Console, MacOS