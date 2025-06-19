---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# Vertex AI

## Overzicht van de zelfstudie

### 1. API Key verkrijgen

*   Voordat u een API Key voor Gemini verkrijgt, moet u een Google Cloud-project hebben (als u er al een heeft, kunt u deze stap overslaan)
*   Ga naar [Google Cloud](https://console.cloud.google.com/projectcreate) om een project te maken, vul de projectnaam in en klik op "Project maken"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

*   Ga naar de [Vertex AI-console](https://console.cloud.google.com/vertex-ai)
*   Schakel de [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA) in binnen het gemaakte project

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. API-toegangsrechten instellen

*   Open de [Serviceaccount](https://console.cloud.google.com/iam-admin/serviceaccounts) rechtenpagina en maak een serviceaccount aan

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

*   Zoek in de beheerpagina van serviceaccounts de zojuist aangemaakte serviceaccount, klik op `Sleutel` en maak een nieuwe sleutel in JSON-formaat

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

*   Na succesvolle aanmaak wordt het sleutelbestand automatisch als JSON-bestand op uw computer opgeslagen – **bewaar dit zorgvuldig**

## 3. Vertex AI configureren in Cherry Studio

*   Selecteer de Vertex AI-serviceprovider
*   Vul de bijbehorende velden in met de gegevens uit het JSON-bestand

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Klik op [Model](https://console.cloud.google.com/vertex-ai/model-garden) toevoegen om direct te beginnen!