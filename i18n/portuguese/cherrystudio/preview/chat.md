---
icon: message
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Interface de Conversa

## Assistentes e Tópicos

### Assistentes

`Assistentes` são configurações personalizadas aplicadas a modelos selecionados, como predefinições de prompts e parâmetros. Essas configurações fazem com que o modelo atenda melhor às suas expectativas de trabalho.

`Assistente padrão do sistema` oferece parâmetros genéricos pré-configurados (sem prompts). Você pode usá-lo diretamente ou acessar a [página de Agentes](agents.md) para encontrar predefinições necessárias.

### Tópicos

`Assistentes` são o conjunto pai de `tópicos`. Um único assistente pode conter vários tópicos (conversas). Todos os `tópicos` compartilham as configurações do modelo do `assistente`, como parâmetros e prompts.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botões da Área de Mensagem

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Novo Tópico`: Cria um novo tópico no assistente atual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Enviar Imagem/Documento`: Imagens requerem suporte do modelo. Documentos serão analisados como texto para contexto.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Pesquisa na Web`: Configure informações de pesquisa nas configurações. Resultados são fornecidos como contexto ao modelo (veja [Modo Online](../../websearch/)).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de Conhecimento`: Ativa a integração com base de conhecimento (veja [Tutorial](../../knowledge-base/knowledge-base.md)).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP`: Ativa recursos do servidor MCP (veja [Tutorial](../../advanced-basic/mcp/)).

![](../../.gitbook/assets/对话界面/生成图片.png) `Gerar Imagem`: Oculto por padrão. Para modelos como Gemini, acione manualmente para gerar imagens.

{% hint style="info" %}
Devido a limitações técnicas, acione manualmente o botão para gerar imagens (será removido após otimização).
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Selecionar Modelo`: Altera o modelo para conversas subsequentes, mantendo o contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases Rápidas`: Pré-configure frases frequentes nas configurações para acesso rápido (suporta variáveis).

![](../../.gitbook/assets/对话界面/清空消息.png) `Limpar Mensagens`: Exclui todo o conteúdo do tópico.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir`: Amplia a área de mensagem para textos longos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpar Contexto`: Remove o contexto das mensagens anteriores sem excluir conteúdo ("esquece" conversas passadas).

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Tokens Estimados`: Mostra `contexto atual`, `contexto máximo` (∞ = ilimitado), `palavras na mensagem` e `tokens estimados`.

{% hint style="info" %}
Estimativa apenas. Tokens reais variam por modelo (consulte o provedor).
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduzir`: Traduz o conteúdo da caixa de entrada para inglês.

## Configurações de Conversa

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configurações do Modelo

Sincronizadas com `Configurações do Modelo` do assistente (veja [Configurar Assistente](chat.md#editar-assistente)).

{% hint style="info" %}
Nas configurações de conversa, apenas `Configurações do Modelo` afeta o assistente atual. Demais configurações são globais (ex.: estilo de bolhas aplica-se a todos os tópicos).
{% endhint %}

### Configurações de Mensagem

#### <mark style="color:blue;">**`Linha Divisória`**</mark>:

Separa o corpo da mensagem da barra de ações.

{% tabs %}
{% tab title="Ativo" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Inativo" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Fonte Serifada`**</mark>：

Alterna estilos de fonte (personalize com [CSS](../../personalization-settings/)).

#### <mark style="color:blue;">**`Mostrar Números de Linha`**</mark>：

Exibe números em blocos de código gerados pelo modelo.

{% tabs %}
{% tab title="Inativo" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativo" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Dobrar Blocos de Código`**</mark>：

Dobra automaticamente blocos de código extensos.

#### <mark style="color:blue;">**`Quebrar Linhas em Código`**</mark>：

Permite quebra automática de linhas longas em blocos de código.

#### <mark style="color:blue;">**`Dobrar Processo de Raciocínio`**</mark>：

Dobra automaticamente etapas de raciocínio de modelos compatíveis.

#### <mark style="color:blue;">**`Estilo de Mensagem`**</mark>：

Alterna entre estilo de bolhas ou lista.

#### <mark style="color:blue;">**`Estilo de Código`**</mark>：

Altera o estilo visual de blocos de código.

#### <mark style="color:blue;">**`Motor de Fórmulas`**</mark>：

* KaTeX: Renderização mais rápida (otimizado para performance);
* MathJax: Mais recursos (suporte a símbolos/comandos avançados), porém mais lento.

#### <mark style="color:blue;">**`Tamanho da Fonte`**</mark>：

Ajusta o tamanho da fonte na interface.

### Configurações de Entrada

#### <mark style="color:blue;">**`Mostrar Tokens Estimados`**</mark>：

Exibe estimativa de tokens para texto digitado (não inclui contexto; apenas referência).

#### <mark style="color:blue;">**`Colar Texto Longo como Arquivo`**</mark>：

Textos longos colados na caixa de entrada são exibidos como arquivos para reduzir interferência.

#### <mark style="color:blue;">**`Renderizar Markdown em Mensagens`**</mark>：

Quando inativo, apenas mensagens de resposta são renderizadas.

{% tabs %}
{% tab title="Inativo" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativo" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traduzir com Três Espaços`**</mark>：

Traduz conteúdo da caixa de entrada para inglês após três espaços consecutivos.

{% hint style="warning" %}
Isso sobrescreve o texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma de Destino`**</mark>：

Define o idioma alvo para traduções (botão e atalho de espaços).

## Configurações do Assistente

Selecione o <mark style="background-color:yellow;">nome do assistente</mark> → <mark style="background-color:yellow;">Menu de contexto</mark> → Configurações

### Editar Assistente

{% hint style="info" %}
As configurações afetam todos os tópicos do assistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configurações de Prompt

#### <mark style="color:blue;">**`Nome`**</mark>：

Nome personalizado para identificação.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Edite conforme exemplos na página de Agentes.

#### Configurações do Modelo

#### <mark style="color:blue;">**`Modelo Padrão`**</mark>：

Define um modelo padrão para o assistente (sobrescreve o [modelo padrão global](settings/default-models.md#modelo-padrão-do-assistente)).

{% hint style="info" %}
Prioridade: Modelo do assistente > Modelo global.
{% endhint %}

#### <mark style="color:blue;">**`Redefinir Modelo Automaticamente`**</mark>：

Ativo: Novos tópicos usam o modelo padrão do assistente.  
Inativo: Novos tópicos herdam o modelo do tópico anterior.

> Exemplo:  
> Modelo padrão: gpt-3.5-turbo.  
> No Tópico 1, você muda para gpt-4o.  
> Ativo → Tópico 2 usa gpt-3.5-turbo.  
> Inativo → Tópico 2 usa gpt-4o.

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark> ：

Controla criatividade (padrão=0.7):

* Baixa (0-0.3): Precisão (ex.: código, dados);
* Média (0.4-0.7): Equilíbrio (ex.: conversas);
* Alta (0.8-1.0): Máxima criatividade (ex.: textos criativos).

#### <mark style="color:blue;">**`Top P (Amostragem Nuclear)`**</mark>：

Padrão=1. Controla diversidade léxica:

* Baixo (0.1-0.3): Vocabulário conservador (ex.: documentação técnica);
* Médio (0.4-0.6): Equilíbrio;
* Alto (0.7-1.0): Máxima diversidade (ex.: criação de conteúdo).

{% hint style="info" %}
- Parâmetros usáveis separada ou conjuntamente  
- Ajuste conforme a tarefa  
- Valores são referenciais; consulte documentação do modelo.
{% endhint %}

#### <mark style="color:blue;">**`Janela de Contexto`**</mark>

Número de mensagens retidas (mais mensagens = mais tokens):

* 5-10: Conversas simples  
* >10: Tarefas complexas  
* > Nota: Mensagens extras consomem mais tokens

#### <mark style="color:blue;">**`Limitar Tamanho (MaxToken)`**</mark>

Máximo de [Tokens](https://docs.cherry-ai.com/question-contact/knowledge#o-que-são-tokens) por resposta. Afeta qualidade/comprimento.

> Exemplo: Para testar conectividade, defina MaxToken=1.

Limites variam por modelo (ex.: 32k/64k tokens).

Sugestões:  
- Conversas: 500-800  
- Textos curtos: 800-2000  
- Código: 2000-3600  
- Textos longos: 4000+ (requer suporte do modelo)

{% hint style="warning" %}
Respostas podem ser truncadas (ex.: código longo). Ajuste conforme necessidade.
{% endhint %}

#### <mark style="color:blue;">**`Saída em Fluxo (Stream)`**</mark>

Transmite respostas incrementalmente (efeito "máquina de escrever").  
Inativo → Respostas completas enviadas de uma vez.

{% hint style="info" %}
Desative para modelos incompatíveis (ex.: o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Parâmetros Customizados`**</mark>

Adicione parâmetros extras (ex.: `presence_penalty`). Uso avançado.

> Exemplos de parâmetros padrão: top-p, maxtokens, stream.  
> Referência: [Documentação](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
- Parâmetros customizados têm prioridade sobre padrões  
  > Ex.: `model: gpt-4o` sobrescreve seleções.  
- Use `<kbd>nome_parametro:undefined</kbd>` para excluir parâmetros.  
- Consulte documentação de provedores para parâmetros exclusivos.
{% endhint %}