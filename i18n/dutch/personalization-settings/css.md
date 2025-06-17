---
icon: file-code
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Aangepaste CSS

Met aangepaste CSS kunt u het uiterlijk van de software aanpassen om beter aan uw voorkeuren te voldoen, bijvoorbeeld:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>Aangepaste CSS</p></figcaption></figure>

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

### Ingebouwde variabelen

```css
:root {
  font-family: "汉仪唐美人" !important; /* lettertype */
}

/* Kleur van uitgevouwen DeepThought-tekst */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Thema variabelen */
:root {
  --color-black-soft: #2a2b2a; /* donkere achtergrondkleur */
  --color-white-soft: #f8f7f2; /* lichte achtergrondkleur */
}

/* Donker thema */
body[theme-mode="dark"] {
  /* Kleuren */
  --color-background: #2b2b2b; /* donkere achtergrondkleur */
  --color-background-soft: #303030; /* lichte achtergrondkleur */
  --color-background-mute: #282c34; /* neutrale achtergrondkleur */
  --navbar-background: var(-–color-black-soft); /* navigatiebalkachtergrondkleur */
  --chat-background: var(–-color-black-soft); /* chatachtergrondkleur */
  --chat-background-user: #323332; /* gebruikerschatachtergrondkleur */
  --chat-background-assistant: #2d2e2d; /* assistent-chatachtergrondkleur */
}

/* Specifieke stijlen voor donker thema */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* inhoudcontainer achtergrondkleur */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* berichtenachtergrondkleur */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* invoerbalkachtergrondkleur */
    border: 1px solid #5e5d5940; /* invoerbalkrandkleur */
    border-radius: 8px; /* invoerbalkrandafronding */
  }

  /* Codestijl */
  code {
    background-color: #e5e5e20d; /* code-achtergrondkleur */
    color: #ea928a; /* codetekstkleur */
  }

  pre code {
    color: #abb2bf; /* voorgeformatteerde codetekstkleur */
  }
}

/* Licht thema */
body[theme-mode="light"] {
  /* Kleuren */
  --color-white: #ffffff; /* wit */
  --color-background: #ebe8e2; /* lichte achtergrondkleur */
  --color-background-soft: #cbc7be; /* lichte achtergrondkleur */
  --color-background-mute: #e4e1d7; /* neutrale achtergrondkleur */
  --navbar-background: var(-–color-white-soft); /* navigatiebalkachtergrondkleur */
  --chat-background: var(-–color-white-soft); /* chatachtergrondkleur */
  --chat-background-user: #f8f7f2; /* gebruikerschatachtergrondkleur */
  --chat-background-assistant: #f6f4ec; /* assistent-chatachtergrondkleur */
}

/* Specifieke stijlen voor licht thema */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* inhoudcontainer achtergrondkleur */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* berichtenachtergrondkleur */
  }

  .inputbar-container {
    background-color: #ffffff; /* invoerbalkachtergrondkleur */
    border: 1px solid #87867f40; /* invoerbalkrandkleur */
    border-radius: 8px; /* invoerbalkrandafronding, pas aan naar uw voorkeur */
  }

  /* Codestijl */
  code {
    background-color: #3d39290d; /* code-achtergrondkleur */
    color: #7c1b13; /* codetekstkleur */
  }

  pre code {
    color: #000000; /* voorgeformatteerde codetekstkleur */
  }
}
```

Raadpleeg de broncode voor meer themavariabelen: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Gerelateerde aanbevelingen

Cherry Studio Thema-collectie: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Deel enkele Chinese stijl Cherry Studio thema's: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)