---
icon: database
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Paramètres de données

Cette interface permet de sauvegarder les données client dans le cloud ou localement, de consulter le répertoire de données local et d'effacer le cache, entre autres opérations.

### Sauvegarde des données

Actuellement, la sauvegarde des données ne prend en charge que la méthode WebDAV. Vous pouvez choisir un service compatible WebDAV pour la sauvegarde cloud.

Vous pouvez également synchroniser des données sur plusieurs appareils via : `Ordinateur A` $$\xrightarrow{\text{sauvegarde}}$$ `WebDAV` $$\xrightarrow{\text{restauration}}$$ `Ordinateur B`.

#### Exemple avec Nutstore

1. Connectez-vous à Nutstore, cliquez sur votre nom d'utilisateur en haut à droite et sélectionnez "Informations du compte" :

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Sélectionnez "Options de sécurité" et cliquez sur "Ajouter une application" :

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Entrez un nom d'application et générez un mot de passe aléatoire :

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copiez et enregistrez le mot de passe :

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtenez l'adresse du serveur, le compte et le mot de passe :

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Dans les paramètres de Cherry Studio > Paramètres de données, saisissez les informations WebDAV :

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Choisissez de sauvegarder ou restaurer les données, et définissez éventuellement la périodicité des sauvegardes automatiques :

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Les services WebDAV les plus accessibles sont généralement des plateformes de stockage cloud :
* [Nutstore](https://www.jianguoyun.com/)
* [123 Cloud](https://www.123pan.com/) (abonnement requis)
* [Aliyun Drive](https://www.alipan.com/) (achat requis)
* [Box](https://www.box.com/) (espace gratuit : 10GB, taille max par fichier : 250MB)
* [Dropbox](https://www.dropbox.com/) (2GB gratuit + 16GB supplémentaires via parrainage)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratuit + 5GB supplémentaires via parrainage)
* [Yandex Disk](https://disk.yandex.com/) (10GB gratuit)

Alternatives nécessitant un déploiement autonome :
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}