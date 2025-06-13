---
icon: book-bookmark
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Conoscenze Scientifiche

## Cosa sono i tokens?

I tokens sono le unità fondamentali con cui i modelli di IA elaborano il testo, pensali come le unità minime di "pensiero" del modello. Non corrispondono esattamente a caratteri o parole come le intendiamo noi, ma rappresentano un metodo speciale di segmentazione del testo proprio del modello.

#### 1. Segmentazione del cinese
* Un carattere cinese viene tipicamente codificato in 1-2 tokens
* Esempio: `"你好"` ≈ 2-4 tokens

#### 2. Segmentazione dell'inglese
* Le parole comuni usano generalmente 1 token
* Parole lunghe o inconsuete vengono suddivise in più tokens
* Esempio:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Caratteri speciali
* Spazi, punteggiatura e simboli occupano tokens
* Un carattere di nuova riga usa tipicamente 1 token

{% hint style="info" %}
I Tokenizer variano tra fornitori di servizi diversi e persino tra modelli dello stesso fornitore. Queste informazioni servono solo a chiarire il concetto di token.
{% endhint %}

***

## Cos'è il Tokenizer?

Il Tokenizer è lo strumento che converte il testo in tokens per i modelli di IA. Determina come suddividere il testo in unità minime comprensibili dal modello.

### Perché i Tokenizer variano tra modelli diversi?

#### 1. Dati di addestramento diversi
* Diversi corpus portano a ottimizzazioni differenti
* Vario supporto multilingue
* Ottimizzazioni specializzate per ambiti specifici (medicina, legge, ecc.)

#### 2. Algoritmi di segmentazione diversi
* BPE (Byte Pair Encoding) - serie GPT di OpenAI
* WordPiece - Google BERT
* SentencePiece - adatto a scenari multilingue

#### 3. Obiettivi di ottimizzazione diversi
* Alcuni focalizzati sull'efficienza di compressione
* Altri sulla conservazione semantica
* Altri sulla velocità di elaborazione

### Impatto pratico

Lo stesso testo può produrre conteggi di token diversi in modelli diversi:

```
Input: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## Cos'è un Modello di Embedding (Embedding Model)?

**Concetto base:** L'embedding model è una tecnica che converte dati discreti ad alta dimensionalità (testo, immagini ecc.) in vettori continui a bassa dimensionalità. Questa conversione aiuta le macchine a comprendere e processare dati complessi. Immaginalo come semplificare un puzzle complesso in coordinate puntuali che conservano le caratteristiche essenziali. Nell'ecosistema dei grandi modelli, funge da "traduttore" convertendo informazioni umane in forme numeriche calcolabili dall'IA.

**Funzionamento:** Nell'elaborazione del linguaggio naturale, i modelli di embedding mappano le parole a posizioni specifiche nello spazio vettoriale. In questo spazio, parole semanticamente affini si raggruppano naturalmente. Esempi:
* I vettori di "re" e "regina" saranno vicini
* Parole come "gatto" e "cane" si posizioneranno vicine
* Parole senza relazione semantica come "auto" e "pane" saranno distanti

**Principali applicazioni:**
* Analisi testuale: classificazione documenti, sentiment analysis
* Sistemi di raccomandazione: suggerimenti personalizzati
* Elaborazione immagini: ricerca di immagini simili
* Motori di ricerca: ottimizzazione ricerca semantica

**Vantaggi principali:**
1. Riduzione dimensionale: semplifica dati complessi in vettori gestibili
2. Conservazione semantica: mantiene informazioni chiave dai dati originali
3. Efficienza computazionale: migliora significativamente training e inferenza dei modelli

**Valore tecnico:** I modelli di embedding sono componenti fondamentali dei sistemi IA moderni, fornendo rappresentazioni di alta qualità per attività di machine learning e guidando progressi in NLP, computer vision e altri campi.

***

## Funzionamento dei Modelli di Embedding nella ricerca conoscitiva

**Flusso di lavoro base:**

1. **Fase di preprocessamento della knowledge base**
* Suddivisione documenti in chunk (blocchi di testo) di dimensioni appropriate
* Conversione di ogni chunk in vettori tramite embedding model
* Archiviazione di vettori e testo originale in database vettoriali

2. **Fase di elaborazione delle query**
* Conversione domande utente in vettori
* Ricerca di contenuti simili nel database vettoriale
* Fornitura dei contenuti rilevanti come contesto agli LLM

***

## Cos'è l'MCP (Model Context Protocol)?

L'MCP è un protocollo open source che standardizza la fornitura di informazioni contestuali ai grandi modelli linguistici (LLM).

* **Analogia:** Immagina l'MCP come una "chiavetta USB" per l'IA. Un server MCP può "collegare" vari "plugin" contestuali, permettendo agli LLM di richiederli quando necessario per arricchire le proprie capacità.
* **Confronto con Function Tool:** I tradizionali Function Tool forniscono funzionalità esterne, ma l'MCP rappresenta un'astrazione di livello superiore. Mentre i Function Tool risolvono task specifici, l'MCP offre un meccanismo contestuale modulare e universale.

### Vantaggi chiave dell'MCP

1. **Standardizzazione:** Offre interfacce e formati dati unificati per collaborazione senza attriti
2. **Modularità:** Consente di scomporre informazioni contestuali in moduli (plugin) indipendenti
3. **Flessibilità:** Permette agli LLM di selezionare dinamicamente i plugin contestuali necessari
4. **Scalabilità:** Supporta l'aggiunta futura di nuovi tipi di plugin contestuali