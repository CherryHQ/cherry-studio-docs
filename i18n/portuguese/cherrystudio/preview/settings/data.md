---
icon: database
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configurações de Dados

Esta interface permite operações como backup de dados do cliente em nuvem e local, consulta do diretório de dados local e limpeza de cache.

### Backup de Dados

Atualmente, o backup de dados é suportado apenas através do método WebDAV. Você pode escolher serviços compatíveis com WebDAV para fazer backup na nuvem.

Também é possível sincronizar dados em múltiplos dispositivos usando o método:  
`Computador A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restauração}}$$ `Computador B`.

#### Exemplo usando Nutstore

1. Faça login no Nutstore, clique no nome de usuário no canto superior direito e selecione "Informações da conta":
<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecione "Opções de segurança" e clique em "Adicionar aplicativo":
<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Insira o nome do aplicativo e gere uma senha aleatória:
<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copie e registre a senha:
<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtenha o endereço do servidor, nome de usuário e senha:
<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. No Cherry Studio Configurações > Configurações de Dados, preencha as informações WebDAV:
<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Selecione fazer backup ou restaurar dados e configure o intervalo de backup automático:
<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Serviços WebDAV com baixo limite de acesso geralmente são serviços de armazenamento em nuvem:
* [Nutstore](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (requer assinatura)
* [AliPan](https://www.alipan.com/) (requer compra)
* [Box](https://www.box.com/) (espaço gratuito de 10GB, limite de 250MB por arquivo)
* [Dropbox](https://www.dropbox.com/) (2GB gratuito, ampliável para 16GB com convites)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratuito, +5GB com convites)
* [Yandex Disk](https://disk.yandex.com/) (10GB gratuito)

Serviços que exigem autoimplatação:
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}