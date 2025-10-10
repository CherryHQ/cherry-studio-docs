# Instalación del entorno MCP


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




**MCP (Model Context Protocol)** es un protocolo de código abierto diseñado para proporcionar información contextual a modelos de lenguaje extenso (LLM) de forma estandarizada. Para más detalles sobre MCP, consulte [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Uso de MCP en Cherry Studio

A continuación, tomaremos la función `fetch` como ejemplo para demostrar cómo usar MCP en Cherry Studio. Puede encontrar detalles en la [documentación](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparación: Instalar uv y bun**

{% hint style="warning" %}
Cherry Studio actualmente solo utiliza las versiones integradas de [uv](https://github.com/astral-sh/uv) y [bun](https://github.com/oven-sh/bun), **y no reutiliza** las instalaciones existentes en el sistema.
{% endhint %}

En `Configuración > Servidor MCP`, haga clic en el botón `Instalar` para descargar e instalar automáticamente. Al descargarse directamente desde GitHub, la velocidad puede ser lenta y existe una alta probabilidad de fallo. La instalación exitosa se verifica mediante la presencia de archivos en las carpetas mencionadas a continuación.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Directorio de instalación de ejecutables:**

Windows: `C:\Users\nombre_de_usuario\.cherrystudio\bin`

macOS y Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Directorio bin</p></figcaption></figure>

**Si la instalación falla:**

Puede crear enlaces simbólicos desde los comandos correspondientes del sistema hacia este directorio. Si el directorio no existe, créelo manualmente. También puede descargar manualmente los ejecutables y colocarlos en esta ubicación:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)