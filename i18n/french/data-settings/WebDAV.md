---
icon: cloud-arrow-up
---
# Sauvegarde WebDAV


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio prend en charge la sauvegarde des données via le protocole WebDAV. Vous pouvez choisir un service WebDAV adapté pour effectuer des sauvegardes dans le cloud.

Basé sur WebDAV, il est possible de synchroniser les données entre plusieurs appareils via le schéma : `Ordinateur A` $$\xrightarrow{\text{sauvegarde}}$$ `WebDAV` $$\xrightarrow{\text{restauration}}$$ `Ordinateur B`.

#### Exemple avec Nutstore

1. Connectez-vous à Nutstore, cliquez sur votre nom d'utilisateur en haut à droite et sélectionnez "Informations du compte" :
<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Choisissez "Options de sécurité" puis cliquez sur "Ajouter une application" :
<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Entrez le nom de l'application et générez un mot de passe aléatoire :
<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copiez et enregistrez le mot de passe :
<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Récupérez l'adresse du serveur, le compte et le mot de passe :
<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Dans les paramètres de Cherry Studio → Paramètres des données, renseignez les informations WebDAV :
<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Sélectionnez la sauvegarde ou la restauration des données, et configurez si besoin la périodicité des sauvegardes automatiques :
<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Les services WebDAV les plus accessibles sont généralement les solutions de stockage cloud :

- [Nutstore](https://www.jianguoyun.com/)
- [123 Pan](https://www.123pan.com/) (abonnement requis)
- [Aliyun Drive](https://www.alipan.com/) (achat requis)
- [Box](https://www.box.com/) (espace gratuit de 10 Go, limitation à 250 Mo par fichier)
- [Dropbox](https://www.dropbox.com/) (2 Go gratuits, extensibles à 16 Go par parrainage)
- [TeraCloud](https://teracloud.jp/en/) (10 Go gratuits + 5 Go supplémentaires par invitation)
- [Yandex Disk](https://disk.yandex.com/) (10 Go pour les utilisateurs gratuits)

Solutions nécessitant un déploiement autonome :

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}