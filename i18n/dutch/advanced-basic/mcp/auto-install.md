
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Automatische installatie van MCP

> Voor de automatische installatie van MCP moet Cherry Studio worden bijgewerkt naar v1.1.18 of hoger.

## Functie-introductie

Naast handmatige installatie bevat Cherry Studio ook de ingebouwde tool `@mcpmarket/mcp-auto-install`, wat een eenvoudigere methode is voor het installeren van MCP-servers. Je hoeft alleen maar de juiste opdracht in te voeren binnen een grootmodeldialoog die MCP-services ondersteunt.

{% hint style="warning" %}
**Testfase waarschuwing:**

* `@mcpmarket/mcp-auto-install` bevindt zich momenteel nog in de testfase
* Het resultaat hangt af van de "intelligentie" van het grootmodel - sommige worden automatisch toegevoegd, maar bij sommige moet je **nog steeds bepaalde parameters handmatig wijzigen in de MCP-instellingen**
* Momenteel worden zoekbronnen gezocht in @modelcontextprotocol, wat handmatig kan worden geconfigureerd (zie uitleg hieronder)
{% endhint %}

## Gebruiksaanwijzing

Je kunt bijvoorbeeld invoeren:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Voer opdracht in om MCP-server te installeren</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>MCP-server configuratiescherm</p></figcaption></figure>

Het systeem herkent automatisch je vereisten en voltooit de installatie via `@mcpmarket/mcp-auto-install`. Deze tool ondersteunt verschillende soorten MCP-servers, waaronder maar niet beperkt tot:

* filesystem (bestandssysteem)
* fetch (netwerkverzoek)
* sqlite (database)
* etc.

> De variabele `MCP_PACKAGE_SCOPES` maakt het mogelijk om MCP-service zoekbronnen aan te passen. Standaardwaarde: `@modelcontextprotocol`, kan handmatig worden geconfigureerd.

## Introductie van `@mcpmarket/mcp-auto-install` bibliotheek

{% hint style="info" %}
**Standaard configuratieverwijzing:**

```json
// `axun-uUpaWEdMEMU8C61K` is service-ID, kan naar wens worden aangepast
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
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
    "MCP_REGISTRY_PATH": "详情见https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` is een open-source npm-pakket. Je kunt de gedetailleerde informatie en gebruikersdocumentatie bekijken in de [officiële npm repository](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` is de officiële Cherry Studio MCP-servicecollectie.
{% endhint %}