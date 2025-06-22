---
icon: cloud-check
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configurações do Provedor

Esta página apenas apresenta as funcionalidades da interface. Para tutoriais de configuração, consulte o tutorial de [Configuração do Provedor](../../../pre-basic/providers/) no guia básico.

{% hint style="info" %}
* Ao usar provedores internos, basta preencher a chave correspondente.
* Diferentes provedores podem usar termos distintos para chave (chave, Key, API Key, token) que se referem ao mesmo conceito.
{% endhint %}

### Chave da API

No Cherry Studio, um único provedor suporta múltiplas chaves em rodízio sequencial.

* Adicione múltiplas chaves separadas por vírgulas inglesas:
<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Sempre use vírgulas **em inglês**.
{% endhint %}

### Endereço da API

Geralmente não é necessário preencher ao usar provedores internos. Se precisar modificar, siga estritamente o endereço da documentação oficial.

> Se o provedor fornecer um endereço como <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, insira apenas a parte base (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
> 
> O Cherry Studio completará automaticamente o caminho (<mark style="background-color:green;">/v1/chat/completions</mark>). Formato incorreto pode causar falhas.

{% hint style="info" %}
Observação: A maioria dos provedores usa rotas padronizadas. Caso o caminho seja atípico (ex: v2, v3):  
- Termine com `/` para concatenar apenas "`chat/completions`"  
- Termine com `#` para usar o endereço completo sem concatenação.  

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Adicionar Modelos

Clique em `Gerenciar` (canto inferior esquerdo) para ver os modelos suportados. Clique no `+` ao lado de cada modelo para adicioná-lo à lista.

{% hint style="info" %}
Modelos na janela pop-up não são adicionados automaticamente. É necessário clicar em `+` para que apareçam na lista de seleção.
{% endhint %}

### Verificação de Conectividade

Clique no botão de verificação ao lado do campo da chave para testar a configuração.

{% hint style="info" %}
Por padrão, usa o último modelo de diálogo da lista. Falhas podem indicar modelos incorretos ou não suportados.
{% endhint %}

{% hint style="danger" %}
Ative o interruptor no canto superior direito após configurar, caso contrário o provedor permanecerá inativo.
{% endhint %}