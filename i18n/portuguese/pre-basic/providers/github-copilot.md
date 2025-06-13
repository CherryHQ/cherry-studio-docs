
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# GitHub Copilot

Para usar o GitHub Copilot, você precisa ter uma conta no GitHub e assinar o serviço GitHub Copilot. A versão gratuita também é aceitável, mas ela não oferece suporte ao modelo Claude 3.7 mais recente. Para detalhes, consulte o [site oficial do GitHub Copilot](https://github.com/features/copilot).

## Obter Device Code

Clique em "登录 GitHub" para gerar e copiar um Device Code.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Exemplo de obtenção de Device Code"><figcaption><p>Obter Device Code</p></figcaption></figure>

## Preencher Device Code no navegador e autorizar

Após gerar o Device Code, clique no link para abrir o navegador. Faça login na conta GitHub, insira o Device Code e conceda autorização.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Exemplo de autorização no GitHub"><figcaption><p>Autorização GitHub</p></figcaption></figure>

Após autorizar, retorne ao Cherry Studio e clique em "连接 GitHub". O sucesso será confirmado com a exibição do nome de usuário e avatar do GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Exemplo de conexão bem-sucedida"><figcaption><p>Conexão GitHub bem-sucedida</p></figcaption></figure>

## Clique em "管理" para obter a lista de modelos

Clique no botão "管理" na parte inferior para buscar automaticamente a lista de modelos suportados.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Exemplo de obtenção da lista de modelos"><figcaption><p>Obter lista de modelos</p></figcaption></figure>

## Perguntas frequentes

### Falha ao obter Device Code, tente novamente

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Exemplo de falha na obtenção de Device Code"><figcaption><p>Falha ao obter Device Code</p></figcaption></figure>

Atualmente usamos Axios para solicitações, que não oferece suporte a proxy socks. Utilize proxy de sistema, HTTP proxy ou configure o Cherry Studio sem proxy (usando proxy global). Garanta primeiro que sua conexão de internet esteja estável para evitar falhas na obtenção do Device Code.