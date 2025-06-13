
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Instalación Automática de MCP

> La instalación automática de MCP requiere actualizar Cherry Studio a la versión v1.1.18 o superior.

## Introducción a la Función

Además de la instalación manual, Cherry Studio incluye integrada la herramienta `@mcpmarket/mcp-auto-install`, que ofrece una forma más conveniente de instalar servidores MCP. Simplemente ingresa el comando correspondiente en un diálogo de modelo grande compatible con servicios MCP.

{% hint style="warning" %}
**Recordatorio de Fase de Pruebas:**

* `@mcpmarket/mcp-auto-install` actualmente sigue en fase de prueba
* Su efectividad depende de la "inteligencia" del modelo grande; algunos se configuran automáticamente, mientras que otros aún **requieren cambios manuales de parámetros en la configuración MCP**
* Actualmente las fuentes de búsqueda se realizan en @modelcontextprotocol, pero pueden configurarse manualmente (explicado abajo)
{% endhint %}

## Instrucciones de Uso

Por ejemplo, puedes ingresar:

```
Ayúdame a instalar un servidor MCP de tipo filesystem
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Ingresar comando para instalar servidor MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interfaz de configuración del servidor MCP</p></figcaption></figure>

El sistema reconocerá automáticamente tu solicitud y completará la instalación mediante `@mcpmarket/mcp-auto-install`. Esta herramienta soporta varios tipos de servidores MCP, incluyendo:

* filesystem (sistema de archivos)
* fetch (solicitudes web)
* sqlite (base de datos)
* etc.

> La variable MCP_PACKAGE_SCOPES permite personalizar las fuentes de búsqueda de servicios MCP. El valor predeterminado es: `@modelcontextprotocol`. Configuración personalizable.

## Introducción a la biblioteca `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Configuración de referencia predeterminada:**

```json
// `axun-uUpaWEdMEMU8C61K` es el ID del servicio, personalizable
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
    "MCP_REGISTRY_PATH": "详情见https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` es un paquete npm de código abierto. Puedes consultar información detallada y documentación en el [repositorio oficial de npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` es la colección oficial de servicios MCP de Cherry Studio.
{% endhint %}