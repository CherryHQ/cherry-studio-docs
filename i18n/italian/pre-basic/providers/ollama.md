
{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Ollama

Ollama è un eccellente strumento open source che permette di eseguire e gestire facilmente vari modelli linguistici di grandi dimensioni (LLMs) in locale. Cherry Studio ora supporta l'integrazione con Ollama, consentendoti di interagire con LLM implementati localmente direttamente nell'interfaccia familiare, senza dipendere da servizi cloud!

## Cos'è Ollama?

Ollama è uno strumento che semplifica l'implementazione e l'utilizzo dei grandi modelli linguistici (LLM). Offre le seguenti caratteristiche:

* **Esecuzione locale:** I modelli vengono eseguiti completamente sul tuo computer locale, senza necessità di connessione Internet, proteggendo la tua privacy e sicurezza dei dati.
* **Facilità d'uso:** Con semplici comandi da terminale, puoi scaricare, eseguire e gestire vari LLM.
* **Amplia gamma di modelli:** Supporta molti modelli open source popolari come Llama 2, Deepseek, Mistral, Gemma.
* **Multi-piattaforma:** Compatibile con macOS, Windows e sistemi Linux.
* **API aperta:** Supporta un'interfaccia compatibile con OpenAI, consentendo l'integrazione con altri strumenti.

## Perché usare Ollama su Cherry Studio?

* **Nessun servizio cloud:** Liberati dai limiti di quote e costi delle API cloud, sfruttando appieno la potenza degli LLM locali.
* **Privacy dei dati:** Tutti i dati delle conversazioni rimangono locali, eliminando preoccupazioni sulla riservatezza.
* **Disponibilità offline:** Interagisci con gli LLM anche senza connessione Internet.
* **Personalizzazione:** Scegli e configura l'LLM più adatto alle tue esigenze specifiche.

## Configurazione di Ollama su Cherry Studio

### **1. Installazione ed esecuzione di Ollama**

Per prima cosa, installa ed esegui Ollama sul tuo computer seguendo questi passaggi:

*   **Scarica Ollama:** Visita il sito ufficiale ([https://ollama.com/](https://ollama.com/)) e scarica il pacchetto per il tuo sistema operativo.\
    Su Linux, installa direttamente con il comando:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Installa Ollama:** Completa l'installazione seguendo le istruzioni del programma.
*   **Scarica un modello:** Apri il terminale (o prompt dei comandi) e usa il comando `ollama run` per scaricare il modello desiderato. Ad esempio, per Llama 2:

    ```sh
    ollama run llama3.2
    ```

    Ollama scaricherà ed eseguirà automaticamente il modello.
* **Mantieni Ollama in esecuzione:** Assicurati che Ollama rimanga attivo mentre usi Cherry Studio per interagire con i modelli.

### **2. Aggiunta di Ollama come fornitore su Cherry Studio**

Aggiungi Ollama come fornitore di servizi AI personalizzati su Cherry Studio:

* **Apri impostazioni:** Nella barra di navigazione laterale, clicca sull'icona "Impostazioni" (ingranaggio).
* **Vai a servizi modello:** Nella pagina delle impostazioni, seleziona la scheda "Servizi Modello".
* **Aggiungi fornitore:** Cerca Ollama nell'elenco e cliccalo.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configurazione del fornitore Ollama**

Configura i dettagli del servizio Ollama nell'elenco fornitori:

1. **Stato attivazione:**
   * Attiva l'interruttore sulla destra del fornitore Ollama per abilitarlo.
2. **Chiave API:**
   * Di default, Ollama **non richiede** chiave API. Lascia il campo vuoto o inserisci qualsiasi valore.
3. **Indirizzo API:**
   *    Inserisci l'indirizzo API locale di Ollama. Solitamente:

       ```
       http://localhost:11434/
       ```

       Modificalo se hai cambiato la porta.
4. **Tempo di mantenimento:** Specifica la durata della sessione in minuti. Cherry Studio interromperà automaticamente la connessione dopo inattività.
5. **Gestione modelli:**
   * Clicca "+ Aggiungi" per inserire manualmente i nomi dei modelli già scaricati su Ollama.
   * Esempio: dopo `ollama run llama3.2`, inserisci `llama3.2`
   * Usa il pulsante "Gestisci" per modificare o eliminare i modelli aggiunti.

## Iniziare a utilizzare

Al termine della configurazione, nella chat di Cherry Studio potrai selezionare il fornitore Ollama e il modello scaricato per iniziare conversazioni con LLM locali!

## Consigli utili

* **Primo avvio del modello:** Al primo utilizzo, Ollama impiegherà tempo per scaricare i file del modello.
* **Elenco modelli disponibili:** Esegui `ollama list` nel terminale per vedere i modelli scaricati.
* **Requisiti hardware:** Gli LLM richiedono risorse computazionali (CPU, RAM, GPU). Verifica la compatibilità del tuo computer.
* **Documentazione Ollama:** Clicca su `Visualizza documentazione e modelli Ollama` nelle impostazioni per accedere rapidamente al sito ufficiale.