---
icon: file-code
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Пользовательский CSS

С помощью пользовательского CSS можно изменить внешний вид программы, чтобы он лучше соответствовал вашим предпочтениям, например, как показано ниже:

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

/* Цвет шрифта при развертывании глубокого размышления */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Переменные темы */
:root {
  --color-black-soft: #2a2b2a; /* Темный фон */
  --color-white-soft: #f8f7f2; /* Светлый фон */
}

/* Темная тема */
body[theme-mode="dark"] {
  /* Цвета */
  --color-background: #2b2b2b; /* Темный фон */
  --color-background-soft: #303030; /* Светлый фон */
  --color-background-mute: #282c34; /* Нейтральный фон */
  --navbar-background: var(-–color-black-soft); /* Фон навигации */
  --chat-background: var(–-color-black-soft); /* Фон чата */
  --chat-background-user: #323332; /* Фон сообщений пользователя */
  --chat-background-assistant: #2d2e2d; /* Фон сообщений ассистента */
}

/* Специальные стили для темной темы */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Фон контейнера контента */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Фон сообщений */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Фон поля ввода */
    border: 1px solid #5e5d5940; /* Граница поля ввода */
    border-radius: 8px; /* Скругление углов поля ввода */
  }

  /* Стили кода */
  code {
    background-color: #e5e5e20d; /* Фон кода */
    color: #ea928a; /* Цвет текста кода */
  }

  pre code {
    color: #abb2bf; /* Цвет текста в преформатированном коде */
  }
}

/* Светлая тема */
body[theme-mode="light"] {
  /* Цвета */
  --color-white: #ffffff; /* Белый */
  --color-background: #ebe8e2; /* Светлый фон */
  --color-background-soft: #cbc7be; /* Светлый фон */
  --color-background-mute: #e4e1d7; /* Нейтральный фон */
  --navbar-background: var(-–color-white-soft); /* Фон навигации */
  --chat-background: var(-–color-white-soft); /* Фон чата */
  --chat-background-user: #f8f7f2; /* Фон сообщений пользователя */
  --chat-background-assistant: #f6f4ec; /* Фон сообщений ассистента */
}

/* Специальные стили для светлой темы */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Фон контейнера контента */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Фон сообщений */
  }

  .inputbar-container {
    background-color: #ffffff; /* Фон поля ввода */
    border: 1px solid #87867f40; /* Граница поля ввода */
    border-radius: 8px; /* Скругление углов поля ввода */
  }

  /* Стили кода */
  code {
    background-color: #3d39290d; /* Фон кода */
    color: #7c1b13; /* Цвет текста кода */
  }

  pre code {
    color: #000000; /* Цвет текста в преформатированном коде */
  }
}
```

Больше переменных темы смотрите в исходном коде: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Рекомендации

Библиотека тем Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Поделиться темами Cherry Studio в китайском стиле: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)