---
icon: cloud-check
---
# Configuração do Serviço de Modelos


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Esta página apenas apresenta as funcionalidades da interface. Para tutoriais de configuração, consulte [Configuração do Provedor](../../../pre-basic/providers/) nos tutoriais básicos.

{% hint style="info" %}
* Ao usar provedores integrados, basta preencher a chave correspondente.
* Diferentes provedores podem usar termos variados para chaves: segredo, Key, API Key, token, etc., todos referindo-se ao mesmo conceito.
{% endhint %}

### Chave da API

No Cherry Studio, um único provedor suporta múltiplas chaves em rotação, seguindo ordem sequencial da lista.

* Adicione várias chaves separadas por vírgulas em inglês. Exemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
É obrigatório usar vírgulas **em inglês**.
{% endhint %}

### Endereço da API

Ao usar provedores integrados, geralmente não é necessário preencher o endereço da API. Se precisar modificá-lo, insira exatamente como consta na documentação oficial.

> Se o provedor fornecer um endereço como <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, insira apenas a parte base (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> O Cherry Studio completará automaticamente o caminho restante (<mark style="background-color:green;">/v1/chat/completions</mark>). Endereços incorretos podem causar falhas de funcionamento.

{% hint style="info" %}
Nota: A maioria dos provedores usa rotas padronizadas para LLMs. Ações adicionais só são necessárias se:
- O caminho da API for `/v2`, `/v3/chat/completions` ou outra versão: termine o endereço com `/`
- A rota não for <mark style="background-color:green;">/v1/chat/completions</mark>: use o endereço completo fornecido pelo provedor terminado com `#`

Resumindo:
* Endereços terminados em `/`: concatenam "<mark style="background-color:green;">chat/completions</mark>"
* Endereços terminados em `#`: usam apenas o valor inserido.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Adicionar modelos

Clique no botão `Gerenciar` no canto inferior esquerdo para obter automaticamente todos os modelos suportados pelo provedor. Adicione-os à lista clicando no `+`.

{% hint style="info" %}
Modelos na janela pop-up não são adicionados automaticamente. Clique no `+` ao lado de cada modelo para incluí-los na lista de seleção.
{% endhint %}

### Verificação de conectividade

Clique no botão `Verificar` ao lado do campo de chave da API para testar a configuração.

{% hint style="info" %}
O teste usa por padrão o último modelo de conversa adicionado à lista. Falhas indicam modelos incorretos ou não suportados.
{% endhint %}

{% hint style="danger" %}
Após configuração bem-sucedida, **ative o interruptor no canto superior direito**. Caso contrário, o provedor permanecerá desativado e seus modelos não aparecerão.
{% endhint %}