---
icon: file-code
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# CSS กำหนดเอง

ด้วย CSS กำหนดเอง คุณสามารถปรับเปลี่ยนรูปลักษณ์ของซอฟต์แวร์ให้ตรงกับความชอบของคุณมากขึ้น ตัวอย่างเช่น:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>CSS กำหนดเอง</p></figcaption></figure>

```css
:root {
  --color-background: #1a462788;
  --color-background-soft: #1a4627aa;
  --color-background-mute: #1a462766;
  --navbar-background: #1a4627;
  --chat-background: #1a4627;
  --chat-background-user: #28b561;
  --chat-background-assistant: #1a462722;
}

#content-container {
  background-color: #2e5d3a !important;
}
```

### ตัวแปรภายใน

```css
:root {
  font-family: "汉仪唐美人" !important; /* แบบอักษร */
}

/* สีแบบอักษรเมื่อเปิดการคิดลึก */
.ant-collapse-content-box .markdown {
  color: red;
}

/* ตัวแปรธีม */
:root {
  --color-black-soft: #2a2b2a; /* สีพื้นหลังโทนมืด */
  --color-white-soft: #f8f7f2; /* สีพื้นหลังโทนอ่อน */
}

/* โหมดธีมมืด */
body[theme-mode="dark"] {
  /* สีต่างๆ */
  --color-background: #2b2b2b; /* สีพื้นหลังโทนมืด */
  --color-background-soft: #303030; /* สีพื้นหลังโทนอ่อน */
  --color-background-mute: #282c34; /* สีพื้นหลังกลาง */
  --navbar-background: var(-–color-black-soft); /* สีพื้นหลังแถบนำทาง */
  --chat-background: var(–-color-black-soft); /* สีพื้นหลังแชท */
  --chat-background-user: #323332; /* สีพื้นหลังข้อความผู้ใช้ */
  --chat-background-assistant: #2d2e2d; /* สีพื้นหลังข้อความผู้ช่วย */
}

/* สไตล์เฉพาะธีมมืด */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* สีพื้นหลังพื้นที่เนื้อหา */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* สีพื้นหลังข้อความ */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* สีพื้นหลังช่องป้อนข้อความ */
    border: 1px solid #5e5d5940; /* สีขอบช่องป้อนข้อความ */
    border-radius: 8px; /* ความโค้งมนของขอบ */
  }

  /* สไตล์โค้ด */
  code {
    background-color: #e5e5e20d; /* สีพื้นหลังโค้ด */
    color: #ea928a; /* สีตัวอักษรโค้ด */
  }

  pre code {
    color: #abb2bf; /* สีตัวอักษรโค้ดแบบมีรูปแบบ */
  }
}

/* โหมดธีมสว่าง */
body[theme-mode="light"] {
  /* สีต่างๆ */
  --color-white: #ffffff; /* สีขาว */
  --color-background: #ebe8e2; /* สีพื้นหลังโทนมืด */
  --color-background-soft: #cbc7be; /* สีพื้นหลังโทนอ่อน */
  --color-background-mute: #e4e1d7; /* สีพื้นหลังกลาง */
  --navbar-background: var(-–color-white-soft); /* สีพื้นหลังแถบนำทาง */
  --chat-background: var(-–color-white-soft); /* สีพื้นหลังแชท */
  --chat-background-user: #f8f7f2; /* สีพื้นหลังข้อความผู้ใช้ */
  --chat-background-assistant: #f6f4ec; /* สีพื้นหลังข้อความผู้ช่วย */
}

/* สไตล์เฉพาะธีมสว่าง */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* สีพื้นหลังพื้นที่เนื้อหา */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* สีพื้นหลังข้อความ */
  }

  .inputbar-container {
    background-color: #ffffff; /* สีพื้นหลังช่องป้อนข้อความ */
    border: 1px solid #87867f40; /* สีขอบช่องป้อนข้อความ */
    border-radius: 8px; /* ความโค้งมนของขอบ แก้ไขเป็นขนาดที่คุณชอบ */
  }

  /* สไตล์โค้ด */
  code {
    background-color: #3d39290d; /* สีพื้นหลังโค้ด */
    color: #7c1b13; /* สีตัวอักษรโค้ด */
  }

  pre code {
    color: #000000; /* สีตัวอักษรโค้ดแบบมีรูปแบบ */
  }
}
```

สำหรับตัวแปรธีมเพิ่มเติม โปรดดูที่ซอร์สโค้ด: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### คำแนะนำที่เกี่ยวข้อง

คลังธีม Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

แบ่งปันสกินธีม Cherry Studio แบบจีน: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)