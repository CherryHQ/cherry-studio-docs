---
icon: book-open-cover
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Tutorial sulla Knowledge Base

Nella versione 0.9.1, CherryStudio introduce la tanto attesa funzionalità di Knowledge Base.

Di seguito presenteremo le istruzioni dettagliate per l'utilizzo di CherryStudio, passo dopo passo.

## Aggiungere modelli di embedding

1. Cerca i modelli nel servizio di gestione dei modelli, puoi cliccare su "Modelli di embedding" per filtrare rapidamente;
2. Trova il modello necessario e aggiungilo ai miei modelli.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Creare una Knowledge Base

1. Accesso alla Knowledge Base: nella barra degli strumenti laterale di CherryStudio, clicca sull'icona della Knowledge Base per accedere alla pagina di gestione;
2. Aggiungi Knowledge Base: clicca su Aggiungi per iniziare a creare una Knowledge Base;
3. Assegna un nome: inserisci il nome della Knowledge Base e aggiungi un modello di embedding, ad esempio bge-m3, per completare la creazione.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Aggiungere file e vettorializzazione

1. Aggiungi file: clicca sul pulsante per aggiungere file per aprire la selezione file;
2. Seleziona file: scegli i formati supportati come pdf, docx, pptx, xlsx, txt, md, mdx, e apri;
3. Vettorializzazione: il sistema eseguirà automaticamente la vettorializzazione. Quando viene visualizzato il completamento (✓ verde), significa che la vettorializzazione è terminata.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Aggiungere dati da più fonti

CherryStudio supporta vari metodi per aggiungere dati:

1. Directory di cartelle: puoi aggiungere un'intera directory di cartelle, i file nei formati supportati verranno vettorializzati automaticamente;
2. Collegamenti web: supporta URL di siti web, come [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3. Mappe del sito: supporta mappe del sito in formato XML, come [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4. Note di testo semplice: supporta l'inserimento di contenuti personalizzati in testo semplice.

{% hint style="info" %}
Suggerimenti:

1. Le illustrazioni nei documenti importati nella Knowledge Base non sono attualmente convertibili in vettori: richiedono conversione manuale in testo;
2. L'utilizzo di URL come fonte per la Knowledge Base potrebbe non avere sempre successo. Alcuni siti hanno meccanismi anti-scraping rigorosi (o richiedono accesso/autorizzazioni), quindi questo metodo potrebbe non recuperare contenuti accurati. Dopo la creazione, si consiglia di effettuare una ricerca di prova;
3. Generalmente i siti web forniscono sitemap, come quella di CherryStudio [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml). Tipicamente si può ottenere aggiungendo `/sitemap.xml` all'indirizzo root del sito (URL). Es. `aaa.com/sitemap.xml`;
4. Se il sito non fornisce sitemap o gli URL sono complessi, è possibile creare manualmente un file XML sitemap. Il file deve essere accessibile pubblicamente tramite un collegamento diretto, i collegamenti a file locali non vengono riconosciuti.

> 1) Puoi chiedere all'AI di generare il file sitemap o creare uno strumento generatore HTML di sitemap;
> 2) Per i collegamenti diretti, puoi utilizzare servizi OSS o cloud storage. Se non disponi di strumenti esistenti, visita il sito ufficiale [ocoolAI](https://one.ocoolai.com/login), accedi e utilizza lo strumento di caricamento file gratuito nella barra superiore per generare collegamenti diretti.
{% endhint %}

## Cercare nella Knowledge Base

Quando la vettorializzazione di file e dati è completata, puoi effettuare ricerche:

1. Clicca sul pulsante "Cerca nella Knowledge Base" in fondo alla pagina;
2. Inserisci il contenuto della ricerca;
3. Vengono presentati i risultati della ricerca;
4. Viene mostrato il punteggio di corrispondenza per ciascun risultato.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Utilizzare la Knowledge Base nelle conversazioni per generare risposte

1. Crea una nuova conversazione, nella barra degli strumenti della chat clicca su "Knowledge Base": apparirà l'elenco delle Knowledge Base create, seleziona quella da utilizzare;
2. Inserisci e invia la domanda: il modello restituirà una risposta generata dai risultati della ricerca;
3. Inoltre, le fonti dei dati citati vengono allegate sotto la risposta per una rapida consultazione del documento originale.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>