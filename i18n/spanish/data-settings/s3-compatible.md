---
icon: cloud-binary
---
# Almacenamiento compatible con S3 para copias de seguridad


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio admite copias de seguridad mediante almacenamiento compatible con S3 (almacenamiento de objetos). Los servicios comunes de almacenamiento compatible con S3 incluyen: AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS y MinIO.

Basado en almacenamiento compatible con S3, se puede implementar sincronización de datos entre múltiples dispositivos mediante el flujo: `Computadora A` $$\xrightarrow{\text{copia de seguridad}}$$ `Almacenamiento S3` $$\xrightarrow{\text{recuperación}}$$ `Computadora B`.

### Configurar almacenamiento compatible con S3

1. Cree un bucket de almacenamiento de objetos y registre su nombre. **¡Se recomienda encarecidamente configurar el bucket como privado de lectura/escritura para evitar filtraciones de datos de respaldo!**
2. Consulte la documentación para obtener en la consola del servicio en la nube: `Access Key ID`, `Secret Access Key`, `Endpoint`, `Bucket`, `Region`, etc.
   - **Endpoint**: Dirección de acceso del almacenamiento S3, generalmente en formato `https://<bucket-name>.<region>.amazonaws.com` o `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`.
   - **Region**: Zona donde reside el bucket, ej. `us-west-1`, `ap-southeast-1`. Para Cloudflare R2 use `auto`.
   - **Bucket**: Nombre del bucket.
   - **Access Key ID** y **Secret Access Key**: Credenciales de autenticación.
   - **Root Path**: Opcional, ruta raíz para copias de seguridad en el bucket (vacío por defecto).
   - **Documentación relacionada**
     - AWS S3: [Obtener Access Key ID y Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
     - Cloudflare R2: [Obtener Access Key ID y Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
     - Alibaba Cloud OSS: [Obtener Access Key ID y Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
     - Tencent Cloud COS: [Obtener SecretId y SecretKey](https://cloud.tencent.com/document/product/436/37421)
3. Complete la información anterior en la configuración de copia de seguridad S3. Haga clic en "Backup" para iniciar la copia de seguridad, o en "Manage" para ver y administrar archivos de respaldo.