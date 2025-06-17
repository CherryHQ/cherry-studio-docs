---
icon: database
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Spiegazione sull'Archiviazione dei Dati

I dati aggiunti nella knowledge base di Cherry Studio vengono archiviati interamente in locale. Durante il processo di aggiunta, viene creata una copia del documento nella directory di archiviazione dati di Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Flusso di elaborazione della knowledge base</p></figcaption></figure>

Database vettoriale: [https://turso.tech/libsql](https://turso.tech/libsql)

Dopo che un documento viene aggiunto alla knowledge base di Cherry Studio:
1. Il file viene suddiviso in più segmenti
2. Questi segmenti vengono elaborati dal modello di embedding

Quando si utilizzano grandi modelli linguistici per rispondere alle domande:
1. Si eseguono ricerche di frammenti di testo rilevanti per la domanda
2. I frammenti selezionati vengono inviati al grande modello linguistico per l'elaborazione

Per requisiti di privacy dei dati, si consiglia di utilizzare:
- Database di embedding locale
- Grande modello linguistico locale