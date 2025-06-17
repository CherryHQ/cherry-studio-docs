---
icon: database
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Explicação sobre Armazenamento de Dados

Os dados adicionados ao repositório de conhecimento do Cherry Studio são inteiramente armazenados localmente. Durante o processo de adição, uma cópia do documento será colocada no diretório de armazenamento de dados do Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Fluxograma de processamento do repositório de conhecimento</p></figcaption></figure>

Banco de dados vetoriais: [https://turso.tech/libsql](https://turso.tech/libsql)

Após adicionar um documento ao repositório de conhecimento do Cherry Studio, o arquivo será dividido em vários fragmentos. Esses fragmentos serão então processados pelo modelo de incorporação (embedding model).

Ao utilizar modelos de linguagem grandes (large models) para perguntas e respostas, os fragmentos de texto relevantes para a pergunta serão consultados e enviados junto ao modelo de linguagem grande para processamento.

Se houver requisitos de privacidade de dados, recomenda-se utilizar um banco de dados de incorporação local e um modelo de linguagem grande local.