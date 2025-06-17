---
icon: file-code
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 自訂CSS

通過自訂 CSS 可以修改軟體的外觀更加符合自己的喜好，例如這樣：

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>自訂 CSS</p></figcaption></figure>

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

### 內建變數

```css
:root {
  font-family: "汉仪唐美人" !important; /* 字體 */
}

/* 深度思考展開字體顏色 */
.ant-collapse-content-box .markdown {
  color: red;
}

/* 主題變數 */
:root {
  --color-black-soft: #2a2b2a; /* 深色背景色 */
  --color-white-soft: #f8f7f2; /* 淺色背景色 */
}

/* 深色主題 */
body[theme-mode="dark"] {
  /* Colors */
  --color-background: #2b2b2b; /* 深色背景色 */
  --color-background-soft: #303030; /* 淺色背景色 */
  --color-background-mute: #282c34; /* 中性背景色 */
  --navbar-background: var(-–color-black-soft); /* 導覽欄背景色 */
  --chat-background: var(–-color-black-soft); /* 聊天背景色 */
  --chat-background-user: #323332; /* 用戶聊天背景色 */
  --chat-background-assistant: #2d2e2d; /* 助手聊天背景色 */
}

/* 深色主題特定樣式 */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* 內容容器背景色 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* 訊息背景色 */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* 輸入框背景色 */
    border: 1px solid #5e5d5940; /* 輸入框邊框顏色 */
    border-radius: 8px; /* 輸入框邊框圓角 */
  }

  /* 代碼樣式 */
  code {
    background-color: #e5e5e20d; /* 代碼背景色 */
    color: #ea928a; /* 代碼文字顏色 */
  }

  pre code {
    color: #abb2bf; /* 預格式化代碼文字顏色 */
  }
}

/* 淺色主題 */
body[theme-mode="light"] {
  /* Colors */
  --color-white: #ffffff; /* 白色 */
  --color-background: #ebe8e2; /* 淺色背景色 */
  --color-background-soft: #cbc7be; /* 淺色背景色 */
  --color-background-mute: #e4e1d7; /* 中性背景色  */
  --navbar-background: var(-–color-white-soft); /* 導覽欄背景色 */
  --chat-background: var(-–color-white-soft); /* 聊天背景色 */
  --chat-background-user: #f8f7f2; /* 用戶聊天背景色 */
  --chat-background-assistant: #f6f4ec; /* 助手聊天背景色 */
}

/* 淺色主題特定樣式 */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* 內容容器背景色 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* 訊息背景色 */
  }

  .inputbar-container {
    background-color: #ffffff; /* 輸入框背景色 */
    border: 1px solid #87867f40; /* 輸入框邊框顏色 */
    border-radius: 8px; /* 輸入框邊框圓角，修改為您喜歡的大小 */
  }

  /* 代碼樣式 */
  code {
    background-color: #3d39290d; /* 代碼背景色 */
    color: #7c1b13; /* 代碼文字顏色 */
  }

  pre code {
    color: #000000; /* 預格式化代碼文字顏色 */
  }
}
```

更多主題變數請參考原始碼：[https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### 相關推薦

Cherry Studio 主題庫: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

分享一些中國風 Cherry Studio 主題皮膚: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)