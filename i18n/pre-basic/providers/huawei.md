
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

```markdown
# Huawei Cloud

I. Créez un compte et connectez-vous sur [Huawei Cloud](https://auth.huaweicloud.com/authui/login)  
II. Cliquez sur [ce lien](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) pour accéder à la console ModelArts  
III. Autorisation  

<details>
<summary>Procédure d'autorisation (ignorer si déjà autorisé)</summary>

1. Après avoir accédé au lien (II), suivez les instructions pour accéder à la page d'autorisation (cliquez sur Utilisateur IAM → Nouvelle délégation → Utilisateur standard)  
![](<../../.gitbook/assets/image (49).png>)  
2. Après avoir cliqué sur Créer, revenez à la page du lien (II)  
3. Un message indique des autorisations d'accès insuffisantes, cliquez sur "Cliquez ici" dans le message  
4. Ajoutez l'autorisation existante et confirmez  

![](<../../.gitbook/assets/image (50).png>)  
Note : Cette méthode convient aux débutants, pas besoin de lire beaucoup de contenu, suivez simplement les instructions. Si vous parvenez à obtenir l'autorisation du premier coup, utilisez votre propre méthode.  
</details>

IV. Cliquez sur Gestion de l'authentification dans la barre latérale, créez une clé API (secret) et copiez-la  
<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>  

Puis créez un nouveau fournisseur dans CherryStudio  
<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>  

Après création, saisissez la clé secrète  

V. Cliquez sur Déploiement de modèles dans la barre latérale et récupérez tous  
<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>  

VI. Cliquez sur Appel  
<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>  

Copiez l'adresse à ①, collez-la dans l'adresse du fournisseur CherryStudio et ajoutez un "#" à la fin  
et ajoutez un "#" à la fin  
et ajoutez un "#" à la fin  
et ajoutez un "#" à la fin  
et ajoutez un "#" à la fin  

Pourquoi ajouter un "#" ? [Voir ici](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)  
> Bien sûr, vous pouvez aussi ignorer cela et suivre simplement le tutoriel;  
> Vous pouvez également utiliser la méthode de suppression de v1/chat/completions pour remplir. Utilisez votre méthode si vous savez comment faire, sinon suivez strictement le tutoriel.  

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>  

Copiez ensuite le nom du modèle à ②, dans CherryStudio cliquez sur le bouton "+Ajouter" pour créer un nouveau modèle  
<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>  

Saisissez le nom du modèle tel quel, sans modifications ou guillemets. Copiez exactement comme dans l'exemple.  
<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>  

Cliquez sur Ajouter un modèle pour terminer.  

{% hint style="info" %}
Dans Huawei Cloud, chaque modèle ayant une adresse différente, chaque modèle nécessite un nouveau fournisseur. Répétez simplement les étapes ci-dessus.  
{% endhint %}
```