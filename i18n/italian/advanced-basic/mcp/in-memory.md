
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Configurazione MCP Integrata

### @cherry/mcp-auto-install

Installazione automatica del servizio MCP (versione beta)

### @cherry/memory

Implementazione di base per memoria persistente basata su knowledge graph locale. Consente al modello di ricordare le informazioni rilevanti dell'utente tra diverse conversazioni.

```typescript
MEMORY_FILE_PATH=/path/to/your/file.json
```

### @cherry/sequentialthinking

Un'implementazione server MCP che fornisce strumenti per la risoluzione dinamica e riflessiva dei problemi attraverso processi di pensiero strutturati.

### @cherry/brave-search

Un'implementazione server MCP che integra l'API di ricerca Brave, offrendo funzionalità duali di ricerca web e locale.

```typescript
BRAVE_API_KEY=YOUR_API_KEY
```

### @cherry/fetch

Server MCP per il recupero dei contenuti di pagine web da URL.

### @cherry/filesystem

Server Node.js che implementa il Model Context Protocol (MCP) per operazioni sul filesystem.