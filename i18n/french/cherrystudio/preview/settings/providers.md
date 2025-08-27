---
icon: cloud-check
---
# Configuration du service de modèles


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cette page présente uniquement les fonctionnalités de l'interface. Pour le tutoriel de configuration, veuillez consulter [Configuration des fournisseurs](../../../pre-basic/providers/) dans les tutoriels de base.

{% hint style="info" %}
* Lors de l'utilisation de fournisseurs intégrés, il suffit de renseigner la clé correspondante.
* Les dénominations des clés peuvent varier selon les fournisseurs : clé, Key, API Key, jeton, etc. désignent tous la même chose.
{% endhint %}

### Clé API

Dans Cherry Studio, un seul fournisseur supporte l'utilisation rotative de plusieurs clés via un cycle séquentiel dans la liste.

* Ajoutez plusieurs clés en les séparant par des virgules anglaises. Par exemple :

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Vous devez utiliser des virgules **anglaises**.
{% endhint %}

### Adresse API

Aucun renseignement n'est généralement nécessaire pour les fournisseurs intégrés. Si modification requise, suivez scrupuleusement l'adresse fournie dans la documentation officielle correspondante.

> Si le fournisseur indique une adresse au format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, saisissez uniquement la partie racine (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio ajoutera automatiquement le chemin restant (<mark style="background-color:green;">/v1/chat/completions</mark>). Un format incorrect peut entraîner des dysfonctionnements.

{% hint style="info" %}
Remarque : La majorité des fournisseurs utilisent des routes unifiées pour les modèles linguistiques. Si le chemin d'API du fournisseur est v2, v3/chat/completions ou une autre version, terminez l'adresse manuellement par "`/`". Pour les chemins non standard (<mark style="background-color:green;">/v1/chat/completions</mark>), utilisez l'adresse complète fournie par le fournisseur et terminez par `#`.

Ainsi :
* Les adresses API terminées par `/` ajoutent uniquement "<mark style="background-color:green;">chat/completions</mark>"
* Les adresses API terminées par `#` n'effectuent aucun ajout et utilisent exactement l'adresse saisie.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Ajouter un modèle

Cliquez généralement sur le bouton `Gérer` en bas à gauche de la page de configuration du fournisseur pour récupérer automatiquement tous ses modèles disponibles, puis ajoutez-les à la liste via le `+`.

{% hint style="info" %}
Les modèles de la fenêtre contextuelle ne sont pas ajoutés automatiquement. Utilisez le `+` à droite de chaque modèle pour les intégrer à la liste des configurations, où ils deviendront sélectionnables.
{% endhint %}

### Vérification de la connectivité

Cliquez sur le bouton de vérification situé après le champ de clé API pour tester la configuration.

{% hint style="info" %}
La vérification utilise par défaut le dernier modèle conversationnel ajouté. En cas d'échec, vérifiez la présence de modèles incorrects ou non supportés dans la liste.
{% endhint %}

{% hint style="danger" %}
Après une configuration réussie, activez impérativement l'interrupteur en haut à droite, sans quoi le fournisseur restera inactif et ses modèles invisibles.
{% endhint %}