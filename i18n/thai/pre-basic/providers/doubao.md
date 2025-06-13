
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# ByteDance (Doubao)

* เข้าสู่ระบบ [Volcano Engine](https://console.volcengine.com/)
* คลิกตรง [ลิงก์นี้](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D) เพื่อเข้าถึงโดยตรง

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### รับคีย์ API

* คลิกที่ [API Key Management](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) ในแถบด้านข้าง
* สร้างคีย์ API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* หลังจากสร้างเสร็จ คลิกไอคอนตา 👁️ ด้านข้างคีย์ API เพื่อเปิดและคัดลอก

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* วางคีย์ API ที่คัดลอกใน CherryStudio จากนั้นเปิดสวิตช์ผู้ให้บริการ

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### เปิดใช้งานและเพิ่มโมเดล

* เปิดใช้งานโมเดลที่ต้องการใน [Open Management](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) ที่ด้านล่างสุดของแถบด้านข้าง สามารถเปิดใช้งานชุดโมเดล Doubao และ DeepSeek ตามต้องการ

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* ใน [เอกสารรายชื่อโมเดล](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90) ให้ค้นหา **Model ID** ที่ตรงกับโมเดลที่ต้องการ

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="ตัวอย่างรายการ Model ID ของ Volcano Engine"><figcaption></figcaption></figure>

* เปิดการตั้งค่า [Model Service](../../cherrystudio/preview/settings/providers.md) ใน Cherry Studio แล้วหา Volcano Engine
* คลิก "เพิ่ม" แล้ววาง Model ID ที่ได้มาลงในช่องข้อความ Model ID

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* เพิ่มโมเดลตามขั้นตอนนี้ทีละตัว

### ที่อยู่ API

ที่อยู่ API มีสองรูปแบบ:
1. รูปแบบเริ่มต้นของไคลเอนต์: `https://ark.cn-beijing.volces.com/api/v3/`
2. รูปแบบอื่น: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
ทั้งสองรูปแบบไม่มีความแตกต่าง ใช้ค่าเริ่มต้นได้เลย ไม่ต้องแก้ไข

สำหรับความแตกต่างระหว่างเครื่องหมาย `/` และ `#` ดูเอกสารเกี่ยวกับที่อยู่ API ของผู้ให้บริการ: [คลิกดู](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>ตัวอย่าง cURL จากเอกสารอย่างเป็นทางการ</p></figcaption></figure>