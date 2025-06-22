---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Modo de Rede

{% hint style="info" %}
Exemplos de cenários que requerem conexão à internet:

* Informações temporais: como preços de futuros de ouro hoje/esta semana/recentemente, etc.
* Dados em tempo real: como clima, taxas de câmbio e outros valores dinâmicos.
* Conhecimentos emergentes: como novas coisas, novos conceitos, novas tecnologias etc.
{% endhint %}

### 1. Como ativar a conexão à internet

Na janela de perguntas do Cherry Studio, clique no ícone 【Globo Terrestre】 para ativar a conexão à internet.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Clique no ícone do globo - Ativar conexão à internet</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Indica - A função de conexão à internet foi ativada</p></figcaption></figure>

### 2. Atenção especial: Dois modos de conexão à internet

#### Modo 1: A capacidade de conexão nativa dos grandes modelos dos provedores

Nesse caso, após ativar a conexão, você pode usar diretamente o serviço online, o que é muito simples.

{% hint style="warning" %}
Você pode verificar rapidamente se o modelo suporta conexão à internet observando se há um ícone de mapa pequeno ao lado do nome do modelo na parte superior da interface de perguntas e respostas.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Na página de gerenciamento de modelos, este método também permite identificar rapidamente quais modelos suportam conexão à internet.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Provedores de modelos com suporte de conexão atualmente no Cherry Studio:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (todos os modelos suportam conexão)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian, etc.</mark>

{% hint style="danger" %}
Atenção especial:
Existe uma situação excepcional em que o modelo pode realizar conexão mesmo sem o ícone do globo, como explicado no tutorial abaixo.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Modo 2: Usar o serviço Tavily para habilitar conexão em modelos não nativos

Quando usamos grandes modelos sem capacidade de conexão nativa (sem ícone de globo) e precisamos acessar informações em tempo real, utilizamos o serviço de pesquisa na web do Tavily.

**No primeiro uso do Tavily**, uma janela pop-up solicitará configurações. Siga as instruções - é muito simples!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Janela pop-up, clique: Ir para Configurações</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Clique para obter a chave secreta</p></figcaption></figure>

Após clicar, você será redirecionado para a página de **login/registro do site oficial do Tavily**. Após registrar e fazer login, crie uma API key e cole-a no Cherry Studio.

{% hint style="danger" %}
Se precisar de ajuda com o registro, consulte o tutorial de registro Tavily neste mesmo diretório.
{% endhint %}

**Documento de referência para registro no Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

A interface abaixo indica que o registro foi bem-sucedido.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Copiar a chave</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Cole a chave - pronto!</p></figcaption></figure>

Teste novamente para ver o efeito. O resultado mostra que a pesquisa online está funcionando, com o número padrão de resultados definido como 5.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Nota: O Tavily tem limites gratuitos mensais; o uso excedente requer pagamento.
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Se encontrar erros, sinta-se à vontade para entrar em contato a qualquer momento.