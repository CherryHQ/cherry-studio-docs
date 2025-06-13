---
icon: file-code
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# CSS Personalizzati

Con il CSS personalizzato puoi modificare l'aspetto del software per adattarlo meglio ai tuoi gusti, ad esempio così:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>CSS Personalizzati</p></figcaption></figure>

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

### Variabili incorporate

```css
:root {
  font-family: "汉仪唐美人" !important; /* Carattere */
}

/* Colore del carattere per il pensiero approfondito */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Variabili del tema */
:root {
  --color-black-soft: #2a2b2a; /* Colore di sfondo scuro */
  --color-white-soft: #f8f7f2; /* Colore di sfondo chiaro */
}

/* Tema scuro */
body[theme-mode="dark"] {
  /* Colori */
  --color-background: #2b2b2b; /* Colore di sfondo scuro */
  --color-background-soft: #303030; /* Colore di sfondo chiaro */
  --color-background-mute: #282c34; /* Colore di sfondo neutro */
  --navbar-background: var(-–color-black-soft); /* Colore di sfondo navbar */
  --chat-background: var(–-color-black-soft); /* Colore di sfondo chat */
  --chat-background-user: #323332; /* Colore di sfondo messaggi utente */
  --chat-background-assistant: #2d2e2d; /* Colore di sfondo messaggi assistente */
}

/* Stili specifici tema scuro */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Colore di sfondo contenitore */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Colore di sfondo messaggi */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Colore di sfondo barra input */
    border: 1px solid #5e5d5940; /* Colore bordo barra input */
    border-radius: 8px; /* Raggio angoli barra input */
  }

  /* Stile codice */
  code {
    background-color: #e5e5e20d; /* Colore di sfondo codice */
    color: #ea928a; /* Colore testo codice */
  }

  pre code {
    color: #abb2bf; /* Colore testo codice preformattato */
  }
}

/* Tema chiaro */
body[theme-mode="light"] {
  /* Colori */
  --color-white: #ffffff; /* Bianco */
  --color-background: #ebe8e2; /* Colore di sfondo chiaro */
  --color-background-soft: #cbc7be; /* Colore di sfondo chiaro */
  --color-background-mute: #e4e1d7; /* Colore di sfondo neutro */
  --navbar-background: var(-–color-white-soft); /* Colore di sfondo navbar */
  --chat-background: var(-–color-white-soft); /* Colore di sfondo chat */
  --chat-background-user: #f8f7f2; /* Colore di sfondo messaggi utente */
  --chat-background-assistant: #f6f4ec; /* Colore di sfondo messaggi assistente */
}

/* Stili specifici tema chiaro */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Colore di sfondo contenitore */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Colore di sfondo messaggi */
  }

  .inputbar-container {
    background-color: #ffffff; /* Colore di sfondo barra input */
    border: 1px solid #87867f40; /* Colore bordo barra input */
    border-radius: 8px; /* Raggio angoli barra input (modificare a piacere) */
  }

  /* Stile codice */
  code {
    background-color: #3d39290d; /* Colore di sfondo codice */
    color: #7c1b13; /* Colore testo codice */
  }

  pre code {
    color: #000000; /* Colore testo codice preformattato */
  }
}
```

Per altre variabili del tema consulta il codice sorgente: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Consigli correlati

Libreria temi Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Condividi temi Cherry Studio in stile cinese: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)