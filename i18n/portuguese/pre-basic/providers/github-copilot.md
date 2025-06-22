
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# GitHub Copilot

Para usar o GitHub Copilot, primeiro você precisa ter uma conta no GitHub e assinar o serviço GitHub Copilot. A assinatura gratuita (free) também funciona, mas a versão gratuita não suporta o modelo mais recente Claude 3.7. Para detalhes, consulte o [site oficial do GitHub Copilot](https://github.com/features/copilot).

## Obter Device Code

Clique em "Login GitHub" para obter o Device Code e copie-o.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Imagem de exemplo de obtenção do Device Code"><figcaption><p>Obter Device Code</p></figcaption></figure>

## Preencher o Device Code no navegador e autorizar

Após obter o Device Code com sucesso, clique no link para abrir o navegador. Faça login na sua conta GitHub no navegador, insira o Device Code e autorize o acesso.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Exemplo de autorização GitHub.png"><figcaption><p>Autorização do GitHub</p></figcaption></figure>

Após a autorização bem-sucedida, retorne ao Cherry Studio e clique em "Conectar GitHub". Após a conexão bem-sucedida, seu nome de usuário e avatar do GitHub serão exibidos.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Exemplo de conexão bem-sucedida ao GitHub"><figcaption><p>Conexão do GitHub bem-sucedida</p></figcaption></figure>

## Clique em "Gerenciar" para obter a lista de modelos

Clique no botão "Gerenciar" abaixo para buscar automaticamente via internet a lista de modelos suportados atualmente.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Exemplo de obtenção da lista de modelos"><figcaption><p>Obter lista de modelos</p></figcaption></figure>

## Perguntas frequentes

### Falha ao obter o Device Code. Tente novamente

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Exemplo de falha ao obter o Device Code"><figcaption><p>Falha ao obter o Device Code</p></figcaption></figure>

Atualmente, usamos o Axios para construir solicitações. O Axios não suporta proxy SOCKS. Use proxy de sistema, proxy HTTP ou não configure proxy no CherryStudio, utilizando um proxy global. Primeiro, certifique-se de que sua conexão de rede esteja normal para evitar falhas ao obter o Device Code.