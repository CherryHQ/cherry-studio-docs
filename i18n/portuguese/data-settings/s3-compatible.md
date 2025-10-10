---
icon: cloud-binary
---
# Backup em Armazenamento Compatível com S3


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




O backup de dados do Cherry Studio suporta armazenamento compatível com S3 (armazenamento de objetos). Serviços comuns de armazenamento compatível com S3 incluem: AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS e MinIO.

A sincronização de dados entre múltiplos dispositivos pode ser realizada através do fluxo: `Computador A` $$\xrightarrow{\text{backup}}$$ `Armazenamento S3` $$\xrightarrow{\text{restauração}}$$ `Computador B`.

### Configurar Armazenamento Compatível com S3

1.  Crie um bucket de armazenamento de objetos e registre seu nome. **É altamente recomendável configurar o bucket como leitura/escrita privada para evitar vazamento de dados de backup!!**
2.  Consulte a documentação para obter no console do serviço em nuvem as informações de `Access Key ID`, `Secret Access Key`, `Endpoint`, `Bucket`, `Region`:
    - **Endpoint**: Endereço de acesso ao armazenamento S3 (ex: `https://<bucket-name>.<region>.amazonaws.com` ou `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`).
    - **Region**: Região do bucket (ex: `us-west-1`, `ap-southeast-1`). Para Cloudflare R2, use `auto`.
    - **Bucket**: Nome do bucket.
    - **Access Key ID** e **Secret Access Key**: Credenciais de autenticação.
    - **Root Path**: Opcional, caminho raiz para backup no bucket (padrão: vazio).
    - **Documentação Relacionada**
      - AWS S3: [Obter Access Key ID e Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
      - Cloudflare R2: [Obter Access Key ID e Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
      - Alibaba Cloud OSS: [Obter Access Key ID e Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
      - Tencent Cloud COS: [Obter SecretId e SecretKey](https://cloud.tencent.com/document/product/436/37421)
3.  Preencha as informações acima nas configurações de backup S3. Clique em **Backup** para iniciar o processo ou em **Gerenciar** para visualizar/gerenciar arquivos de backup.