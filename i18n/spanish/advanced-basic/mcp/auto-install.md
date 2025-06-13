
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Instalación Automática de MCP

> La instalación automática de MCP requiere actualizar Cherry Studio a la versión v1.1.18 o superior.

## Introducción a la Función

Además de la instalación manual, Cherry Studio incluye la herramienta `@mcpmarket/mcp-auto-install`, una forma más conveniente de instalar servidores MCP. Solo necesitas ingresar el comando correspondiente en el diálogo de modelos grandes que admiten servicios MCP.

{% hint style="warning" %}
**Recordatorio de fase de prueba:**

* `@mcpmarket/mcp-auto-install` aún está en fase de prueba
* El efecto depende de la "inteligencia" del modelo grande; algunos se agregan automáticamente, mientras que otros **requieren ajustes manuales en la configuración de MCP**
* Actualmente, la fuente de búsqueda es @modelcontextprotocol, pero puede configurarse manualmente (ver más abajo)
{% endhint %}

## Instrucciones de Uso

Por ejemplo, puedes ingresar:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Ingresar comando para instalar servidor MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interfaz de configuración del servidor MCP</p></figcaption></figure>

El sistema reconocerá automáticamente tus necesidades y completará la instalación mediante `@mcpmarket/mcp-auto-install`. Esta herramienta admite múltiples tipos de servidores MCP, incluyendo:

* filesystem (sistema de archivos)
* fetch (solicitudes de red)
* sqlite (base de datos)
* etc...

> La variable MCP_PACKAGE_SCOPES permite personalizar las fuentes de búsqueda de servicios MCP. El valor predeterminado es: `@modelcontextprotocol`.

## Introducción a la biblioteca `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Configuración de referencia predeterminada:**

```json
// `axun-uUpaWEdMEMU8C61K` es el ID de servicio, personalizable
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

`@mcpmarket/mcp-auto-install` es un paquete npm de código abierto. Puedes consultar detalles y documentación en el [repositorio oficial de npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` es la colección oficial de servicios MCP de Cherry Studio.
{% endhint %}