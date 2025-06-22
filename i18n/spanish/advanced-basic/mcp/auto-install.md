
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Instalación automática de MCP

> La instalación automática de MCP requiere actualizar Cherry Studio a la versión v1.1.18 o superior.

## Introducción a la funcionalidad

Además de la instalación manual, Cherry Studio incluye integrada la herramienta `@mcpmarket/mcp-auto-install`, una forma más conveniente de instalar servidores MCP. Solo necesitas ingresar el comando correspondiente en el chat de modelos grandes que admitan servicios MCP.

{% hint style="warning" %}
**Advertencia de fase de prueba:**
* `@mcpmarket/mcp-auto-install` sigue en fase de prueba
* Su eficacia depende de la "inteligencia" del modelo grande. Algunos añaden automáticamente, pero otros **aún requieren ajustes manuales de parámetros en la configuración MCP**
* Actualmente las fuentes de búsqueda se realizan desde @modelcontextprotocol. Es configurable (ver abajo)
{% endhint %}

## Instrucciones de uso

Por ejemplo, puedes ingresar:

```
Ayúdame a instalar un servidor MCP de filesystem
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Ingresar comando para instalar servidor MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interfaz de configuración del servidor MCP</p></figcaption></figure>

El sistema reconocerá automáticamente tu solicitud y completará la instalación mediante `@mcpmarket/mcp-auto-install`. Esta herramienta soporta múltiples tipos de servidores MCP, incluyendo:

* filesystem (sistema de archivos)
* fetch (solicitudes web)
* sqlite (base de datos)
* etc...

> La variable MCP_PACKAGE_SCOPES permite personalizar las fuentes de búsqueda de servicios MCP. Valor predeterminado: `@modelcontextprotocol`. Configurable.

## Introducción a la librería `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Configuración de referencia predeterminada:**

```json
// `axun-uUpaWEdMEMU8C61K` es el ID del servicio, personalizable
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Instalación automática de servicios MCP (versión Beta)",
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
    "MCP_REGISTRY_PATH": "Detalles en https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` es un paquete npm de código abierto. Consulta detalles y documentación en el [repositorio oficial de npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` es el conjunto oficial de servicios MCP de Cherry Studio.
{% endhint %}