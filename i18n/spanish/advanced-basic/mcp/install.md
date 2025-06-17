
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Instalación del entorno MCP

**MCP(Model Context Protocol)** es un protocolo de código abierto diseñado para proporcionar información contextual a los modelos de lenguaje grandes (LLM) de manera estandarizada. Para obtener más información sobre MCP, consulte [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Uso de MCP en Cherry Studio

A continuación, se utiliza la función `fetch` como ejemplo para demostrar cómo usar MCP en Cherry Studio. Puede encontrar detalles en la [documentación](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparativos: Instalación de uv y bun**

{% hint style="warning" %}
Cherry Studio actualmente solo utiliza [uv](https://github.com/astral-sh/uv) y [bun](https://github.com/oven-sh/bun) integrados, y **no reutiliza** las versiones de uv y bun ya instaladas en el sistema.
{% endhint %}

En `Configuración - Servidor MCP`, haga clic en el botón `Instalar` para descargar e instalar automáticamente. Como se descarga directamente de GitHub, la velocidad puede ser lenta y es posible que falle. El éxito de la instalación se verifica por la presencia de archivos en las carpetas mencionadas a continuación.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Directorio de instalación de ejecutables:**

Windows: `C:\Users\用户名\.cherrystudio\bin`

macOS y Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Directorio bin</p></figcaption></figure>

**En caso de instalación fallida:**

Puede crear enlaces simbólicos a los comandos correspondientes del sistema en este directorio. Si el directorio no existe, debe crearse manualmente. También puede descargar manualmente los ejecutables y colocarlos en este directorio:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)