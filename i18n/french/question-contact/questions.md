---
icon: seal-question
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Foire aux questions (FAQ)

## Codes d'erreur courants

* **4xx (Codes d'état d'erreur client)** : Généralement des erreurs de syntaxe de requête, d'authentification ou d'autorisation empêchant le traitement de la requête.
* **5xx (Codes d'état d'erreur serveur)** : Généralement des erreurs côté serveur comme un serveur inaccessible ou des délais de traitement dépassés.

| Code d'erreur  | Cas possibles                                             | Solution                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <h4>400</h4> | Format incorrect du corps de la requête, etc.              | <p>Vérifiez le contenu de l'erreur renvoyé dans la conversation ou consultez la <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a> pour voir le message d'erreur, puis suivez les instructions.</p><p><mark style="color:purple;">[Cas fréquent 1]</mark> : Pour les modèles Gemini, une activation de carte bancaire peut être nécessaire ;<br><mark style="color:purple;">[Cas fréquent 2]</mark> : Taille de données dépassée (surtout avec les modèles visuels). Les images dépassant la limite de taille renverront cette erreur ;<br><mark style="color:purple;">[Cas fréquent 3]</mark> : Paramètre non supporté ou mal configuré. Testez avec un assistant vierge ;<br><mark style="color:purple;">[Cas fréquent 4]</mark> : Limite de contexte dépassée. Effacez le contexte, démarrez une nouvelle conversation ou réduisez le nombre de messages contextuels.</p> |
| <h4>401</h4> | Authentification échouée : modèle non supporté ou compte banni | Contactez le fournisseur de services ou vérifiez l'état du compte                                                                                                                                                                                                                                                                                                                                                              |
| <h4>403</h4> | Droits insuffisants pour l'opération                      | Suivez les instructions de l'erreur renvoyée ou dans la <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a>                                                                                                                                                                                                                                                                                              |
| <h4>404</h4> | Ressource introuvable                                     | Vérifiez le chemin de la requête                                                                                                                                                                                                                                                                                                                                                                                                |
| <h4>422</h4> | Syntaxe correcte mais erreur sémantique                    | Erreur dans l'interprétation JSON (ex: valeur nulle ; nombre/boolean au lieu d'une chaîne)                                                                                                                                                                                                                                                                                                                                      |
| <h4>429</h4> | Limite de taux de requête atteinte                         | Attendez avant de réessayer (dépassement TPM ou RPM)                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>500</h4> | Erreur interne du serveur                                 | Contactez le fournisseur de services si persistant                                                                                                                                                                                                                                                                                                                                                                              |
| <h4>501</h4> | Fonctionnalité non supportée                              |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>502</h4> | Réponse invalide d'un serveur intermédiaire               |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>503</h4> | Serveur surchargé/en maintenance                          | Vérifiez l'en-tête Retry-After pour le délai                                                                                                                                                                                                                                                                                                                                                                                   |
| <h4>504</h4> | Délai dépassé par un serveur intermédiaire                 |                                                                                                                                                                                                                                                                                                                                                                                                                                 |

***

## Comment voir les erreurs dans la console

* Cliquez sur la fenêtre du client Cherry Studio, puis appuyez sur le raccourci clavier <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (macOS : <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- La fenêtre active doit être celle du client Cherry Studio pour ouvrir la console ;
- Ouvrez la console avant de lancer des tests ou des requêtes pour collecter les informations.
{% endhint %}

* Dans la console ouverte, cliquez sur <mark style="color:blue;">`Network`</mark> → Cherchez dans la zone ② le dernier élément marqué d'un <mark style="color:red;">`×`</mark> rouge nommé <mark style="color:red;">`completions`</mark> _(pour les erreurs de dialogue/traduction)_ ou <mark style="color:red;">`generations`</mark> _(pour les erreurs de génération d'images)_ → Cliquez sur <mark style="color:blue;">`Response`</mark> pour voir le message complet (zone ④ sur l'image).

> Si vous ne parvenez pas à identifier la cause de l'erreur, envoyez une capture d'écran de cette interface au [groupe de discussion officiel](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Cette méthode fonctionne aussi pour les tests de modèles, l'ajout de bases de connaissances, ou la génération d'images. Ouvrez toujours la console avant de lancer les opérations.

{% hint style="info" %}
Les noms dans la colonne Name (zone ②) varient selon le contexte :

Dialogues/traduction/vérification de modèle : <mark style="color:red;">`completions`</mark>&#x20;

Génération d'images : <mark style="color:red;">`generations`</mark>

Création de base de connaissances : <mark style="color:red;">`embeddings`</mark>&#x20;
{% endhint %}

***

## Formules non rendues / Erreurs de rendu

* Si les formules s'affichent en code, vérifiez les délimiteurs :

> **Utilisation des délimiteurs**
>
> _Formule en ligne_
>
> * Un dollar unique : `$formule$`
> * Ou `\(` et `\)` : `\(formule\)`
>
> _Bloc de formule_
>
> * Deux dollars : `$$formule$$`
> * Ou `\[formule\]`
> * Exemple : `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Si le rendu est corrompu (surtout avec du chinois dans les formules), basculez vers le moteur de rendu KateX.

***

## Impossible de créer une base de connaissances / Échec de récupération des dimensions d'embedding

1. Modèle indisponible

> Vérifiez si le fournisseur supporte ce modèle ou son état de service.

2. Utilisation d'un modèle non-embedding

***

## Le modèle ne reconnaît pas les images / Impossible d'uploader/sélectionner des images

Vérifiez d'abord si le modèle supporte la reconnaissance d'images. Dans Cherry Studio, les modèles populaires sont classés : une icône d'œil 👁️ après le nom indique cette capacité.

Les modèles compatibles permettent l'upload d'images. Si cette option n'apparaît pas, dans la liste des modèles du fournisseur, cliquez sur l'icône de paramètres et cochez "Image".

Les spécifications des modèles sont disponibles chez chaque fournisseur. Comme pour les embeddings, cocher l'option sur des modèles non-visuels n'aura aucun effet.