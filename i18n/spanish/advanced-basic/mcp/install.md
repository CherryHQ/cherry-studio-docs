# Instalación del entorno MCP


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




**MCP (Model Context Protocol)** es un protocolo de código abierto diseñado para proporcionar información contextual a modelos de lenguaje extenso (LLM) de manera estandarizada. Para más información sobre MCP, consulta [#qué-es-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention").

## Uso de MCP en Cherry Studio

A continuación, se utiliza la funcionalidad `fetch` como ejemplo para demostrar cómo usar MCP en Cherry Studio. Puedes encontrar detalles en la [documentación](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparación: instalar uv y bun**

{% hint style="warning" %}
Cherry Studio actualmente solo utiliza [uv](https://github.com/astral-sh/uv) y [bun](https://github.com/oven-sh/bun) integrados, **sin reutilizar** las versiones instaladas en el sistema.
{% endhint %}

En `Configuración - Servidor MCP`, haz clic en el botón `Instalar` para descargar e instalar automáticamente. Como se descarga directamente desde GitHub, la velocidad puede ser lenta y existe una alta probabilidad de fallo. La instalación exitosa se verifica por la presencia de archivos en las carpetas mencionadas a continuación.

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Directorio de instalación del ejecutable:**

Windows: `C:\Users\nombre_de_usuario\.cherrystudio\bin`

macOS y Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Directorio bin</p></figcaption></figure>

**Si no se puede instalar correctamente:**

Puedes crear enlaces simbólicos desde los comandos correspondientes del sistema a este directorio. Si el directorio no existe, créalo manualmente. También puedes descargar manualmente los ejecutables y colocarlos en este directorio:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)