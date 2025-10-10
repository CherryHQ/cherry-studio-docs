---
icon: cloud-check
---
# Configuração do Serviço de Modelos


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Esta página apresenta apenas as funcionalidades da interface. Para tutoriais de configuração, consulte o guia [Configuração de Provedores](../../../pre-basic/providers/) nos tutoriais básicos.

{% hint style="info" %}
* Ao usar provedores integrados, basta preencher a chave correspondente.
* Provedores diferentes podem usar terminologias diversas para chaves: chave secreta, Key, API Key ou token referem-se ao mesmo conceito.
{% endhint %}

### Chave de API

No Cherry Studio, um único provedor suporta múltiplas chaves em uso rotativo, seguindo uma sequência cíclica da primeira à última chave na lista.

* Adicione múltiplas chaves separadas por vírgulas em inglês, conforme o exemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
É obrigatório usar vírgulas em **inglês**.
{% endhint %}

### Endereço da API

Geralmente não é necessário preencher o endereço da API ao usar provedores integrados. Caso precise modificar, insira exatamente o endereço fornecido na documentação oficial.

> Se o provedor fornecer um endereço no formato <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, insira apenas a parte raiz (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> O Cherry Studio concatenará automaticamente o caminho restante (<mark style="background-color:green;">/v1/chat/completions</mark>). Preenchimentos incorretos podem causar falhas de funcionamento.

{% hint style="info" %}
Observação: A maioria dos provedores usa rotas unificadas para modelos de linguagem, geralmente não requerendo ajustes. Se o caminho da API for v2, v3/chat/completions ou outra versão, adicione manualmente a versão com "`/`" no final. Para rotas não convencionais (<mark style="background-color:green;">/v1/chat/completions</mark>), use o endereço completo fornecido pelo provedor terminado em `#`.

Resumindo:
* Endereços terminados em `/` concatenam automaticamente "<mark style="background-color:green;">chat/completions</mark>"
* Endereços terminados em `#` utilizam apenas o endereço inserido, sem concatenação.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Adicionar Modelos

Normalmente, clique no botão `Gerenciar` no canto inferior esquerdo da página de configuração do provedor para obter automaticamente todos os modelos suportados. Selecione modelos na lista e clique em `+` para adicioná-los à lista de modelos.

{% hint style="info" %}
Ao clicar em "Gerenciar", os modelos na janela pop-up não são adicionados automaticamente. É necessário clicar em `+` ao lado de cada modelo para que apareçam na lista de seleção de modelos.
{% endhint %}

### Verificação de Conectividade

Clique no botão de verificação ao lado do campo de chave de API para testar a configuração.

{% hint style="info" %}
O teste usa por padrão o último modelo de conversa adicionado à lista. Se houver falhas, verifique se há modelos incorretos ou não suportados na lista.
{% endhint %}

{% hint style="danger" %}
Após a configuração bem-sucedida, **ative obrigatoriamente** o interruptor no canto superior direito. Caso contrário, o provedor permanecerá desativado e seus modelos não aparecerão na lista.
{% endhint %}