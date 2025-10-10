---
icon: cloud-binary
---
# S3 相容儲存備份


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




Cherry Studio 資料備份支援透過 S3 相容儲存（物件儲存）的方式進行備份。常見的 S3 相容儲存服務有：AWS S3、Cloudflare R2、阿里雲 OSS、騰訊雲 COS 以及 MinIO 等。

基於 S3 相容儲存可以透過 `A電腦` $$\xrightarrow{\text{備份}}$$ `S3儲存` $$\xrightarrow{\text{恢復}}$$ `B電腦` 的方式來實現多端資料同步。

### 配置 S3 相容儲存

1.  建立物件儲存桶（Bucket），並記錄下儲存桶名稱。**強烈建議將儲存桶設定為私有讀寫以避免備份資料洩露！！**
2.  參考文件，前往雲服務控制台取得 S3 相容儲存的 `Access Key ID`、`Secret Access Key`、`Endpoint`、`Bucket`、`Region` 等資訊。
    - **Endpoint**：S3 相容儲存的存取地址，通常形如 `https://<bucket-name>.<region>.amazonaws.com` 或 `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`。
    - **Region**：儲存桶所在的區域，例如 `us-west-1`、`ap-southeast-1` 等，cloudflare R2 請填寫 `auto`。
    - **Bucket**：儲存桶名稱。
    - **Access Key ID** 和 **Secret Access Key**：用於身份驗證的憑證。
    - **Root Path**：可選，指定備份到儲存桶時的根路徑，預設為空。
    - **相關文件**
        - AWS S3：[取得 Access Key ID 和 Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
        - Cloudflare R2：[取得 Access Key ID 和 Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
        - 阿里雲 OSS：[取得 Access Key ID 和 Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
        - 騰訊雲 COS：[取得 SecretId 和 SecretKey](https://cloud.tencent.com/document/product/436/37421)
3.  在 S3 備份設定中填寫上述資訊，點擊備份按鈕即可進行備份，點擊管理按鈕可以查看和管理備份檔案列表。