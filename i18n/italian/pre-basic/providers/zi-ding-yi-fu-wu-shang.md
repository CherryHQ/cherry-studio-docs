
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Provider Personalizzati

Cherry Studio non solo integra i principali servizi di modelli AI, ma ti offre anche potenti capacità di personalizzazione. Attraverso la funzione di **Provider AI Personalizzato**, puoi facilmente integrare qualsiasi modello AI di cui hai bisogno.

## Perché scegliere un Provider AI Personalizzato?

* **Flessibilità:** Non sei più limitato alla lista predefinita di provider: scegli liberamente il modello AI che meglio si adatta alle tue esigenze.
* **Varietà:** Sperimenta modelli AI da diverse piattaforme per scoprire i loro punti di forza unici.
* **Controllo:** Gestisci direttamente le tue chiavi API e gli indirizzi di accesso, garantendo sicurezza e privacy.
* **Personalizzazione:** Integra modelli implementati privatamente per soddisfare scenari aziendali specifici.

## Come aggiungere un Provider AI Personalizzato?

Con pochi semplici passaggi, puoi aggiungere il tuo Provider AI personalizzato a Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Apri le impostazioni:** Clicca sull'icona a forma di ingranaggio "Impostazioni" nella barra di navigazione laterale di Cherry Studio.
2. **Accedi ai servizi di modelli:** Nella pagina delle impostazioni, seleziona la scheda "Servizi modelli".
3. **Aggiungi un provider:** Nella pagina "Servizi modelli", troverai l'elenco dei provider esistenti. Clicca sul pulsante "+ Aggiungi" in fondo all'elenco per aprire la finestra modale.
4. **Compila le informazioni:** Completare i seguenti campi nella finestra modale:
   * **Nome provider:** Assegna un nome identificativo al tuo provider personalizzato (es. MyCustomOpenAI).
   * **Tipo provider:** Seleziona il tipo di provider dal menu a discesa. Attualmente supportiamo:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Salva la configurazione:** Clicca sul pulsante "Aggiungi" per salvare la configurazione.

## Configurazione di Provider AI Personalizzati

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Dopo l'aggiunta, individua il nuovo provider nell'elenco e configuralo nel dettaglio:

1. **Stato di attivazione:** All'estrema destra dell'elenco trovi un interruttore: quando è acceso, il servizio personalizzato è attivo.
2. **Chiave API:**
   * Inserisci la chiave API (API Key) fornita dal tuo provider AI.
   * Usa il pulsante "Verifica" a destra per testare la validità della chiave.
3. **Indirizzo API:**
   * Specifica l'URL di accesso all'API (Base URL).
   * Consulta sempre la documentazione ufficiale del provider per ottenere l'indirizzo corretto.
4. **Gestione modelli:**
   * Clicca "+ Aggiungi" per inserire manualmente gli ID dei modelli che desideri utilizzare (es. `gpt-3.5-turbo`, `gemini-pro`).

   <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

   * Consulta la documentazione ufficiale se non conosci il nome esatto del modello.
   * Usa il pulsante "Gestisci" per modificare o eliminare modelli esistenti.

## Inizia a utilizzare

Al termine della configurazione, nella sezione di chat di Cherry Studio potrai selezionare il tuo provider AI personalizzato e iniziare le conversazioni!

## Utilizzare vLLM come Provider AI Personalizzato

vLLM è una libreria di inferenza LLM semplice e veloce, simile a Ollama. Ecco come integrarlo in Cherry Studio:

1. **Installa vLLM:** Segui la documentazione ufficiale ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # Se usi pip
    uv pip install vllm # Se usi uv
    ```
2. **Avvia il servizio vLLM:** Utilizza l'interfaccia compatibile OpenAI di vLLM. Due modalità principali:

    * Avvio con `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Avvio con `uvicorn`

    ```sh
    vllm --model gpt2 --servered-model-name gpt2
    ```

Verifica che il servizio sia attivo sulla porta predefinita `8000`. Puoi specificare altre porte con il parametro `--port`.

3. **Aggiungi il provider vLLM in Cherry Studio:**
   * Segui la procedura standard per aggiungere un nuovo provider AI personalizzato.
   * **Nome provider:** `vLLM`
   * **Tipo provider:** Seleziona `OpenAI`.
4. **Configura il provider vLLM:**
   * **Chiave API:** Campo vuoto o valore arbitrario (vLLM non richiede chiave).
   * **Indirizzo API:** Specifica l'URL dell'API vLLM (predefinito: `http://localhost:8000/`).
   * **Gestione modelli:** Aggiungi il nome del modello caricato in vLLM. Nell'esempio precedente, inserire `gpt2`.
5. **Inizia a dialogare:** Seleziona il provider vLLM e il modello `gpt2` per iniziare conversazioni!

## Suggerimenti utili

* **Leggi la documentazione:** Prima di aggiungere un provider, consulta sempre la documentazione ufficiale per informazioni su chiavi API, URL e nomi modello.
* **Verifica le chiavi API:** Usa il pulsante "Verifica" per evitare errori di configurazione.
* **Attenzione agli URL API:** Gli indirizzi possono variare tra provider e modelli.
* **Gestione modelli intelligente:** Aggiungi solo i modelli effettivamente utilizzati per evitare sovraccarichi.