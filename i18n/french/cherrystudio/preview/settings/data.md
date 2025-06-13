---
icon: database
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Paramétrage des données

Cette interface permet d'effectuer des opérations telles que la sauvegarde des données client sur le cloud et localement, la consultation des répertoires de données locaux et l'effacement du cache.

### Sauvegarde des données

Actuellement, la sauvegarde des données ne prend en charge que la méthode WebDAV. Vous pouvez choisir des services compatibles WebDAV pour la sauvegarde sur le cloud.

Vous pouvez également synchroniser les données entre plusieurs appareils via la méthode : `Ordinateur A` $$\xrightarrow{\text{sauvegarde}}$$ `WebDAV` $$\xrightarrow{\text{restauration}}$$ `Ordinateur B`.

#### Prendre Nutstore comme exemple

1. Connectez-vous à Nutstore, cliquez sur le nom d'utilisateur en haut à droite et sélectionnez "Informations du compte" :

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Sélectionnez "Options de sécurité", cliquez sur "Ajouter une application"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Saisissez le nom de l'application, générez un mot de passe aléatoire ;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copiez le mot de passe enregistré ;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtenez l'adresse du serveur, le compte et le mot de passe ;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Dans les paramètres de Cherry Studio → Paramétrage des données, renseignez les informations WebDAV ;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Sélectionnez la sauvegarde ou la restauration des données, et paramétrez éventuellement la périodicité des sauvegardes automatiques.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Les services WebDAV avec une faible barrière d'entrée sont généralement les solutions de stockage en cloud :

* [Nutstore](https://www.jianguoyun.com/)
* [123 Cloud](https://www.123pan.com/) (abonnement requis)
* [Alibaba Cloud Drive](https://www.alipan.com/) (achat nécessaire)
* [Box](https://www.box.com/) (espace gratuit de 10GB, taille de fichier limitée à 250MB)
* [Dropbox](https://www.dropbox.com/) (2GB gratuit, extensible à 16GB via parrainage)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratuit + 5GB supplémentaires par parrainage)
* [Yandex Disk](https://disk.yandex.com/) (10GB pour les utilisateurs gratuits)

Ensuite, il y a des services nécessitant un déploiement autonome :

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}