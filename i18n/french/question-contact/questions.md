---
icon: seal-question
---
# Foire aux questions


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Codes d'erreur courants

* **4xx (codes d'état d'erreur client)** : Généralement causés par une syntaxe de requête incorrecte, un échec d'authentification ou d'autorisation.
* **5xx (codes d'état d'erreur serveur)** : Généralement des erreurs côté serveur comme un serveur défaillant ou des délais de traitement dépassés.

| Code | Causes possibles | Solution |
|------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **400** | Corps de requête mal formaté | <p>Consultez l'erreur renvoyée ou utilisez la <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a> pour voir le contenu de l'erreur.<br><a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa"><mark style="color:purple;">[Cas 1]</mark> : Pour Gemini, vérifiez la liaison de carte bancaire ;<br><mark style="color:purple;">[Cas 2]</mark> : Données trop volumineuses (notamment images) ;<br><mark style="color:purple;">[Cas 3]</mark> : Paramètres non supportés ou erronés ;<br><mark style="color:purple;">[Cas 4]</mark> : Contexte dépasse la limite.</a></p> |
| **401** | Échec d'authentification : modèle non supporté ou compte bloqué | Contactez le fournisseur du service |
| **403** | Permission refusée | Vérifiez les informations d'erreur dans la console |
| **404** | Ressource introuvable | Vérifiez le chemin d'accès |
| **422** | Syntaxe correcte mais erreur sémantique | Problèmes de format JSON (valeurs nulles, types incorrects) |
| **429** | Limite de requêtes atteinte | Attendez avant de réessayer |
| **500** | Erreur interne du serveur | Contactez le fournisseur du service |
| **501** | Fonctionnalité non implémentée |  |
| **502** | Réponse invalide d'un serveur proxy |  |
| **503** | Service indisponible (surcharge ou maintenance) |  |
| **504** | Délai de réponse dépassé |  |

***

## Consulter les erreurs dans la console

* Appuyez sur <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac : <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>) avec la fenêtre Cherry Studio active.

{% hint style="info" %}
- La fenêtre de Cherry Studio doit être active pour ouvrir la console ;
- Ouvrez d'abord la console avant de tester ou démarrer des conversations.
{% endhint %}

* Dans l'onglet <mark style="color:blue;">`Network`</mark>, cliquez sur la dernière ligne marquée ❌ (<mark style="color:red;">`completions`</mark> pour conversations ou <mark style="color:red;">`generations`</mark> pour images) → Affichez le contenu complet dans l'onglet <mark style="color:blue;">`Response`</mark>.

> Si l'erreur persiste, partagez une capture d'écran dans notre [groupe communautaire](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Cette méthode fonctionne pour les conversations, tests de modèles, bases de connaissances, et images. Ouvrez toujours la console avant l'opération.

{% hint style="info" %}
**Noms dans l'onglet Network**  
Conversations/traduction : <mark style="color:red;">`completions`</mark>  
Images : <mark style="color:red;">`generations`</mark>  
Bases de connaissances : <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Problèmes de rendu des formules

* Si le code s'affiche au lieu d'être rendu, vérifiez les délimiteurs :

> **Utilisation des délimiteurs**  
> _Formule en ligne_  
> - `$formula$` ou `\(formula\)`  
>   
> _Bloc de formule_  
> - `$$formula$$` ou `\[formula\]`  
> Exemple : `$$\sum_{i=1}^n x_i$$` →  
> $$\sum_{i=1}^n x_i$$

* Pour les erreurs de rendu avec caractères chinois, passez au moteur KateX.

***

## Impossible de créer une base de connaissances

1. Modèle indisponible  
> Vérifiez sa disponibilité auprès du fournisseur.  
2. Modèle non adapté aux embeddings  

***

## Modèle ne reconnaît pas les images

* Les modèles compatibles sont marqués par l'icône 👁️.
* Activez l'option "Images" dans les paramètres du modèle chez le fournisseur.
* Seuls les modèles avec prise en charge visuelle peuvent traiter des images.