---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Guida alla Configurazione di Obsidian

Cherry Studio supporta l'integrazione con Obsidian per esportare intere conversazioni o singoli messaggi nella tua libreria di Obsidian.

{% hint style="warning" %}
Questo processo non richiede l'installazione di plugin aggiuntivi di Obsidian. Tuttavia, poiché il principio utilizzato da Cherry Studio per l'importazione in Obsidian è simile a Obsidian Web Clipper, si consiglia di aggiornare Obsidian all'ultima versione (attualmente almeno superiore a **1.7.2**) per evitare [problemi di importazione per conversazioni troppo lunghe](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Guida Aggiornata

{% hint style="info" %}
Rispetto alla vecchia versione per l'esportazione in Obsidian, la nuova funzionalità seleziona automaticamente il percorso della libreria, senza richiedere l'inserimento manuale del nome della libreria o della cartella.
{% endhint %}

### Passo 1: Configurare Cherry Studio

Apri _Impostazioni_ → _Impostazioni Dati_ → Menu _Configurazione Obsidian_ in Cherry Studio. I nomi delle librerie Obsidian aperte localmente appariranno automaticamente nel menu a tendina. Seleziona la tua libreria Obsidian target:

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Passo 2: Esportare le Conversazioni

#### Esportare un'intera conversazione

Torna all'interfaccia di conversazione di Cherry Studio. Fai clic destro su una conversazione, seleziona _Esporta_ e clicca _Esporta in Obsidian_:

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Apparirà una finestra per configurare le **Properties (proprietà)** della nota, la **posizione della cartella** in Obsidian e le **modalità di elaborazione**:

* **Vault**: Seleziona altre librerie Obsidian dal menu a tendina
* **Percorso**: Seleziona la cartella di destinazione dalla quale salvare la nota della conversazione
* Proprietà della nota Obsidian:
  * Tag (tags)
  * Data di creazione (created)
  * Origine (source)
* **Modalità di elaborazione** disponibili:
  * **Nuova (sovrascrivi se esiste)**: Crea una nuova nota nella cartella specificata, sovrascrivendo eventuali note esistenti con lo stesso nome
  * **Aggiungi all'inizio**: Aggiunge il contenuto selezionato all'inizio di una nota esistente con lo stesso nome
  * **Aggiungi alla fine**: Aggiunge il contenuto selezionato alla fine di una nota esistente con lo stesso nome

{% hint style="info" %}
Solo la prima modalità include le Properties (proprietà), le altre due modalità non le includono.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Configura le proprietà della nota</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Seleziona il percorso</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Seleziona la modalità di elaborazione</p></figcaption></figure>

Dopo aver selezionato tutte le opzioni, clicca su OK per esportare l'intera conversazione nella cartella corrispondente della tua libreria Obsidian.

#### Esportare un singolo messaggio

Per esportare un singolo messaggio, clicca sul menu _Tre linee_ sotto il messaggio, seleziona _Esporta_ e clicca _Esporta in Obsidian_:

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Esportare un singolo messaggio</p></figcaption></figure>

Apparirà la stessa finestra della sezione precedente per configurare le proprietà e le modalità di elaborazione. Segui le stesse istruzioni descritte sopra per [Esportare un'intera conversazione](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Esportazione Completata

🎉 Complimenti! Hai completato la configurazione dell'integrazione tra Cherry Studio e Obsidian e hai eseguito con successo l'intero processo di esportazione. Enjoy yourselves!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Esportato in Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Visualizza il risultato dell'esportazione</p></figcaption></figure>

***

## Vecchia Guida (per Cherry Studio <v1.1.13)

### Passo 1: Preparare Obsidian

Apri la tua libreria Obsidian e crea una `cartella` per salvare le conversazioni esportate (nell'esempio la cartella si chiama Cherry Studio):

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Prendi nota del nome evidenziato nell'angolo inferiore sinistro: questo è il nome del tuo `vault`.

### Passo 2: Configurare Cherry Studio

In _Impostazioni_ → _Impostazioni Dati_ → _Configurazione Obsidian_ di Cherry Studio, inserisci il nome del `vault` e della `cartella` ottenuti nel [Passo 1](obsidian.md#di-yi-bu):

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

Il campo `Tag globali` è opzionale: qui puoi impostare i tag applicati a tutte le conversazioni esportate in Obsidian.

### Passo 3: Esportare le Conversazioni

#### Esportare un'intera conversazione

Torna all'interfaccia di conversazione di Cherry Studio. Fai clic destro su una conversazione, seleziona _Esporta_ e clicca _Esporta in Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Esportare un'intera conversazione</p></figcaption></figure>

Apparirà una finestra per configurare le **Properties (proprietà)** della nota e le **modalità di elaborazione** disponibili:

* **Nuova (sovrascrivi se esiste)**: Crea una nuova nota nella `cartella` specificata nel [Passo 2](obsidian.md#di-er-bu), sovrascrivendo eventuali note esistenti con lo stesso nome
* **Aggiungi all'inizio**: Aggiunge il contenuto selezionato all'inizio di una nota esistente con lo stesso nome
* **Aggiungi alla fine**: Aggiunge il contenuto selezionato alla fine di una nota esistente con lo stesso nome

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Configura le proprietà della nota</p></figcaption></figure>

{% hint style="info" %}
Solo la prima modalità include le Properties (proprietà), le altre due modalità non le includono.
{% endhint %}

#### Esportare un singolo messaggio

Per esportare un singolo messaggio, clicca sul menu _Tre linee_ sotto il messaggio, seleziona _Esporta_ e clicca _Esporta in Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Esportare un singolo messaggio</p></figcaption></figure>

Apparirà la stessa finestra della sezione precedente. Segui le stesse istruzioni descritte sopra per [Esportare un'intera conversazione](obsidian.md#dao-chu-wan-zheng-dui-hua).

### Esportazione Completata

🎉 Complimenti! Hai completato la configurazione dell'integrazione tra Cherry Studio e Obsidian e hai eseguito con successo l'intero processo di esportazione. Enjoy yourselves!

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Esportato in Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Visualizza il risultato dell'esportazione</p></figcaption></figure>