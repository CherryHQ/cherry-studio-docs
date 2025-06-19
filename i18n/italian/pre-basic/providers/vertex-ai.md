---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Vertex AI

## Panoramica del Tutorial

### 1. Ottenere la Chiave API

* Prima di ottenere la chiave API per Gemini, è necessario avere un progetto Google Cloud (se ne hai già uno, puoi saltare questo passaggio)
* Vai su [Google Cloud](https://console.cloud.google.com/projectcreate) per creare un progetto, inserisci il nome del progetto e clicca su "Crea progetto"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Accedi alla [console di Vertex AI](https://console.cloud.google.com/vertex-ai)
* Nel progetto creato, attiva [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Configurare i Permessi di Accesso API

* Apri la pagina di gestione degli [account di servizio](https://console.cloud.google.com/iam-admin/serviceaccounts) e crea un account di servizio

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Nella pagina di gestione degli account di servizio, trova l'account appena creato, clicca su `Chiavi` e crea una nuova chiave in formato JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Dopo la creazione, il file della chiave verrà salvato automaticamente sul tuo computer in formato JSON: **conservalo con cura**

## 3. Configurare Vertex AI in Cherry Studio

* Seleziona il fornitore Vertex AI
* Inserisci i valori corrispondenti dal file JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Clicca su "Aggiungi [modello](https://console.cloud.google.com/vertex-ai/model-garden)" per iniziare a usarlo con piacere!