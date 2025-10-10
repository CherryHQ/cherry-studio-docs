# Configuración y uso de MCP


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Abre la configuración de Cherry Studio.
2. Ubica la opción `Servidor MCP`.
3. Haz clic en `Agregar servidor`.
4. Completa los parámetros del MCP Server ([enlace de referencia](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Los campos pueden incluir:
   * Nombre: Personaliza un nombre, por ejemplo `fetch-server`
   * Tipo: Selecciona `STDIO`
   * Comando: Ingresa `uvx`
   * Parámetros: Ingresa `mcp-server-fetch`
   * (Puede haber otros parámetros según el servidor específico)
5. Haz clic en `Guardar`.

{% hint style="success" %}
Tras completar esta configuración, Cherry Studio descargará automáticamente el MCP Server necesario: `fetch server`. Una vez finalizada la descarga, ¡podremos comenzar a usarlo! Nota: Si la configuración de mcp-server-fetch falla, intenta reiniciar el equipo.
{% endhint %}

### Habilitar el servicio MCP en el cuadro de chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Se ha agregado exitosamente un servidor MCP en la configuración de `Servidor MCP`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demostración del efecto de uso**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Como muestra la imagen superior, al combinar la función `fetch` de MCP, Cherry Studio comprende mejor la intención de consulta del usuario, obtiene información relevante de la web y proporciona respuestas más precisas y completas.