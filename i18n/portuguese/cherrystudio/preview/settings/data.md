---
icon: database
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Definições de Dados

Esta interface permite realizar operações como backup local e em nuvem de dados do cliente, consulta de diretórios de dados locais e limpeza de cache.

### Backup de Dados

Atualmente, o backup de dados é suportado apenas através do método WebDAV. Você pode escolher serviços compatíveis com WebDAV para realizar backups em nuvem.

Você também pode sincronizar dados entre dispositivos usando:  
`Computador A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restauro}}$$ `Computador B`

#### Exemplo com Nutstore

1. Faça login no Nutstore, clique no nome de usuário no canto superior direito e selecione "Informações da Conta":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecione "Opções de Segurança" e clique em "Adicionar Aplicativo":

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Insira o nome do aplicativo e gere uma senha aleatória:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copie e registre a senha:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtenha o endereço do servidor, nome de usuário e senha:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. No Cherry Studio (Configurações > Definições de Dados), preencha as informações do WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Selecione "Backup" ou "Restaurar Dados" e configure o intervalo de backup automático:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Serviços WebDAV com baixa barreira de entrada (armazenamento em nuvem):
* [Nutstore](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (requer assinatura)
* [Aliyun Drive](https://www.alipan.com/) (requer compra)
* [Box](https://www.box.com/) (10GB gratuitos, limite de 250MB por arquivo)
* [Dropbox](https://www.dropbox.com/) (2GB gratuitos, expansão para 16GB via convites)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratuitos, +5GB via convites)
* [Yandex Disk](https://disk.yandex.com/) (10GB para usuários gratuitos)

Serviços de autohospedagem:
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}