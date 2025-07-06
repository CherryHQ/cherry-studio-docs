---
icon: cloud-binary
---
# S3互換ストレージバックアップ


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




{% hint style="warning" %}
このドキュメントは中国語から翻訳されており、現在レビューされていません。翻訳が適切かどうか、順次確認する予定です。
{% endhint %}

Cherry Studioのデータバックアップは、S3互換ストレージ（オブジェクトストレージ）方式をサポートしています。代表的なS3互換ストレージサービスには、AWS S3、Cloudflare R2、Alibaba Cloud OSS、Tencent Cloud COS、およびMinIOなどがあります。

S3互換ストレージを利用することで、`Aコンピュータ` $$\xrightarrow{\text{バックアップ}}$$ `S3ストレージ` $$\xrightarrow{\text{復元}}$$ `Bコンピュータ` の形式でマルチデバイスデータ同期を実現できます。

### S3互換ストレージ設定手順

1.  オブジェクトストレージバケット（Bucket）を作成し、バケット名を記録します。**※バックアップデータ漏洩防止のため、バケットはプライベート読み書きモードに設定することを強く推奨します！**
2.  各クラウドサービスのドキュメントを参照し、管理コンソールから以下のS3互換ストレージ情報を取得します：
    - **Endpoint**：S3互換ストレージのアクセスURL（例: `https://<bucket-name>.<region>.amazonaws.com` または `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`）
    - **Region**：バケットのリージョン（例: `us-west-1`, `ap-southeast-1`）。Cloudflare R2の場合は`auto`を入力
    - **Bucket**：バケット名
    - **Access Key ID** と **Secret Access Key**：認証用クレデンシャル
    - **Root Path**（オプション）：バックアップ時のルートパス（デフォルトは空）
    - **関連ドキュメント**
        - AWS S3：[Access Key IDとSecret Access Keyの取得方法](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
        - Cloudflare R2：[Access Key IDとSecret Access Keyの取得方法](https://developers.cloudflare.com/r2/api/tokens/)
        - Alibaba Cloud OSS：[Access Key IDとAccess Key Secretの取得方法](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
        - Tencent Cloud COS：[SecretIdとSecretKeyの取得方法](https://cloud.tencent.com/document/product/436/37421)
3.  S3バックアップ設定に上記情報を入力後、「バックアップ」ボタンで実行、「管理」ボタンでバックアップファイルの一覧確認・管理が可能です。