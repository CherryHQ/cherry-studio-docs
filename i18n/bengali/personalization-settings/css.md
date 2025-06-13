---
icon: file-code
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# কাস্টম CSS

কাস্টম CSS-এর মাধ্যমে সফ্টওয়্যারটির লুক কাস্টমাইজ করে নিজের পছন্দমতো সাজানো যায়, যেমন:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>কাস্টম CSS</p></figcaption></figure>

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

### বিল্ট-ইন ভ্যারিয়েবল

```css
:root {
  font-family: "汉仪唐美人" !important; /* ফন্ট */
}

/* গভীর চিন্তা সম্প্রসারণের টেক্সট কালার */
.ant-collapse-content-box .markdown {
  color: red;
}

/* থিম ভ্যারিয়েবল */
:root {
  --color-black-soft: #2a2b2a; /* ডার্ক ব্যাকগ্রাউন্ড কালার */
  --color-white-soft: #f8f7f2; /* লাইট ব্যাকগ্রাউন্ড কালার */
}

/* ডার্ক থিম */
body[theme-mode="dark"] {
  /* কালার */
  --color-background: #2b2b2b; /* ডার্ক ব্যাকগ্রাউন্ড কালার */
  --color-background-soft: #303030; /* হালকা কালার ব্যাকগ্রাউন্ড */
  --color-background-mute: #282c34; /* নিউট্রাল ব্যাকগ্রাউন্ড কালার */
  --navbar-background: var(-–color-black-soft); /* ন্যাভবার ব্যাকগ্রাউন্ড কালার */
  --chat-background: var(–-color-black-soft); /* চ্যাট ব্যাকগ্রাউন্ড কালার */
  --chat-background-user: #323332; /* ইউজার চ্যাট ব্যাকগ্রাউন্ড কালার */
  --chat-background-assistant: #2d2e2d; /* সহকারী চ্যাট ব্যাকগ্রাউন্ড কালার */
}

/* ডার্ক থিম স্পেসিফিক স্টাইল */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* কন্টেইনার ব্যাকগ্রাউন্ড কালার */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* মেসেজ ব্যাকগ্রাউন্ড কালার */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* ইনপুট ফিল্ড ব্যাকগ্রাউন্ড কালার */
    border: 1px solid #5e5d5940; /* ইনপুট ফিল্ড বর্ডার কালার */
    border-radius: 8px; /* ইনপুট ফিল্ড বর্ডার রেডিয়াস */
  }

  /* কোড স্টাইল */
  code {
    background-color: #e5e5e20d; /* কোড ব্যাকগ্রাউন্ড কালার */
    color: #ea928a; /* কোড টেক্সট কালার */
  }

  pre code {
    color: #abb2bf; /* প্রিফরম্যাটেড কোড টেক্সট কালার */
  }
}

/* লাইট থিম */
body[theme-mode="light"] {
  /* কালার */
  --color-white: #ffffff; /* সাদা */
  --color-background: #ebe8e2; /* হালকা ব্যাকগ্রাউন্ড কালার */
  --color-background-soft: #cbc7be; /* হালকা ব্যাকগ্রাউন্ড কালার */
  --color-background-mute: #e4e1d7; /* নিউট্রাল ব্যাকগ্রাউন্ড কালার */
  --navbar-background: var(-–color-white-soft); /* ন্যাভবার ব্যাকগ্রাউন্ড কালার */
  --chat-background: var(-–color-white-soft); /* চ্যাট ব্যাকগ্রাউন্ড কালার */
  --chat-background-user: #f8f7f2; /* ইউজার চ্যাট ব্যাকগ্রাউন্ড কালার */
  --chat-background-assistant: #f6f4ec; /* সহকারী চ্যাট ব্যাকগ্রাউন্ড কালার */
}

/* লাইট থিম স্পেসিফিক স্টাইল */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* কন্টেইনার ব্যাকগ্রাউন্ড কালার */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* মেসেজ ব্যাকগ্রাউন্ড কালার */
  }

  .inputbar-container {
    background-color: #ffffff; /* ইনপুট ফিল্ড ব্যাকগ্রাউন্ড কালার */
    border: 1px solid #87867f40; /* ইনপুট ফিল্ড বর্ডার কালার */
    border-radius: 8px; /* ইনপুট ফিল্ড বর্ডার রেডিয়াস */
  }

  /* কোড স্টাইল */
  code {
    background-color: #3d39290d; /* কোড ব্যাকগ্রাউন্ড কালার */
    color: #7c1b13; /* কোড টেক্সট কালার */
  }

  pre code {
    color: #000000; /* প্রিফরম্যাটেড কোড টেক্সট কালার */
  }
}
```

আরও থিম ভ্যারিয়েবল দেখতে সোর্স কোড রেফারেন্স করুন: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### সম্পর্কিত সুপারিশ

Cherry Studio থিম লাইব্রেরি: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

কিছু চাইনিজ-স্টাইলের Cherry Studio থিম শেয়ার করা হয়েছে: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)