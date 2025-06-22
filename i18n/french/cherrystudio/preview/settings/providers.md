---
icon: cloud-check
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Paramètres du fournisseur

Cette page présente uniquement les fonctionnalités de l'interface. Pour le didacticiel de configuration, reportez-vous au didacticiel [Configuration des fournisseurs](../../../pre-basic/providers/) dans les didacticiels de base.

{% hint style="info" %}
* Lorsque vous utilisez un fournisseur intégré, il suffit de saisir la clé correspondante.
* Différents fournisseurs peuvent utiliser des termes différents pour la clé : clé secrète, Key, API Key, jeton, etc., mais ils désignent tous la même chose.
{% endhint %}

### Clé API

Dans Cherry Studio, un seul fournisseur prend en charge l'utilisation de plusieurs clés en rotation. La rotation s'effectue en bouclant de la première à la dernière clé de la liste.

* Saisissez plusieurs clés en les séparant par des virgules. Exemple :

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Vous devez utiliser une virgule **anglaise**.
{% endhint %}

### URL de l'API

Il n'est généralement pas nécessaire de saisir l'URL de l'API lors de l'utilisation d'un fournisseur intégré. Si vous avez besoin de la modifier, veuillez saisir strictement l'URL fournie par la documentation officielle correspondante.

> Si le fournisseur donne une adresse au format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, ne saisissez que la partie racine de l'adresse (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio ajoutera automatiquement le reste du chemin (<mark style="background-color:green;">/v1/chat/completions</mark>). Si vous ne suivez pas ces instructions, cela pourrait empêcher un fonctionnement normal.

{% hint style="info" %}
Remarque : La route du modèle de grand langage est uniforme pour la plupart des fournisseurs. En général, il n'est pas nécessaire d'effectuer les opérations suivantes. Si le chemin de l'API du fournisseur est v2, v3/chat/completions ou une autre version, vous pouvez saisir manuellement la version correspondante dans la barre d'adresse en terminant par '/'. Lorsque la route de requête du fournisseur n'est pas le <mark style="background-color:green;">/v1/chat/completions</mark> conventionnel, utilisez l'adresse complète fournie par le fournisseur et terminez par `#`.

À savoir :
* Lorsque l'URL de l'API se termine par `/`, seul "chat/completions" est ajouté
* Lorsque l'URL de l'API se termine par `#`, aucune concaténation n'est effectuée et seule l'adresse saisie est utilisée

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Ajouter des modèles

En général, en cliquant sur le bouton `Gérer` en bas à gauche de la page de configuration du fournisseur, vous obtiendrez automatiquement tous les modèles pouvant être appelés par ce fournisseur. Cliquez ensuite sur le `+` à côté de chaque modèle dans la liste obtenue pour l'ajouter à la liste des modèles.

{% hint style="info" %}
Les modèles de la liste contextuelle lors du clic sur le bouton "Gérer" ne sont pas tous ajoutés. Vous devez cliquer sur le `+` à droite du modèle pour l'ajouter à la liste des modèles de la page de configuration du fournisseur, afin qu'il apparaisse dans la liste de sélection des modèles.
{% endhint %}

### Vérification de la connectivité

Cliquez sur le bouton de vérification à côté du champ de saisie de la clé API pour tester si la configuration a réussi.

{% hint style="info" %}
Par défaut, la vérification du modèle utilise le dernier modèle de dialogue ajouté à la liste. Si la vérification échoue, vérifiez la liste des modèles pour voir s'il y a des modèles incorrects ou non pris en charge.
{% endhint %}

{% hint style="danger" %}
Une fois la configuration réussie, assurez-vous d'activer le commutateur en haut à droite. Sinon, le fournisseur restera désactivé et les modèles correspondants ne seront pas disponibles dans la liste des modèles.
{% endhint %}