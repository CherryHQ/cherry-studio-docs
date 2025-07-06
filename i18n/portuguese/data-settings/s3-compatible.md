---
icon: cloud-binary
---
# Armazenamento S3 Compatível para Backup


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




O backup de dados do Cherry Studio é suportado através de armazenamento compatível com S3 (armazenamento de objetos). Serviços comuns de armazenamento compatível com S3 incluem: AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS e MinIO, entre outros.

Com base no armazenamento compatível com S3, a sincronização de dados entre múltiplos dispositivos pode ser realizada através de: `Computador A` $$\xrightarrow{\text{backup}}$$ `Armazenamento S3` $$\xrightarrow{\text{restaurar}}$$ `Computador B`.

### Configurar Armazenamento S3 Compatível

1.  Crie um bucket de armazenamento de objetos (Bucket) e registre seu nome. **É altamente recomendável definir o bucket como privado para leitura/escrita para evitar vazamento de dados de backup!!**
2.  Consulte a documentação e acesse o console do serviço em nuvem para obter:
    `Access Key ID`, `Secret Access Key`, `Endpoint`, `Bucket`, `Region` e outras informações:
    - **Endpoint**: Endereço de acesso do armazenamento S3 compatível, geralmente no formato `https://<bucket-name>.<region>.amazonaws.com` ou `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`.
    - **Region**: Região onde o bucket está localizado (ex: `us-west-1`, `ap-southeast-1`). Para Cloudflare R2 use `auto`.
    - **Bucket**: Nome do bucket.
    - **Access Key ID** e **Secret Access Key**: Credenciais para autenticação.
    - **Root Path**: (Opcional) Caminho raiz para backups no bucket. Padrão: vazio.
    - **Documentação relacionada**:
      - AWS S3: [Obter Access Key ID e Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
      - Cloudflare R2: [Obter Access Key ID e Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
      - Alibaba Cloud OSS: [Obter Access Key ID e Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
      - Tencent Cloud COS: [Obter SecretId e SecretKey](https://cloud.tencent.com/document/product/436/37421)
3.  Insira essas informações nas configurações de backup S3. Clique em **Backup** para iniciar ou em **Gerenciar** para visualizar/administrar arquivos de backup.