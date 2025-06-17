
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configuração MCP Integrada

### @cherry/mcp-auto-install

Instalação automática do serviço MCP (versão beta)

### @cherry/memory

Implementação básica de memória persistente baseada em gráficos de conhecimento local. Isso permite que o modelo se lembre de informações relevantes do usuário entre diferentes conversas.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

Uma implementação de servidor MCP que fornece ferramentas para resolução dinâmica e reflexiva de problemas através de processos de pensamento estruturados.

### @cherry/brave-search

Uma implementação de servidor MCP que integra a API de pesquisa Brave, fornecendo funcionalidade dupla de pesquisa na web e local.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

Servidor MCP para recuperar conteúdo de páginas da web por URL.

### @cherry/filesystem

Servidor Node.js que implementa o Model Context Protocol (MCP) para operações de sistema de arquivos.