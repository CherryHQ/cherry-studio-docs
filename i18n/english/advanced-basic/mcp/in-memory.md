
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Built-in MCP Configurations

### @cherry/mcp-auto-install  
Automatically install MCP service (Beta)

### @cherry/memory  
Persistence memory base implementation based on local knowledge graph. This enables models to remember user-related information across different conversations.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking  
An MCP server implementation providing tools for dynamic and reflective problem-solving through structured thought processes.

### @cherry/brave-search  
An MCP server implementation integrated with Brave Search API, offering dual functionality for both web and local searches.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch  
MCP server for retrieving web content from URLs.

### @cherry/filesystem  
Node.js server implementing the Model Context Protocol (MCP) for file system operations.