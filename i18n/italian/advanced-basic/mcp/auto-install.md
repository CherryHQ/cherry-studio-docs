
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Installazione Automatica MCP

> L'installazione automatica MCP richiede l'aggiornamento di Cherry Studio alla versione v1.1.18 o successiva.

## Introduzione alle Funzionalità

Oltre all'installazione manuale, Cherry Studio include lo strumento integrato `@mcpmarket/mcp-auto-install`, un metodo più conveniente per installare i server MCP. Ti basterà inserire il comando appropriato nella chat di un modello linguistico di grandi dimensioni che supporti il servizio MCP.

{% hint style="warning" %}
**Avviso fase di test:**

* `@mcpmarket/mcp-auto-install` è attualmente ancora in fase di test
* L'efficacia dipende dall'"intelligenza" del modello linguistico: alcuni aggiungono automaticamente i parametri, mentre altri richiedono **modifiche manuali nelle impostazioni MCP**
* Attualmente le fonti di ricerca provengono da @modelcontextprotocol, ma sono configurabili (spiegato sotto)
{% endhint %}

## Istruzioni per l'Uso

Ad esempio, puoi inserire:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Inserisci comando per installare il server MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Interfaccia di configurazione server MCP</p></figcaption></figure>

Il sistema riconoscerà automaticamente la tua richiesta e completerà l'installazione tramite `@mcpmarket/mcp-auto-install`. Questo strumento supporta diversi tipi di server MCP, tra cui:

* filesystem (file system)
* fetch (richieste web)
* sqlite (database)
* ecc...

> La variabile MCP_PACKAGE_SCOPES consente di personalizzare le fonti di ricerca dei servizi MCP. Il valore predefinito è `@modelcontextprotocol`.

## Introduzione alla libreria `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Configurazione di riferimento predefinita:**

```json
// `axun-uUpaWEdMEMU8C61K` è l'ID del servizio, personalizzabile
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Installa automaticamente servizi MCP (versione Beta)",
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

`@mcpmarket/mcp-auto-install` è un pacchetto npm open source. Puoi trovare informazioni dettagliate e documentazione su [npm registry](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` rappresenta la raccolta ufficiale di servizi MCP di Cherry Studio.
{% endhint %}