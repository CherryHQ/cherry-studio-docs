---
icon: cloud-check
---
# Configuration du service de modèles


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cette page présente uniquement les fonctionnalités de l'interface. Pour le tutoriel de configuration, référez-vous au guide [Configuration des fournisseurs](../../../pre-basic/providers/) dans les tutoriels de base.

{% hint style="info" %}
* Lors de l'utilisation de fournisseurs intégrés, il suffit de saisir la clé correspondante.
* Les différents fournisseurs peuvent utiliser des termes variés pour la clé : clé secrète, Key, API Key, token, etc. désignent tous la même chose.
{% endhint %}

### Clé API

Dans Cherry Studio, un seul fournisseur prend en charge l'utilisation de plusieurs clés en rotation, selon un mode de rotation circulaire séquentiel.

* Séparez plusieurs clés par des virgules anglaises. Exemple :

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Vous devez utiliser des virgules **anglaises**.
{% endhint %}

### Adresse API

Lors de l'utilisation de fournisseurs intégrés, il n'est généralement pas nécessaire de remplir l'adresse API. Si une modification est requise, suivez scrupuleusement l'adresse fournie dans la documentation officielle.

> Si le fournisseur fournit une adresse au format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, saisissez uniquement la partie racine (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio ajoutera automatiquement le chemin restant (<mark style="background-color:green;">/v1/chat/completions</mark>). Un format incorrect pourrait entraîner un dysfonctionnement.

{% hint style="info" %}
Remarque : La plupart des fournisseurs ont des routes de modèles de langage unifiées. Généralement, les opérations suivantes ne sont pas nécessaires. Si le chemin d'API du fournisseur est v2, v3/chat/completions ou une autre version, saisissez manuellement la version correspondante dans la barre d'adresse en la terminant par "`/`". Lorsque la route de requête du fournisseur n'est pas le conventionnel <mark style="background-color:green;">/v1/chat/completions</mark>, utilisez l'adresse complète fournie par le fournisseur et terminez par `#`.

C'est-à-dire :
* Lorsque l'adresse API se termine par `/`, seule "<mark style="background-color:green;">chat/completions</mark>" est ajoutée
* Lorsque l'adresse API se termine par `#`, aucune concaténation n'est effectuée, seule l'adresse saisie est utilisée.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Ajout de modèles

En général, cliquez sur le bouton `Gérer` en bas à gauche de la page de configuration du fournisseur pour récupérer automatiquement tous les modèles pris en charge. Cliquez ensuite sur `+` dans la liste obtenue pour les ajouter à la liste des modèles.

{% hint style="info" %}
Les modèles de la fenêtre contextuelle ne sont pas tous ajoutés automatiquement. Vous devez cliquer sur `+` à droite du modèle pour l'ajouter à la liste des modèles de la page de configuration, afin qu'il apparaisse dans la liste de sélection des modèles.
{% endhint %}

### Vérification de la connectivité

Cliquez sur le bouton de vérification après la zone de saisie de la clé API pour tester la configuration.

{% hint style="info" %}
Par défaut, la vérification utilise le dernier modèle de conversation ajouté à la liste. En cas d'échec, vérifiez la présence de modèles incorrects ou non pris en charge.
{% endhint %}

{% hint style="danger" %}
Après une configuration réussie, activez impérativement l'interrupteur en haut à droite. Sinon, le fournisseur restera désactivé et ses modèles seront indisponibles.
{% endhint %}