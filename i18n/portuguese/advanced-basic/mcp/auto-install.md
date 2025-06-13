
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Instalação Automática do MCP

> A instalação automática do MCP requer atualização do Cherry Studio para a versão v1.1.18 ou superior.

## Introdução à Funcionalidade

Além da instalação manual, o Cherry Studio incorpora a ferramenta `@mcpmarket/mcp-auto-install`, que oferece uma forma mais conveniente de instalar servidores MCP. Basta inserir o comando correspondente durante um diálogo com um modelo de linguagem grande compatível com serviços MCP.

{% hint style="warning" %}
**Aviso sobre fase de testes:**
* `@mcpmarket/mcp-auto-install` ainda está em fase de testes
* O desempenho depende da "inteligência" do modelo de linguagem — alguns instalam automaticamente, outros ainda exigem **ajustes manuais de parâmetros nas configurações do MCP**
* Atualmente utiliza como fonte de pesquisa padrão o @modelcontextprotocol, configurável conforme descrito abaixo
{% endhint %}

## Instruções de Uso

Por exemplo, você pode inserir:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Instrução para instalação do servidor MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interface de configuração do servidor MCP</p></figcaption></figure>

O sistema reconhecerá automaticamente sua solicitação e completará a instalação via `@mcpmarket/mcp-auto-install`. Esta ferramenta suporta diversos tipos de servidores MCP, incluindo:

* filesystem (sistema de arquivos)
* fetch (requisições de rede)
* sqlite (banco de dados)
* entre outros...

> A variável MCP_PACKAGE_SCOPES permite personalizar a fonte de pesquisa de serviços MCP. O valor padrão é `@modelcontextprotocol`.

## Introdução à Biblioteca `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Configuração padrão de referência:**

```json
// `axun-uUpaWEdMEMU8C61K` é o ID de serviço (personalizável)
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

`@mcpmarket/mcp-auto-install` é um pacote npm de código aberto. Consulte o [repositório oficial npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install) para detalhes e documentação. `@mcpmarket` representa a coleção oficial de serviços MCP do Cherry Studio.
{% endhint %}