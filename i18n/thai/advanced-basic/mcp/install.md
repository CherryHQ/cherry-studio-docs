
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การติดตั้งสภาพแวดล้อม MCP

**MCP (Model Context Protocol)** เป็นโปรโตคอลโอเพนซอร์สที่ออกแบบมาเพื่อจัดเตรียมข้อมูลบริบทให้แบบจำลองภาษาขนาดใหญ่ (LLM) ในรูปแบบมาตรฐาน ดูข้อมูลเพิ่มเติมเกี่ยวกับ MCP ที่ [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## การใช้ MCP ใน Cherry Studio

ตัวอย่างด้านล่างใช้ฟังก์ชัน `fetch` เพื่อสาธิตวิธีใช้งาน MCP ใน Cherry Studio ดูรายละเอียดเพิ่มเติมได้ที่ [เอกสาร](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)

### **การเตรียมการ: ติดตั้ง uv และ bun**

{% hint style="warning" %}
ปัจจุบัน Cherry Studio ใช้เฉพาะ [uv](https://github.com/astral-sh/uv) และ [bun](https://github.com/oven-sh/bun) ที่ติดตั้งในตัวเท่านั้น และ**จะไม่นำ** uv และ bun ที่ติดตั้งไว้ในระบบเดิมกลับมาใช้อีก
{% endhint %}

ใน `การตั้งค่า - เซิร์ฟเวอร์ MCP` คลิกปุ่ม `ติดตั้ง` เพื่อดาวน์โหลดและติดตั้งโดยอัตโนมัติ เนื่องจากการดาวน์โหลดโดยตรงจาก GitHub อาจใช้เวลานานและมีโอกาสล้มเหลวสูง ให้ยืนยันการติดตั้งสำเร็จโดยตรวจสอบว่ามีไฟล์ในโฟลเดอร์ที่กล่าวถึงด้านล่างหรือไม่

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**ตำแหน่งติดตั้งโปรแกรมปฏิบัติการ:**

Windows: `C:\Users\用户名\.cherrystudio\bin`

macOS และ Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>ไดเรกทอรี bin</p></figcaption></figure>

**กรณีไม่สามารถติดตั้งได้ตามปกติ:**
- เชื่อมโยงคำสั่งที่ตรงกันในระบบมาที่นี่โดยใช้ symbolic link (หากไม่มีไดเรกทอรีที่เกี่ยวข้อง ต้องสร้างเอง)
- หรือดาวน์โหลดไฟล์ปฏิบัติการด้วยตนเองแล้ววางในไดเรกทอรีนี้:
  - Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)
  - UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)