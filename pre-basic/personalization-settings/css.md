---
icon: file-code
---

# 自定义 CSS

通过自定义 CSS 可以修改软件的外观更加符合自己的喜好，例如这样：

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y (1).jpg" alt=""><figcaption><p>自定义 CSS</p></figcaption></figure>

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

### 内置变量

```css
:root {
  font-family: "汉仪唐美人" !important; /* 字体 */
}

/* 深度思考展开字体颜色 */
.ant-collapse-content-box .markdown {
  color: red;
}

/* 主题变量 */
:root {
  --color-black-soft: #2a2b2a; /* 深色背景色 */
  --color-white-soft: #f8f7f2; /* 浅色背景色 */
}

/* 深色主题 */
body[theme-mode="dark"] {
  /* Colors */
  --color-background: #2b2b2b; /* 深色背景色 */
  --color-background-soft: #303030; /* 浅色背景色 */
  --color-background-mute: #282c34; /* 中性背景色 */
  --navbar-background: var(-–color-black-soft); /* 导航栏背景色 */
  --chat-background: var(–-color-black-soft); /* 聊天背景色 */
  --chat-background-user: #323332; /* 用户聊天背景色 */
  --chat-background-assistant: #2d2e2d; /* 助手聊天背景色 */
}

/* 深色主题特定样式 */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* 内容容器背景色 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* 消息背景色 */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* 输入框背景色 */
    border: 1px solid #5e5d5940; /* 输入框边框颜色 */
    border-radius: 8px; /* 输入框边框圆角 */
  }

  /* 代码样式 */
  code {
    background-color: #e5e5e20d; /* 代码背景色 */
    color: #ea928a; /* 代码文字颜色 */
  }

  pre code {
    color: #abb2bf; /* 预格式化代码文字颜色 */
  }
}

/* 浅色主题 */
body[theme-mode="light"] {
  /* Colors */
  --color-white: #ffffff; /* 白色 */
  --color-background: #ebe8e2; /* 浅色背景色 */
  --color-background-soft: #cbc7be; /* 浅色背景色 */
  --color-background-mute: #e4e1d7; /* 中性背景色  */
  --navbar-background: var(-–color-white-soft); /* 导航栏背景色 */
  --chat-background: var(-–color-white-soft); /* 聊天背景色 */
  --chat-background-user: #f8f7f2; /* 用户聊天背景色 */
  --chat-background-assistant: #f6f4ec; /* 助手聊天背景色 */
}

/* 浅色主题特定样式 */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* 内容容器背景色 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* 消息背景色 */
  }

  .inputbar-container {
    background-color: #ffffff; /* 输入框背景色 */
    border: 1px solid #87867f40; /* 输入框边框颜色 */
    border-radius: 8px; /* 输入框边框圆角，修改为您喜欢的大小 */
  }

  /* 代码样式 */
  code {
    background-color: #3d39290d; /* 代码背景色 */
    color: #7c1b13; /* 代码文字颜色 */
  }

  pre code {
    color: #000000; /* 预格式化代码文字颜色 */
  }
}
```

更多主题变量请参考源代码：[https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### 相关推荐

Cherry Studio 主题库: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

分享一些中国风 Cherry Studio 主题皮肤: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)
