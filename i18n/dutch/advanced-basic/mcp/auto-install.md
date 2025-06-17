
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Automatische installatie van MCP

> Voor automatische installatie van MCP is Cherry Studio v1.1.18 of hoger vereist.

## Functie-inleiding

Naast handmatige installatie heeft Cherry Studio de ingebouwde tool `@mcpmarket/mcp-auto-install`, een handigere methode om MCP-servers te installeren. Je hoeft alleen de bijbehorende opdracht in te voeren in een modeldialoog die MCP-services ondersteunt.

{% hint style="warning" %}
**Testfase herinnering:**
* `@mcpmarket/mcp-auto-install` bevindt zich momenteel nog in de testfase
* Het resultaat hangt af van de "intelligentie" van het grote model - sommige worden automatisch toegevoegd, terwijl voor andere **bepaalde parameters handmatig moeten worden gewijzigd in de MCP-instellingen**
* Momenteel wordt er gezocht vanuit @modelcontextprotocol als bron, je kunt dit zelf configureren (zie uitleg hieronder)
{% endhint %}

## Gebruiksaanwijzing

Je kunt bijvoorbeeld invoeren:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Voer opdracht in om MCP-server te installeren</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Configuratiescherm van MCP-server</p></figcaption></figure>

Het systeem herkent automatisch uw behoeften en voltooit de installatie via `@mcpmarket/mcp-auto-install`. Deze tool ondersteunt verschillende soorten MCP-servers, waaronder:
* filesystem (bestandssysteem)
* fetch (netwerkverzoek)
* sqlite (database)
* enz.

> De variabele MCP_PACKAGE_SCOPES kan de zoekbron voor MCP-services aanpassen. Standaardwaarde is: `@modelcontextprotocol`, configureerbaar naar wens.

## Introductie van `@mcpmarket/mcp-auto-install` bibliotheek

{% hint style="info" %}
**Standaard configuratie referentie:**

```json
// `axun-uUpaWEdMEMU8C61K` is de service-ID, aanpasbaar
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatisch MCP-services installeren (Betaversie)",
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
    "MCP_REGISTRY_PATH": "Details op https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` is een open source npm-pakket. Bekijk details en documentatie in de [npm officiële repository](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` is Cherry Studio's officiële collectie van MCP-services.
{% endhint %}