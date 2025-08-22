---
icon: cloud-check
---
# Configuration des services de modèles


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cette page présente uniquement les fonctionnalités de l'interface. Pour le tutoriel de configuration, consultez le [guide de configuration des fournisseurs](../../../pre-basic/providers/) dans les tutoriels de base.

{% hint style="info" %}
* Lorsque vous utilisez des fournisseurs intégrés, il suffit de renseigner la clé correspondante.
* Les appellations des clés peuvent varier selon les fournisseurs : clé secrète, clé, clé API, jeton désignent tous la même chose.
{% endhint %}

### Clé API

Dans Cherry Studio, un seul fournisseur prend en charge l'utilisation de plusieurs clés en rotation selon un cycle séquentiel de la liste.

* Ajoutez plusieurs clés en les séparant par des virgules. Exemple :

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4</strong>
</code></pre>

{% hint style="warning" %}
Vous devez utiliser **exclusivement** la virgule anglaise.
{% endhint %}

### URL de l'API

Lorsque vous utilisez des fournisseurs intégrés, il n'est généralement pas nécessaire de renseigner l'URL de l'API. Si vous devez la modifier, respectez strictement l'adresse indiquée dans la documentation officielle.

> Si le fournisseur fournit une adresse au format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, ne renseignez que la partie racine (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio ajoutera automatiquement le chemin restant (<mark style="background-color:green;">/v1/chat/completions</mark>). Un format incorrect pourrait rendre le service inutilisable.

{% hint style="info" %}
Remarque : La plupart des fournisseurs utilisent un routage unifié LLM. Si le chemin d'API du fournisseur est v2, v3/chat/completions ou autre, saisissez la version spécifique suivie de "`/`". Pour les routes non conventionnelles (<mark style="background-color:green;">/v1/chat/completions</mark>), utilisez l'adresse complète fournie avec "#" à la fin.

Autrement dit :
* Les URL avec "`/`" final ajoutent automatiquement "<mark style="background-color:green;">chat/completions</mark>"
* Les URL avec "#" final utilisent l'adresse telle quelle sans modification.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Ajouter des modèles

Cliquez généralement sur le bouton `Gérer` en bas à gauche pour récupérer automatiquement tous les modèles pris en charge par le fournisseur. Sélectionnez-les via "`+`" pour les ajouter à la liste des modèles.

{% hint style="info" %}
Les modèles de la fenêtre contextuelle ne sont pas tous ajoutés automatiquement : cliquez sur "`+`" à droite de chaque modèle pour les rendre sélectionnables dans les interfaces.
{% endhint %}

### Test de connectivité

Cliquez sur le bouton de vérification à droite du champ "Clé API" pour tester la configuration.

{% hint style="info" %}
Le test utilise par défaut le dernier modèle de conversation ajouté. En cas d'échec, vérifiez les erreurs ou les modèles non pris en charge dans votre liste.
{% endhint %}

{% hint style="danger" %}
Après configuration réussie, activez **obligatoirement** l'interrupteur en haut à droite. Sinon, le fournisseur reste inactif et ses modèles seront indisponibles.
{% endhint %}