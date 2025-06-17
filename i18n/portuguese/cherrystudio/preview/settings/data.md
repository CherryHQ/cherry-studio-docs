---
icon: database
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configurações de Dados

Esta interface permite operações como backup de dados do cliente na nuvem e local, consulta de diretórios de dados locais e limpeza de cache.

### Backup de Dados

Atualmente, o backup de dados é suportado apenas através de WebDAV. Você pode escolher serviços compatíveis com WebDAV para realizar backup na nuvem.

Também é possível sincronizar dados entre dispositivos utilizando o método:  
`Computador A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restauração}}$$ `Computador B`.

#### Usando Nutstore como exemplo

1. Acesse o Nutstore, clique no nome de usuário no canto superior direito e selecione "Informações da conta":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecione "Opções de segurança" e clique em "Adicionar aplicativo":

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Insira o nome do aplicativo e gere uma senha aleatória:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copie e registre a senha:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtenha o endereço do servidor, conta e senha:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Nas configurações do Cherry Studio → Configurações de dados, preencha as informações do WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Selecione backup ou restauração de dados e configure o intervalo para backups automáticos:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Serviços WebDAV com menor limitação geralmente são provedores de armazenamento em nuvem:

* [Nutstore](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (requer assinatura)
* [Aliyun Drive](https://www.alipan.com/) (requer compra)
* [Box](https://www.box.com/) (espaço gratuito de 10GB, limite de 250MB por arquivo.)
* [Dropbox](https://www.dropbox.com/) (2GB gratuitos, expansão para 16GB via convites.)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratuitos, +5GB via convites.)
* [Yandex Disk](https://disk.yandex.com/) (10GB para usuários gratuitos.)

Alternativas que exigem implantação própria:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}