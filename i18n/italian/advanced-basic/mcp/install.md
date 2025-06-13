
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Installazione ambiente MCP

**MCP (Model Context Protocol)** è un protocollo open source progettato per fornire informazioni di contesto ai Large Language Model (LLM) in modo standardizzato. Maggiori dettagli su MCP sono disponibili in [#shen-me-shi-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Utilizzo di MCP in Cherry Studio

Di seguito, prendiamo la funzione `fetch` come esempio per dimostrare l'utilizzo di MCP in Cherry Studio. I dettagli sono consultabili nella [documentazione](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Preparazione: installare uv e bun**

{% hint style="warning" %}
Cherry Studio utilizza attualmente solo [uv](https://github.com/astral-sh/uv) e [bun](https://github.com/oven-sh/bun) integrati e **non riutilizza** le versioni di uv e bun già installate nel sistema.
{% endhint %}

Nelle `Impostazioni > Server MCP`, fai clic sul pulsante `Installa` per scaricare e installare automaticamente. Essendo i download effettuati direttamente da GitHub, la velocità potrebbe essere ridotta con possibilità di fallimento. Verifica la corretta installazione controllando la presenza di file nelle cartelle indicate di seguito.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Directory di installazione eseguibili:**

Windows: `C:\Users\username\.cherrystudio\bin`

macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Cartella bin</p></figcaption></figure>

**Se l'installazione non riesce:**

Collega i comandi di sistema tramite symbolic link a questa directory (crea manualmente le cartelle se non esistono). In alternativa, scarica manualmente gli eseguibili e posizionali qui:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)