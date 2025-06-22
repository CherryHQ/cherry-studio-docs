
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Instalación del entorno MCP

**MCP(Model Context Protocol)** es un protocolo de código abierto diseñado para proporcionar información contextual a modelos de lenguaje grandes (LLM) de manera estandarizada. Para obtener más información sobre MCP, consulte [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Usando MCP en Cherry Studio

A continuación se muestra cómo utilizar MCP en Cherry Studio tomando como ejemplo la función `fetch`. Los detalles se pueden consultar en la [documentación](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparación: Instalación de uv y bun**

{% hint style="warning" %}
Cherry Studio actualmente solo utiliza las versiones integradas de [uv](https://github.com/astral-sh/uv) y [bun](https://github.com/oven-sh/bun), y **no reutilizará** las versiones de uv y bun previamente instaladas en el sistema.
{% endhint %}

En `Configuración - Servidor MCP`, haga clic en el botón `Instalar` para descargar e instalar automáticamente. Debido a que se descarga directamente desde GitHub, la velocidad puede ser lenta y existe una alta probabilidad de fallo. Verifique si la instalación fue exitosa comprobando la presencia de archivos en las carpetas mencionadas a continuación.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Directorios de instalación de ejecutables:**

Windows: `C:\Users\用户名\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Directorio bin</p></figcaption></figure>

**Si la instalación falla:**

Puede crear enlaces simbólicos desde los comandos correspondientes del sistema hacia estos directorios. Si no existen los directorios, créelos manualmente. Alternativamente, descargue manualmente los ejecutables y colóquelos en estos directorios:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)