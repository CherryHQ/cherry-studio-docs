
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# GitHub Copilot

Pour utiliser GitHub Copilot, vous devez d'abord disposer d'un compte GitHub et souscrire au service GitHub Copilot. La version gratuite est également acceptée, mais elle ne prend pas en charge le dernier modèle Claude 3.7. Consultez le [site officiel de GitHub Copilot](https://github.com/features/copilot) pour plus de détails.

## Obtenir le Device Code

Cliquez sur « Connexion à GitHub » pour obtenir et copier votre Device Code.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Exemple d'obtention du Device Code"><figcaption><p>Obtention du Device Code</p></figcaption></figure>

## Saisir le Device Code dans le navigateur et autoriser

Après avoir obtenu le Device Code, cliquez sur le lien pour ouvrir votre navigateur. Connectez-vous à votre compte GitHub, saisissez le Device Code et accordez les autorisations.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Exemple d'autorisation GitHub"><figcaption><p>Autorisation GitHub</p></figcaption></figure>

Après autorisation, revenez sur Cherry Studio et cliquez sur « Connecter GitHub ». Une fois la connexion établie, votre nom d'utilisateur et votre avatar GitHub s'afficheront.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Exemple de connexion GitHub réussie"><figcaption><p>Connexion GitHub réussie</p></figcaption></figure>

## Cliquer sur « Gérer » pour obtenir la liste des modèles

Cliquez sur le bouton « Gérer » ci-dessous pour récupérer automatiquement la liste des modèles actuellement pris en charge.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Exemple d'obtention de la liste des modèles"><figcaption><p>Obtenir la liste des modèles</p></figcaption></figure>

## Questions fréquentes

### Échec de l'obtention du Device Code, veuillez réessayer

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Exemple d'échec d'obtention du Device Code"><figcaption><p>Échec de l'obtention du Device Code</p></figcaption></figure>

La requête est actuellement construite avec Axios, qui ne prend pas en charge les proxies SOCKS. Utilisez un proxy système ou HTTP, ou ne configurez pas de proxy dans CherryStudio en privilégiant un proxy global. Vérifiez d'abord votre connexion réseau pour éviter cet échec.