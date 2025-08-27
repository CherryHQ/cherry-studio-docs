---
icon: message
---
# Interface de Conversação


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Assistentes e Tópicos

### Assistentes

Um `assistente` é uma configuração personalizada para usar um modelo específico, como predefinições de prompt e parâmetros, permitindo que o modelo atenda melhor às suas expectativas de trabalho.

O `assistente padrão do sistema` vem com parâmetros universais (sem prompts). Você pode usá-lo diretamente ou encontrar predefinições no [página de agentes](agents.md).

### Tópicos

O `assistente` é o conjunto pai dos `tópicos`. Um único assistente pode criar múltiplos tópicos (diálogos), onde todos os `tópicos` compartilham as configurações do modelo do assistente, como parâmetros e prompts.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botões na Caixa de Diálogo

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Novo Tópico`: Cria um novo tópico no assistente atual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Carregar Imagem/Documento`: Exige suporte do modelo para imagens; documentos são automaticamente analisados como contexto.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Busca na Web`: Requer configuração prévia; resultados são enviados como contexto ao modelo. Detalhes em [Modo Online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de Conhecimento`: Ativa recursos de conhecimento. Veja [Tutorial de Base de Conhecimento](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP`: Ativa funcionalidades do servidor MCP. Tutorial em [Guia MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Gerar Imagem`: Oculto por padrão. Para modelos com suporte (ex: Gemini), acione manualmente.

{% hint style="info" %}
Devido a limitações técnicas, você deve ativar manualmente este botão. Será removido em atualizações futuras.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Selecionar Modelo`: Altera o modelo para o diálogo seguinte, mantendo o contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases Rápidas`: Use frases predefinidas nas configurações. Suporta variáveis.

![](../../.gitbook/assets/对话界面/清空消息.png) `Limpar Mensagens`: Exclui todo o conteúdo do tópico.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir`: Amplia a caixa de diálogo para textos longos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpar Contexto`: "Esquece" diálogos anteriores sem apagar mensagens.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Tokens Estimados`: Exibe `contexto atual`, `máximo de contexto` (∞ = ilimitado), `caracteres na caixa de entrada`, `tokens estimados`.

{% hint style="info" %}
Esta estimativa é referencial. Tokens reais variam por modelo—consulte o fornecedor.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduzir`: Traduz o conteúdo da caixa de entrada para inglês.

## Configurações de Diálogo

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configurações do Modelo

Sincronizadas com o assistente. Veja [Editar Assistente](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Apenas as configurações de modelo afetam o assistente atual. Outras configurações são globais (ex: estilo de mensagem).
{% endhint %}

### Configurações de Mensagem

#### <mark style="color:blue;">**`Divisor de Mensagens`**</mark>:
Adiciona linha divisória entre conteúdo e ações.

{% tabs %}
{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar Fonte Serifada`**</mark>：
Alterna estilo de fonte. Personalize via [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Mostrar Números de Linha em Códigos`**</mark>：
Exibe numeração em blocos de código.

{% tabs %}
{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocos de Código Dobráveis`**</mark>：
Dobra automaticamente blocos de código longos.

#### <mark style="color:blue;">**`Quebra de Linha em Códigos`**</mark>：
Quebra linhas longas de código que excedam a janela.

#### <mark style="color:blue;">**`Dobrar Conteúdo de Pensamento`**</mark>：
Dobra automaticamente o processo de raciocínio de modelos compatíveis.

#### <mark style="color:blue;">**`Estilo de Mensagem`**</mark>：
Alterna entre estilo de bolhas ou lista.

#### <mark style="color:blue;">**`Estilo de Código`**</mark>：
Altera tema de realce de sintaxe.

#### <mark style="color:blue;">**`Renderizador de Fórmulas`**</mark>：
* **KaTeX**: Mais rápido, otimizado para desempenho;
* **MathJax**: Mais lento, suporta símbolos avançados.

#### <mark style="color:blue;">**`Tamanho da Fonte`**</mark>：
Ajusta tamanho do texto no diálogo.

### Configurações de Entrada

#### <mark style="color:blue;">**`Mostrar Tokens Estimados`**</mark>：
Exibe tokens estimados para texto inserido (referencial).

#### <mark style="color:blue;">**`Colar Texto Longo como Arquivo`**</mark>：
Exibe textos colados longos como arquivos, reduzindo interferências.

#### <mark style="color:blue;">**`Renderizar Markdown em Entrada`**</mark>：
Desativado: Renderiza apenas respostas do modelo; Ativado: Renderiza também mensagens enviadas.

{% tabs %}
{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traduzir com Três Espaços`**</mark>：
Traduz o texto para inglês ao pressionar espaço três vezes.

{% hint style="warning" %}
Isso substitui o texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma Alvo`**</mark>：
Define idioma para traduções (botão ou três espaços).

## Configurações do Assistente

Selecione o <mark style="background-color:yellow;">nome do assistente</mark> → Menu de clique direito → Configurações

### Editar Assistente

{% hint style="info" %}
As configurações afetam todos os tópicos do assistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configurações de Prompt

#### <mark style="color:blue;">**`Nome`**</mark>：
Personalize um nome identificável.

#### <mark style="color:blue;">**`Prompt`**</mark>：
Personalize o prompt usando exemplos da página de agentes.

### Configurações do Modelo

#### <mark style="color:blue;">**`Modelo Padrão`**</mark>：
Define um modelo fixo para o assistente. Se não definido, usa o [modelo padrão global](settings/default-models.md#mo-ren-zhu-shou-mo-xing).

{% hint style="info" %}
Modelos padrão do assistente têm prioridade sobre o global.
{% endhint %}

#### <mark style="color:blue;">**`Redefinir Modelo Automaticamente`**</mark>：
Ativado: Novos tópicos usam o modelo padrão do assistente; Desativado: Usam o último modelo do tópico anterior.

> Exemplo: Assistente padrão: GPT-3.5. Se alternar para GPT-4 no Tópico 1:
> - **Redefinir ativado**: Tópico 2 usa GPT-3.5;
> - **Redefinir desativado**: Tópico 2 usa GPT-4.

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark>：
Controla criatividade das respostas (padrão=0.7):
* **Baixa (0-0.3)**: Saída previsível (ex: código);
* **Média (0.4-0.7)**: Equilíbrio (ex: conversas);
* **Alta (0.8-1.0)**: Criativa (ex: escrita).

#### <mark style="color:blue;">**`Top P (Amostragem Nuclear)`**</mark>：
Padrão=1. Valores menores: respostas conservadoras; maiores: diversificadas.
* **0.1-0.3**: Vocabulário restrito (ex: documentação);
* **0.4-0.6**: Equilíbrio;
* **0.7-1.0**: Amplo (ex: criação).

{% hint style="info" %}
- Use os parâmetros de forma combinada;
- Experimente valores conforme sua necessidade;
- Faixas sugeridas podem variar por modelo.
{% endhint %}

#### <mark style="color:blue;">**`Janela de Contexto`**</mark>
Número de mensagens retidas (maior valor = mais tokens):
* **5-10**: Diálogos simples;
* **>10**: Tarefas complexas (ex: escrita longa);
* ⚠️ Mensagens extras aumentam consumo.

#### <mark style="color:blue;">**`Limitar Comprimento de Resposta (MaxToken)`**</mark>
Limite de [tokens](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) por resposta. Afeta qualidade e extensão.

> Exemplo: Para testar conectividade, defina MaxToken=1.

Alguns modelos suportam até 32k/64k tokens (verifique especificações).

{% hint style="success" %}
Sugestões:
* Conversas: 500-800 tokens;
* Textos curtos: 800-2000;
* Código: 2000-3600;
* Textos longos: >4000 (requer suporte do modelo).
{% endhint %}

{% hint style="warning" %}
Respostas podem ser truncadas (ex: código longo). Ajuste conforme necessário.
{% endhint %}

#### <mark style="color:blue;">**`Saída em Fluxo (Stream)`**</mark>
Exibe respostas gradualmente (efeito máquina de escrever). Desativado: exibe toda a resposta de uma vez.

{% hint style="info" %}
Desative para modelos sem suporte a stream (ex: o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Parâmetros Personalizados`**</mark>
Adicione parâmetros extras (ex: `presence_penalty`). Referência: [Documentação](https://openai.apifox.cn/doc-3222739).

> Exemplos: `top-p`, `maxtokens`.

{% hint style="info" %}
- Parâmetros personalizados sobrescrevem os internos;
- Use `<kbd>nome:undefined</kbd>` para ignorar parâmetros.
{% endhint %}