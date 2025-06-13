
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Instalação do Ambiente MCP

**MCP (Model Context Protocol)** é um protocolo de código aberto projetado para fornecer informações de contexto a modelos de linguagem de grande escala (LLMs) de forma padronizada. Para mais detalhes sobre o MCP, consulte [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Usando o MCP no Cherry Studio

O exemplo a seguir demonstra como usar o recurso `fetch` do MCP no Cherry Studio. Detalhes completos estão disponíveis na [documentação](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparação: Instalando uv e bun**

{% hint style="warning" %}
Atualmente, o Cherry Studio utiliza exclusivamente [uv](https://github.com/astral-sh/uv) e [bun](https://github.com/oven-sh/bun) integrados, **não reutilizando** versões instaladas no sistema.
{% endhint %}

Na seção `Configurações → Servidor MCP`, clique no botão `Instalar` para baixar e instalar automaticamente. O download é feito diretamente do GitHub, podendo ser lento ou falhar com frequência. A instalação é bem-sucedida somente se os arquivos aparecerem nas pastas mencionadas abaixo.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Diretório de instalação dos executáveis:**

Windows: `C:\Users\nome_do_usuário\.cherrystudio\bin`

macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Diretório bin</p></figcaption></figure>

**Se a instalação automática falhar:**

Você pode criar links simbólicos para os comandos do sistema neste diretório (crie a pasta manualmente se inexistente). Alternativamente, baixe os executáveis manualmente:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)