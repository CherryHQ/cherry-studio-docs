---
icon: message
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Interface de Conversa

## Assistente e Tópico

### Assistente

`Assistente` é uma configuração personalizada do modelo selecionado para utilizá-lo, como predefinições de prompts e parâmetros. Através dessas configurações, o modelo escolhido pode atender melhor às suas expectativas de trabalho.

O `assistente padrão do sistema` fornece parâmetros genéricos (sem prompt) para uso imediato. Você pode utilizá-lo diretamente ou acessar a [página de agentes inteligentes](agents.md) para encontrar predefinições que atendam às suas necessidades.

### Tópico

O `assistente` é o conjunto pai do `tópico`. Um único assistente pode criar múltiplos tópicos (ou seja, conversas). Todos os `tópicos` compartilham as configurações do modelo do assistente, incluindo parâmetros e prompts.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botões na Área de Conversa

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Novo Tópico` Cria um novo tópico dentro do assistente atual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Upload de Imagem ou Documento` Requer suporte do modelo para imagens. Documentos são automaticamente analisados como texto para contexto.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Busca na Web` Exige configuração prévia. Os resultados são fornecidos como contexto para o modelo. Detalhes em [Modo Online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de Conhecimento` Ativa a base de conhecimento. Tutorial completo em [Tutorial da Base de Conhecimento](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP` Ativa a funcionalidade do servidor MCP. Detalhes em [Tutorial de Uso do MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Gerar Imagem` Não exibido por padrão. Para modelos compatíveis (ex: Gemini), deve ser ativado manualmente.

{% hint style="info" %}
Por limitações técnicas, você deve ativar este botão manualmente para gerar imagens. Ele será removido após otimizações.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Selecionar Modelo` Altera o modelo para conversas subsequentes mantendo o contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases Rápidas` Requer configuração prévia de frases para inserção rápida, suportando variáveis.

![](../../.gitbook/assets/对话界面/清空消息.png) `Limpar Mensagens` Exclui todo o conteúdo do tópico atual.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir` Amplia a área de entrada para textos longos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpar Contexto` Restringe o contexto disponível ao modelo sem apagar conteúdo, efetivamente "esquecendo" conversas anteriores.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimativa de Tokens` Mostra: `contexto atual`, `contexto máximo` (∞ = ilimitado), `caracteres na entrada` e `tokens estimados`.

{% hint style="info" %}
Esta estimativa é referencial. Tokens reais variam por modelo; consulte o fornecedor.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduzir` Converte o conteúdo da entrada para inglês.

## Configurações de Conversa

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configuração do Modelo

Sincronizado com os parâmetros do assistente. Detalhes em [Configurar Assistente](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Apenas esta configuração afeta o assistente atual. Outras configurações são globais (ex: estilo de mensagem).
{% endhint %}

### Configuração de Mensagens

#### <mark style="color:blue;">**`Separador de Mensagens`**</mark>:

Insere linha divisória entre conteúdo e ações.

{% tabs %}
{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar Fonte Serifada`**</mark>：

Altera estilo de fonte. Personalize via [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Mostrar Números de Linha em Código`**</mark>：

Exibe numeração em blocos de código gerados pelo modelo.

{% tabs %}
{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocos de Código Colapsáveis`**</mark>：

Colapsa automaticamente blocos de código extensos.

#### <mark style="color:blue;">**`Quebra de Linha em Código`**</mark>：

Ativa quebra de linha automática para códigos que excedem a janela.

#### <mark style="color:blue;">**`Colapsar Processo de Pensamento`**</mark>：

Colapsa automaticamente etapas de raciocínio em modelos compatíveis.

#### <mark style="color:blue;">**`Estilo de Mensagem`**</mark>：

Alterna entre estilo "balão" ou "lista".

#### <mark style="color:blue;">**`Estilo de Código`**</mark>：

Altera tema de destaque de sintaxe para blocos de código.

#### <mark style="color:blue;">**`Mecanismo de Fórmulas Matemáticas`**</mark>：

* **KaTeX**: Renderização rápida, otimizada para desempenho.
* **MathJax**: Renderização lenta, suporte amplo a símbolos e comandos.

#### <mark style="color:blue;">**`Tamanho da Fonte em Mensagens`**</mark>：

Ajusta tamanho do texto na interface.

### Configuração de Entrada

#### <mark style="color:blue;">**`Mostrar Estimativa de Tokens`**</mark>：

Exibe tokens estimados para texto de entrada (referência, não contexto real).

#### <mark style="color:blue;">**`Colar Texto Longo como Arquivo`**</mark>：

Textos longos colados são exibidos como arquivos para reduzir interferências.

#### <mark style="color:blue;">**`Renderizar Markdown em Entradas`**</mark>：

Quando desativado, renderiza apenas respostas do modelo.

{% tabs %}
{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traduzir com 3 Espaços Rápidos`**</mark>：

Pressione espaço três vezes para traduzir entrada para inglês.

{% hint style="warning" %}
Atenção: Substitui o texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma Alvo`**</mark>：

Define idioma para botão de tradução e atalho de 3 espaços.

## Configuração do Assistente

Selecione o <mark style="background-color:yellow;">nome do assistente</mark> → <mark style="background-color:yellow;">menu contextual</mark> → configurações

### Editar Assistente

{% hint style="info" %}
A configuração aplica-se a todos os tópicos deste assistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configuração de Prompt

#### <mark style="color:blue;">**`Nome`**</mark>：

Personalize para fácil identificação.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Consulte agentes inteligentes para exemplos de escrita.

#### Configuração do Modelo

#### <mark style="color:blue;">**`Modelo Padrão`**</mark>：

Define modelo fixo para este assistente. Sobrescreve o modelo global se configurado.

{% hint style="info" %}
Hierarquia: 
1. Modelo padrão do assistente 
2. [Modelo de conversa global](settings/default-models.md#mo-ren-zhu-shou-mo-xing)
{% endhint %}

#### <mark style="color:blue;">**`Redefinir Modelo Automaticamente`**</mark>：

Quando ativado, novos tópicos usam o modelo padrão do assistente. Quando desativado, herdam o modelo do último tópico.

> **Exemplo**:  
> Assistente padrão: gpt-3.5-turbo  
> Tópico1: Alterado para gpt-4o  
> Com redefinição: Tópico2 usa gpt-3.5-turbo  
> Sem redefinição: Tópico2 usa gpt-4o

#### <mark style="color:blue;">**`Temperatura`**</mark> ：

Controla criatividade (padrão=0.7):
* **Baixa (0-0.3)**: Saída precisa (código/dados)
* **Média (0.4-0.7)**: Equilíbrio (conversas/diálogos)
* **Alta (0.8-1.0)**: Criativa (brainstorm/redação)

#### <mark style="color:blue;">**`Top P (Amostragem Nucleus)`**</mark>：

Padrão=1:
* **Valores baixos (0.1-0.3)**: Vocabulário conservador
* **Médios (0.4-0.6)**: Equilíbrio diversidade-precisão
* **Altos (0.7-1.0)**: Saída diversificada

{% hint style="info" %}
- Use parâmetros isolados ou combinados
- Valores sugeridos são referenciais (consulte documentação do modelo)
{% endhint %}

#### <mark style="color:blue;">**`Janela de Contexto`**</mark>

Quantidade de mensagens retidas (maior=mais tokens):
* 5-10: Conversas simples
* \>10: Tarefas complexas

#### <mark style="color:blue;">**`Ativar Limite de Tokens`**</mark>

Tokens máximos por resposta. Limites variam por modelo (ex: 32k, 64k).

{% hint style="success" %}
**Sugestões**:
* Conversas: 500-800
* Texto curto: 800-2000
* Código: 2000-3600
* Texto longo: 4000+ (requer suporte)
{% endhint %}

{% hint style="warning" %}
Respostas podem ser truncadas se excederem o limite. Ajuste conforme necessidade.
{% endhint %}

#### <mark style="color:blue;">**`Saída em Fluxo Contínuo`**</mark>

Saída imediata (efeito máquina de escrever) vs. saída completa após geração.

{% hint style="info" %}
Desative para modelos incompatíveis (ex: o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Parâmetros Personalizados`**</mark>

Adicione parâmetros específicos ao corpo da requisição (ex: `presence_penalty`). Referência: [Documentação](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
- Parâmetros personalizados têm prioridade sobre padrões
- Use `nome:undefined` para excluir parâmetros
- Consulte documentação do fornecedor para parâmetros exclusivos
{% endhint %}