
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# MCP-Umgebungsinstallation

**MCP (Model Context Protocol)** ist ein Open-Source-Protokoll, das darauf abzielt, Kontextinformationen für große Sprachmodelle (LLM) auf standardisierte Weise bereitzustellen. Weitere Informationen zu MCP finden Sie unter [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Verwendung von MCP in Cherry Studio

Nachfolgend wird die `fetch`-Funktion als Beispiel verwendet, um zu demonstrieren, wie MCP in Cherry Studio eingesetzt werden kann. Details finden Sie in der [Dokumentation](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Vorbereitungen: Installation von uv und bun**

{% hint style="warning" %}
Cherry Studio verwendet derzeit nur die integrierten [uv](https://github.com/astral-sh/uv)- und [bun](https://github.com/oven-sh/bun)-Tools und **verwendet nicht** systemseitig installierte Versionen.
{% endhint %}

Unter `Einstellungen - MCP-Server` können Sie durch Anklicken der `Installieren`-Schaltfläche den automatischen Download und die Installation starten. Da der Download direkt von GitHub erfolgt, kann die Geschwindigkeit langsam sein und die Installation möglicherweise fehlschlagen. Der Erfolg der Installation kann überprüft werden, indem geprüft wird, ob Dateien im folgenden Ordner vorhanden sind.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Installationsverzeichnis für ausführbare Dateien:**

Windows: `C:\Users\Benutzername\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>bin-Verzeichnis</p></figcaption></figure>

**Bei Installationsproblemen:**

Sie können systemseitige Befehle per Softlink in dieses Verzeichnis verlinken. Falls das Verzeichnis nicht existiert, muss es manuell erstellt werden. Alternativ können ausführbare Dateien manuell heruntergeladen werden:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)