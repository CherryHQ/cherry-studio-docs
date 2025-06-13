
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Huawei Cloud

I. Créez un compte et connectez-vous sur [Huawei Cloud](https://auth.huaweicloud.com/authui/login)

II. Cliquez sur [ce lien](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) pour accéder à la console MaaS

III. Autorisation

<details>

<summary>Étapes d'autorisation (ignorer si déjà autorisé)</summary>

1. Après avoir accédé au lien en (II), suivez les invites pour accéder à la page d'autorisation (cliquez sur Utilisateur IAM → Ajouter un mandat → Utilisateur standard)

![](<../../.gitbook/assets/image (49).png>)

2. Après la création, retournez à la page du lien en (II)
3. Un message d'erreur d'autorisation apparaîtra, cliquez sur "Cliquez ici" dans le message
4. Ajoutez l'autorisation existante et confirmez

![](<../../.gitbook/assets/image (50).png>)

Remarque : Cette méthode convient aux débutants pour éviter des contenus complexes. Suivez simplement les invites. Si vous réussissez à autoriser en une seule fois, procédez à votre manière.

</details>

IV. Cliquez sur la barre latérale "Gestion de l'authentification", créez une clé API et copiez-la

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Ensuite, créez un nouveau fournisseur dans CherryStudio

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Après création, collez la clé secrète



V. Cliquez sur la barre latérale "Déploiement de modèles", puis sur "Tout récupérer"

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

VI. Cliquez sur "Appeler"

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Copiez l'adresse à l'emplacement ①, collez-la dans l'adresse du fournisseur CherryStudio et ajoutez "#" à la fin

Ajoutez "#" à la fin

Ajoutez "#" à la fin

Ajoutez "#" à la fin

Ajoutez "#" à la fin

Pourquoi ajouter "#" ? [Voir ici](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> Vous pouvez bien sûr ignorer ce lien et simplement suivre le tutoriel.
> Vous pouvez également utiliser la méthode de suppression de v1/chat/completions pour renseigner l'adresse. Si vous savez comment faire, utilisez votre méthode. Sinon, suivez strictement le tutoriel.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Copiez ensuite le nom du modèle à l'emplacement ②, cliquez sur "+ Ajouter" dans CherryStudio pour créer un nouveau modèle

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Saisissez le nom du modèle exactement comme indiqué dans l'exemple, sans ajouts ni guillemets.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Cliquez sur "Ajouter le modèle" pour finaliser.

{% hint style="info" %}
Dans Huawei Cloud, chaque modèle ayant une adresse différente, vous devrez créer un fournisseur distinct par modèle en répétant les étapes ci-dessus.
{% endhint %}