# Instalación del entorno MCP


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




**MCP (Model Context Protocol)** es un protocolo de código abierto diseñado para proporcionar información contextual a los modelos de lenguaje grande (LLM) de manera estandarizada. Para más detalles sobre MCP, consulta [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Uso de MCP en Cherry Studio

Tomemos la función `fetch` como ejemplo para demostrar cómo usar MCP en Cherry Studio. Puedes encontrar detalles en la [documentación](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparación: instalar uv y bun**

{% hint style="warning" %}
Cherry Studio actualmente solo utiliza [uv](https://github.com/astral-sh/uv) y [bun](https://github.com/oven-sh/bun) integrados, **sin reutilizar** las versiones preinstaladas en el sistema.
{% endhint %}

En `Configuración - Servidor MCP`, haz clic en el botón `Instalar` para descargar e instalar automáticamente. Como se descarga directamente desde GitHub, la velocidad puede ser lenta y es probable que falle. La instalación exitosa se verifica por la presencia de archivos en las carpetas mencionadas a continuación.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Directorio de instalación de ejecutables:**

Windows: `C:\Users\用户名\.cherrystudio\bin`

macOS y Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Directorio bin</p></figcaption></figure>

**Si la instalación falla:**

Puedes enlazar los comandos del sistema a este directorio usando enlaces simbólicos. Si no existe el directorio correspondiente, créalo manualmente. También puedes descargar manualmente los ejecutables y colocarlos en este directorio:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)