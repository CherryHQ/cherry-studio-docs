---
icon: cloud-check
---
# Configurações do Serviço de Modelos


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Esta página apresenta apenas as funcionalidades da interface. Para tutoriais de configuração, consulte o guia [Configuração de Provedores](../../../pre-basic/providers/) nos tutoriais básicos.

{% hint style="info" %}
* Ao usar provedores integrados, basta preencher a chave correspondente.
* Provedores diferentes podem usar terminologias distintas para chaves: chave secreta, Key, API Key e token referem-se ao mesmo conceito.
{% endhint %}

### Chave Secreta de API

No Cherry Studio, um único provedor suporta múltiplas chaves em uso rotativo, seguindo uma sequência linear da primeira à última.

* Adicione múltiplas chaves separadas por vírgulas em inglês. Por exemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
É **obrigatório** usar vírgulas em inglês.
{% endhint %}

### Endereço da API

Ao usar provedores integrados, geralmente não é necessário preencher o endereço da API. Se precisar modificar, siga estritamente o endereço fornecido na documentação oficial.

> Se o provedor fornecer um endereço no formato <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, preencha **apenas** a parte raiz (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> O Cherry Studio concatenará automaticamente o caminho restante (<mark style="background-color:green;">/v1/chat/completions</mark>). Preenchimentos incorretos podem causar falhas no serviço.

{% hint style="info" %}
Observação: A maioria dos provedores usa rotas padronizadas para modelos de linguagem grandes, tornando esta configuração opcional. Caso o caminho da API seja v2, v3/chat/completions ou outra versão, insira manualmente a versão terminando com "`/`". Se a rota não for <mark style="background-color:green;">/v1/chat/completions</mark>, use o endereço completo fornecido pelo provedor terminando com `#`.

Resumindo:
* Endereços terminando em `/` concatenam automaticamente "<mark style="background-color:green;">chat/completions</mark>"
* Endereços terminando em `#` usam apenas o endereço fornecido, sem concatenação.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Adicionar Modelos

Clique no botão `Gerenciar` no canto inferior esquerdo da página de configuração para obter automaticamente todos os modelos suportados pelo provedor. Clique em `+` ao lado de cada modelo para adicioná-lo à lista.

{% hint style="info" %}
Os modelos na janela pop-up não são adicionados automaticamente. É necessário clicar em `+` ao lado de cada modelo para que apareçam na lista de seleção.
{% endhint %}

### Verificação de Conectividade

Clique no botão `Verificar` ao lado do campo de chave de API para testar a configuração.

{% hint style="info" %}
A verificação usa por padrão o último modelo de conversa adicionado à lista. Se falhar, verifique se há modelos incorretos ou não suportados na lista.
{% endhint %}

{% hint style="danger" %}
Após a configuração bem-sucedida, **ative o interruptor no canto superior direito**. Caso contrário, o provedor permanecerá desativado e seus modelos não serão listados.
{% endhint %}