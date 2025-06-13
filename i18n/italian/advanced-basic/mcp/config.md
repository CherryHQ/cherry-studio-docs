
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Configurazione e utilizzo di MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1.  Apri le impostazioni di Cherry Studio.
2.  Individua l'opzione `MCP Server`.
3.  Clicca su `Aggiungi Server`.
4.  Inserisci i parametri del MCP Server ([link di riferimento](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). I campi richiesti includono:
    *   Nome: Personalizzato (es. `fetch-server`)
    *   Tipo: Seleziona `STDIO`
    *   Comando: `uvx`
    *   Parametri: `mcp-server-fetch`
    *   (Altri parametri specifici potrebbero essere richiesti in base al server)
5.  Clicca su `Salva`.

{% hint style="success" %}
Dopo la configurazione, Cherry Studio scaricherà automaticamente il MCP Server - `fetch server`. Al termine del download, sarà pronto per l'utilizzo! Nota: Se `mcp-server-fetch` non funziona correttamente, prova a riavviare il computer.
{% endhint %}

### Attivare il servizio MCP nella chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

*   `MCP Server` deve essere configurato correttamente per abilitare il servizio

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demo funzionale**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Come mostrato, integrando la funzione `fetch` di MCP, Cherry Studio comprende meglio le richieste degli utenti e fornisce risposte più precise recuperando informazioni dalla rete.