---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Modalità Internet

{% hint style="info" %}
Esempi di scenari che richiedono la connessione a Internet:

* Informazioni tempestive: ad esempio i prezzi dei futures sull'oro di oggi/questa settimana/da poco.
* Dati in tempo reale: come il meteo, i tassi di cambio e altri valori dinamici.
* Conoscenze emergenti: come nuove entità, nuovi concetti, nuove tecnologie, ecc.
{% endhint %}

### 1. Come attivare la modalità Internet

Nella finestra di domanda di Cherry Studio, fai clic sull'icona 【Piccolo globo】 per attivare la connessione a Internet.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Fai clic sull'icona del globo - Attiva la connessione</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Indica - Funzione di connessione attivata</p></figcaption></figure>

### 2. Attenzione: Esistono due modalità di accesso a Internet

#### Modalità 1: Funzione di connessione integrata nel modello dell'operatore

In questo caso, dopo aver attivato la connessione, puoi utilizzare direttamente il servizio Internet in modo molto semplice.

{% hint style="warning" %}
Puoi verificare rapidamente se il modello supporta la connessione controllando se accanto al nome del modello nell'interfaccia di domanda/risposta è presente un'icona di piccola mappa.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Anche nella pagina di gestione dei modelli, questo metodo ti consente di distinguere rapidamente quali modelli supportano la connessione e quali no.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Operatori di modelli con connessione attualmente supportati da Cherry Studio**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (tutti i modelli supportano la connessione)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian</mark>

{% hint style="danger" %}
Attenzione speciale:
Esiste una situazione particolare in cui anche se il modello non ha l'icona del piccolo globo, può comunque accedere a Internet, come spiegato nel tutorial qui sotto.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Modalità 2: Utilizzo del servizio Tavily per implementare la funzione di connessione

Quando utilizziamo un modello linguistico senza funzione di connessione (senza l'icona del piccolo globo accanto al nome) ma abbiamo bisogno di ottenere informazioni in tempo reale, è necessario utilizzare il servizio di ricerca web Tavily.

**Al primo utilizzo del servizio Tavily**, apparirà una finestra pop-up che chiederà di impostare alcune informazioni. Segui le istruzioni: è molto semplice!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Finestra pop-up, fai clic: Vai alle impostazioni</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Fai clic su: Ottieni chiave</p></figcaption></figure>

Dopo aver cliccato su "Ottieni chiave", verrai reindirizzato automaticamente alla pagina di **accesso/registrazione del sito ufficiale di Tavily**. Registrati, accedi, crea una chiave API e poi copiala in Cherry Studio.

{% hint style="danger" %}
Se non sai come registrarti, consulta il tutorial di registrazione Tavily nella stessa directory di questo documento.
{% endhint %}

**Documento di riferimento per la registrazione a Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

L'interfaccia sottostante indica che la registrazione è avvenuta con successo.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Copia la chiave</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Incolla la chiave: tutto fatto</p></figcaption></figure>

Proviamo di nuovo per vedere il risultato. Il test conferma che la ricerca web funziona correttamente, con il numero predefinito di risultati impostato su 5.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Nota: Tavily ha un limite mensile gratuito. Superato tale limite, è necessario pagare.
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Se notate errori, siete i benvenuti a contattarci in qualsiasi momento.