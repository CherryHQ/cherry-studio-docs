
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การติดตั้ง MCP อัตโนมัติ

> การติดตั้ง MCP อัตโนมัติจำเป็นต้องอัปเกรด Cherry Studio เป็นเวอร์ชัน v1.1.18 หรือสูงกว่า

## บทนำเกี่ยวกับฟังก์ชัน

นอกเหนือจากการติดตั้งด้วยมือ Cherry Studio ยังมีเครื่องมือ `@mcpmarket/mcp-auto-install` ในตัวซึ่งเป็นวิธีการติดตั้งเซิร์ฟเวอร์ MCP ที่สะดวกยิ่งขึ้น คุณเพียงแค่ต้องป้อนคำสั่งที่เกี่ยวข้องในการสนทนาของโมเดลขนาดใหญ่ที่รองรับบริการ MCP

{% hint style="warning" %}
**ข้อควรระวังในระยะทดสอบ:**

* `@mcpmarket/mcp-auto-install` ยังคงอยู่ในระยะทดสอบ
* ผลลัพธ์ขึ้นอยู่กับ "ความฉลาด" ของโมเดลขนาดใหญ่ บางตัวจะเพิ่มโดยอัตโนมัติ ส่วนบางตัวยัง**จำเป็นต้องเปลี่ยนพารามิเตอร์บางอย่างใน MCP settings ด้วยตนเอง**
* ในปัจจุบัน แหล่งค้นหามาจาก @modelcontextprotocol ซึ่งสามารถกำหนดค่าด้วยตนเองได้ (อธิบายด้านล่าง)
{% endhint %}

## คำแนะนำในการใช้งาน

ตัวอย่างเช่น คุณสามารถป้อนคำสั่ง:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>ป้อนคำสั่งเพื่อติดตั้งเซิร์ฟเวอร์ MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>อินเทอร์เฟซการกำหนดค่าเซิร์ฟเวอร์ MCP</p></figcaption></figure>

ระบบจะรับรู้ความต้องการของคุณโดยอัตโนมัติและติดตั้งผ่าน `@mcpmarket/mcp-auto-install` เครื่องมือนี้รองรับเซิร์ฟเวอร์ MCP หลายประเภท รวมถึงแต่ไม่จำกัดเฉพาะ:

* filesystem (ระบบไฟล์)
* fetch (การร้องขอเครือข่าย)
* sqlite (ฐานข้อมูล)
* เป็นต้น

> ตัวแปร MCP_PACKAGE_SCOPES สามารถกำหนดแหล่งที่มาของการค้นหาบริการ MCP แบบกำหนดเองได้ โดยค่าเริ่มต้นคือ: `@modelcontextprotocol`

## การแนะนำห้องสมุด `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**การอ้างอิงการกำหนดค่าเริ่มต้น:**

```json
// `axun-uUpaWEdMEMU8C61K` เป็นรหัสบริการ สามารถกำหนดเองได้
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "รายละเอียดดูได้ที่ https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` เป็นแพ็คเกจ npm แบบโอเพนซอร์ส คุณสามารถดูรายละเอียดและเอกสารการใช้งานได้ที่ [คลังอย่างเป็นทางการของ npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) `@mcpmarket` เป็นคอลเลกชันบริการ MCP อย่างเป็นทางการของ Cherry Studio
{% endhint %}