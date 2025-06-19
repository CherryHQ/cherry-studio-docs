---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Vertex AI

## Aperçu du tutoriel

### 1. Obtenir une clé API

* Avant d'obtenir la clé API Gemini, vous devez disposer d'un projet Google Cloud (si vous en avez déjà un, cette étape peut être ignorée)
* Accédez à [Google Cloud](https://console.cloud.google.com/projectcreate) pour créer un projet, remplissez le nom du projet et cliquez sur "Créer un projet"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Accédez à la [console Vertex AI](https://console.cloud.google.com/vertex-ai)
* Activez l'[API Vertex AI](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1&invt=Ab0iBA) dans le projet créé

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Configurer les autorisations d'accès à l'API

* Ouvrez l'interface des autorisations des [comptes de service](https://console.cloud.google.com/iam-admin/serviceaccounts) et créez un compte de service

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Sur la page de gestion des comptes de service, trouvez le compte que vous venez de créer, cliquez sur `Clés` et créez une nouvelle clé au format JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Après création réussie, le fichier de clé sera automatiquement enregistré sur votre ordinateur au format JSON. Veuillez le **conserver précieusement**

## 3. Configurer Vertex AI dans Cherry Studio

* Sélectionnez le fournisseur Vertex AI
* Remplissez les champs correspondants du fichier JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Cliquez sur Ajouter un [modèle](https://console.cloud.google.com/vertex-ai/model-garden) et vous pouvez commencer à l'utiliser avec plaisir !\