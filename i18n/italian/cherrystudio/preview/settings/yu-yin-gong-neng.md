---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Funzionalità Vocali

```
Guida all'uso delle funzionalità vocali di Cherry Studio

1. Panoramica delle funzionalità vocali

Cherry Studio offre tre principali moduli di funzionalità vocali: TTS (Testo a Voce), ASR (Riconoscimento Vocale) e Chiamata Vocale. Queste funzionalità consentono di interagire naturalmente con l'IA tramite la voce, migliorando l'esperienza d'uso.

- TTS (Testo a Voce): converte le risposte testuali dell'IA in output vocali
- ASR (Riconoscimento Vocale): converte la tua voce in input testuali
- Chiamata Vocale: combina TTS e ASR per un'esperienza di dialogo vocale simile a ChatGPT

2. Funzione TTS (Testo a Voce)

1. Tipi di servizi supportati

Cherry Studio supporta quattro tipi di servizi TTS:

- OpenAI: utilizza l'API TTS di OpenAI, richiede chiave API
- TTS del browser: utilizza la sintesi vocale integrata del browser, gratuito e senza configurazione
- Siliconflow: utilizza il servizio TTS di Siliconflow, richiede chiave API
- TTS online gratuito: utilizza servizi TTS online gratuiti, nessuna chiave API necessaria

2. Metodo di configurazione

1) Accedi alla pagina delle impostazioni, seleziona la scheda "Funzionalità Vocali"
2) Nella sottoscheda "TTS":
   - Abilita la funzione TTS (attiva l'interruttore)
   - Seleziona il tipo di servizio TTS
   - Configura i parametri in base al servizio selezionato:
     - OpenAI: inserisci chiave API, indirizzo API, seleziona voce e modello
     - TTS del browser: seleziona la voce
     - Siliconflow: inserisci chiave API, indirizzo API, seleziona voce, modello, formato di risposta e velocità
     - TTS online gratuito: seleziona voce e formato di output
3) Configura le opzioni di filtraggio TTS (opzionale):
   - Filtra il processo di ragionamento
   - Filtra i marcatori Markdown
   - Filtra i blocchi di codice
4) Imposta se visualizzare la barra di avanzamento TTS
5) Clicca sul pulsante "Test TTS" per verificare la configurazione

3. Metodo di utilizzo

- Con TTS attivato, le risposte dell'IA verranno automaticamente convertite in output vocale
- Nell'interfaccia di chat, sotto ogni risposta dell'IA verrà visualizzato un pulsante di riproduzione TTS
- Clicca sul pulsante per riprodurre/mettere in pausa la voce
- Se la barra di avanzamento TTS è abilitata, verrà visualizzato il progresso sotto il testo
- I testi lunghi verranno sintetizzati e riprodotti in segmenti consecutivi

3. Funzione ASR (Riconoscimento Vocale)

1. Tipi di servizi supportati

Cherry Studio supporta tre tipi di servizi ASR:

- OpenAI: utilizza il modello Whisper di OpenAI, richiede chiave API
- Browser: utilizza il riconoscimento vocale integrato del browser, gratuito e senza configurazione
- Server locale: si connette a un server WebSocket locale per il riconoscimento vocale

2. Metodo di configurazione

1) Accedi alla pagina delle impostazioni, seleziona la scheda "Funzionalità Vocali"
2) Nella sottoscheda "ASR":
   - Abilita la funzione ASR (attiva l'interruttore)
   - Seleziona il tipo di servizio ASR
   - Configura i parametri in base al servizio selezionato:
     - OpenAI: inserisci chiave API, indirizzo API, seleziona modello
     - Browser: nessuna configurazione aggiuntiva
     - Server locale: puoi impostare se avviare automaticamente il server ASR all'avvio dell'app
   - Seleziona la lingua di riconoscimento vocale (predefinita: cinese)
3) Clicca sul pulsante "Test ASR" per verificare la configurazione

3. Metodo di utilizzo

- Con ASR attivato, apparirà un pulsante di riconoscimento vocale accanto al campo di input
- Clicca sul pulsante per iniziare la registrazione
- Dopo aver parlato, la voce verrà convertita in testo e inserita nel campo di input
- Clicca nuovamente il pulsante per terminare la registrazione
- Il riconoscimento vocale supporta più frasi consecutive in modalità cumulativa

4. Funzione di Chiamata Vocale

1. Caratteristiche principali

- Combina TTS e ASR per un'esperienza di dialogo vocale simile a ChatGPT
- Utilizza un'interfaccia a finestra fluttuante trascinabile
- Supporta la modalità "premi per parlare"
- Supporta scorciatoie personalizzate
- Supporta l'opzione di compattare la finestra
- Possibilità di selezionare modelli dedicati per le chiamate vocali
- Supporto per prompt personalizzati

2. Metodo di configurazione

1) Accedi alla pagina delle impostazioni, seleziona la scheda "Funzionalità Vocali"
2) Nella sottoscheda "Funzione Chiamata":
   - Abilita la funzione di chiamata vocale (attiva l'interruttore)
   - Clicca su "Seleziona Modello" per scegliere il modello IA per le chiamate vocali
   - Personalizza il prompt vocale nel campo di testo (opzionale)
   - Clicca "Salva" per memorizzare il prompt o "Ripristina" per reimpostare quello predefinito

3. Metodo di utilizzo

1) Nell'interfaccia di chat, clicca sul pulsante di chiamata vocale (icona telefono) a destra del campo di input
2) Si aprirà la finestra di chiamata vocale e verrà riprodotto un messaggio di benvenuto
3) Tieni premuto il pulsante "Premi per parlare" per iniziare la registrazione (o usa la scorciatoia)
4) Rilascia il pulsante per terminare la registrazione e inviare all'IA
5) L'IA genererà una risposta che verrà riprodotta via TTS
6) Usa i pulsanti di controllo nella finestra:
   - Pulsante Muto/Attiva suono: controlla l'output TTS
   - Pulsante Pausa/Riprendi: sospende o riprende la conversazione
   - Pulsante Impostazioni: configura le scorciatoie
   - Pulsante Comprimi: riduce la finestra mantenendo solo la riga "Premi per parlare"
7) Clicca sul pulsante Chiudi per terminare la chiamata

4. Configurazione delle scorciatoie

1) Nella finestra di chiamata vocale, clicca sul pulsante Impostazioni
2) Nel pannello delle impostazioni, clicca sul pulsante Scorciatoia
3) Premi il tasto che desideri impostare (es. barra spaziatrice, Shift, ecc.)
4) Clicca "Salva" per memorizzare le impostazioni
5) Durante l'uso, tieni premuta la scorciatoia per iniziare la registrazione, rilascia per terminare e inviare

5. Problemi comuni e soluzioni

1. Problemi relativi al TTS

- Problema: TTS non riproduce suono
  Soluzione: verifica se la funzione TTS è attiva, controlla il tipo di servizio selezionato e i parametri necessari

- Problema: scarsa qualità della riproduzione TTS
  Soluzione: prova a cambiare tipo di servizio TTS o voce

- Problema: durante la riproduzione TTS appare un messaggio di errore
  Soluzione: controlla la correttezza della chiave API e la connessione di rete

2. Problemi relativi all'ASR

- Problema: ASR non riconosce la voce
  Soluzione: verifica se la funzione ASR è attiva, controlla il tipo di servizio selezionato e i parametri necessari

- Problema: bassa accuratezza del riconoscimento ASR
  Soluzione: prova a cambiare tipo di servizio ASR, o regola posizione e volume del microfono

- Problema: connessione al server ASR fallita
  Soluzione: controlla se il server locale è in esecuzione, o riavvia l'applicazione

3. Problemi relativi alla chiamata vocale

- Problema: impossibile aprire la finestra di chiamata vocale
  Soluzione: verifica se la funzione chiamata vocale è attiva, assicurati che TTS e ASR siano configurati correttamente

- Problema: nessuna risposta al tasto "Premi per parlare"
  Soluzione: controlla se sono stati concessi i permessi al microfono, o riavvia la chiamata vocale

- Problema: nessun output vocale dalle risposte dell'IA
  Soluzione: controlla se la funzione TTS è attiva e che non sia impostata su muto

6. Impostazioni avanzate e opzioni personalizzate

1. Impostazioni avanzate TTS

- Opzioni di filtraggio: possibile filtrare ragionamenti, marcatori Markdown e blocchi codice
- Visualizzazione barra avanzamento: possibile attivare/disattivare la visualizzazione
- Voci e modelli personalizzati: possibile aggiungere opzioni personalizzate

2. Impostazioni avanzate ASR

- Avvio automatico server: possibile impostare l'avvio automatico del server ASR all'avvio dell'app
- Selezione lingua: possibile scegliere diverse lingue per il riconoscimento vocale

3. Impostazioni avanzate chiamata vocale

- Prompt personalizzati: possibile personalizzare le istruzioni vocali per guidare le risposte dell'IA
- Selezione modelli dedicati: possibile scegliere modelli IA specifici per le chiamate vocali
- Personalizzazione scorciatoie: possibile impostare scorciatoie personalizzate per il controllo della registrazione

7. Suggerimenti per l'uso

1. Scegli il servizio TTS adatto:
   - Per alta qualità vocale: consigliati OpenAI o Siliconflow
   - Senza configurazione API: utilizza TTS del browser o TTS online gratuito

2. Scegli il servizio ASR adatto:
   - Per alta accuratezza: consigliato OpenAI
   - Senza configurazione API: utilizza il riconoscimento vocale integrato nel browser

3. Ottimizza l'esperienza di chiamata vocale:
   - Usa cuffie per evitare che l'output TTS venga catturato nuovamente dall'ASR
   - Utilizza in ambienti silenziosi per migliorare l'accuratezza del riconoscimento
   - Usa prompt personalizzati per adattare le risposte dell'IA alla riproduzione vocale

4. Personalizza le impostazioni in base alle esigenze:
   - Per interazioni testuali predominanti: attiva solo TTS
   - Per input vocali predominanti: attiva solo ASR
   - Per esperienza vocale completa: attiva la funzione di chiamata vocale

Speriamo che questa guida ti aiuti a sfruttare appieno le funzionalità vocali di Cherry Studio per un'esperienza IA più naturale e intuitiva!
```