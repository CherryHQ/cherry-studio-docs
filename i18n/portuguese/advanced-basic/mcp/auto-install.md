
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Instalação Automática MCP

> A instalação automática do MCP requer atualização do Cherry Studio para v1.1.18 ou superior.

## Introdução à Funcionalidade

Além da instalação manual, o Cherry Studio inclui a ferramenta integrada `@mcpmarket/mcp-auto-install`, uma maneira mais conveniente de instalar servidores MCP. Basta inserir o comando correspondente no diálogo de modelos de linguagem que suportam serviços MCP.

{% hint style="warning" %}
**Aviso sobre fase de testes:**

* `@mcpmarket/mcp-auto-install` ainda está em fase de testes
* Os resultados dependem da "inteligência" do modelo de linguagem - alguns adicionam automaticamente, enquanto outros **ainda exigem alterações manuais de parâmetros nas configurações do MCP**
* Atualmente, as fontes de busca são pesquisadas em @modelcontextprotocol, podendo ser configuradas manualmente (explicado abaixo)
{% endhint %}

## Instruções de Uso

Por exemplo, você pode inserir:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Inserir comando para instalar servidor MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interface de configuração do servidor MCP</p></figcaption></figure>

O sistema reconhecerá automaticamente sua solicitação e completará a instalação via `@mcpmarket/mcp-auto-install`. Esta ferramenta suporta vários tipos de servidores MCP, incluindo:

* filesystem (sistema de arquivos)
* fetch (requisição web)
* sqlite (banco de dados)
* etc...

> A variável MCP_PACKAGE_SCOPES permite personalizar a fonte de busca de serviços MCP, com valor padrão: `@modelcontextprotocol`. Pode ser configurada conforme necessário.

## Introdução à biblioteca `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Configuração padrão de referência:**

```json
// `axun-uUpaWEdMEMU8C61K` é o ID do serviço, pode ser personalizado
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Instala automaticamente serviços MCP (versão Beta)",
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

`@mcpmarket/mcp-auto-install` é um pacote npm de código aberto. Veja detalhes e documentação no [repositório oficial npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` representa a coleção oficial de serviços MCP do Cherry Studio.
{% endhint %}