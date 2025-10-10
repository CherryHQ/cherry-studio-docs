# Built-in MCP Configuration


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




### @cherry/mcp-auto-install

Automatically installs MCP services (beta)

### @cherry/memory

A persistent memory base implementation based on a local knowledge graph. This allows the model to remember relevant user information across different conversations.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

An MCP server implementation that provides tools for dynamic and reflective problem-solving through structured thinking processes.

### @cherry/brave-search

An MCP server implementation integrated with the Brave search API, providing both web and local search capabilities.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

An MCP server used to fetch web content from URLs.

### @cherry/filesystem

A Node.js server that implements the Model Context Protocol (MCP) for file system operations.