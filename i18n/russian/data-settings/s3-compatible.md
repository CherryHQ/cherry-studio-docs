---
icon: cloud-binary
---
# Резервное копирование в S3-совместимое хранилище


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




Резервное копирование данных Cherry Studio поддерживается через S3-совместимое хранилище (объектное хранилище). Распространённые S3-совместимые сервисы: AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS и MinIO.

На основе S3-совместимого хранилища можно реализовать синхронизацию данных между устройствами по схеме: `Компьютер A` $$\xrightarrow{\text{резервное копирование}}$$ `S3-хранилище` $$\xrightarrow{\text{восстановление}}$$ `Компьютер B`.

### Настройка S3-совместимого хранилища

1.  Создайте бакет (Bucket) объектного хранилища и запишите его имя. **Настоятельно рекомендуется установить для бакета режим приватного чтения/записи для предотвращения утечки резервных данных!**
2.  Обратитесь к документации вашего облачного провайдера, чтобы получить в консоли управления следующие параметры S3-хранилища: `Access Key ID`, `Secret Access Key`, `Endpoint`, `Bucket`, `Region`.
    - **Endpoint**: Адрес доступа к S3-хранилищу, обычно в формате `https://<bucket-name>.<region>.amazonaws.com` или `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`.
    - **Region**: Регион расположения бакета, например `us-west-1`, `ap-southeast-1`. Для Cloudflare R2 укажите `auto`.
    - **Bucket**: Имя бакета.
    - **Access Key ID** и **Secret Access Key**: Учётные данные для аутентификации.
    - **Root Path**: Опциональный параметр, указывает корневой путь для резервных копий в бакете (по умолчанию пустой).
    - **Документация**
        - AWS S3: [Получение Access Key ID и Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
        - Cloudflare R2: [Получение Access Key ID и Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
        - Alibaba Cloud OSS: [Получение Access Key ID и Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
        - Tencent Cloud COS: [Получение SecretId и SecretKey](https://cloud.tencent.com/document/product/436/37421)
3.  Введите полученные данные в настройках резервного копирования S3. Нажмите "Backup" для создания резервной копии или "Manage" для просмотра и управления файлами резервных копий.