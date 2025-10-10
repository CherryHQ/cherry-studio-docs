# GitHub Copilot


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Para usar o GitHub Copilot, você precisa primeiro ter uma conta GitHub e assinar o serviço GitHub Copilot. A assinatura da versão gratuita (free) também é válida, mas observe que a versão gratuita não suporta o modelo mais recente Claude 3.7. Detalhes podem ser encontrados no [site oficial do GitHub Copilot](https://github.com/features/copilot).

## Obter Device Code

Clique em "Login GitHub" para obter e copiar o Device Code.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Exemplo de obtenção do Device Code"><figcaption><p>Obter Device Code</p></figcaption></figure>

## Inserir Device Code no navegador e autorizar

Após obter o Device Code com sucesso, clique no link para abrir o navegador. Faça login na sua conta GitHub, insira o Device Code e conceda a autorização.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Exemplo de autorização GitHub"><figcaption><p>Autorização GitHub</p></figcaption></figure>

Após autorização bem-sucedida, retorne ao Cherry Studio e clique em "Conectar GitHub". Após conexão bem-sucedida, seu nome de usuário e avatar do GitHub serão exibidos.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Exemplo de conexão GitHub bem-sucedida"><figcaption><p>Conexão GitHub bem-sucedida</p></figcaption></figure>

## Clique em "Gerenciar" para obter lista de modelos

Clique no botão "Gerenciar" abaixo para buscar automaticamente pela Internet a lista de modelos atualmente suportados.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Exemplo do botão Gerenciar para obter lista de modelos"><figcaption><p>Obter lista de modelos</p></figcaption></figure>

## Perguntas frequentes

### Falha ao obter Device Code, tente novamente

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Exemplo de falha ao obter Device Code"><figcaption><p>Falha ao obter Device Code</p></figcaption></figure>

Atualmente, as solicitações são construídas usando Axios. O Axios não suporta proxies SOCKS. Utilize proxy de sistema ou proxy HTTP, ou simplesmente não configure proxy no CherryStudio usando proxy global. Primeiro, verifique se sua conexão de rede está normal para evitar falhas na obtenção do Device Code.