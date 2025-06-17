
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# MCP-omgevingsinstallatie

**MCP (Model Context Protocol)** is een open-source protocol dat contextinformatie op een gestandaardiseerde manier aan grote taalmodellen (LLM) levert. Meer informatie over MCP vindt u in [#wat-is-mcp-model-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "verwijzing").

## MCP gebruiken in Cherry Studio

Hieronder wordt de `fetch`-functionaliteit als voorbeeld gebruikt om te demonstreren hoe MCP in Cherry Studio werkt. Details zijn te vinden in de [documentatie](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Voorbereidingen: Installeer uv en bun**

{% hint style="warning" %}
Cherry Studio gebruikt momenteel alleen de ingebouwde [uv](https://github.com/astral-sh/uv) en [bun](https://github.com/oven-sh/bun), en **hergebruikt niet** de reeds geïnstalleerde uv en bun op het systeem.
{% endhint %}

Klik in `Instellingen - MCP-server` op de knop `Installeren` om automatisch te downloaden en installeren. Omdat het bestanden rechtstreeks van GitHub downloadt, kan het proces traag zijn en kans op fouten hebben. De succesvolle installatie wordt bepaald door de aanwezigheid van bestanden in onderstaande mappen.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Installatiemap voor uitvoerbare programma's:**

Windows: `C:\Users\gebruikersnaam\.cherrystudio\bin`

macOS, Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>bin-map</p></figcaption></figure>

**Bij installatieproblemen:**

U kunt symbolische links maken naar de systeemcommando's. Ontbreekt de map, maak deze dan handmatig aan. Of download handmatig uitvoerbare bestanden naar deze map:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)