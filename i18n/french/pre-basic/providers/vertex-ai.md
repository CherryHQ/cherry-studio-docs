---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Aperçu du tutoriel

### 1. Obtenir la clé API

* Pour obtenir la clé API Gemini, vous devez disposer d'un projet Google Cloud (à ignorer si vous en avez déjà un)
* Accédez à [Google Cloud](https://console.cloud.google.com/projectcreate) pour créer un projet, remplissez le nom du projet et cliquez sur "Créer un projet"

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Accédez à la [console Vertex AI](https://console.cloud.google.com/vertex-ai)
* Dans le projet créé, activez l'[API Vertex AI](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Configurer les droits d'accès à l'API

* Ouvrez l'interface des autorisations des [comptes de service](https://console.cloud.google.com/iam-admin/serviceaccounts) et créez un compte de service

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* Dans la page de gestion des comptes de service, trouvez le compte créé, cliquez sur `Clés` et créez une nouvelle clé au format JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* Une fois créée, le fichier de clé sera automatiquement enregistré sur votre ordinateur au format JSON. **Conservez-le précieusement**

## 3. Configurer Vertex AI dans Cherry Studio

* Sélectionnez le fournisseur de services Vertex AI
* Remplissez les champs correspondants du fichier JSON

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Cliquez sur "Ajouter [modèle](https://console.cloud.google.com/vertex-ai/model-garden)" pour commencer à l'utiliser immédiatement !