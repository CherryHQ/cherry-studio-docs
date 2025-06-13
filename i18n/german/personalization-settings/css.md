---
icon: file-code
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Benutzerdefinierte CSS

Durch benutzerdefinierte CSS können Sie das Erscheinungsbild der Software an Ihre Vorlieben anpassen, wie zum Beispiel:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>Benutzerdefinierte CSS</p></figcaption></figure>

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

### Integrierte Variablen

```css
:root {
  font-family: "汉仪唐美人" !important; /* Schriftart */
}

/* Textfarbe für erweitertes Deep Thinking */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Designvariablen */
:root {
  --color-black-soft: #2a2b2a; /* Dunkler Hintergrund */
  --color-white-soft: #f8f7f2; /* Heller Hintergrund */
}

/* Dunkles Design */
body[theme-mode="dark"] {
  /* Farben */
  --color-background: #2b2b2b; /* Dunkler Hintergrund */
  --color-background-soft: #303030; /* Hellere Hintergrundfarbe */
  --color-background-mute: #282c34; /* Neutraler Hintergrund */
  --navbar-background: var(-–color-black-soft); /* Navigationsleistenhintergrund */
  --chat-background: var(–-color-black-soft); /* Chat-Hintergrund */
  --chat-background-user: #323332; /* Benutzer-Chat-Hintergrund */
  --chat-background-assistant: #2d2e2d; /* Assistenten-Chat-Hintergrund */
}

/* Dunkles Design-spezifische Stile */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Container-Hintergrund */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Nachrichten-Hintergrund */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Eingabefeld-Hintergrund */
    border: 1px solid #5e5d5940; /* Eingabefeld-Rahmenfarbe */
    border-radius: 8px; /* Eingabefeld-Rahmenradius */
  }

  /* Code-Stil */
  code {
    background-color: #e5e5e20d; /* Code-Hintergrund */
    color: #ea928a; /* Code-Textfarbe */
  }

  pre code {
    color: #abb2bf; /* Formatierter Code-Text */
  }
}

/* Helles Design */
body[theme-mode="light"] {
  /* Farben */
  --color-white: #ffffff; /* Weiß */
  --color-background: #ebe8e2; /* Heller Hintergrund */
  --color-background-soft: #cbc7be; /* Hellere Hintergrundfarbe */
  --color-background-mute: #e4e1d7; /* Neutraler Hintergrund  */
  --navbar-background: var(-–color-white-soft); /* Navigationsleistenhintergrund */
  --chat-background: var(-–color-white-soft); /* Chat-Hintergrund */
  --chat-background-user: #f8f7f2; /* Benutzer-Chat-Hintergrund */
  --chat-background-assistant: #f6f4ec; /* Assistenten-Chat-Hintergrund */
}

/* Helles Design-spezifische Stile */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Container-Hintergrund */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Nachrichten-Hintergrund */
  }

  .inputbar-container {
    background-color: #ffffff; /* Eingabefeld-Hintergrund */
    border: 1px solid #87867f40; /* Eingabefeld-Rahmenfarbe */
    border-radius: 8px; /* Eingabefeld-Rahmenradius */
  }

  /* Code-Stil */
  code {
    background-color: #3d39290d; /* Code-Hintergrund */
    color: #7c1b13; /* Code-Textfarbe */
  }

  pre code {
    color: #000000; /* Formatierter Code-Text */
  }
}
```

Weitere Designvariablen finden Sie im Quellcode: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Empfehlungen

Cherry Studio Designbibliothek: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Sammlung chinesisch inspirierter Cherry Studio Designs: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)