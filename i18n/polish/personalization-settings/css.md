---
icon: file-code
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

# Niestandardowy CSS

Poprzez niestandardowy CSS możesz zmodyfikować wygląd oprogramowania, aby lepiej odpowiadał Twoim preferencjom, na przykład w taki sposób:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>Niestandardowy CSS</p></figcaption></figure>

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

### Wbudowane zmienne

```css
:root {
  font-family: "汉仪唐美人" !important; /* czcionka */
}

/* Kolor czcionki rozwinięcia głębokiego myślenia */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Zmienne motywu */
:root {
  --color-black-soft: #2a2b2a; /* kolor tła ciemnego */
  --color-white-soft: #f8f7f2; /* kolor tła jasnego */
}

/* Motyw ciemny */
body[theme-mode="dark"] {
  /* Kolory */
  --color-background: #2b2b2b; /* kolor tła ciemnego */
  --color-background-soft: #303030; /* kolor tła jasnego */
  --color-background-mute: #282c34; /* kolor tła neutralnego */
  --navbar-background: var(-–color-black-soft); /* kolor tła paska nawigacji */
  --chat-background: var(–-color-black-soft); /* kolor tła rozmów */
  --chat-background-user: #323332; /* tło wiadomości użytkownika */
  --chat-background-assistant: #2d2e2d; /* tło wiadomości asystenta */
}

/* Specyficzne style motywu ciemnego */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* kolor tła kontenera */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* kolor tła wiadomości */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* tło pola wprowadzania */
    border: 1px solid #5e5d5940; /* kolor obramowania pola wprowadzania */
    border-radius: 8px; /* zaokrąglenie rogów pola wprowadzania */
  }

  /* Styl kodu */
  code {
    background-color: #e5e5e20d; /* tło kodu */
    color: #ea928a; /* kolor tekstu kodu */
  }

  pre code {
    color: #abb2bf; /* kolor tekstu preformatowanego kodu */
  }
}

/* Motyw jasny */
body[theme-mode="light"] {
  /* Kolory */
  --color-white: #ffffff; /* kolor biały */
  --color-background: #ebe8e2; /* kolor tła jasnego */
  --color-background-soft: #cbc7be; /* kolor tła jasnego */
  --color-background-mute: #e4e1d7; /* kolor tła neutralnego */
  --navbar-background: var(-–color-white-soft); /* kolor tła paska nawigacji */
  --chat-background: var(-–color-white-soft); /* kolor tła rozmów */
  --chat-background-user: #f8f7f2; /* tło wiadomości użytkownika */
  --chat-background-assistant: #f6f4ec; /* tło wiadomości asystenta */
}

/* Specyficzne style motywu jasnego */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* kolor tła kontenera */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* kolor tła wiadomości */
  }

  .inputbar-container {
    background-color: #ffffff; /* tło pola wprowadzania */
    border: 1px solid #87867f40; /* kolor obramowania pola wprowadzania */
    border-radius: 8px; /* zaokrąglenie rogów pola wprowadzania */
  }

  /* Styl kodu */
  code {
    background-color: #3d39290d; /* tło kodu */
    color: #7c1b13; /* kolor tekstu kodu */
  }

  pre code {
    color: #000000; /* kolor tekstu preformatowanego kodu */
  }
}
```

Więcej zmiennych motywu znajdziesz w kodzie źródłowym: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Powiązane rekomendacje

Repozytorium motywów Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Podziel się skórami tematycznymi Cherry Studio w stylu chińskim: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)