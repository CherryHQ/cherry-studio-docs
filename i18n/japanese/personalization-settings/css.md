---
icon: file-code
---
# カスタムCSS


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




カスタム CSS を使用してソフトウェアの外観を変更し、自分の好みに合わせることができます。例：

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>カスタム CSS</p></figcaption></figure>

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

/* 深い思考展開時のフォント色 */
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
  /* カラー設定 */
  --color-background: #2b2b2b; /* ダーク背景色 */
  --color-background-soft: #303030; /* ソフト背景色 */
  --color-background-mute: #282c34; /* ミュート背景色 */
  --navbar-background: var(-–color-black-soft); /* ナビゲーションバーの背景色 */
  --chat-background: var(–-color-black-soft); /* チャット背景色 */
  --chat-background-user: #323332; /* ユーザーのチャット背景色 */
  --chat-background-assistant: #2d2e2d; /* アシスタントのチャット背景色 */
}

/* ダークテーマ固有のスタイル */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* コンテンツコンテナの背景色 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* メッセージ背景色 */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* 入力バーの背景色 */
    border: 1px solid #5e5d5940; /* 入力バーのボーダー色 */
    border-radius: 8px; /* 入力バーの角丸 */
  }

  /* コードスタイル */
  code {
    background-color: #e5e5e20d; /* コード背景色 */
    color: #ea928a; /* コード文字色 */
  }

  pre code {
    color: #abb2bf; /* プリフォーマットコード文字色 */
  }
}

/* ライトテーマ */
body[theme-mode="light"] {
  /* カラー設定 */
  --color-white: #ffffff; /* 白色 */
  --color-background: #ebe8e2; /* ライト背景色 */
  --color-background-soft: #cbc7be; /* ソフト背景色 */
  --color-background-mute: #e4e1d7; /* ミュート背景色 */
  --navbar-background: var(-–color-white-soft); /* ナビゲーションバーの背景色 */
  --chat-background: var(-–color-white-soft); /* チャット背景色 */
  --chat-background-user: #f8f7f2; /* ユーザーのチャット背景色 */
  --chat-background-assistant: #f6f4ec; /* アシスタントのチャット背景色 */
}

/* ライトテーマ固有のスタイル */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* コンコンテンンツコンコンテナの背景色 */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* メッセージ背景色 */
  }

  .inputbar-container {
    background-color: #ffffff; /* 入力バーの背景色 */
    border: 1px solid #87867f40; /* 入力バーのボーーダー色 */
    border-radius: 8px; /* 入力バーの角丸（好みのサイズに変更可） */
  }

  /* コードスタイル */
  code {
    background-color: #3d39290d; /* コード背景色 */
    color: #7c1b13; /* コード文字色 */
  }

  pre code {
    color: #000000; /* プリフォーマットコード文字色 */
  }
}
```

その他のテーマ変数については、ソースコードを参照してください：[https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### 関連のおすすめ

Cherry Studio テーマライブラリ: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

中国風のCherry Studioテーマスキンのいくつかを共有: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)