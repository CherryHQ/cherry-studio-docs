
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Instalação Automática do MCP

> A instalação automática do MCP requer a atualização do Cherry Studio para a versão v1.1.18 ou superior.

## Introdução ao Funcionamento

Além da instalação manual, o Cherry Studio possui integrado a ferramenta `@mcpmarket/mcp-auto-install`, uma forma mais conveniente de instalar servidores MCP. Basta inserir o comando correspondente em uma conversa de modelo grande que suporte o serviço MCP.

{% hint style="warning" %}
**Lembrete da fase de teste:**

* `@mcpmarket/mcp-auto-install` ainda está na fase de testes
* O desempenho depende da "inteligência" do modelo grande: algumas instalações serão automáticas, enquanto outras exigirão **ajustes manuais de parâmetros nas configurações do MCP**
* Atualmente, a fonte de pesquisa é @modelcontextprotocol, podendo ser personalizada (explicado abaixo)
{% endhint %}

## Instruções de Uso

Por exemplo, você pode inserir:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Inserir comando para instalar o servidor MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interface de configuração do servidor MCP</p></figcaption></figure>

O sistema identificará automaticamente sua solicitação e completará a instalação através do `@mcpmarket/mcp-auto-install`. Essa ferramenta suporta diversos tipos de servidores MCP, incluindo mas não limitados a:

* filesystem (sistema de arquivos)
* fetch (requisição de rede)
* sqlite (banco de dados)
* etc.

> A variável MCP_PACKAGE_SCOPES permite personalizar a fonte de pesquisa de serviços MCP, com valor padrão: `@modelcontextprotocol`.

## Introdução à biblioteca `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Referência de configuração padrão:**

```json
// `axun-uUpaWEdMEMU8C61K` é o ID do serviço, pode ser personalizado
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "Detalhes em https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` é um pacote npm de código aberto. Consulte detalhes e documentação no [repositório oficial npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` representa a coleção oficial de serviços MCP do Cherry Studio.
{% endhint %}