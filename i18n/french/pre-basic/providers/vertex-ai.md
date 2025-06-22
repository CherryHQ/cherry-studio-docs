---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Vertex AI

## Aperçu du tutoriel

### 1. Obtenir la clé API

* Avant d'obtenir la clé API de Gemini, vous devez avoir un projet Google Cloud (si vous en avez déjà un, vous pouvez sauter cette étape)
* Rendez-vous sur [Google Cloud](https://console.cloud.google.com/projectcreate) pour créer un projet, renseignez le nom du projet et cliquez sur Créer un projet

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Accédez à la [Console Vertex AI](https://console.cloud.google.com/vertex-ai)
* Dans le projet créé, activez [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

### 2. Configurer les autorisations d'accès à l'API

* Ouvrez la page des autorisations du [compte de service](https://console.cloud.google.com/iam-admin/serviceaccounts) et créez un compte de service

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Sur la page de gestion des comptes de service, trouvez le compte que vous venez de créer, cliquez sur `Clés` et créez une nouvelle clé au format JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Après création réussie, le fichier clé sera automatiquement enregistré sur votre ordinateur au format JSON. Veuillez le **conserver en lieu sûr**

### 3. Configurer Vertex AI dans Cherry Studio

* Sélectionnez le fournisseur de services Vertex AI
* Remplissez les champs correspondants du fichier JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Cliquez sur Ajouter un [modèle](https://console.cloud.google.com/vertex-ai/model-garden), et vous pouvez commencer à l'utiliser avec plaisir !