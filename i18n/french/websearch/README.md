---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Mode Connecté

{% hint style="info" %}
Exemples de situations nécessitant une connexion internet :

* Informations temporelles : comme le prix des contrats à terme sur l'or aujourd'hui/cette semaine/à l'instant.
* Données en temps réel : comme la météo, les taux de change et autres valeurs dynamiques.
* Connaissances émergentes : comme les nouvelles tendances, concepts, technologies, etc.
{% endhint %}

### I. Comment activer la connexion internet

Dans la fenêtre de saisie de Cherry Studio, cliquez sur l'icône 【Petite Terre】 pour activer la connexion internet.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Cliquez sur l'icône Terre - Activation de la connexion</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Indication - Fonction de connexion activée</p></figcaption></figure>

### II. Remarque importante : deux modes de connexion existent

#### Mode 1 : Connexion intégrée aux grands modèles des fournisseurs

Dans ce cas, une fois activée, la connexion internet est immédiatement disponible pour utilisation.

{% hint style="warning" %}
Vérifiez si le modèle supporte la connexion en repérant une icône de planète 🌐 à côté de son nom dans l'interface de discussion.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Cette méthode permet également d'identifier rapidement les modèles compatibles dans la page de gestion des modèles.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Fournisseurs actuellement pris en charge par Cherry Studio**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (tous les modèles)</mark>
> * <mark style="color:green;">Hunyuan (Tencent)</mark>
> * <mark style="color:green;">ZHIPU AI</mark>
> * <mark style="color:green;">Bailian (Alibaba Cloud)</mark>

{% hint style="danger" %}
Cas particulier :
Certains modèles sans icône 🌐 peuvent exceptionnellement accéder à internet, comme expliqué dans ce tutoriel.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Mode 2 : Utilisation du service Tavily pour les modèles non connectés

Si votre modèle n'intègre pas la fonction internet (pas d'icône 🌐) mais nécessite des informations actualisées, utilisez le service de recherche Tavily.

**Première utilisation** : Un pop-up vous guidera dans la configuration. Suivez les instructions simples !

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Pop-up : cliquez sur Configurer</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Cliquez sur Obtenir la clé API</p></figcaption></figure>

Après avoir cliqué, vous serez redirigé vers le site de **Tavily**. Créez un compte, connectez-vous, générez votre clé API et collez-la dans Cherry Studio.

{% hint style="danger" %}
Besoin d'aide ? Consultez le tutoriel d'inscription Tavily dans ce répertoire.
{% endhint %}

**Document de référence pour l'inscription :**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Cette interface confirme votre inscription réussie :

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Copiez la clé API</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Collez la clé - Configuration terminée !</p></figcaption></figure>

Testez le service : les résultats montrent 5 sources trouvées (valeur par défaut).

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Limite : Tavily propose un quota gratuit mensuel. Les dépassements sont payants.
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS : Pour signaler des erreurs, contactez-nous à tout moment.