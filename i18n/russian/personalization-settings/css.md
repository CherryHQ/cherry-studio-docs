---
icon: file-code
---
# Пользовательский CSS


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




С помощью пользовательского CSS вы можете настроить внешний вид ПО по своему вкусу. Пример:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>Пользовательский CSS</p></figcaption></figure>

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

### Встроенные переменные

```css
:root {
  font-family: "汉仪唐美人" !important; /* Шрифт */
}

/* Цвет текста при раскрытии блока */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Переменные темы */
:root {
  --color-black-soft: #2a2b2a; /* Тёмный цвет фона */
  --color-white-soft: #f8f7f2; /* Светлый цвет фона */
}

/* Тёмная тема */
body[theme-mode="dark"] {
  /* Цвета */
  --color-background: #2b2b2b; /* Тёмный цвет фона */
  --color-background-soft: #303030; /* Светлый цвет фона */
  --color-background-mute: #282c34; /* Нейтральный цвет фона */
  --navbar-background: var(–-color-black-soft); /* Цвет фона навигации */
  --chat-background: var(–-color-black-soft); /* Цвет фона чата */
  --chat-background-user: #323332; /* Цвет фона сообщений пользователя */
  --chat-background-assistant: #2d2e2d; /* Цвет фона сообщений ассистента */
}

/* Стили для тёмной темы */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(–-chat-background-assistant) !important; /* Цвет фона контейнера */
  }

  #content-container #messages {
    background-color: var(–-chat-background-assistant); /* Цвет фона сообщений */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Цвет фона поля ввода */
    border: 1px solid #5e5d5940; /* Цвет рамки поля ввода */
    border-radius: 8px; /* Скругление рамки */
  }

  /* Стили кода */
  code {
    background-color: #e5e5e20d; /* Цвет фона кода */
    color: #ea928a; /* Цвет текста кода */
  }

  pre code {
    color: #abb2bf; /* Цвет текста в блоке кода */
  }
}

/* Светлая тема */
body[theme-mode="light"] {
  /* Цвета */
  --color-white: #ffffff; /* Белый */
  --color-background: #ebe8e2; /* Светлый цвет фона */
  --color-background-soft: #cbc7be; /* Светлый цвет фона */
  --color-background-mute: #e4e1d7; /* Нейтральный цвет фона */
  --navbar-background: var(–-color-white-soft); /* Цвет фона навигации */
  --chat-background: var(–-color-white-soft); /* Цвет фона чата */
  --chat-background-user: #f8f7f2; /* Цвет фона сообщений пользователя */
  --chat-background-assistant: #f6f4ec; /* Цвет фона сообщений ассистента */
}

/* Стили для светлой темы */
body[theme-mode="light"] {
  #content-container {
    background-color: var(–-chat-background-assistant) !important; /* Цвет фона контейнера */
  }

  #content-container #messages {
    background-color: var(–-chat-background-assistant); /* Цвет фона сообщений */
  }

  .inputbar-container {
    background-color: #ffffff; /* Цвет фона поля ввода */
    border: 1px solid #87867f40; /* Цвет рамки поля ввода */
    border-radius: 8px; /* Скругление рамки */
  }

  /* Стили кода */
  code {
    background-color: #3d39290d; /* Цвет фона кода */
    color: #7c1b13; /* Цвет текста кода */
  }

  pre code {
    color: #000000; /* Цвет текста в блоке кода */
  }
}
```

Больше переменных темы в исходном коде: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Рекомендуем

Библиотека тем Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Коллекция тем Cherry Studio в китайском стиле: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)