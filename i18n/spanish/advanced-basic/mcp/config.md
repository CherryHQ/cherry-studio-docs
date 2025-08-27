# Configurar y usar MCP


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Abra la configuración de Cherry Studio.
2. Busque la opción `Servidor MCP`.
3. Haga clic en `Agregar servidor`.
4. Complete los parámetros del servidor MCP ([enlace de referencia](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Los campos a completar pueden incluir:
   * Nombre: Un nombre personalizado, por ejemplo `fetch-server`
   * Tipo: Seleccione `STDIO`
   * Comando: Ingrese `uvx`
   * Parámetros: Ingrese `mcp-server-fetch`
   * (Puede haber otros parámetros dependiendo del servidor específico)
5. Haga clic en `Guardar`.

{% hint style="success" %}
¡Después de completar esta configuración, Cherry Studio descargará automáticamente el servidor MCP necesario - `fetch server`. Una vez descargado, ¡podremos empezar a usarlo! Nota: Si mcp-server-fetch no se configura correctamente, intente reiniciar su computadora.
{% endhint %}

### Habilitar servicios MCP en el cuadro de chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* El servidor MCP debe estar configurado correctamente en `Servidor MCP`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demostración de efectos de uso**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Como se muestra en la imagen superior, al combinar la función `fetch` de MCP, Cherry Studio puede comprender mejor la intención de consulta del usuario, obtener información relevante de Internet y brindar respuestas más precisas y completas.