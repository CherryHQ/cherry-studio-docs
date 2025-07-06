---
icon: cloud-binary
---
# Sauvegarde de stockage compatible S3


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




La sauvegarde des données de Cherry Studio prend en charge le stockage compatible S3 (stockage objet). Les services de stockage compatibles S3 courants incluent : AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS et MinIO.

Grâce au stockage compatible S3, vous pouvez synchroniser les données entre plusieurs appareils via la méthode : `Ordinateur A` $$\xrightarrow{\text{sauvegarde}}$$ `Stockage S3` $$\xrightarrow{\text{restauration}}$$ `Ordinateur B`.

### Configuration du stockage compatible S3

1. Créez un compartiment de stockage d'objets (Bucket) et notez son nom. **Il est fortement recommandé de définir le compartiment en lecture/écriture privée pour éviter les fuites de données de sauvegarde !!**
2. Consultez la documentation et accédez à la console du service cloud pour obtenir les informations du stockage compatible S3 telles que `Access Key ID`, `Secret Access Key`, `Endpoint`, `Bucket`, `Region`, etc.
   - **Endpoint** : Adresse d'accès du stockage compatible S3, généralement sous la forme `https://<bucket-name>.<region>.amazonaws.com` ou `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`.
   - **Region** : Région où se trouve le compartiment, par exemple `us-west-1`, `ap-southeast-1`, etc. Pour Cloudflare R2, indiquez `auto`.
   - **Bucket** : Nom du compartiment.
   - **Access Key ID** et **Secret Access Key** : Informations d'identification pour l'authentification.
   - **Root Path** : Optionnel, spécifie le chemin racine lors de la sauvegarde dans le compartiment, vide par défaut.
   - **Documentation associée**
     - AWS S3 : [Obtenir Access Key ID et Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
     - Cloudflare R2 : [Obtenir Access Key ID et Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
     - Alibaba Cloud OSS : [Obtenir Access Key ID et Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
     - Tencent Cloud COS : [Obtenir SecretId et SecretKey](https://cloud.tencent.com/document/product/436/37421)
3. Dans les paramètres de sauvegarde S3, remplissez les informations ci-dessus, cliquez sur le bouton **Sauvegarder** pour effectuer la sauvegarde, et cliquez sur le bouton **Gérer** pour afficher et gérer la liste des fichiers de sauvegarde.