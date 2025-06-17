---
icon: seal-question
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Domande Frequenti

## Codici di errore comuni

* **4xx (Codici di stato per errori client)** : Generalmente causati da errori nella sintassi della richiesta, autorizzazione fallita o problemi di autenticazione che impediscono il completamento della richiesta.
* **5xx (Codici di stato per errori server)** : Generalmente errori del server, come server offline, timeout nell'elaborazione delle richieste, ecc.

| Codice di errore       | Possibili cause                                                                       | Soluzioni                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4>     | Formato del corpo della richiesta errato                                                     | <p>Verificare il contenuto dell'errore restituito nella conversazione o controllare tramite la <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a> seguendo le istruzioni.</p><p><mark style="color:purple;">【Caso comune 1】</mark>: Per il modello Gemini potrebbe essere necessaria la registrazione della carta;<br><mark style="color:purple;">【Caso comune 2】</mark>: Dati sovradimensionati, frequenti nei modelli visivi. Le immagini che superano il limite superiore restituiscono questo errore;<br><mark style="color:purple;">【Caso comune 3】</mark>: Parametri non supportati o errati. Provare a testare con un assistente pulito;<br><mark style="color:purple;">【Caso comune 4】</mark>: Contesto eccessivo, cancellare il contesto o iniziare una nuova conversazione.</p> |
| <h4>401</h4>     | Autenticazione fallita: modello non supportato o account server bloccato                              | Contattare o verificare lo stato dell'account presso il provider                                                                                                                                                                                                                                                                                                                                                                     |
| <h4>403</h4>     | Nessuna autorizzazione per l'operazione richiesta                                                    | Seguire le informazioni d'errore nella conversazione o nella [console](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                       |
| <h4>404</h4>     | Risorsa richiesta non trovata                                                              | Verificare il percorso della richiesta                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>422</h4>     | Sintassi corretta ma semantica errata                                                            | Il server comprende ma non può elaborare. Comune con valori JSON errati (es. valori null, numeri dove servono stringhe).                                                                                                                                                                                                                                                                                                |
| <h4>429</h4>     | Limite di velocità delle richieste raggiunto                                                          | RPM/TPM al limite. Attendere prima di riprovare                                                                                                                                                                                                                                                                                                                                                                                   |
| <h4>500</h4>     | Errore interno del server                                                                 | Se persistente, contattare il provider                                                                                                                                                                                                                                                                                                                                                                                              |
| <h4>501</h4>     | Funzionalità richiesta non supportata dal server                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <h4>502</h4>     | Gateway o server proxy ha ricevuto una risposta non valida dal server remoto                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <h4>503</h4>     | Server temporaneamente sovraccarico o in manutenzione. Il ritardo può essere indicato nell'intestazione Retry-After |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <h4>504</h4>     | Gateway o proxy non ha ricevuto tempestivamente la risposta dal server remoto                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |



***



## Metodo per visualizzare gli errori nella console

* Premere <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> dopo aver fatto clic sulla finestra del client Cherry Studio (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- La finestra attiva deve essere quella del client Cherry Studio per aprire la console;
- È necessario aprire la console prima di eseguire test o avviare conversazioni per raccogliere le informazioni.
{% endhint %}

* Nella console che appare, fare clic su <mark style="color:blue;">`Network`</mark> → Cercare l'ultimo <mark style="color:red;">`completions`</mark> contrassegnato con <mark style="color:red;">`×`</mark> rosso (per errori in conversazioni/traduzioni) o <mark style="color:red;">`generations`</mark> (errori in disegni) → Fare clic su <mark style="color:blue;">`Response`</mark> per vedere il contenuto completo (area ④ nell'immagine).

> Se non è possibile identificare la causa, inviare uno screenshot nel [gruppo ufficiale](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Questo metodo funziona anche per test di modelli, aggiunta di knowledge base, disegni, ecc. Bisogna sempre aprire la console prima di eseguire le operazioni.

{% hint style="info" %}
I nomi nella colonna Name (②) variano per scenario

Conversazioni/traduzioni/test: <mark style="color:red;">`completions`</mark>&#x20;

Disegni: <mark style="color:red;">`generations`</mark>

Creazione knowledge base: <mark style="color:red;">`embeddings`</mark>&#x20;
{% endhint %}

***



## Formule non renderizzate/errori di rendering

* Se le formule non vengono renderizzate (mostrano solo codice), verificare i delimitatori:

> **Uso dei delimitatori**
>
> _Formula in linea_
>
> * Usare un singolo dollaro: `$formula$`
> * Oppure `\(formula\)`
>
>
>
> _Blocco formula_
>
> * Usare doppio dollaro: `$$formula$$`
> * Oppure `\[formula\]`
> * Esempio: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Errori di rendering/caratteri errati (comuni con testo cinese nelle formule): cambiare motore di rendering in KateX.



***



## Impossibile creare knowledge base/errore di acquisizione dimensioni embedding

1. Modello non disponibile

> Verificare col provider il supporto o lo stato del modello.

2. Uso di modelli non di embedding

***

## Modello non riconosce immagini/impossibile caricare o selezionare immagini

Verificare innanzitutto se il modello supporta il riconoscimento immagini. Cherry Studio classifica i modelli popolari: l'icona 👁️ accanto al nome indica il supporto immagini.

I modelli con supporto immagini permettono il caricamento di file. Se la funzionalità non è corretta, accedere all'elenco modelli del provider, trovare il modello e attivare l'opzione immagini tramite l'icona delle impostazioni.

Le specifiche dei modelli sono consultabili presso i provider. Modelli senza supporto visivo non funzionano anche con l'opzione attivata.