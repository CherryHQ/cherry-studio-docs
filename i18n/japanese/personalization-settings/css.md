---
icon: file-code
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# カスタムCSS

カスタムCSSを使用すると、ソフトウェアの外観を好みに合わせて変更できます。例：

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>カスタムCSS</p></figcaption></figure>

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

### 組み込み変数

```css
:root {
  font-family: "汉仪唐美人" !important; /* フォント */
}

/* 深層思考展開時のフォント色 */
.ant-collapse-content-box .markdown {
  color: red;
}

/* テーマ変数 */
:root {
  --color-black-soft: #2a2b2a; /* ダーク背景色 */
  --color-white-soft: #f8f7f2; /* ライト背景色 */
}

/* ダークテーマ */
body[theme-mode="dark"] {
  /* カラー */
  --color-background: #2b2b2b; /* ダーク背景色 */
  --color-background-soft: #303030; /* ライト背景色 */
  --color-background-mute: #282c34; /* ニュートラル背景色 */
  --navbar-background: var(-–color-black-soft); /* ナビゲーションバー背景色 */
  --chat-background: var(–-color-black-soft); /* チャット背景色 */
  --chat-background-user: #323332; /* ユーザーチャット背景色 */
  --chat-background-assistant: #2d2e2d; /* アシスタントチャット背景色 */
}

/* ダークテーマ固有スタイル */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* コンテンツコンテナ背景色 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* メッセージ背景色 */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* 入力バー背景色 */
    border: 1px solid #5e5d5940; /* 入力バー枠線色 */
    border-radius: 8px; /* 入力バー角丸 */
  }

  /* コードスタイル */
  code {
    background-color: #e5e5e20d; /* コード背景色 */
    color: #ea928a; /* コード文字色 */
  }

  pre code {
    color: #abb2bf; /* 整形済みコード文字色 */
  }
}

/* ライトテーマ */
body[theme-mode="light"] {
  /* カラー */
  --color-white: #ffffff; /* ホワイト */
  --color-background: #ebe8e2; /* ライト背景色 */
  --color-background-soft: #cbc7be; /* ライト背景色 */
  --color-background-mute: #e4e1d7; /* ニュートラル背景色 */
  --navbar-background: var(-–color-white-soft); /* ナビゲーションバー背景色 */
  --chat-background: var(-–color-white-soft); /* チャット背景色 */
  --chat-background-user: #f8f7f2; /* ユーザーチャット背景色 */
  --chat-background-assistant: #f6f4ec; /* アシスタントチャット背景色 */
}

/* ライトテーマ固有スタイル */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* コンテンツコンテナ背景色 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* メッセージ背景色 */
  }

  .inputbar-container {
    background-color: #ffffff; /* 入力バー背景色 */
    border: 1px solid #87867f40; /* 入力バー枠線色 */
    border-radius: 8px; /* 入力バー角丸 */
  }

  /* コードスタイル */
  code {
    background-color: #3d39290d; /* コード背景色 */
    color: #7c1b13; /* コード文字色 */
  }

  pre code {
    color: #000000; /* 整形済みコード文字色 */
  }
}
```

その他のテーマ変数はソースコードを参照: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### 関連リソース

Cherry Studio テーマライブラリ: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

中華風Cherry Studioテーマスキン例: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)