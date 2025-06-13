---
icon: book-bookmark
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

```markdown
# Conhecimento Básico

## O que são tokens?

Tokens são as unidades básicas que os modelos de IA usam para processar texto, podendo ser entendidos como as menores unidades de "pensamento" do modelo. Eles não correspondem exatamente a caracteres ou palavras como entendemos, mas representam uma forma especial de segmentação de texto criada pelo próprio modelo.

#### 1. Segmentação em Chinês
* Um caractere chinês geralmente é codificado como 1-2 tokens
* Exemplo: `"你好"` ≈ 2-4 tokens

#### 2. Segmentação em Inglês
* Palavras comuns geralmente são 1 token
* Palavras longas ou incomuns são divididas em múltiplos tokens
* Exemplo:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Caracteres especiais
* Espaços, pontuação também consomem tokens
* Quebras de linha geralmente contam como 1 token

{% hint style="info" %}
Os Tokenizers variam entre provedores de serviço, e até mesmo entre modelos diferentes do mesmo provedor. Este conhecimento serve apenas para esclarecer o conceito de token.
{% endhint %}

***

## O que é Tokenizer?

Tokenizer (segmentador) é a ferramenta que converte texto em tokens para modelos de IA. Ele define como o texto de entrada é dividido nas menores unidades compreensíveis pelo modelo.

### Por que Tokenizers variam entre modelos?

#### 1. Dados de treinamento diferentes
* Corpora diferentes levam a otimizações distintas
* Suporte variado para multilinguismo
* Otimizações específicas para domínios (médico, jurídico, etc.)

#### 2. Algoritmos de segmentação diferentes
* BPE (Byte Pair Encoding) - usado em GPT da OpenAI
* WordPiece - usado no BERT do Google
* SentencePiece - ideal para cenários multilíngues

#### 3. Objetivos de otimização diferentes
* Alguns focam em eficiência de compressão
* Outros priorizam preservação semântica
* Outros buscam velocidade de processamento

### Impacto prático

O mesmo texto pode ter contagens diferentes de tokens em modelos distintos:

```
Entrada: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## O que são Modelos de Embedding?

**Conceito básico:** Modelos de embedding são técnicas que convertem dados discretos de alta dimensão (texto, imagens, etc.) em vetores contínuos de baixa dimensão, permitindo que máquinas compreendam e processem dados complexos. Imagine simplificar um quebra-cabeça complexo em um ponto coordenado que mantém características essenciais. No ecossistema de grandes modelos, eles atuam como "tradutores", convertendo informações humanas em formas numéricas computáveis.

**Funcionamento:** Em processamento de linguagem natural, modelos de embedding mapeiam palavras para posições específicas no espaço vetorial. Neste espaço:
* Vetores de "rei" e "rainha" ficam próximos
* Termos como "gato" e "cachorro" também se agrupam
* Palavras semanticamente não relacionadas como "carro" e "pão" ficam distantes

**Principais aplicações:**
* Análise de texto: classificação de documentos, análise de sentimentos
* Sistemas de recomendação: conteúdo personalizado
* Processamento de imagens: busca por imagens similares
* Motores de busca: otimização de pesquisa semântica

**Vantagens-chave:**
1. Redução dimensional: simplificação de dados complexos
2. Preservação semântica: manutenção do significado original
3. Eficiência computacional: aceleração no treinamento e inferência de modelos

**Valor técnico:** Modelos de embedding são componentes fundamentais de sistemas modernos de IA, fornecendo representações de dados de alta qualidade para tarefas de aprendizado de máquina e impulsionando avanços em NLP, visão computacional e áreas afins.

***

## Funcionamento de Modelos de Embedding em Recuperação de Conhecimento

**Fluxo básico de trabalho:**

1. **Fase de pré-processamento do conhecimento:**
   * Divisão de documentos em chunks (partes de texto) de tamanho adequado
   * Conversão de cada chunk em vetor usando o modelo de embedding
   * Armazenamento dos vetores e textos originais em banco de dados vetorial

2. **Fase de processamento de consulta:**
   * Conversão da pergunta do usuário em vetor
   * Busca de conteúdos similares no banco vetorial
   * Fornecimento do contexto recuperado ao LLM para resposta

***

## O que é MCP (Model Context Protocol)?

MCP é um protocolo open-source que fornece informações contextuais para grandes modelos de linguagem (LLMs) de maneira padronizada.

* **Analogia:** Pense no MCP como um "pendrive para IA". Assim como pendrives armazenam arquivos que podem ser usados ao conectar-se a computadores, servidores MCP permitem "conectar" diversos "plugins contextuais". LLMs solicitam esses plugins conforme necessário para obter contextos mais ricos e ampliar suas capacidades.
* **Comparação com Function Tools:** Ferramentas tradicionais fornecem funcionalidades externas pontuais, mas o MCP oferece uma abstração de nível superior. Enquanto Function Tools atendem a tarefas específicas, o MCP proporciona um mecanismo modular e universal de obtenção de contexto.

### Principais vantagens do MCP

1. **Padronização:** Interface e formato de dados unificados para colaboração perfeita entre LLMs e provedores de contexto.
2. **Modularidade:** Contexto dividido em módulos (plugins) independentes para fácil gerenciamento e reutilização.
3. **Flexibilidade:** Seleção dinâmica de plugins contextuais conforme demandas do LLM, permitindo interações mais inteligentes e personalizadas.
4. **Escalabilidade:** Projeto aberto para incorporação futura de novos tipos de plugins contextuais, ampliando ilimitadamente as capacidades dos LLMs.
```