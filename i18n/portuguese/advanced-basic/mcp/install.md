# Instalação do Ambiente MCP


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




**MCP (Model Context Protocol)** é um protocolo open-source projetado para fornecer informações contextuais a modelos de linguagem de grande porte (LLMs) de forma padronizada. Para mais detalhes sobre o MCP, consulte [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Usando o MCP no Cherry Studio

O exemplo abaixo demonstra o uso da funcionalidade `fetch` no Cherry Studio. Detalhes completos podem ser encontrados na [documentação](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparação: Instalar uv e bun**

{% hint style="warning" %}
O Cherry Studio utiliza exclusivamente as instalações internas de [uv](https://github.com/astral-sh/uv) e [bun](https://github.com/oven-sh/bun), **não reaproveitando** versões instaladas no sistema.
{% endhint %}

Em `Configurações > Servidor MCP`, clique no botão `Instalar` para realizar o download automático. Como o download é feito diretamente do GitHub, a velocidade pode ser baixa e há maior possibilidade de falha. A instalação é considerada bem-sucedida se os arquivos estiverem presentes nas pastas mencionadas abaixo.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Diretórios de instalação dos executáveis:**

Windows: `C:\Users\NomeDeUsuário\.cherrystudio\bin`

macOS e Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Diretório bin</p></figcaption></figure>

**Caso a instalação automática falhe:**

É possível criar links simbólicos a partir dos comandos do sistema neste diretório. Se o diretório não existir, crie-o manualmente. Alternativamente, baixe os executáveis manualmente:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)