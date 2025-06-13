
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การกำหนดค่าและการใช้งาน MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. เปิดการตั้งค่า Cherry Studio
2. ค้นหาตัวเลือก `MCP เซิร์ฟเวอร์`
3. คลิก `เพิ่มเซิร์ฟเวอร์`
4. ป้อนพารามิเตอร์ที่เกี่ยวข้องของ MCP Server ([ลิงค์อ้างอิง](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)) ซึ่งอาจรวมถึง:
   * ชื่อ: ตั้งชื่อเอง เช่น `fetch-server`
   * ประเภท: เลือก `STDIO`
   * คำสั่ง: ป้อน `uvx`
   * พารามิเตอร์: ป้อน `mcp-server-fetch`
   * (อาจมีพารามิเตอร์อื่น ๆ ขึ้นอยู่กับเซิร์ฟเวอร์)
5. คลิก `บันทึก`

{% hint style="success" %}
หลังจากการกำหนดค่าดังกล่าวเสร็จสิ้น Cherry Studio จะดาวน์โหลด MCP Server ที่ต้องการ - `fetch server` โดยอัตโนมัติ เมื่อดาวน์โหลดเสร็จสมบูรณ์ เราสามารถเริ่มใช้งานได้! หมายเหตุ: หากการกำหนดค่า mcp-server-fetch ไม่สำเร็จ อาจลองรีสตาร์ทคอมพิวเตอร์
{% endhint %}

### เปิดใช้งานบริการ MCP ในช่องแชท

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* คุณได้เพิ่ม MCP เซิร์ฟเวอร์ในการตั้งค่า `MCP เซิร์ฟเวอร์` เรียบร้อยแล้ว

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **การสาธิตผลการใช้งาน**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

จากภาพด้านบนจะเห็นได้ว่า หลังจากผสานฟังก์ชัน `fetch` ของ MCP แล้ว Cherry Studio สามารถเข้าใจความตั้งใจในการสืบค้นของผู้ใช้ได้ดีขึ้น และดึงข้อมูลที่เกี่ยวข้องจากเครือข่าย เพื่อให้คำตอบที่ถูกต้องและครอบคลุมมากขึ้น