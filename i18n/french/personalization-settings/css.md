---
icon: file-code
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# CSS personnalisé

En personnalisant le CSS, vous pouvez modifier l'apparence du logiciel pour qu'elle corresponde mieux à vos préférences, par exemple comme ceci :

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>CSS personnalisé</p></figcaption></figure>

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

### Variables intégrées

```css
:root {
  font-family: "汉仪唐美人" !important; /* police de caractères */
}

/* Couleur du texte en mode réflexion approfondie */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Variables de thème */
:root {
  --color-black-soft: #2a2b2a; /* couleur de fond sombre */
  --color-white-soft: #f8f7f2; /* couleur de fond claire */
}

/* Thème sombre */
body[theme-mode="dark"] {
  /* Couleurs */
  --color-background: #2b2b2b; /* couleur de fond sombre */
  --color-background-soft: #303030; /* couleur de fond claire */
  --color-background-mute: #282c34; /* couleur de fond neutre */
  --navbar-background: var(-–color-black-soft); /* couleur de fond de la barre de navigation */
  --chat-background: var(–-color-black-soft); /* couleur de fond du chat */
  --chat-background-user: #323332; /* couleur de fond des messages utilisateur */
  --chat-background-assistant: #2d2e2d; /* couleur de fond des messages de l'assistant */
}

/* Styles spécifiques au thème sombre */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* couleur de fond du conteneur */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* couleur de fond des messages */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* couleur de fond de la zone de saisie */
    border: 1px solid #5e5d5940; /* couleur de bordure de la zone de saisie */
    border-radius: 8px; /* rayon de bordure de la zone de saisie */
  }

  /* Styles de code */
  code {
    background-color: #e5e5e20d; /* couleur de fond du code */
    color: #ea928a; /* couleur du texte du code */
  }

  pre code {
    color: #abb2bf; /* couleur du texte du code préformaté */
  }
}

/* Thème clair */
body[theme-mode="light"] {
  /* Couleurs */
  --color-white: #ffffff; /* blanc */
  --color-background: #ebe8e2; /* couleur de fond claire */
  --color-background-soft: #cbc7be; /* couleur de fond claire */
  --color-background-mute: #e4e1d7; /* couleur de fond neutre */
  --navbar-background: var(-–color-white-soft); /* couleur de fond de la barre de navigation */
  --chat-background: var(-–color-white-soft); /* couleur de fond du chat */
  --chat-background-user: #f8f7f2; /* couleur de fond des messages utilisateur */
  --chat-background-assistant: #f6f4ec; /* couleur de fond des messages de l'assistant */
}

/* Styles spécifiques au thème clair */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* couleur de fond du conteneur */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* couleur de fond des messages */
  }

  .inputbar-container {
    background-color: #ffffff; /* couleur de fond de la zone de saisie */
    border: 1px solid #87867f40; /* couleur de bordure de la zone de saisie */
    border-radius: 8px; /* rayon de bordure de la zone de saisie (ajustez à votre convenance) */
  }

  /* Styles de code */
  code {
    background-color: #3d39290d; /* couleur de fond du code */
    color: #7c1b13; /* couleur du texte du code */
  }

  pre code {
    color: #000000; /* couleur du texte du code préformaté */
  }
}
```

Pour plus de variables de thème, consultez le code source : [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Recommandations connexes

Bibliothèque de thèmes Cherry Studio : [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Partage de thèmes Cherry Studio de style chinois : [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)