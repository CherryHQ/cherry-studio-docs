
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Installazione Automatica di MCP

> L'installazione automatica di MCP richiede di aggiornare Cherry Studio alla versione v1.1.18 o superiore.

## Panoramica della Funzionalità

Oltre all'installazione manuale, Cherry Studio include lo strumento integrato `@mcpmarket/mcp-auto-install`, che offre un metodo più rapido per configurare i server MCP. Ti basterà inserire il comando appropriato nella conversazione con un modello di grandi dimensioni che supporta i servizi MCP.

{% hint style="warning" %}
**Avviso Fase di Test:**

* `@mcpmarket/mcp-auto-install` è attualmente in fase di test
* L'efficacia dipende dalle capacità del modello linguistico: alcuni parametri vengono aggiunti automaticamente, altri richiedono **modifiche manuali nelle impostazioni MCP**
* Attualmente le sorgenti vengono cercate in @modelcontextprotocol, configurabile manualmente (vedi sotto)
{% endhint %}

## Istruzioni per l'Uso

Ad esempio, puoi inserire:

```
Installa un server MCP per il filesystem
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Inserimento comando per installare il server MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interfaccia di configurazione del server MCP</p></figcaption></figure>

Il sistema riconoscerà automaticamente la richiesta e completerà l'installazione tramite `@mcpmarket/mcp-auto-install`. Questo strumento supporta diversi tipi di server MCP:

* filesystem (sistema di file)
* fetch (richieste web)
* sqlite (database)
* ecc...

> La variabile MCP_PACKAGE_SCOPES personalizza la sorgente per la ricerca dei servizi MCP. Il valore predefinito è `@modelcontextprotocol`.

## Presentazione della Libreria `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Configurazione Predefinita di Riferimento:**

```json
// `axun-uUpaWEdMEMU8C61K` è l'ID servizio (personalizzabile)
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
    "MCP_REGISTRY_PATH": "Dettagli su https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` è un pacchetto npm open source. Consulta dettagli e documentazione sul [repository ufficiale npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` rappresenta la raccolta ufficiale di servizi MCP di Cherry Studio.
{% endhint %}