---
icon: cloud-arrow-up
---
# Backup via WebDAV


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




O backup de dados do Cherry Studio suporta o método WebDAV. Você pode escolher um serviço WebDAV adequado para fazer backup na nuvem.

Com base no WebDAV, você pode sincronizar dados em vários dispositivos através do método: `Computador A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restauração}}$$ `Computador B`.

#### Exemplo com Nutstore

1. Faça login no Nutstore, clique no nome de usuário no canto superior direito e selecione "Informações da conta":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecione "Opções de segurança" e clique em "Adicionar aplicativo"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Digite o nome do aplicativo e gere uma senha aleatória;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copie e registre a senha;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtenha o endereço do servidor, conta e senha;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Nas configurações do Cherry Studio → Configurações de dados, preencha as informações do WebDAV;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Escolha fazer backup ou restaurar dados e pode definir o período de tempo para backup automático.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Serviços WebDAV com baixa barreira de entrada geralmente são serviços de armazenamento em nuvem:

- [Nutstore](https://www.jianguoyun.com/)
- [123 Pan](https://www.123pan.com/) (requer assinatura)
- [Aliyun Drive](https://www.alipan.com/) (requer compra)
- [Box](https://www.box.com/) (Espaço gratuito: 10GB, limite de arquivo único: 250MB)
- [Dropbox](https://www.dropbox.com/) (2GB gratuitos, expansão até 16GB via convites)
- [TeraCloud](https://teracloud.jp/en/) (10GB gratuitos, +5GB via convites)
- [Yandex Disk](https://disk.yandex.com/) (10GB para usuários gratuitos)

Além disso, existem serviços que exigem implantação própria:

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}