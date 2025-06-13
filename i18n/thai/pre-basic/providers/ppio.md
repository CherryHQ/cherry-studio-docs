
{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# PPIO ไพโอคลาวด์

## การเชื่อมต่อ Cherry Studio กับ PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)ภาพรวมบทเรียน <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio เป็นไคลเอนต์เดสก์ท็อปที่รองรับหลายโมเดล ปัจจุบันรองรับ: Windows, Linux, และ MacOS ซึ่งรวมโมเดล LLM ยอดนิยมต่างๆ โดยมอบความช่วยเหลือหลากหลายสถานการณ์ ผู้ใช้สามารถเพิ่มประสิทธิภาพการทำงานผ่านการจัดการการสนทนาอัจฉริยะ การกำหนดค่าแบบโอเพ่นซอร์ส และอินเทอร์เฟซหลายธีม

ตอนนี้ Cherry Studio ได้รับการปรับให้เข้ากันอย่างลึกซึ้งกับ **PPIO High-performance API Channel** - ด้วยการรับประกันพลังการประมวลผลระดับองค์กร มันมอบ **การตอบสนองที่รวดเร็วสำหรับ DeepSeek-R1/V3** และ **ความพร้อมใช้งานของบริการ 99.9%** ส่งมอบประสบการณ์ที่รวดเร็วและลื่นไหลให้กับคุณ

บทเรียนด้านล่างนี้รวมวิธีการเชื่อมต่อแบบครบวงจร (รวมถึงการตั้งค่าคีย์) เริ่มใช้โหมดขั้นสูงของ "การจัดระเบียบอัจฉริยะ Cherry Studio + PPIO High-performance API" ภายใน 3 นาที

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. เข้าไปที่ CherryStudio และเพิ่ม "PPIO" เป็นผู้ให้บริการโมเดล <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

ก่อนอื่นดาวน์โหลด Cherry Studio จากเว็บไซต์หลัก: [ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) (หากเข้าไม่ได้ สามารถเปิดลิงก์ Quark Pan ด้านล่างเพื่อดาวน์โหลดเวอร์ชันที่ต้องการ: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) เริ่มต้นด้วยคลิกที่การตั้งค่ามุมซ้ายล่าง กำหนดชื่อผู้ให้บริการเป็น: `PPIO` แล้วคลิก "ตกลง"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) ไปที่ [การจัดการ API Keys ของ PPIO Computing Cloud ](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio) คลิก【ไอคอนผู้ใช้】—【การจัดการ API Keys】เพื่อเข้าสู่คอนโซล

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

คลิกปุ่ม 【+ สร้าง】เพื่อสร้าง API Key ใหม่ ตั้งชื่อคีย์ที่ต้องการ **คีย์ที่สร้างขึ้นจะแสดงเฉพาะตอนสร้างเท่านั้น โปรดคัดลอกและบันทึกไว้ในเอกสารเพื่อไม่ให้เกิดปัญหากับการใช้ในภายหลัง**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) ใน CherryStudio ป้อนคีย์ คลิกการตั้งค่า เลือก【PPIO ไพโอคลาวด์】ป้อน API Key ที่สร้างจากเว็บไซต์หลัก แล้วคลิก【ตรวจสอบ】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) เลือกโมเดล: เช่น deepseek/deepseek-r1/community หากต้องการเปลี่ยนโมเดลอื่น สามารถเปลี่ยนได้โดยตรง

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 และ V3 เวอร์ชัน community ใช้เพื่อทดลองใช้งานเท่านั้น ซึ่งเป็นโมเดลเวอร์ชันเต็มพารามิเตอร์ มีความเสถียรและประสิทธิภาพไม่แตกต่าง หากต้องการใช้งานจำนวนมากจำเป็นต้อง **เติมเงินและเปลี่ยนไปใช้เวอร์ชันที่ไม่ใช่ community**

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. การกำหนดค่าการใช้โมเดล <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) คลิก【ตรวจสอบ】เมื่อแสดงการเชื่อมต่อสำเร็จแล้วก็สามารถใช้งานได้ตามปกติ

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) สุดท้ายคลิก【@】เลือกโมเดล DeepSeek R1 ที่เพิ่งเพิ่มภายใต้ผู้ให้บริการ PPIO เพื่อเริ่มการสนทนา\~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【เนื้อหาบางส่วนจาก: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. บทเรียนวิดีโอการใช้ PPIO × Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

หากคุณต้องการเรียนรู้ด้วยภาพ เรามีบทเรียนวิดีโอบน Bilibili ผ่านการสอนทีละขั้นตอน ช่วยให้คุณเชี่ยวชาญวิธีการตั้งค่า "PPIO API + Cherry Studio" ได้อย่างรวดเร็ว คลิกลิงก์ด้านล่างเพื่อดูวิดีโอโดยตรงและเริ่มประสบการณ์การพัฒนาที่ลื่นไหล → [《【ยังหัวร้อนกับ DeepSeek ที่โหลดไม่ขึ้นหรือเปล่า?】PPIO Cloud + DeepSeek เวอร์ชันเต็ม =? ไม่ติดขัดอีกต่อไป，พร้อมใช้ทันที》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【แหล่งที่มาวิดีโอ: sola】