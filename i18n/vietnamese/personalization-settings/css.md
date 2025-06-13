---
icon: file-code
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# CSS Tùy chỉnh

Bằng cách tùy chỉnh CSS, bạn có thể sửa đổi giao diện phần mềm theo sở thích cá nhân, ví dụ như sau:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>CSS tùy chỉnh</p></figcaption></figure>

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

### Biến tích hợp sẵn

```css
:root {
  font-family: "汉仪唐美人" !important; /* Phông chữ */
}

/* Màu chữ khi mở rộng Suy nghĩ sâu */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Biến chủ đề */
:root {
  --color-black-soft: #2a2b2a; /* Màu nền tối */
  --color-white-soft: #f8f7f2; /* Màu nền sáng */
}

/* Chủ đề tối */
body[theme-mode="dark"] {
  /* Màu sắc */
  --color-background: #2b2b2b; /* Màu nền tối */
  --color-background-soft: #303030; /* Màu nền sáng */
  --color-background-mute: #282c34; /* Màu nền trung tính */
  --navbar-background: var(-–color-black-soft); /* Màu nền thanh điều hướng */
  --chat-background: var(–-color-black-soft); /* Màu nền trò chuyện */
  --chat-background-user: #323332; /* Màu nền trò chuyện người dùng */
  --chat-background-assistant: #2d2e2d; /* Màu nền trò chuyện trợ lý */
}

/* Kiểu dáng riêng cho chủ đề tối */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Màu nền vùng chứa nội dung */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Màu nền tin nhắn */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Màu nền ô nhập */
    border: 1px solid #5e5d5940; /* Màu viền ô nhập */
    border-radius: 8px; /* Góc bo viền ô nhập */
  }

  /* Kiểu dáng code */
  code {
    background-color: #e5e5e20d; /* Màu nền code */
    color: #ea928a; /* Màu văn bản code */
  }

  pre code {
    color: #abb2bf; /* Màu văn bản code đã định dạng trước */
  }
}

/* Chủ đề sáng */
body[theme-mode="light"] {
  /* Màu sắc */
  --color-white: #ffffff; /* Màu trắng */
  --color-background: #ebe8e2; /* Màu nền sáng */
  --color-background-soft: #cbc7be; /* Màu nền sáng */
  --color-background-mute: #e4e1d7; /* Màu nền trung tính */
  --navbar-background: var(-–color-white-soft); /* Màu nền thanh điều hướng */
  --chat-background: var(-–color-white-soft); /* Màu nền trò chuyện */
  --chat-background-user: #f8f7f2; /* Màu nền trò chuyện người dùng */
  --chat-background-assistant: #f6f4ec; /* Màu nền trò chuyện trợ lý */
}

/* Kiểu dáng riêng cho chủ đề sáng */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Màu nền vùng chứa nội dung */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Màu nền tin nhắn */
  }

  .inputbar-container {
    background-color: #ffffff; /* Màu nền ô nhập */
    border: 1px solid #87867f40; /* Màu viền ô nhập */
    border-radius: 8px; /* Góc bo viền ô nhập, điều chỉnh theo sở thích */
  }

  /* Kiểu dáng code */
  code {
    background-color: #3d39290d; /* Màu nền code */
    color: #7c1b13; /* Màu văn bản code */
  }

  pre code {
    color: #000000; /* Màu văn bản code đã định dạng trước */
  }
}
```

Để biết thêm các biến chủ đề, vui lòng tham khảo mã nguồn: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Đề xuất liên quan

Thư viện chủ đề Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Chia sẻ một số theme Cherry Studio phong cách Trung Quốc: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)