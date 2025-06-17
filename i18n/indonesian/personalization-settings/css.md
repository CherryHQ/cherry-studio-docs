---
icon: file-code
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# CSS Kustom

Dengan CSS kustom, Anda dapat mengubah tampilan perangkat lunak agar lebih sesuai dengan preferensi pribadi, contohnya seperti ini:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>CSS Kustom</p></figcaption></figure>

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

### Variabel Bawaan

```css
:root {
  font-family: "汉仪唐美人" !important; /* font */
}

/* Warna teks saat ekspansi pemikiran mendalam */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Variabel tema */
:root {
  --color-black-soft: #2a2b2a; /* Warna latar belakang gelap */
  --color-white-soft: #f8f7f2; /* Warna latar belakang terang */
}

/* Tema gelap */
body[theme-mode="dark"] {
  /* Warna */
  --color-background: #2b2b2b; /* Warna latar belakang gelap */
  --color-background-soft: #303030; /* Warna latar belakang terang */
  --color-background-mute: #282c34; /* Warna latar belakang netral */
  --navbar-background: var(-–color-black-soft); /* Warna latar belakang navbar */
  --chat-background: var(–-color-black-soft); /* Warna latar belakang chat */
  --chat-background-user: #323332; /* Warna latar belakang chat pengguna */
  --chat-background-assistant: #2d2e2d; /* Warna latar belakang chat asisten */
}

/* Gaya khusus tema gelap */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Warna latar belakang kontainer konten */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Warna latar belakang pesan */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Warna latar belakang input */
    border: 1px solid #5e5d5940; /* Warna border input */
    border-radius: 8px; /* Ukuran sudut border input */
  }

  /* Gaya kode */
  code {
    background-color: #e5e5e20d; /* Warna latar belakang kode */
    color: #ea928a; /* Warna teks kode */
  }

  pre code {
    color: #abb2bf; /* Warna teks kode praformat */
  }
}

/* Tema terang */
body[theme-mode="light"] {
  /* Warna */
  --color-white: #ffffff; /* Putih */
  --color-background: #ebe8e2; /* Warna latar belakang terang */
  --color-background-soft: #cbc7be; /* Warna latar belakang terang */
  --color-background-mute: #e4e1d7; /* Warna latar belakang netral */
  --navbar-background: var(-–color-white-soft); /* Warna latar belakang navbar */
  --chat-background: var(-–color-white-soft); /* Warna latar belakang chat */
  --chat-background-user: #f8f7f2; /* Warna latar belakang chat pengguna */
  --chat-background-assistant: #f6f4ec; /* Warna latar belakang chat asisten */
}

/* Gaya khusus tema terang */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Warna latar belakang kontainer konten */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Warna latar belakang pesan */
  }

  .inputbar-container {
    background-color: #ffffff; /* Warna latar belakang input */
    border: 1px solid #87867f40; /* Warna border input */
    border-radius: 8px; /* Ukuran sudut border input, ubah sesuai preferensi */
  }

  /* Gaya kode */
  code {
    background-color: #3d39290d; /* Warna latar belakang kode */
    color: #7c1b13; /* Warna teks kode */
  }

  pre code {
    color: #000000; /* Warna teks kode praformat */
  }
}
```

Untuk lebih banyak variabel tema, lihat kode sumber: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Rekomendasi Terkait

Pustaka Tema Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Bagikan beberapa skin tema Cherry Studio bergaya Tiongkok: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)