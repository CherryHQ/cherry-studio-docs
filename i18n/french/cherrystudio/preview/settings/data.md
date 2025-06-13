---
icon: database
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Paramètres des Données

Cette interface permet d'effectuer des sauvegardes cloud et locales des données client, de consulter le répertoire de données local, de vider le cache et d'autres opérations.

### Sauvegarde des Données

Actuellement, la sauvegarde des données prend uniquement en charge la méthode WebDAV. Vous pouvez choisir un service compatible WebDAV pour la sauvegarde cloud.

Vous pouvez également synchroniser les données entre plusieurs appareils via la méthode :  
`Ordinateur A` $$\xrightarrow{\text{sauvegarder}}$$ `WebDAV` $$\xrightarrow{\text{restaurer}}$$ `Ordinateur B`.

#### Exemple avec Nutstore

1. Connectez-vous à Nutstore, cliquez sur le nom d'utilisateur en haut à droite, sélectionnez "Informations du compte" :

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Sélectionnez "Options de sécurité", cliquez sur "Ajouter une application" :

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Saisissez le nom de l’application, générez un mot de passe aléatoire ;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copiez et enregistrez le mot de passe ;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtenez l’adresse du serveur, le compte et le mot de passe ;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Dans les paramètres de Cherry Studio → Paramètres des données, renseignez les informations WebDAV ;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Choisissez de sauvegarder ou restaurer les données, et paramétrez la périodicité des sauvegardes automatiques.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Les services WebDAV les plus accessibles sont généralement les clouds :

* [Nutstore](https://www.jianguoyun.com/)
* [123 Cloud](https://www.123pan.com/) (abonnement requis)
* [Alibaba Cloud](https://www.alipan.com/) (achat requis)
* [Box](https://www.box.com/) (espace gratuit : 10 Go, limitation par fichier : 250 Mo)
* [Dropbox](https://www.dropbox.com/) (gratuit 2 Go, +16 Go par parrainage)
* [TeraCloud](https://teracloud.jp/en/) (gratuit 10 Go, +5 Go par parrainage)
* [Yandex Disk](https://disk.yandex.com/) (gratuit 10 Go)

Alternatives nécessitant votre propre déploiement :

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}