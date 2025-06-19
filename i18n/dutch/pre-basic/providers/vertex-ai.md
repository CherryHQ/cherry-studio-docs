---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Vertex AI

## Tutorial Overzicht

### 1. API Key verkrijgen

* Om een Gemini API key te verkrijgen, moet je eerst een Google Cloud-project hebben (als je er al een hebt, kun je deze stap overslaan)
* Ga naar [Google Cloud](https://console.cloud.google.com/projectcreate) om een project aan te maken, vul de projectnaam in en klik op "Project maken"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Ga naar de [Vertex AI-console](https://console.cloud.google.com/vertex-ai)
* Schakel de [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) in binnen het aangemaakte project

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API Toegangsrechten instellen

* Open de [Serviceaccount](https://console.cloud.google.com/iam-admin/serviceaccounts) rechtenpagina en maak een serviceaccount aan

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Zoek op de serviceaccountbeheerpagina het zojuist aangemaakte serviceaccount, klik op `Sleutel` en maak een nieuwe sleutel aan in JSON-formaat

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Na succesvolle aanmaak wordt het sleutelbestand automatisch opgeslagen als JSON-bestand op je computer - **bewaar dit zorgvuldig**

## 3. Vertex AI configureren in Cherry Studio

* Selecteer de Vertex AI-leverancier
* Vul de corresponderende velden in met gegevens uit het JSON-bestand

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Klik op [Model toevoegen](https://console.cloud.google.com/vertex-ai/model-garden) en je kunt met plezier beginnen gebruiken!