
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# ByteDance (Doubao)

* Connectez-vous à [Volc Engine](https://console.volcengine.com/)
* Cliquez directement [ici pour accéder](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Obtenir une clé API

* Cliquez sur [Gestion des clés API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) dans la barre latérale
* Créez une clé API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* Après création réussie, cliquez sur l'icône en forme d'œil à côté de votre clé API pour l'afficher et la copier

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* Collez la clé API copiée dans CherryStudio, puis activez le commutateur du fournisseur de service.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Activer et ajouter des modèles

* Activez les modèles nécessaires dans [Gestion des activations](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) de la console Ark. Vous pouvez activer la série Doubao, DeepSeek ou d'autres modèles selon vos besoins.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* Dans le [document de liste des modèles](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), localisez l'ID de modèle correspondant au modèle requis.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Exemple de liste des ID de modèle de Volc Engine"><figcaption></figcaption></figure>

* Accédez aux [paramètres des services de modèles](../../cherrystudio/preview/settings/providers.md) de Cherry Studio et sélectionnez Volc Engine
* Cliquez sur "Ajouter" et collez l'ID de modèle obtenu dans la zone de texte ID de modèle

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* Ajoutez les modèles un par un en suivant ce processus

### Adresse API

L'adresse API peut s'écrire de deux manières

* La première est celle par défaut du client : `https://ark.cn-beijing.volces.com/api/v3/`
* La deuxième écriture est : `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Les deux formats sont équivalents. Gardez celui par défaut, aucune modification n'est nécessaire.

Concernant la différence entre les terminaisons par `/` et `#`, consultez la section sur l'adresse API des paramètres du fournisseur dans la documentation : [cliquez ici](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Exemple de cURL dans la documentation officielle</p></figcaption></figure>