
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# GitHub Copilot

Pour utiliser GitHub Copilot, vous devez d'abord disposer d'un compte GitHub et souscrire au service GitHub Copilot. L'abonnement gratuit est possible, mais la version gratuite ne prend pas en charge le dernier modèle Claude 3.7. Pour plus de détails, consultez le [site officiel de GitHub Copilot](https://github.com/features/copilot).

## Obtenir le Device Code

Cliquez sur « Se connecter à GitHub » pour obtenir le Device Code et copiez-le.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Exemple d'obtention du Device Code"><figcaption><p>Obtenir le Device Code</p></figcaption></figure>

## Remplir le Device Code dans le navigateur et autoriser

Après avoir obtenu le Device Code, cliquez sur le lien pour ouvrir le navigateur. Connectez-vous à votre compte GitHub, saisissez le Device Code et autorisez l'accès.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Autorisation GitHub"><figcaption><p>Autorisation GitHub</p></figcaption></figure>

Après autorisation réussie, revenez à Cherry Studio et cliquez sur « Connecter GitHub ». Une fois connecté, votre nom d'utilisateur et votre avatar GitHub s'afficheront.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Connexion GitHub réussie"><figcaption><p>Connexion GitHub réussie</p></figcaption></figure>

## Cliquer sur « Gérer » pour obtenir la liste des modèles

Cliquez sur le bouton « Gérer » ci-dessous pour récupérer automatiquement la liste des modèles actuellement pris en charge.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Obtenir la liste des modèles"><figcaption><p>Obtenir la liste des modèles</p></figcaption></figure>

## Questions fréquentes

### Échec d'obtention du Device Code, veuillez réessayer

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Échec d'obtention du Device Code"><figcaption><p>Échec d'obtention du Device Code</p></figcaption></figure>

Les requêtes actuelles utilisent Axios, qui ne prend pas en charge les proxy SOCKS. Utilisez un proxy système ou HTTP, ou ne configurez pas de proxy dans CherryStudio pour utiliser un proxy global. Assurez-vous d'abord que votre connexion réseau est normale pour éviter cet échec.