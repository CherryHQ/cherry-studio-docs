---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Vertex AI

## Panoramica del Tutorial

### 1. Ottenere la chiave API

* Prima di ottenere la chiave API Gemini, è necessario disporre di un progetto Google Cloud (puoi saltare questo passaggio se ne hai già uno)
* Accedi a [Google Cloud](https://console.cloud.google.com/projectcreate) per creare un progetto, inserisci il nome del progetto e fai clic su "Crea progetto"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Accedi alla [console Vertex AI](https://console.cloud.google.com/vertex-ai)
* Attiva [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) nel progetto creato

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Configurare le autorizzazioni di accesso API

* Apri la pagina delle autorizzazioni degli [account del servizio](https://console.cloud.google.com/iam-admin/serviceaccounts) e crea un account del servizio

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Nella pagina di gestione degli account del servizio, trova l'account appena creato, fai clic su `Chiavi` e crea una nuova chiave in formato JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Dopo la creazione, il file della chiave verrà salvato automaticamente sul tuo computer in formato JSON, **conservalo con cura**

## 3. Configurare Vertex AI in Cherry Studio

* Seleziona il provider di servizi Vertex AI
* Completa i campi corrispondenti dal file JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Fai clic su Aggiungi [modelli](https://console.cloud.google.com/vertex-ai/model-garden) e puoi iniziare a usarlo con piacere!