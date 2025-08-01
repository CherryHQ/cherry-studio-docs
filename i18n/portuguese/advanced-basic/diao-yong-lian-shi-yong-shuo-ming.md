---
icon: route
---
# Instruções de Uso da Cadeia de Chamadas


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Funcionalidade

A Cadeia de Chamadas (também conhecida como "trace") oferece aos usuários capacidade de insights sobre diálogos, ajudando a observar o desempenho específico de modelos, bases de conhecimento, MCP, buscas na web durante conversas. É uma ferramenta de observabilidade implementada com base no [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), que realiza visualização através da coleta, armazenamento e processamento de dados no lado do cliente, fornecendo base quantitativa para localização de problemas e otimização de resultados.

Cada diálogo corresponde a um dado de trace, onde um trace consiste em múltiplos spans. Cada span corresponde a uma lógica de processamento do Cherry Studio, como chamada de sessão de modelo, invocação de MCP, consulta à base de conhecimento ou busca na web. O trace é exibido em estrutura de árvore, com spans como nós, contendo dados principais como tempo gasto e consumo de tokens. Detalhes de entrada/saída podem ser visualizados nas informações do span.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Ativar Trace

Por padrão, após a instalação do Cherry Studio, o Trace permanece oculto. Ative-o em "Configurações" > "Configurações Gerais" > "Modo Desenvolvedor", conforme ilustrado:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Diálogos anteriores não geram registros de Trace. Os registros são gerados apenas em novas interações de perguntas e respostas. Os dados são armazenados localmente. Para limpeza completa do Trace:
1. Acesse: "Configurações" > "Configurações de Dados" > "Diretório de Dados" > "Limpar Cache"
2. Ou exclua manualmente os arquivos em `~/.cherrystudio/trace`, conforme mostrado:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Cenários de Uso

### Visualização Completa da Cadeia
Clique em "Cadeia de Chamadas" no diálogo do Cherry Studio para ver todos os dados da cadeia. Todas as chamadas - modelos, buscas na web, bases de conhecimento ou MCP - são exibidas na janela de trace.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Detalhes de Modelos na Cadeia
Para ver detalhes de modelos na cadeia, clique no nó de chamada do modelo e visualize entradas/saídas específicas.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Detalhes de Busca na Web
Clique no nó de busca na web para ver consultas realizadas e resultados retornados.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Detalhes de Base de Conhecimento
Clique no nó de base de conhecimento para visualizar a pergunta consultada e resposta retornada.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Detalhes de Chamadas MCP
Clique no nó MCP para ver parâmetros de entrada e retornos da ferramenta do servidor MCP.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Problemas e Sugestões

Esta funcionalidade é fornecida pela equipe [EDAS](https://www.aliyun.com/product/edas) da Alibaba Cloud. Para problemas ou sugestões, entre no grupo DingTalk (ID: 21958624) para comunicação direta com os desenvolvedores.