---
icon: cloud-arrow-up
---
# Sauvegarde WebDAV


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio prend en charge la sauvegarde des données via le protocole WebDAV. Vous pouvez choisir un service WebDAV adapté pour effectuer des sauvegardes dans le cloud.

Grâce à WebDAV, la synchronisation multi-appareils s'effectue via le schéma :  
`Ordinateur A` $$\xrightarrow{\text{sauvegarde}}$$ `WebDAV` $$\xrightarrow{\text{restauration}}$$ `Ordinateur B`.

#### Exemple avec Nutstore

1. Connectez-vous à Nutstore, cliquez sur le nom d'utilisateur en haut à droite et sélectionnez "Informations du compte" :

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Sélectionnez "Options de sécurité", puis cliquez sur "Ajouter une application" :

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Saisissez le nom de l'application et générez un mot de passe aléatoire :

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copiez et enregistrez le mot de passe :

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Récupérez l'adresse du serveur, le compte et le mot de passe :

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Dans Cherry Studio > Paramètres > Configuration des données, renseignez les informations WebDAV :

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Choisissez de sauvegarder ou restaurer les données, et paramétrez la fréquence des sauvegardes automatiques :

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Services WebDAV avec faible seuil d'utilisation (stockage cloud) :
- [Nutstore](https://www.jianguoyun.com/)
- [123 Pan](https://www.123pan.com/) (abonnement requis)
- [Aliyun Drive](https://www.alipan.com/) (achat requis)
- [Box](https://www.box.com/) (espace gratuit : 10GB, taille max par fichier : 250MB)
- [Dropbox](https://www.dropbox.com/) (2GB gratuits, extensible à 16GB via parrainage)
- [TeraCloud](https://teracloud.jp/en/) (10GB gratuits + 5GB supplémentaires par parrainage)
- [Yandex Disk](https://disk.yandex.com/) (10GB pour les utilisateurs gratuits)

Services nécessitant un déploiement autonome :
- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}