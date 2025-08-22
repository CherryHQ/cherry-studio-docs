---
icon: message
---
# Interface de Conversa


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Assistentes e Tópicos

### Assistente

O `Assistente` refere-se às configurações personalizadas aplicadas ao modelo selecionado para utilização, como predefinições de prompts e parâmetros. Essas configurações permitem que o modelo escolhido opere de forma mais alinhada às suas expectativas de trabalho.

O `Assistente padrão do sistema` vem com parâmetros genéricos pré-definidos (sem prompt). Você pode usá-lo diretamente ou encontrar predefinições necessárias na [página de agentes](agents.md).

### Tópicos

O `Assistente` é o elemento pai dos `Tópicos`. Um único assistente pode conter múltiplos tópicos (conversas), onde todos os `tópicos` compartilham as configurações do modelo definidas no `assistente`, como parâmetros e prompts.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botões na Área de Mensagem

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Novo Tópico` Cria uma nova conversa no assistente atual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Carregar Imagem/Documento` Requer suporte do modelo para imagens. Documentos são analisados como texto para contextualização.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Pesquisa na Web` Exige configuração prévia. Resultados são fornecidos como contexto ao modelo. Detalhes em [Modo Online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de Conhecimento` Ativa a funcionalidade. Veja [Tutorial](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP` Ativa o recurso de servidor. Veja [Tutorial](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Gerar Imagem` Oculto por padrão. Para modelos com suporte (ex: Gemini), ative manualmente para gerar imagens.

{% hint style="info" %}
Devido a limitações técnicas, o botão deve ser ativado manualmente para geração de imagens. Será removido após otimizações.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Selecionar Modelo` Altera o modelo para a conversa atual mantendo o contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases Rápidas` Use frases pré-configuradas com suporte a variáveis.

![](../../.gitbook/assets/对话界面/清空消息.png) `Limpar Mensagens` Exclui todo o conteúdo do tópico.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir` Amplia a área de texto para entradas longas.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpar Contexto` Trunca o contexto visível pelo modelo sem excluir mensagens.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Tokens Estimados` Exibe:  
- `Contexto atual`  
- `Máximo de contexto` (∞ = ilimitado)  
- `Mensagem atual`  
- `Tokens estimados`  

{% hint style="info" %}
Funcionalidade estimativa. Tokens reais variam por modelo. Consulte provedores.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduzir` Traduz o conteúdo atual para inglês.

## Configurações de Conversa

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configurações de Modelo

Sincronizadas com `Configurações de Modelo` do assistente. Detalhes em [Editar Assistente](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Nas configurações de conversa, apenas `Configurações de Modelo` aplicam-se ao assistente atual. Demais configurações são globais.
{% endhint %}

### Configurações de Mensagem

#### <mark style="color:blue;">**`Divisória de Mensagem`**</mark>:
Separa conteúdo de mensagem da barra de ações.

{% tabs %}
{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar Fonte Serifada`**</mark>：
Alterna estilos de fonte. Personalize via [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Números de Linha em Código`**</mark>：
Exibe numeração em blocos de código.

{% tabs %}
{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocos de Código Recolhíveis`**</mark>：
Recolhe automaticamente blocos de código extensos.

#### <mark style="color:blue;">**`Quebra de Linha em Blocos de Código`**</mark>：
Quebra linhas longas que excedam a janela.

#### <mark style="color:blue;">**`Recolher Processos de Raciocínio`**</mark>：
Recolhe automaticamente etapas de pensamento após conclusão.

#### <mark style="color:blue;">**`Estilo de Mensagem`**</mark>：
Alterna entre estilo bolha ou lista.

#### <mark style="color:blue;">**`Estilo de Código`**</mark>：
Altera esquema de cores para trechos de código.

#### <mark style="color:blue;">**`Motor de Fórmulas Matemáticas`**</mark>：
- **KaTeX**: Renderização mais rápida (otimizado).
- **MathJax**: Mais recursos (símbolos/comandos).

#### <mark style="color:blue;">**`Tamanho da Fonte`**</mark>：
Ajusta dimensão do texto nas mensagens.

### Configurações de Entrada

#### <mark style="color:blue;">**`Exibir Tokens Estimados`**</mark>：
Mostra consumo estimado de Tokens na entrada (referência).

#### <mark style="color:blue;">**`Colar Texto Longo como Arquivo`**</mark>：
Converte colagens extensas em formato arquivo para reduzir ruído visual.

#### <mark style="color:blue;">**`Renderizar Markdown na Entrada`**</mark>：
Desative para renderizar apenas respostas do modelo.

{% tabs %}
{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Tradução com 3 Espaços`**</mark>：
Triplo espaço traduz conteúdo para inglês.

{% hint style="warning" %}
Substitui texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma Alvo`**</mark>：
Define idioma para traduções rápidas e botão de tradução.

## Configurações de Assistente

Selecione o assistente → Menu de contexto → Configuração correspondente

### Editar Assistente

{% hint style="info" %}
Configurações aplicam-se a todos os tópicos deste assistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configurações de Prompt

#### <mark style="color:blue;">**`Nome`**</mark>：
Personalize conforme necessidade.

#### <mark style="color:blue;">**`Prompt`**</mark>：
Consulte formatação na página de agentes.

#### Configurações de Modelo

#### <mark style="color:blue;">**`Modelo Padrão`**</mark>：
Define modelo fixo para o assistente. Não configurado = modelo global ([Padrão](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
Modelo padrão do assistente possui prioridade sobre o modelo global.
{% endhint %}

#### <mark style="color:blue;">**`Redefinir Modelo Automaticamente`**</mark>：
Quando ativado, novos tópicos usam o modelo padrão do assistente, não o último modelo utilizado.

> **Exemplo:** Assistente padrão: gpt-3.5-turbo  
> **Com redefinição:** Novo tópico = gpt-3.5-turbo  
> **Sem redefinição:** Novo tópico = último modelo usado (ex: gpt-4o)

#### <mark style="color:blue;">**`Temperatura`**</mark> ：
Controla criatividade (padrão: 0.7):
- **Baixa (0-0.3)**: Precisão (geração de código)  
- **Média (0.4-0.7)**: Equilíbrio ideal (conversas)  
- **Alta (0.8-1.0)**: Máxima criatividade  

#### <mark style="color:blue;">**`Top P (Amostragem Nucleus)`**</mark>：
Padrão: 1. Controla diversidade léxica:
- **Valor baixo (0.1-0.3)**: Saída conservadora  
- **Valor médio (0.4-0.6)**: Balanceamento  
- **Valor alto (0.7-1.0)**: Máxima diversidade  

{% hint style="info" %}
Use esses parâmetros combinados conforme necessidades específicas. Valores indicativos - consulte documentação dos modelos.
{% endhint %}

#### <mark style="color:blue;">**`Janela de Contexto`**</mark>
Número de mensagens retidas no contexto. Valores maiores consomem mais tokens:
- **5-10**: Conversas simples  
- **>10**: Tarefas complexas com contexto longo  

#### <mark style="color:blue;">**`Limitar Comprimento (MaxToken)`**</mark>
Tokens máximos por resposta (ex: configuração básica de teste = 1 token). Limites variam por modelo (consultar documentação).

{% hint style="success" %}
**Sugestões:**  
- Conversas: 500-800  
- Textos curtos: 800-2000  
- Geração de código: 2000-3600  
- Textos longos: 4000+  
{% endhint %}

{% hint style="warning" %}
Respostas podem ser truncadas se excederem MaxToken. Ajuste conforme necessidade.
{% endhint %}

#### <mark style="color:blue;">**`Saída em Fluxo (Stream)`**</mark>
- **Ativado**: Exibição incremental (digitação)  
- **Desativado**: Entrega completa após geração  

{% hint style="info" %}
Desative para modelos sem suporte a stream (ex: o1-mini).
{% endhint %}

#### <mark style="color:blue;">**`Parâmetros Personalizados`**</mark>
Adicione parâmetros específicos ao corpo da requisição (ex: `presence_penalty`). Formato: `nome:tipo:valor` ([referência](https://openai.apifox.cn/doc-3222739)).

{% hint style="info" %}
- Parâmetros personalizados substituem configurações internas  
- Use `<nome>:undefined` para excluir parâmetros  
{% endhint %}