
{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Konfiguration und Verwendung von MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1.  Öffnen Sie die Cherry Studio-Einstellungen.
2.  Suchen Sie die Option `MCP-Server`.
3.  Klicken Sie auf `Server hinzufügen`.
4.  Tragen Sie die relevanten Parameter für den MCP-Server ein ([Referenzlink](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Mögliche erforderliche Angaben:
    *   Name: Benutzerdefinierter Name, z. B. `fetch-server`
    *   Typ: Wählen Sie `STDIO`
    *   Befehl: Tragen Sie `uvx` ein
    *   Argumente: Tragen Sie `mcp-server-fetch` ein
    *   (Je nach Server können weitere Parameter erforderlich sein)
5.  Klicken Sie auf `Speichern`.

{% hint style="success" %}
Nach erfolgreicher Konfiguration lädt Cherry Studio automatisch den erforderlichen MCP-Server - `fetch server` herunter. Nach Abschluss des Downloads kann die Nutzung beginnen! Hinweis: Bei fehlgeschlagener Konfiguration von mcp-server-fetch können Sie versuchen, Ihren Computer neu zu starten.
{% endhint %}

### Aktivierung des MCP-Dienstes im Chatfenster

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

*   Voraussetzung: Ein MCP-Server wurde unter `MCP-Server` erfolgreich hinzugefügt

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Anwendungsbeispiel**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Wie oben zu sehen ist, kann Cherry Studio nach Integration der `fetch`-Funktion von MCP die Absichten von Benutzeranfragen besser verstehen, relevante Informationen aus dem Netz abrufen und präzisere, umfassendere Antworten liefern.