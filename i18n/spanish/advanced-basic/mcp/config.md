# Configuración y uso de MCP


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Abre la configuración de Cherry Studio.
2. Encuentra la opción `MCP 服务器`.
3. Haz clic en `添加服务器`.
4. Completa los parámetros del MCP Server ([referencia](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Los campos pueden incluir:
   * Nombre: Personaliza un nombre, ej. `fetch-server`
   * Tipo: Selecciona `STDIO`
   * Comando: Ingresa `uvx`
   * Parámetros: Ingresa `mcp-server-fetch`
   * (Pueden existir otros parámetros según el servidor específico)
5. Haz clic en `保存`.

{% hint style="success" %}
Tras completar la configuración, Cherry Studio descargará automáticamente el MCP Server requerido: `fetch server`. ¡Una vez descargado podremos empezar a usarlo! Nota: Si mcp-server-fetch no se configura correctamente, intenta reiniciar tu computadora.
{% endhint %}

### Habilitar el servicio MCP en el cuadro de chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Cuando se añade exitosamente un servidor MCP en `MCP 服务器`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demostración de resultados**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Como muestra la imagen superior, al combinar la función `fetch` de MCP, Cherry Studio comprende mejor las intenciones de consulta del usuario, obtiene información relevante de internet y ofrece respuestas más precisas y completas.