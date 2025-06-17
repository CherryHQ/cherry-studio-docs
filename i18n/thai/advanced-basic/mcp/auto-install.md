
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การติดตั้ง MCP อัตโนมัติ

> การติดตั้ง MCP อัตโนมัติต้องอัปเกรด Cherry Studio เป็นเวอร์ชัน v1.1.18 หรือสูงกว่า

## ความรู้เบื้องต้นเกี่ยวกับฟังก์ชัน

นอกเหนือจากการติดตั้งด้วยตนเอง Cherry Studio ยังมีเครื่องมือในตัว `@mcpmarket/mcp-auto-install` ซึ่งเป็นวิธีการติดตั้งเซิร์ฟเวอร์ MCP ที่สะดวกยิ่งขึ้น คุณเพียงแค่ต้องป้อนคำสั่งที่เกี่ยวข้องในการสนทนาของโมเดลใหญ่ที่รองรับบริการ MCP

{% hint style="warning" %}
**ข้อควรทราบในช่วงทดสอบ:**

* `@mcpmarket/mcp-auto-install` ยังอยู่ในช่วงทดสอบ
* ผลลัพธ์ขึ้นอยู่กับ "ความฉลาด" ของโมเดลใหญ่ บางตัวจะเพิ่มโดยอัตโนมัติ บางตัว**ยังคงต้องเปลี่ยนพารามิเตอร์บางอย่างด้วยตนเองในการตั้งค่า MCP**
* ในปัจจุบันที่มาของการค้นหาจะถูกค้นหาจาก @modelcontextprotocol ซึ่งคุณสามารถกำหนดค่าได้เอง (อธิบายด้านล่าง)
{% endhint %}

## คำแนะนำในการใช้งาน

ตัวอย่างเช่น คุณสามารถป้อน:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>ป้อนคำสั่งเพื่อติดตั้งเซิร์ฟเวอร์ MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>อินเทอร์เฟซการกำหนดค่าเซิร์ฟเวอร์ MCP</p></figcaption></figure>

ระบบจะรับรู้ความต้องการของคุณโดยอัตโนมัติและทำการติดตั้งผ่าน `@mcpmarket/mcp-auto-install` เครื่องมือนี้รองรับเซิร์ฟเวอร์ MCP หลากหลายประเภท รวมถึงแต่ไม่จำกัดเพียง:

* filesystem (ระบบไฟล์)
* fetch (การร้องขอเครือข่าย)
* sqlite (ฐานข้อมูล)
* และอื่นๆ...

> ตัวแปร MCP_PACKAGE_SCOPES สามารถกำหนดที่มาของการค้นหาบริการ MCP ได้ ค่าเริ่มต้นคือ: `@modelcontextprotocol`

## ความรู้เบื้องต้นเกี่ยวกับไลบรารี `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**การอ้างอิงค่ากำหนดเริ่มต้น:**

```json
// `axun-uUpaWEdMEMU8C61K` เป็นรหัสบริการ, กำหนดเองได้
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

`@mcpmarket/mcp-auto-install` เป็นแพ็คเกจ npm แบบโอเพนซอร์ส คุณสามารถดูรายละเอียดและเอกสารการใช้งานได้ที่ [npm 官方仓库](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) `@mcpmarket` เป็นชุดบริการ MCP อย่างเป็นทางการของ Cherry Studio
{% endhint %}