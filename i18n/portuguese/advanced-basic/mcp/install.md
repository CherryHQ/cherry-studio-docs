# Instalação do Ambiente MCP


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




**MCP (Model Context Protocol)** é um protocolo de código aberto projetado para fornecer informações de contexto a modelos de linguagem grande (LLM) de maneira padronizada. Para mais detalhes sobre o MCP, consulte [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Usando o MCP no Cherry Studio

A seguir, usando a funcionalidade `fetch` como exemplo, demonstraremos como usar o MCP no Cherry Studio. Detalhes podem ser encontrados na [documentação](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparação: Instalação do uv e bun**

{% hint style="warning" %}
Atualmente, o Cherry Studio usa apenas o [uv](https://github.com/astral-sh/uv) e [bun](https://github.com/oven-sh/bun) integrados, e **não reutilizará** as versões já instaladas no sistema.
{% endhint %}

Em `Configurações → Servidor MCP`, clique no botão `Instalar` para realizar o download e instalação automáticos. Como o download é feito diretamente do GitHub, pode ser lento e há maior chance de falhas. O sucesso da instalação é verificado pela presença de arquivos nas pastas mencionadas abaixo.

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Diretório de instalação dos executáveis:**

Windows: `C:\Users\NomeDoUsuário\.cherrystudio\bin`

macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Diretório bin</p></figcaption></figure>

**Caso a instalação automática falhe:**

Você pode vincular os comandos correspondentes do sistema a este diretório usando links simbólicos. Se o diretório não existir, crie-o manualmente. Alternativamente, baixe manualmente os executáveis e coloque-os neste diretório:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)  
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)