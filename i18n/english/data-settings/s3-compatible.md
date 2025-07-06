---
icon: cloud-binary
---
# S3 Compatible Storage Backup


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




Cherry Studio data backup supports backup via S3 compatible storage (object storage). Common S3 compatible storage services include: AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS, and MinIO.

Based on S3 compatible storage, multi-terminal data synchronization can be achieved by the method of `Computer A` $$\xrightarrow{\text{Backup}}$$ `S3 Storage` $$\xrightarrow{\text{Restore}}$$ `Computer B`.

### Configure S3 Compatible Storage

1.  Create an object storage bucket, and record the bucket name. **It is highly recommended to set the bucket to private read/write to prevent backup data leakage!!**
2.  Refer to the documentation, go to the cloud service console to obtain information such as `Access Key ID`, `Secret Access Key`, `Endpoint`, `Bucket`, `Region` for S3 compatible storage.
    *   **Endpoint**: The access address for S3 compatible storage, usually in the form of `https://<bucket-name>.<region>.amazonaws.com` or `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`.
    *   **Region**: The region where the bucket is located, such as `us-west-1`, `ap-southeast-1`, etc. For Cloudflare R2, please fill in `auto`.
    *   **Bucket**: The bucket name.
    *   **Access Key ID** and **Secret Access Key**: Credentials used for authentication.
    *   **Root Path**: Optional, specifies the root path when backing up to the bucket, default is empty.
    *   **Related Documentation**
        *   AWS S3: [Obtain Access Key ID and Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
        *   Cloudflare R2: [Obtain Access Key ID and Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
        *   Alibaba Cloud OSS: [Obtain Access Key ID and Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
        *   Tencent Cloud COS: [Obtain SecretId and SecretKey](https://cloud.tencent.com/document/product/436/37421)
3.  Fill in the above information in the S3 backup settings, click the backup button to perform backup, and click the manage button to view and manage the list of backup files.