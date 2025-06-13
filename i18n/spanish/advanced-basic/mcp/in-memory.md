
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuraciones MCP integradas

### @cherry/mcp-auto-install  
Instalación automática del servicio MCP (versión beta)

### @cherry/memory  
Implementación básica de memoria persistente basada en gráficos de conocimiento local. Permite que el modelo recuerde información relevante del usuario entre diferentes conversaciones.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking  
Implementación de servidor MCP que proporciona herramientas para resolver problemas de manera dinámica y reflexiva mediante procesos de pensamiento estructurados.

### @cherry/brave-search  
Implementación de servidor MCP que integra la API de búsqueda de Brave, ofreciendo funcionalidad dual de búsqueda web y local.

```typescript
BRAVE_API_KEY=TU_CLAVE_API
```

### @cherry/fetch  
Servidor MCP para obtener contenido de páginas web a través de URL.

### @cherry/filesystem  
Servidor Node.js que implementa el Model Context Protocol (MCP) para operaciones del sistema de archivos.