---
icon: cloud-binary
---
# Stockage de sauvegarde compatible S3


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio prend en charge la sauvegarde des données via un stockage compatible S3 (stockage d'objets). Les services de stockage compatibles S3 courants incluent : AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS et MinIO.

Avec le stockage compatible S3, vous pouvez synchroniser les données entre plusieurs appareils via le schéma : `Ordinateur A` $$\xrightarrow{\text{sauvegarde}}$$ `Stockage S3` $$\xrightarrow{\text{restauration}}$$ `Ordinateur B`.

### Configuration du stockage compatible S3

1. Créez un bucket de stockage d'objets et notez son nom. **Il est fortement recommandé de configurer le bucket en lecture/écriture privée pour éviter les fuites de données de sauvegarde !**
2. Référez-vous à la documentation du fournisseur cloud pour obtenir les informations S3 : `Access Key ID`, `Secret Access Key`, `Endpoint`, `Bucket`, `Region`, etc.
   - **Endpoint** : URL d'accès au stockage compatible S3, généralement sous la forme `https://<bucket-name>.<region>.amazonaws.com` ou `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`.
   - **Region** : Zone géographique du bucket (ex: `us-west-1`, `ap-southeast-1`). Pour Cloudflare R2, indiquez `auto`.
   - **Bucket** : Nom du bucket.
   - **Access Key ID** et **Secret Access Key** : Identifiants d'authentification.
   - **Root Path** : Optionnel, chemin racine dans le bucket pour les sauvegardes (vide par défaut).
   - **Documentation associée**
     - AWS S3 : [Obtenir Access Key ID et Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
     - Cloudflare R2 : [Obtenir Access Key ID et Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
     - Alibaba Cloud OSS : [Obtenir Access Key ID et Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
     - Tencent Cloud COS : [Obtenir SecretId et SecretKey](https://cloud.tencent.com/document/product/436/37421)
3. Dans les paramètres de sauvegarde S3, renseignez ces informations. Cliquez sur "Backup" pour lancer une sauvegarde, ou sur "Manage" pour consulter/gérer les fichiers sauvegardés.