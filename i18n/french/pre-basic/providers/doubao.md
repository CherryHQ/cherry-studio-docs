
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# ByteDance (Doubao)

* Connectez-vous sur [Volc Engine](https://console.volcengine.com/)
* Cliquez directement [ici pour accéder](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Obtenir la clé API

* Accédez à [Gestion des clés API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) dans la barre latérale
* Créez une clé API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* Après création réussie, cliquez sur l'icône 👁️ de la clé API puis copiez-la

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* Collez la clé API copiée dans Cherry Studio, puis activez le commutateur du fournisseur

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Activer et ajouter des modèles

* Activez les modèles nécessaires dans [Gestion des activations](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) (bas de barre latérale). Vous pouvez activer la série Doubao, DeepSeek et autres modèles selon vos besoins.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* Trouvez l'**ID de modèle** correspondant dans la [documentation de la liste des modèles](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Exemple de liste des ID de modèle Volc Engine"><figcaption></figcaption></figure>

* Accédez aux paramètres des [services de modèles](../../cherrystudio/preview/settings/providers.md) de Cherry Studio et localisez Volc Engine
* Cliquez sur **Ajouter**, puis collez l'ID de modèle dans le champ texte

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* Ajoutez les modèles successivement en suivant ce processus

### Adresse API

Deux formats d'adresse API sont disponibles :

1. Format par défaut du client : `https://ark.cn-beijing.volces.com/api/v3/`
2. Format alternatif : `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Aucune différence fonctionnelle. Conservez le format par défaut sans modification.

Pour la différence entre les suffixes `/` et `#`, consultez la section *Adresse API des fournisseurs* dans la documentation :  
[Accéder ici](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Exemple cURL de la documentation officielle</p></figcaption></figure>