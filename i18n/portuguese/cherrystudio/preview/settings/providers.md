---
icon: cloud-check
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configurações do Provedor

Esta página explica apenas as funcionalidades da interface. Para tutoriais de configuração, consulte o guia [Configuração de Provedores](../../../pre-basic/providers/) na seção básica.

{% hint style="info" %}
* Ao usar provedores integrados, basta preencher a chave correspondente.
* Diferentes provedores podem usar termos diferentes para a chave: segredo, Key, API Key, token, etc., todos se referem à mesma coisa.
{% endhint %}

### Chave da API

No Cherry Studio, um único provedor suporta múltiplas chaves de rotação. O método de rotação é sequencial, da primeira à última chave na lista.

* Adicione múltiplas chaves separadas por vírgulas em inglês. Exemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Você **deve** usar vírgulas em inglês.
{% endhint %}

### Endereço da API

Geralmente não é necessário preencher o endereço da API ao usar provedores integrados. Se precisar modificar, preencha estritamente conforme o endereço fornecido na documentação oficial.

> Se o provedor fornecer um endereço no formato <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, informe apenas o endereço base (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> O Cherry Studio adicionará automaticamente o caminho restante (<mark style="background-color:green;">/v1/chat/completions</mark>). O preenchimento incorreto pode impedir o funcionamento adequado.

{% hint style="info" %}
Observação: A maioria dos provedores usa rotas padronizadas para modelos de linguagem grandes, geralmente sem necessidade de ajustes. Se o caminho da API do provedor for v2, v3/chat/completions ou outra versão, insira manualmente a versão correspondente terminando com "`/`". Quando a rota de solicitação do provedor não for a padrão <mark style="background-color:green;">/v1/chat/completions</mark>, use o endereço completo fornecido terminando com `#`.

Ou seja:
* Endereços API terminados com `/` acionam concatenação automática de "<mark style="background-color:green;">chat/completions</mark>"
* Endereços API terminados com `#` não sofrem concatenação.

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Adicionar Modelos

Clique no botão `Gerenciar` no canto inferior esquerdo da página de configuração do provedor para obter automaticamente todos os modelos suportados. Clique no `+` ao lado do modelo para adicioná-lo à lista.

{% hint style="info" %}
Os modelos na janela pop-up não são adicionados automaticamente. Você deve clicar no `+` ao lado do modelo para que ele apareça na lista de seleção de modelos.
{% endhint %}

### Verificação de Conectividade

Clique no botão de verificação ao lado do campo de chave da API para testar a configuração.

{% hint style="info" %}
O teste usa por padrão o último modelo de diálogo adicionado. Se falhar, verifique se há modelos incorretos ou não suportados na lista.
{% endhint %}

{% hint style="danger" %}
Após configurar com sucesso, **ative sempre** o interruptor no canto superior direito. Caso contrário, o provedor permanecerá desativado e seus modelos não aparecerão na lista.
{% endhint %}