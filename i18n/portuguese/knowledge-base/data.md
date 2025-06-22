---
icon: database
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Instruções de Armazenamento de Dados

Os dados adicionados à base de conhecimento do Cherry Studio são armazenados localmente. Durante o processo de adição, uma cópia do documento é colocada no diretório de armazenamento de dados do Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Fluxograma de processamento da base de conhecimento</p></figcaption></figure>

Banco de dados vetorial: [https://turso.tech/libsql](https://turso.tech/libsql)

Após os documentos serem adicionados à base de conhecimento do Cherry Studio, os arquivos são divididos em vários fragmentos. Esses fragmentos são então processados pelo modelo de embedding.

Ao usar o modelo de linguagem grande para Q&A, fragmentos de texto relevantes à pergunta são recuperados e enviados ao modelo de linguagem grande para processamento.

Se houver requisitos de privacidade de dados, recomenda-se usar um banco de dados de embedding local e um modelo de linguagem grande local.