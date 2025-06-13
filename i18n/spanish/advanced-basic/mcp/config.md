
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configurar y Usar MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Abre la configuración de Cherry Studio.
2. Localiza la opción `Servidor MCP`.
3. Haz clic en `Añadir Servidor`.
4. Completa los parámetros del MCP Server ([enlace de referencia](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Los campos requeridos pueden incluir:
   * **Nombre**: Define uno personalizado, ej. `fetch-server`
   * **Tipo**: Selecciona `STDIO`
   * **Comando**: Ingresa `uvx`
   * **Parámetros**: Escribe `mcp-server-fetch`
   * *(Puede haber otros parámetros según el servidor específico)*
5. Haz clic en `Guardar`.

{% hint style="success" %}
¡Tras completar esta configuración, Cherry Studio descargará automáticamente el MCP Server requerido: `fetch server`! Una vez descargado, podrás comenzar a usarlo. Nota: Si falla la configuración de mcp-server-fetch, prueba reiniciando tu computadora.
{% endhint %}

### Activar Servicio MCP en el Chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Asegúrate de haber añadido exitosamente el servidor MCP en la configuración:

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demostración de Uso**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Como muestra la imagen superior, al integrar la función `fetch` de MCP, Cherry Studio comprende mejor la intención de la consulta del usuario, obtiene información relevante de internet y proporciona respuestas más precisas y completas.