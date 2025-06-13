---
icon: file-code
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Custom CSS

With custom CSS, you can modify the software's appearance to better suit your preferences, like this:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>Custom CSS</p></figcaption></figure>

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

### Built-in Variables

```css
:root {
  font-family: "HanYiTangMeiRen" !important; /* Font */
}

/* Font color for expanded deep thinking section */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Theme Variables */
:root {
  --color-black-soft: #2a2b2a; /* Dark background color */
  --color-white-soft: #f8f7f2; /* Light background color */
}

/* Dark Theme */
body[theme-mode="dark"] {
  /* Colors */
  --color-background: #2b2b2b; /* Dark background color */
  --color-background-soft: #303030; /* Light background color */
  --color-background-mute: #282c34; /* Neutral background color */
  --navbar-background: var(-–color-black-soft); /* Navbar background color */
  --chat-background: var(–-color-black-soft); /* Chat background color */
  --chat-background-user: #323332; /* User chat background color */
  --chat-background-assistant: #2d2e2d; /* Assistant chat background color */
}

/* Dark Theme Specific Styles */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Content container background color */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Messages background color */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Input bar background color */
    border: 1px solid #5e5d5940; /* Input bar border color */
    border-radius: 8px; /* Input bar border radius */
  }

  /* Code Style */
  code {
    background-color: #e5e5e20d; /* Code background color */
    color: #ea928a; /* Code text color */
  }

  pre code {
    color: #abb2bf; /* Preformatted code text color */
  }
}

/* Light Theme */
body[theme-mode="light"] {
  /* Colors */
  --color-white: #ffffff; /* White */
  --color-background: #ebe8e2; /* Light background color */
  --color-background-soft: #cbc7be; /* Light background color */
  --color-background-mute: #e4e1d7; /* Neutral background color  */
  --navbar-background: var(-–color-white-soft); /* Navbar background color */
  --chat-background: var(-–color-white-soft); /* Chat background color */
  --chat-background-user: #f8f7f2; /* User chat background color */
  --chat-background-assistant: #f6f4ec; /* Assistant chat background color */
}

/* Light Theme Specific Styles */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Content container background color */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Messages background color */
  }

  .inputbar-container {
    background-color: #ffffff; /* Input bar background color */
    border: 1px solid #87867f40; /* Input bar border color */
    border-radius: 8px; /* Input bar border radius, change to your preferred size */
  }

  /* Code Style */
  code {
    background-color: #3d39290d; /* Code background color */
    color: #7c1b13; /* Code text color */
  }

  pre code {
    color: #000000; /* Preformatted code text color */
  }
}
```

For more theme variables, please refer to the source code: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Related Recommendations

Cherry Studio Theme Library: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Share some Chinese-style Cherry Studio theme skins: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)