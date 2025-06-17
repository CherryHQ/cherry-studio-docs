
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Built-in MCP Configurations

### @cherry/mcp-auto-install

Automatically installs MCP services (beta).

### @cherry/memory

A basic implementation of persistent memory based on a local knowledge graph. This allows the model to remember relevant user information across different conversations.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

An MCP server implementation that provides tools for dynamic and reflective problem-solving through structured thought processes.

### @cherry/brave-search

An MCP server implementation that integrates the Brave Search API, providing dual functionality for web and local search.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

An MCP server for fetching web page content from a URL.

### @cherry/filesystem

A Node.js server that implements the Model Context Protocol (MCP) for file system operations.