---
icon: file-code
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# CSS Personalizado

Con CSS personalizado, puedes modificar la apariencia del software para que se ajuste mejor a tus preferencias, por ejemplo:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>CSS personalizado</p></figcaption></figure>

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

### Variables integradas

```css
:root {
  font-family: "汉仪唐美人" !important; /* Fuente */
}

/* Color de texto expandido para pensamiento profundo */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Variables de tema */
:root {
  --color-black-soft: #2a2b2a; /* Color de fondo oscuro */
  --color-white-soft: #f8f7f2; /* Color de fondo claro */
}

/* Tema oscuro */
body[theme-mode="dark"] {
  /* Colores */
  --color-background: #2b2b2b; /* Color de fondo oscuro */
  --color-background-soft: #303030; /* Color de fondo claro */
  --color-background-mute: #282c34; /* Color de fondo neutro */
  --navbar-background: var(-–color-black-soft); /* Color de fondo de la barra de navegación */
  --chat-background: var(–-color-black-soft); /* Color de fondo del chat */
  --chat-background-user: #323332; /* Color de fondo del mensaje del usuario */
  --chat-background-assistant: #2d2e2d; /* Color de fondo del mensaje del asistente */
}

/* Estilos específicos del tema oscuro */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Color de fondo del contenedor de contenido */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Color de fondo de los mensajes */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Color de fondo de la barra de entrada */
    border: 1px solid #5e5d5940; /* Color del borde de la barra de entrada */
    border-radius: 8px; /* Radio del borde de la barra de entrada */
  }

  /* Estilos de código */
  code {
    background-color: #e5e5e20d; /* Color de fondo del código */
    color: #ea928a; /* Color del texto del código */
  }

  pre code {
    color: #abb2bf; /* Color del texto del código preformateado */
  }
}

/* Tema claro */
body[theme-mode="light"] {
  /* Colores */
  --color-white: #ffffff; /* Blanco */
  --color-background: #ebe8e2; /* Color de fondo claro */
  --color-background-soft: #cbc7be; /* Color de fondo claro */
  --color-background-mute: #e4e1d7; /* Color de fondo neutro */
  --navbar-background: var(-–color-white-soft); /* Color de fondo de la barra de navegación */
  --chat-background: var(-–color-white-soft); /* Color de fondo del chat */
  --chat-background-user: #f8f7f2; /* Color de fondo del mensaje del usuario */
  --chat-background-assistant: #f6f4ec; /* Color de fondo del mensaje del asistente */
}

/* Estilos específicos del tema claro */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Color de fondo del contenedor de contenido */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Color de fondo de los mensajes */
  }

  .inputbar-container {
    background-color: #ffffff; /* Color de fondo de la barra de entrada */
    border: 1px solid #87867f40; /* Color del borde de la barra de entrada */
    border-radius: 8px; /* Radio del borde de la barra de entrada, modifícalo a tu gusto */
  }

  /* Estilos de código */
  code {
    background-color: #3d39290d; /* Color de fondo del código */
    color: #7c1b13; /* Color del texto del código */
  }

  pre code {
    color: #000000; /* Color del texto del código preformateado */
  }
}
```

Para más variables de tema, consulta el código fuente: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Recomendaciones relacionadas

Biblioteca de temas de Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Comparte algunos temas de piel estilo chino para Cherry Studio: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)