---
icon: file-code
---
# CSS Personalizado


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Com CSS personalizado, você pode modificar a aparência do software para se adequar melhor às suas preferências, por exemplo:

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6311935435315724879-y.jpg" alt=""><figcaption><p>CSS Personalizado</p></figcaption></figure>

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

### Variáveis Internas

```css
:root {
  font-family: "汉仪唐美人" !important; /* Fonte */
}

/* Cor do texto expandido de pensamento profundo */
.ant-collapse-content-box .markdown {
  color: red;
}

/* Variáveis do tema */
:root {
  --color-black-soft: #2a2b2a; /* Cor de fundo escura */
  --color-white-soft: #f8f7f2; /* Cor de fundo clara */
}

/* Tema escuro */
body[theme-mode="dark"] {
  /* Colors */
  --color-background: #2b2b2b; /* Cor de fundo escura */
  --color-background-soft: #303030; /* Cor de fundo clara */
  --color-background-mute: #282c34; /* Cor de fundo neutra */
  --navbar-background: var(-–color-black-soft); /* Cor de fundo da barra de navegação */
  --chat-background: var(–-color-black-soft); /* Cor de fundo do chat */
  --chat-background-user: #323332; /* Cor de fundo do chat do usuário */
  --chat-background-assistant: #2d2e2d; /* Cor de fundo do chat do assistente */
}

/* Estilos específicos do tema escuro */
body[theme-mode="dark"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Cor de fundo do contêiner de conteúdo */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Cor de fundo das mensagens */
  }

  .inputbar-container {
    background-color: #3d3d3a; /* Cor de fundo da caixa de entrada */
    border: 1px solid #5e5d5940; /* Cor da borda da caixa de entrada */
    border-radius: 8px; /* Raio da borda da caixa de entrada */
  }

  /* Estilo de código */
  code {
    background-color: #e5e5e20d; /* Cor de fundo do código */
    color: #ea928a; /* Cor do texto do código */
  }

  pre code {
    color: #abb2bf; /* Cor do texto do código pré-formatado */
  }
}

/* Tema claro */
body[theme-mode="light"] {
  /* Colors */
  --color-white: #ffffff; /* Branco */
  --color-background: #ebe8e2; /* Cor de fundo clara */
  --color-background-soft: #cbc7be; /* Cor de fundo clara */
  --color-background-mute: #e4e1d7; /* Cor de fundo neutra */
  --navbar-background: var(-–color-white-soft); /* Cor de fundo da barra de navegação */
  --chat-background: var(-–color-white-soft); /* Cor de fundo do chat */
  --chat-background-user: #f8f7f2; /* Cor de fundo do chat do usuário */
  --chat-background-assistant: #f6f4ec; /* Cor de fundo do chat do assistente */
}

/* Estilos específicos do tema claro */
body[theme-mode="light"] {
  #content-container {
    background-color: var(-–chat-background-assistant) !important; /* Cor de fundo do contêiner de conteúdo */
  }

  #content-container #messages {
    background-color: var(-–chat-background-assistant); /* Cor de fundo das mensagens */
  }

  .inputbar-container {
    background-color: #ffffff; /* Cor de fundo da caixa de entrada */
    border: 1px solid #87867f40; /* Cor da borda da caixa de entrada */
    border-radius: 8px; /* Raio da borda da caixa de entrada (ajuste conforme preferência) */
  }

  /* Estilo de código */
  code {
    background-color: #3d39290d; /* Cor de fundo do código */
    color: #7c1b13; /* Cor do texto do código */
  }

  pre code {
    color: #000000; /* Cor do texto do código pré-formatado */
  }
}
```

Para mais variáveis de tema, consulte o código-fonte: [https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles](https://github.com/CherryHQ/cherry-studio/tree/main/src/renderer/src/assets/styles)

### Recomendações Relacionadas

Biblioteca de temas do Cherry Studio: [https://github.com/boilcy/cherrycss](https://github.com/boilcy/cherrycss)

Compartilhe temas de Cherry Studio com estilo chinês: [https://linux.do/t/topic/325119/129](https://linux.do/t/topic/325119/129)