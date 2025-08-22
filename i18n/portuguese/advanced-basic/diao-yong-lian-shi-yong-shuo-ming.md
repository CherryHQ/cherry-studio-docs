---
icon: route
---
# Instruções de Uso da Cadeia de Chamadas (Trace)


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Funcionalidade

A Cadeia de Chamadas (também conhecida como "trace") oferece insights sobre diálogos, ajudando usuários a identificar o desempenho de modelos, bases de conhecimento, MCP, buscas na web e outros componentes durante conversas. É uma ferramenta de observabilidade implementada com base no [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), que coleta, armazena e processa dados do lado do cliente para visualização, fornecendo métricas quantitativas para localizar problemas e otimizar resultados.

Cada diálogo corresponde a um conjunto de dados trace. Um trace consiste em múltiplos spans, onde cada span representa uma lógica de processamento do Cherry Studio, como chamadas de sessão de modelo, invocações de MCP, consultas a bases de conhecimento ou buscas na web. O trace é exibido em estrutura de árvore, com spans como nós, apresentando dados principais como tempo de execução e consumo de tokens. Detalhes de entradas/saídas podem ser inspecionados nas informações do span.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Ativar Trace

Por padrão, o Trace fica oculto após a instalação do Cherry Studio. Ative-o em **Configurações → Configurações Gerais → Modo Desenvolvedor**, conforme ilustrado:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Diálogos anteriores não geram registros de Trace. Novos registros são criados apenas após novas interações e armazenados localmente. Para limpar completamente os Traces:
- Acesse **Configurações → Configurações de Dados → Diretório de Dados → Limpar Cache**
- Ou exclua manualmente os arquivos em `~/.cherrystudio/trace`, como mostrado:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Cenários de Uso

### Visualização Completa da Cadeia
Clique no ícone de Trace no diálogo para ver todos os dados da cadeia. Todas as chamadas — modelos, buscas na web, bases de conhecimento ou MCP — são exibidas na janela de Trace.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Inspecionar Modelos na Cadeia
Clique no nó de chamada de modelo para ver detalhes de entrada/saída.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Analisar Buscas na Web
Clique no nó de busca na web para ver consultas e resultados retornados.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Verificar Bases de Conhecimento
Clique no nó de base de conhecimento para inspecionar perguntas e respostas retornadas.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Monitorar Chamadas MCP
Clique no nó MCP para visualizar parâmetros de entrada e retornos das ferramentas do servidor.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Problemas e Sugestões

Esta funcionalidade é desenvolvida pela equipe [EDAS](https://www.aliyun.com/product/edas) da Alibaba Cloud. Para problemas ou sugestões, entre no grupo DingTalk (**ID: 21958624**) para comunicação direta com os desenvolvedores.

\