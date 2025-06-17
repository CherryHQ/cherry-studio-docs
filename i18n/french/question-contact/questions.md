---
icon: seal-question
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Foire aux questions

## Codes d'erreur courants

* **4xx (Codes d'état d'erreur client)** : Généralement des erreurs de syntaxe de requête, échec d'authentification ou d'autorisation empêchant l'exécution de la requête.
* **5xx (Codes d'état d'erreur serveur)** : Généralement des erreurs côté serveur, serveur hors ligne, dépassement du délai de traitement des requêtes, etc.

| Code d'erreur     | Scénarios possibles                                           | Méthode de résolution                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4> | Corps de requête mal formé, etc.                            | <p>Consultez le contenu d'erreur retourné par le dialogue ou vérifiez le message d'erreur dans la <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a>, puis suivez les instructions.</p><p><mark style="color:purple;">【Cas courant 1】</mark> : Pour les modèles Gemini, une opération de liaison de carte peut être nécessaire ;<br><mark style="color:purple;">【Cas courant 2】</mark> : Données trop volumineuses, fréquent pour les modèles visuels où les images dépassent la limite de taille ;<br><mark style="color:purple;">【Cas courant 3】</mark> : Paramètres non pris en charge ou mal renseignés. Testez avec un nouvel assistant vierge ;<br><mark style="color:purple;">【Cas courant 4】</mark> : Contexte trop important. Effacez le contexte, créez un nouveau dialogue ou réduisez le nombre d'éléments contextuels.</p> |
| <h4>401</h4> | Échec d'authentification : modèle non pris en charge ou compte serveur suspendu | Contactez ou vérifiez l'état du compte du fournisseur de service                                                                                                                                                                                                                                                                                                                                                                                           |
| <h4>403</h4> | Droits insuffisants pour l'opération demandée              | Suivez les instructions d'erreur dans la réponse du dialogue ou dans la console                                                                                                                                                                                                                                                                                                                                                                          |
| <h4>404</h4> | Ressource introuvable                                      | Vérifiez le chemin de la requête, etc.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>422</h4> | Format correct mais erreur sémantique                       | Erreurs compréhensibles par le serveur mais non traitables. Fréquent avec des erreurs JSON (ex : valeur null ; chaîne attendue mais nombre ou booléen renseigné).                                                                                                                                                                                                                                                                                           |
| <h4>429</h4> | Limite de débit atteinte                                   | Le taux de requêtes (TPM ou RPM) a atteint son maximum, patientez avant de réessayer                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>500</h4> | Erreur interne du serveur, requête impossible à traiter    | Contactez le fournisseur de service si l'erreur persiste                                                                                                                                                                                                                                                                                                                                                                                                  |
| <h4>501</h4> | Fonction non implémentée par le serveur                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <h4>502</h4> | Réponse invalide reçue d'un serveur distant par la passerelle |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <h4>503</h4> | Service temporairement indisponible (surcharge ou maintenance) |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <h4>504</h4> | Délai dépassé pour la réponse d'un serveur distant par la passerelle |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

***

## Méthode pour consulter les erreurs dans la console

* Appuyez sur <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac : <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>) après avoir cliqué sur la fenêtre client de Cherry Studio

{% hint style="info" %}
- La fenêtre active doit être celle du client Cherry Studio pour ouvrir la console ;
- La console doit être ouverte avant de lancer des tests ou des dialogues pour collecter les informations de requête.
{% endhint %}

* Dans la console, cliquez sur <mark style="color:blue;">`Network`</mark> → recherchez la dernière entrée marquée d'un <mark style="color:red;">`×`</mark> rouge : <mark style="color:red;">`completions`</mark> _(erreurs de dialogue, traduction ou vérification de modèle)_ ou <mark style="color:red;">`generations`</mark> _(erreurs de dessin)_ → cliquez sur <mark style="color:blue;">`Response`</mark> pour voir le contenu complet de la réponse (zone ④ sur l'image).

> Si la cause de l'erreur n'est pas identifiable, envoyez une capture d'écran de cette interface dans le [groupe communautaire officiel](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Cette méthode fonctionne pour les dialogues, tests de modèle, ajout de base de connaissances, dessin, etc. Ouvrez toujours la console avant l'opération pour obtenir les informations de requête.

{% hint style="info" %}
Le nom dans la colonne Name (zone ② sur l'image) varie selon le contexte :

Dialogue, traduction, vérification de modèle : <mark style="color:red;">`completions`</mark>

Dessin : <mark style="color:red;">`generations`</mark>

Création de base de connaissances : <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Formules non interprétées / erreur d'interprétation

* Si la formule s'affiche en code brute, vérifiez les délimiteurs :

> **Utilisation des délimiteurs**
> 
> _Formule en ligne_
> * Un signe dollar : `$formule$`
> * Ou `\(` et `\)` : `\(formule\)`
>
> _Bloc de formule indépendant_
> * Deux signes dollars : `$$formule$$`
> * Ou `\[formule\]`
> * Exemple : `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Erreur d'interprétation/caractères illisibles : survient souvent avec du texte chinois dans les formules. Essayez de changer le moteur d'interprétation pour KateX.

***

## Impossible de créer une base de connaissances / Échec d'obtention des dimensions d'embedding

1. État du modèle indisponible
> Vérifiez si le fournisseur prend en charge ce modèle et si son service fonctionne normalement.

2. Utilisation d'un modèle non adapté à l'embedding

***

## Modèle ne reconnaît pas les images / Impossible d'importer ou de sélectionner des images

Vérifiez d'abord si le modèle prend en charge la reconnaissance d'image. Cherry Studio indique les modèles compatibles avec une icône en forme d'œil à côté du nom.

Les modèles compatibles permettent d'importer des fichiers image. Si la fonction n'est pas correctement activée, accédez à la liste des modèles du fournisseur, cliquez sur le bouton des paramètres après le nom du modèle et cochez l'option d'image.

Consultez les informations spécifiques du modèle chez le fournisseur correspondant. Comme pour les modèles d'embedding, activer l'option d'image pour un modèle non visuel est inutile.