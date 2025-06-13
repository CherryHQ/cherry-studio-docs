---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Modo de Conexão à Internet

{% hint style="info" %}
Exemplos de cenários que requerem conexão à internet:

* Informações com validade temporal: como o preço do ouro hoje/esta semana/agora.
* Dados em tempo real: como clima, taxas de câmbio e outros valores dinâmicos.
* Conhecimentos emergentes: como novos fenômenos, conceitos inovadores, tecnologias recentes, etc.
{% endhint %}

### 1. Como ativar a conexão à internet

Na janela de perguntas do Cherry Studio, clique no ícone 【🌐】 para ativar a conexão à internet.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Clique no ícone do globo - ativar conexão de rede</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Indica - função de conexão à internet ativada</p></figcaption></figure>

### 2. Atenção especial: dois modos de conexão

#### Modo 1: Modelos com função nativa de conexão

Nesse caso, após ativar a conexão, você pode usar o serviço diretamente, de forma simples.

{% hint style="warning" %}
Verifique acima da área de perguntas se há um ícone de 🌐 após o nome do modelo para identificar rapidamente se ele suporta conexão.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Na página de gerenciamento de modelos, este método também permite identificar rapidamente quais modelos suportam conexão.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Fornecedores atualmente suportados pelo Cherry Studio:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (todos os modelos)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian, etc.</mark>

{% hint style="danger" %}
Atenção especial:
Há casos excepcionais onde mesmo sem o ícone 🌐, o modelo pode conectar-se, conforme explicado no tutorial abaixo.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Modo 2: Utilização do serviço Tavily para conexão

Ao usar modelos sem função nativa de conexão (sem ícone 🌐) que necessitem processar informações em tempo real, utilize o serviço Tavily.

**Primeiro uso do Tavily:** um pop-up solicitará configurações. Siga as instruções - é simples!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Pop-up, clique: Configurar</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Clique para obter chave</p></figcaption></figure>

Após clicar, você será redirecionado para o site do **Tavily**. Registre-se, faça login, crie uma API key e copie-a para o Cherry Studio.

{% hint style="danger" %}
Dúvidas no registro? Consulte o tutorial Tavily neste diretório.
{% endhint %}

**Documento de referência para registro Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Esta interface indica registro bem-sucedido:

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Copiar chave</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Cole a chave - pronto!</p></figcaption></figure>

Teste novamente: resultados mostram busca normal com padrão de 5 resultados.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Atenção: Tavily tem limite mensal gratuito. Excedido? Requer pagamento.
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Encontrou erros? Entre em contato conosco a qualquer momento.