---
icon: cloud-binary
---
# Backup en Almacenamiento Compatible con S3


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio admite copias de seguridad mediante almacenamiento compatible con S3 (almacenamiento de objetos). Los servicios de almacenamiento compatibles con S3 más comunes incluyen: AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS y MinIO.

Utilizando almacenamiento compatible con S3, puede sincronizar datos entre múltiples dispositivos mediante el esquema: `Computadora A` $$\xrightarrow{\text{backup}}$$ `Almacenamiento S3` $$\xrightarrow{\text{restauración}}$$ `Computadora B`.

### Configuración de Almacenamiento Compatible con S3

1.  Cree un bucket de almacenamiento de objetos y registre su nombre. **¡¡Se recomienda encarecidamente configurar el bucket como privado (lectura/escritura) para evitar fugas de datos de respaldo!!**
2.  Consulte la documentación del proveedor para obtener: `Access Key ID`, `Secret Access Key`, `Endpoint`, `Bucket`, `Region`, etc.:
    -   **Endpoint**: Dirección de acceso del almacenamiento S3 (ej. `https://<bucket-name>.<region>.amazonaws.com` o `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`).
    -   **Region**: Región del bucket (ej. `us-west-1`, `ap-southeast-1`). Para Cloudflare R2 use `auto`.
    -   **Bucket**: Nombre del bucket.
    -   **Access Key ID** y **Secret Access Key**: Credenciales de autenticación.
    -   **Root Path**: (Opcional) Ruta raíz para respaldos en el bucket. Valor predeterminado: vacío.
    -   **Documentación relacionada:**
        -   AWS S3: [Obtener Access Key ID y Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
        -   Cloudflare R2: [Obtener Access Key ID y Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
        -   Alibaba Cloud OSS: [Obtener Access Key ID y Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
        -   Tencent Cloud COS: [Obtener SecretId y SecretKey](https://cloud.tencent.com/document/product/436/37421)
3.  Ingrese esta información en la configuración de respaldo S3. Haga clic en **Backup** para iniciar una copia de seguridad, o en **Manage** para ver/gestionar archivos de respaldo.