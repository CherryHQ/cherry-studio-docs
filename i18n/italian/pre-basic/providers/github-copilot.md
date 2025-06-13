
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# GitHub Copilot

Per utilizzare GitHub Copilot è necessario disporre di un account GitHub e sottoscrivere il servizio GitHub Copilot. È possibile utilizzare anche la versione gratuita, ma questa non supporta il nuovo modello Claude 3.7. Per maggiori dettagli, consultare il [sito ufficiale di GitHub Copilot](https://github.com/features/copilot).

## Ottenere il Device Code

Fare clic su "Accedi con GitHub" per ottenere e copiare il Device Code.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Esempio di acquisizione del Device Code"><figcaption><p>Ottenere Device Code</p></figcaption></figure>

## Inserire il Device Code nel browser e autorizzare

Dopo aver ottenuto con successo il Device Code, fare clic sul link per aprire il browser, accedere al proprio account GitHub, inserire il Device Code e concedere l'autorizzazione.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Esempio di autorizzazione GitHub"><figcaption><p>Autorizzazione GitHub</p></figcaption></figure>

Dopo l'autorizzazione, tornare a Cherry Studio e fare clic su "Connetti GitHub". Al termine, verranno visualizzati il nome utente e l'avatar di GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Esempio di connessione GitHub riuscita"><figcaption><p>Connessione GitHub riuscita</p></figcaption></figure>

## Fare clic su "Gestisci" per ottenere l'elenco dei modelli

Fare clic sul pulsante "Gestisci" in basso per ottenere automaticamente l'elenco dei modelli attualmente supportati tramite connessione internet.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Esempio di acquisizione elenco modelli"><figcaption><p>Ottenere elenco modelli</p></figcaption></figure>

## Domande frequenti

### Acquisizione Device Code fallita, riprova

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Esempio di fallimento acquisizione Device Code"><figcaption><p>Acquisizione Device Code fallita</p></figcaption></figure>

Attualmente le richieste vengono effettuate con Axios, che non supporta proxy SOCKS. Utilizzare proxy di sistema, proxy HTTP, oppure non impostare alcun proxy in CherryStudio e utilizzare un proxy globale. Assicurarsi innanzitutto che la connessione di rete sia funzionante per evitare fallimenti nell'acquisizione del Device Code.