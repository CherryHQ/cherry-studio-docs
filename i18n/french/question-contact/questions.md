---
icon: seal-question
---
# Foire Aux Questions


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Codes d'erreur courants

* **4xx (codes d'état d'erreur client)** : Généralement des erreurs de syntaxe de requête, d'échec d'authentification ou d'autorisation empêchant l'exécution de la demande.
* **5xx (codes d'état d'erreur serveur)** : Généralement des erreurs côté serveur, comme un serveur en panne ou un dépassement du délai de traitement.

| Code erreur | Scénarios possibles                                                                 | Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **400** | Format du corps de la requête incorrect, etc.                                         | <p>Consultez le contenu d'erreur renvoyé ou <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">la console</a> pour l'erreur et agissez selon les instructions.</p><p><a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa"><mark style="color:purple;">[Cas courant 1]</mark> : Pour les modèles Gemini, une configuration de carte peut être nécessaire ;<br><mark style="color:purple;">[Cas courant 2]</mark> : Limite de données dépassée (modèles visuels) - la taille de l'image dépasse la limite de requête ;<br><mark style="color:purple;">[Cas courant 3]</mark> : Paramètre non pris en charge ou erroné - tester avec un nouvel assistant vierge ;<br><mark style="color:purple;">[Cas courant 4]</mark> : Contexte trop large - réinitialiser ou réduire l'historique.</a></p> |
| **401** | Échec d'authentification : modèle non pris en charge ou compte suspendu                                        | Vérifier l'état du compte auprès du fournisseur                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **403** | Autorisation refusée pour l'opération demandée                                         | Suivre les instructions dans l'erreur ou consulter les erreurs dans la [console](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                                                                                                                |
| **404** | Ressource introuvable                                                                | Vérifier le chemin de la requête                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **422** | Format de requête correct mais erreur sémantique                                           | Erreur interprétable par le serveur mais non traitable (ex : valeur nulle, type incorrect comme un nombre au lieu d'une chaîne).                                                                                                                                                                                                                                                                                                                                                                                           |
| **429** | Limite de débit de requêtes atteinte                                               | Réessayer après une durée de refroidissement                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **500** | Erreur interne du serveur                                                            | Contacter le fournisseur si persistant                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **501** | Fonction non implémentée par le serveur                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **502** | Réponse invalide d'un serveur proxy ou passerelle                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **503** | Serveur temporairement surchargé (retry après délai dans l'en-tête Retry-After)                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **504** | Serveur proxy/passerelle n'a pas reçu la réponse du serveur distant à temps                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

***

## Comment consulter les erreurs dans la console

* Appuyer sur <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>) devant la fenêtre client de Cherry Studio

{% hint style="info" %}
- La fenêtre active doit être celle du client Cherry Studio pour ouvrir la console ;
- Ouvrir d'abord la console avant de lancer les requêtes (test, dialogue, etc.).
{% endhint %}

* Dans la console, cliquer sur <mark style="color:blue;">`Network`</mark> → Sélectionner le dernier élément marqué d'un <mark style="color:red;">`×`</mark> rouge : <mark style="color:red;">`completions`</mark> _(erreurs de dialogue/traduction)_ ou <mark style="color:red;">`generations`</mark> _(erreurs de génération d'images)_ → Cliquer sur <mark style="color:blue;">`Response`</mark> pour voir le contenu complet (zone ④).

> Si vous ne trouvez pas la cause de l'erreur, partagez une capture de cet écran dans le [groupe officiel](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Cette méthode fonctionne pour les dialogues, tests de modèles, ajout de bases de connaissances, générations d'images, etc. Ouvrir toujours la console avant l'opération.

{% hint style="info" %}
Différents scénarios utilisent des noms différents dans la colonne Name(②) :

Dialogue/traduction/vérification de modèle : <mark style="color:red;">`completions`</mark>

Génération d'images : <mark style="color:red;">`generations`</mark>

Création de base de connaissances : <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Formules non rendues / erreurs de rendu

* Si la formule s'affiche en code source, vérifier les délimiteurs :

> **Utilisation des délimiteurs**
>
> _Formule en ligne_
>
> * Utiliser `$formule$` 
> * ou `\(formule\)`
>
> _Bloc de formule_
>
> * Utiliser `$$formule$$`
> * ou `\[formule\]`
> * Exemple : `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Si le rendu est incorrect (souvent avec des caractères chinois), basculer le moteur de formules vers KateX.

***

## Impossible de créer une base de connaissances / échec de récupération des dimensions d'embedding

1. Modèle indisponible

> Vérifier si le modèle est pris en charge par le fournisseur et si son statut est normal.

2. Utilisation d'un modèle non adapté à l'embedding

***

## Modèle ne reconnaît pas les images / impossibilité de sélectionner ou télécharger des images

Vérifier d'abord si le modèle supporte la reconnaissance d'images. Dans Cherry Studio, les modèles compatibles sont indiqués par une icône d'œil 👁️ après leur nom.

Les modèles compatibles permettent le téléchargement d'images. Si la fonctionnalité n'est pas activée, accéder aux paramètres du modèle chez le fournisseur et cocher l'option "image".

Consulter les informations détaillées du modèle chez le fournisseur. Les modèles non visuels n'utiliseront pas cette fonction même si activée.