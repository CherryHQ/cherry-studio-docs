---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Accesso alla rete con Volcano Engine

### 1. Accesso/registrazione dell'account "Volcano Engine" <a href="#rclz7" id="rclz7"></a>

Visita il sito ufficiale: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Sito ufficiale di Volcano Engine</p></figcaption></figure>

### 2. Creazione dell'applicazione "Può connettersi in rete" <a href="#gvzaa" id="gvzaa"></a>

2.1 Accedi a Volcano Engine e accedi alla pagina "Volcano Ark": [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2 **Fai clic in sequenza su:** <mark style="color:red;">**「Le mie applicazioni」 - 「Crea applicazione」 - 「Zero codice」 - 「Chat one-to-one」**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Compilazione delle informazioni e pubblicazione dell'applicazione <a href="#zzdfe" id="zzdfe"></a>

**Nome applicazione**: Scegli un nome qualsiasi come richiesto. (Solo i campi contrassegnati con <mark style="color:red;">**\* sono obbligatori**</mark>, gli altri possono essere omessi)

<mark style="color:red;">**Punto chiave: attivare il plugin di connessione (richiede attivazione preventiva)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1 Attivazione della funzionalità del plugin di connessione (attenzione ai costi e al limite gratuito) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Clicca su "Acquista ora", segui i passaggi fino a visualizzare questa schermata, indicando che l'attivazione è riuscita.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Controlla lo stato: a questo punto l'attivazione è completata</p></figcaption></figure>

Torna quindi all'interfaccia "Compila informazioni applicazione" per continuare.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2 Spiegazioni sulla "Configurazione avanzata" della ricerca in rete <a href="#sp6uz" id="sp6uz"></a>

Scegli in base alle tue esigenze, suggerimenti personali:

* Per un controllo preciso di input/output, usa la connessione "**Chiamata personalizzata**";
* Per semplicità, mantieni "**Chiamata automatica**" - valore predefinito;
* Per informazioni ad alta tempestività (senza problemi di budget), scegli "**Forza attivazione**".

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3 Pubblicazione dell'applicazione <a href="#fe1gf" id="fe1gf"></a>

Clicca sul pulsante "Pubblica" in alto a destra: creazione applicazione completata.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Ottenimento della chiave API <a href="#jtqlu" id="jtqlu"></a>

Procedi in sequenza: **「Guida chiamate API」-「Seleziona e copia API Key」-「Visualizza e seleziona」**

Copia la API key, poi incollala in Cherry Studio. (Dettagli operativi nell'interfaccia seguente)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Nota: se non hai una API key, clicca su "**Crea API Key**" nell'angolo superiore destro della finestra popup, quindi copia la chiave API.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Uso della chiave API in Cherry Studio per l'accesso in rete a DeepSeek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1 Apri Cherry Studio - 「Impostazioni」- 「Nome arbitrario」-「Tipo: openAI」 <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2 Configurazione di URL e chiave <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Nota: se non trovi l'indirizzo o non è il nodo di Pechino, puoi trovare l'URL specifico qui. Attenzione a non dimenticare "/":</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3 Aggiungi il nome del modello <a href="#qmh3i" id="qmh3i"></a>

Copia il testo in piccolo come nome modello, altrimenti genererà errori.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Anteprima del risultato <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>