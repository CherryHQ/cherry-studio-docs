---
icon: cloud-check
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuration des fournisseurs de services

Cette page présente uniquement les fonctionnalités de l'interface. Pour le guide de configuration, veuillez consulter le tutoriel [Configuration des fournisseurs](../../../pre-basic/providers/) dans les bases.

{% hint style="info" %}
* Lors de l'utilisation de fournisseurs intégrés, il suffit de renseigner la clé correspondante.
* Les différents fournisseurs peuvent utiliser des termes variés pour désigner la clé : clé secrète, Key, API Key, token, etc. Ils font tous référence au même élément.
{% endhint %}



### Clé API

Dans Cherry Studio, chaque fournisseur prend en charge plusieurs clés utilisées en rotation selon un cycle séquentiel de haut en bas.

* Ajoutez plusieurs clés en les séparant par des virgules. Par exemple :

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Vous **devez** utiliser des virgules **anglaises**.
{% endhint %}

### Adresse API

Lors de l'utilisation de fournisseurs intégrés, il n'est généralement pas nécessaire de renseigner l'adresse API. Si vous devez la modifier, saisissez-la exactement comme indiquée dans la documentation officielle.

> Si le fournisseur fournit une adresse au format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, renseignez uniquement la racine (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio complétera automatiquement le chemin restant (<mark style="background-color:green;">/v1/chat/completions</mark>). Un format incorrect pourrait entraîner des dysfonctionnements.

{% hint style="info" %}
Note : La plupart des fournisseurs utilisent un routage unifié pour les modèles de langage, cette étape est donc généralement inutile. Si le chemin d'API du fournisseur est v2, v3/chat/completions ou une autre version, saisissez manuellement la version avec un "/" final. Si le routage n'est pas conventionnel (<mark style="background-color:green;">/v1/chat/completions</mark>), utilisez l'adresse complète fournie par le fournisseur avec un "#" final.

Résumé :
* Adresse API se terminant par "/" : concaténation automatique de "<mark style="background-color:green;">chat/completions</mark>"
* Adresse API se terminant par "#" : aucune concaténation, utilisation directe de l'adresse saisie

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}



### Ajouter un modèle

Généralement, cliquez sur le bouton `Gérer` en bas à gauche de la page de configuration du fournisseur pour récupérer automatiquement tous les modèles disponibles. Cliquez ensuite sur `+` dans la liste pour les ajouter.

{% hint style="info" %}
Cliquer sur "Gérer" n'ajoute pas tous les modèles. Vous devez cliquer sur `+` à droite de chaque modèle pour les intégrer à la liste de configuration, afin qu'ils apparaissent dans la sélection de modèles.
{% endhint %}

### Vérification de la connectivité

Cliquez sur le bouton de vérification à droite du champ de la clé API pour tester la configuration.

{% hint style="info" %}
La vérification utilise par défaut le dernier modèle conversationnel ajouté. En cas d'échec, vérifiez la présence de modèles incorrects ou non pris en charge.
{% endhint %}

{% hint style="danger" %}
Après configuration réussie, activez obligatoirement l'interrupteur en haut à droite. Sinon, le fournisseur restera désactivé et ses modèles seront indisponibles.
{% endhint %}