
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Instalação do Ambiente MCP

**MCP (Model Context Protocol)** é um protocolo de código aberto projetado para fornecer informações contextuais a modelos de linguagem de grande porte (LLMs) de forma padronizada. Para mais informações sobre o MCP, consulte [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Usando o MCP no Cherry Studio

Veja a seguir um exemplo usando a funcionalidade `fetch` para demonstrar como utilizar o MCP no Cherry Studio. Detalhes podem ser encontrados na [documentação](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparação: Instalação do uv e bun**

{% hint style="warning" %}
Atualmente, o Cherry Studio usa exclusivamente [uv](https://github.com/astral-sh/uv) e [bun](https://github.com/oven-sh/bun) integrados, **não reutilizando** as versões instaladas no sistema.
{% endhint %}

Em `Configurações - Servidor MCP`, clique no botão `Instalar` para iniciar o download e instalação automáticos. Como o download é feito diretamente do GitHub, pode ser lento e ter alta probabilidade de falha. A instalação é considerada bem-sucedida apenas se os arquivos estiverem presentes nas pastas mencionadas abaixo.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Diretório de instalação dos executáveis:**

Windows: `C:\Users\Nome do Usuário\.cherrystudio\bin`

macOS e Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Diretório bin</p></figcaption></figure>

**Se a instalação automática falhar:**

Você pode criar links simbólicos a partir dos comandos correspondentes no sistema para este diretório. Se o diretório não existir, crie-o manualmente. Como alternativa, faça o download manual dos executáveis e coloque-os neste diretório:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)