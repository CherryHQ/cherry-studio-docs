---
icon: book-bookmark
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Conhecimento Científico Popular

## O que são tokens?

Tokens são as unidades básicas de processamento de texto em modelos de IA, podendo ser entendidos como as menores unidades de "pensamento" do modelo. Eles não correspondem exatamente a caracteres ou palavras como as entendemos, mas sim a um método especial de segmentação de texto usado pelo próprio modelo.

#### 1. Segmentação de Texto em Chinês
* Um caractere chinês geralmente é codificado como 1-2 tokens
* Exemplo: `"你好"` ≈ 2-4 tokens

#### 2. Segmentação de Texto em Inglês
* Palavras comuns geralmente são 1 token
* Palavras longas ou incomuns são divididas em múltiplos tokens
* Exemplo:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Caracteres Especiais
* Espaços, pontuação e outros também ocupam tokens
* Caracteres de nova linha geralmente são 1 token

{% hint style="info" %}
Os Tokenizers variam entre diferentes provedores de serviços, e até mesmo entre diferentes modelos do mesmo provedor. Este conhecimento serve apenas para esclarecer o conceito de token.
{% endhint %}

***

## O que é um Tokenizer?

Tokenizer (segmentador) é a ferramenta que converte texto em tokens para modelos de IA. Ele determina como o texto de entrada é dividido nas menores unidades compreensíveis pelo modelo.

### Por que Tokenizers variam entre modelos?

#### 1. Dados de Treinamento Diferentes
* Corpus linguísticos distintos levam a diferentes otimizações
* Variações no suporte a múltiplos idiomas
* Otimizações especializadas para áreas específicas (saúde, direito, etc.)

#### 2. Algoritmos de Segmentação Diferentes
* BPE (Byte Pair Encoding) - OpenAI GPT series
* WordPiece - Google BERT
* SentencePiece - Ideal para cenários multilíngues

#### 3. Objetivos de Otimização Diferentes
* Alguns focam em eficiência de compressão
* Outros em preservação semântica
* Outros em velocidade de processamento

### Impacto Prático
O mesmo texto pode ter contagens diferentes de tokens em modelos distintos:

```
Entrada: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## O que são Modelos de Incorporação (Embedding Models)?

**Conceito Básico:** Modelos de incorporação são técnicas que convertem dados discretos de alta dimensão (texto, imagens, etc.) em vetores contínuos de baixa dimensão, permitindo que máquinas compreendam e processem melhor informações complexas. Imagine como simplificar um quebra-cabeça complexo em um ponto coordenado que ainda mantém características essenciais. No ecossistema de grandes modelos, atuam como "tradutores" convertendo informações humanas em formas numéricas computáveis.

**Funcionamento:** No processamento de linguagem natural, modelos de incorporação mapeiam palavras para posições específicas em espaços vetoriais. Nesse espaço, palavras semanticamente relacionadas agrupam-se naturalmente. Por exemplo:

* "Rei" e "rainha" terão vetores próximos
* "Gato" e "cachorro" como animais domésticos estarão próximos
* "Carro" e "pão", semanticamente não relacionados, ficarão distantes

**Principais Casos de Uso:**
* Análise de texto: classificação de documentos, análise de sentimentos
* Sistemas de recomendação: sugestão de conteúdo personalizado
* Processamento de imagens: busca por imagens semelhantes
* Motores de busca: otimização de pesquisa semântica

**Vantagens-Chave:**
1. Redução dimensional: simplifica dados complexos para formas vetoriais tratáveis
2. Preservação semântica: mantém informações semânticas cruciais dos dados originais
3. Eficiência computacional: acelera significativamente treinamento e inferência de modelos

**Valor Tecnológico:** Modelos de incorporação são componentes fundamentais de sistemas modernos de IA, fornecendo representações de alta qualidade para tarefas de aprendizado de máquina e são essenciais para avanços em processamento de linguagem natural, visão computacional e áreas afins.

***

## Funcionamento de Modelos Embedding em Recuperação de Conhecimento

**Fluxo de Trabalho Básico:**

1. **Fase de Pré-processamento do Banco de Conhecimento**
* Divisão de documentos em chunks (segmentos de texto) de tamanho apropriado
* Conversão de cada chunk em vetor usando o modelo embedding
* Armazenamento de vetores e texto original em banco de dados vetorial

2. **Fase de Processamento de Consultas**
* Conversão da pergunta do usuário em vetor
* Busca por conteúdo similar no banco vetorial
* Fornecimento do conteúdo recuperado como contexto para o LLM

***

## O que é MCP (Model Context Protocol)?

MCP é um protocolo open-source que fornece informações contextuais a modelos de linguagem (LLM) de forma padronizada.

* **Analogia:** Imagine MCP como um "pen drive" para IA. Assim como pen drives armazenam vários arquivos que ficam acessíveis ao conectar no computador, servidores MCP aceitam "plugins" contextuais diversos. LLMs podem solicitar esses plugins conforme necessário, obtendo informações contextuais ricas para expandir suas capacidades.
* **Comparação com Function Tools:** Ferramentas funcionais tradicionais também ampliam capacidades de LLMs, mas MCP opera em abstração mais elevada. Enquanto Function Tools focam em tarefas específicas, MCP oferece um mecanismo modular e universal de obtenção de contexto.

### Vantagens Essenciais do MCP

1. **Padronização:** Interface e formato de dados unificados permitem colaboração direta entre diferentes LLMs e provedores de contexto.
2. **Modularidade:** Contexto pode ser dividido em módulos (plugins) independentes para fácil gerenciamento e reuso.
3. **Flexibilidade:** LLMs selecionam plugins contextuais dinamicamente conforme necessidades, viabilizando interações mais inteligentes e personalizadas.
4. **Escalabilidade:** Arquitetura do MCP suporta futuras inclusões de tipos contextuais adicionais, oferecendo possibilidades ilimitadas para expansão de capacidades de LLMs.