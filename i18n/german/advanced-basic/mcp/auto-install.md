
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Automatische Installation von MCP

> Für die automatische Installation von MCP muss Cherry Studio auf Version v1.1.18 oder höher aktualisiert werden.

## Funktionsübersicht

Zusätzlich zur manuellen Installation bietet Cherry Studio das integrierte Tool `@mcpmarket/mcp-auto-install`, eine bequemere Methode zur Installation von MCP-Servern. Geben Sie einfach den entsprechenden Befehl in einem Chat mit einem großen Modell ein, das MCP-Dienste unterstützt.

{% hint style="warning" %}
**Hinweis während der Testphase:**

* `@mcpmarket/mcp-auto-install` befindet sich derzeit noch in der Testphase
* Die Effektivität hängt von der "Intelligenz" des großen Modells ab – manchmal werden Parameter automatisch hinzugefügt, manchmal **müssen bestimmte Parameter in den MCP-Einstellungen manuell angepasst werden**
* Derzeit werden Suchquellen von @modelcontextprotocol durchsucht (kann individuell konfiguriert werden, siehe unten)
{% endhint %}

## Verwendungshinweise

Beispielsweise können Sie eingeben:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Eingabe einer Anweisung zum Installieren des MCP-Servers</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP-Serverkonfigurationsoberfläche</p></figcaption></figure>

Das System erkennt automatisch Ihre Anforderung und installiert sie über `@mcpmarket/mcp-auto-install`. Dieses Tool unterstützt verschiedene MCP-Servertypen, einschließlich:

* filesystem (Dateisystem)
* fetch (Netzwerkanfragen)
* sqlite (Datenbank)
* usw.

> Die Variable MCP\_PACKAGE\_SCOPES ermöglicht die Anpassung der MCP-Dienstsuchquelle. Standardwert: `@modelcontextprotocol`.

## Einführung der `@mcpmarket/mcp-auto-install`-Bibliothek

{% hint style="info" %}
**Referenz zur Standardkonfiguration:**

```json
// `axun-uUpaWEdMEMU8C61K` ist die Dienst-ID, die beliebig angepasst werden kann
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatische Installation von MCP-Diensten (Beta-Version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "Details unter https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` ist ein Open-Source-npm-Paket. Details und Dokumentation finden Sie im [offiziellen npm-Repository](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` ist die offizielle MCP-Dienstesammlung von Cherry Studio.
{% endhint %}