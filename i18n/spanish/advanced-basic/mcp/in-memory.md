
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuración MCP integrada

### @cherry/mcp-auto-install

Instalación automática del servicio MCP (beta)

### @cherry/memory

Implementación básica de memoria persistente basada en gráficos de conocimiento local. Permite al modelo recordar información relevante del usuario entre diferentes conversaciones.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

Una implementación de servidor MCP que proporciona herramientas para resolución dinámica y reflexiva de problemas mediante procesos de pensamiento estructurados.

### @cherry/brave-search

Implementación de servidor MCP que integra la API de búsqueda Brave, ofreciendo funcionalidad dual de búsqueda web y local.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

Servidor MCP para obtener contenido web de URLs.

### @cherry/filesystem

Servidor Node.js que implementa el Model Context Protocol (MCP) para operaciones del sistema de archivos.