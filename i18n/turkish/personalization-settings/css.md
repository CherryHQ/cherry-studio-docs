---
icon: file-code
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Özel CSS

Özel CSS ile yazılımın görünümünü kendi zevkinize göre düzenleyebilirsiniz, örneğin:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>Özel CSS</p></figcaption></figure>

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

### Yerleşik Değişkenler

```css
:root {
  font-family: "汉仪唐美人" !important; /* Yazı tipi */
}

/* Derin düşünme genişletme metin rengi */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Tema değişkenleri */
:root {
  --color-black-soft: #2a2b2a; /* Koyu arkaplan rengi */
  --color-white-soft: #f8f7f2; /* Açık arkaplan rengi */
}

/* Koyu tema */
body[theme-mode="dark"] {
  /* Renkler */
  --color-background: #2b2b2b; /* Koyu arkaplan rengi */
  --color-background-soft: #303030; /* Açık arkaplan rengi */
  --color-background-mute: #282c34; /* Nötr arkaplan rengi */
  --navbar-background: var(-–color-black-soft); /* Navigasyon çubuğu arkaplanı */
  --chat-background: var(–-color-black-soft); /* Sohbet arkaplanı */
  --chat-background-user: #323332; /* Kullanıcı sohbet arkaplanı */
  --chat-background-assistant: #2d2e2d; /* Asistan sohbet arkaplanı */
}

/* Koyu tema özel stilleri */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* İçerik konteyneri arkaplanı */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Mesaj arkaplanı */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Giriş çubuğu arkaplanı */
    border: 1px solid #5e5d5940; /* Giriş çubuğu kenarlık rengi */
    border-radius: 8px; /* Giriş çubuğu köşe yuvarlaklığı */
  }

  /* Kod stili */
  code {
    background-color: #e5e5e20d; /* Kod arkaplan rengi */
    color: #ea928a; /* Kod metin rengi */
  }

  pre code {
    color: #abb2bf; /* Ön biçimlendirilmiş kod metin rengi */
  }
}

/* Açık tema */
body[theme-mode="light"] {
  /* Renkler */
  --color-white: #ffffff; /* Beyaz */
  --color-background: #ebe8e2; /* Açık arkaplan rengi */
  --color-background-soft: #cbc7be; /* Açık arkaplan rengi */
  --color-background-mute: #e4e1d7; /* Nötr arkaplan rengi */
  --navbar-background: var(-–color-white-soft); /* Navigasyon çubuğu arkaplanı */
  --chat-background: var(-–color-white-soft); /* Sohbet arkaplanı */
  --chat-background-user: #f8f7f2; /* Kullanıcı sohbet arkaplanı */
  --chat-background-assistant: #f6f4ec; /* Asistan sohbet arkaplanı */
}

/* Açık tema özel stilleri */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* İçerik konteyneri arkaplanı */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Mesaj arkaplanı */
  }

  .inputbar-container {
    background-color: #ffffff; /* Giriş çubuğu arkaplanı */
    border: 1px solid #87867f40; /* Giriş çubuğu kenarlık rengi */
    border-radius: 8px; /* Giriş çubuğu köşe yuvarlaklığı (istediğiniz boyuta ayarlayın) */
  }

  /* Kod stili */
  code {
    background-color: #3d39290d; /* Kod arkaplan rengi */
    color: #7c1b13; /* Kod metin rengi */
  }

  pre code {
    color: #000000; /* Ön biçimlendirilmiş kod metin rengi */
  }
}
```

Daha fazla tema değişkeni için kaynak koda bakın: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### İlgili Öneriler

Cherry Studio Tema Kütüphanesi: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Bazı Çin tarzı Cherry Studio tema derilerini paylaş: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)