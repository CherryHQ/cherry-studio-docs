
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configuração Interna do MCP

### @cherry/mcp-auto-install

Instalação automática do serviço MCP (beta)

### @cherry/memory

Implementação baseada em grafo de conhecimento local para memória persistente. Isso permite que o modelo se lembre de informações relevantes do usuário entre diferentes conversas.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

Uma implementação de servidor MCP que fornece ferramentas para resolução dinâmica e reflexiva de problemas através de processos de pensamento estruturados.

### @cherry/brave-search

Uma implementação de servidor MCP que integra a API de busca Brave, oferecendo funcionalidade dupla de pesquisa na web e pesquisa local.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

Servidor MCP para obter conteúdo de páginas da web a partir de URLs.

### @cherry/filesystem

Servidor Node.js que implementa o Model Context Protocol (MCP) para operações de sistema de arquivos.