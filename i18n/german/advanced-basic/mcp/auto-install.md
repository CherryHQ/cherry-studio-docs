
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Automatische MCP-Installation

> Für die automatische Installation muss Cherry Studio auf Version v1.1.18 oder höher aktualisiert werden.

## Funktionen-Übersicht

Zusätzlich zur manuellen Installation enthält Cherry Studio das integrierte Tool `@mcpmarket/mcp-auto-install` – eine bequemere Methode zur Einrichtung von MCP-Servern. Geben Sie einfach den entsprechenden Befehl in einem Gespräch mit einem großen KI-Modell ein, das MCP-Dienste unterstützt.

{% hint style="warning" %}
**Hinweis zur Testphase:**

* `@mcpmarket/mcp-auto-install` befindet sich derzeit noch in der Beta-Phase
* Die Ergebnisse hängen von den Fähigkeiten des Modells ab: Manche fügen automatisch alles hinzu, andere erfordern **manuelle Anpassungen bestimmter Parameter in den MCP-Einstellungen**
* Aktuell erfolgt die Suche nach Quellen in @modelcontextprotocol, kann aber konfiguriert werden (siehe unten)
{% endhint %}

## Anleitung

Geben Sie beispielsweise Folgendes ein:

```
Installiere mir einen filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Befehleingabe zur MCP-Server-Installation</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP-Server-Konfigurationsinterface</p></figcaption></figure>

Das System erkennt automatisch Ihre Anforderung und installiert über `@mcpmarket/mcp-auto-install`. Das Tool unterstützt verschiedene MCP-Server-Typen, einschließlich:

* filesystem (Dateisystem)
* fetch (Netzwerkanfragen)
* sqlite (Datenbank)
* uvm.

> Die Variable MCP_PACKAGE_SCOPES ermöglicht die Anpassung der MCP-Dienstsuchquellen. Standardwert: `@modelcontextprotocol`, kann konfiguriert werden.

## Einführung zur `@mcpmarket/mcp-auto-install` Bibliothek

{% hint style="info" %}
**Standardkonfigurationsreferenz:**

```json
// `axun-uUpaWEdMEMU8C61K` ist die Dienst-ID, frei wählbar
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

`@mcpmarket/mcp-auto-install` ist ein Open-Source-npm-Paket. Weitere Informationen finden Sie im [offiziellen npm-Repository](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` ist die offizielle MCP-Dienstesammlung von Cherry Studio.
{% endhint %}