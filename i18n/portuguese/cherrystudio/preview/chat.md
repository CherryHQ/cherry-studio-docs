---
icon: message
---
# Interface de Conversa


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Assistentes e Tópicos

### Assistentes

`Assistente` é para configurar personalizações no modelo selecionado, como predefinições de prompts e parâmetros, permitindo que o modelo atenda melhor às suas expectativas de trabalho.

`Assistente Padrão do Sistema` possui parâmetros genéricos pré-definidos (sem prompts), você pode usá-lo diretamente ou acessar a [página de Agentes](agents.md) para encontrar as predefinições necessárias.

### Tópicos

`Assistente` é o conjunto pai de `Tópicos`, onde é possível criar múltiplos tópicos (ou seja, conversas) sob um único assistente. Todos os `Tópicos` compartilham as configurações de parâmetros e prompts do `Assistente`.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botões dentro da Caixa de Diálogo

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Novo Tópico` Cria um novo tópico sob o assistente atual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Enviar imagem ou documento` O envio de imagens requer suporte do modelo; documentos enviados são automaticamente convertidos em texto e fornecidos como contexto ao modelo.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Pesquisa na Web` Requer configuração prévia nas configurações; os resultados da pesquisa são retornados como contexto ao modelo, consulte [Modo Online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de Conhecimento` Ativa a base de conhecimento, consulte [Tutorial da Base de Conhecimento](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP` Ativa a funcionalidade do Servidor MCP, consulte [Tutorial de Uso do MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Gerar Imagem` Exibido apenas quando o **modelo de conversa** selecionado suporta geração de imagens. (Para modelos não conversacionais, acesse [Desenho](./drawing.md))

![](../../.gitbook/assets/对话界面/选择模型.png) `Selecionar Modelo` Alterna para o modelo especificado na próxima conversa, mantendo o contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases Rápidas` Requer pré-configuração de frases comuns nas configurações; ao serem acionadas, inserem texto diretamente com suporte a variáveis.

![](../../.gitbook/assets/对话界面/清空消息.png) `Limpar Mensagens` Exclui todo o conteúdo deste tópico.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir` Amplia a caixa de diálogo para facilitar a inserção de textos longos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpar Contexto` Trunca o contexto acessível ao modelo sem excluir o conteúdo, fazendo com que o modelo "esqueça" as conversas anteriores.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimativa de tokens` Mostra a estimativa de tokens. Os quatro valores representam: `Contagem atual de contexto`, `Contagem máxima de contexto` (∞ indica contexto ilimitado), `Contagem de caracteres na caixa de entrada atual`, `Estimativa de tokens`.

{% hint style="info" %}
Esta função serve apenas para estimar tokens; o número real varia conforme o modelo. Consulte os dados fornecidos pelo provedor do modelo.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traduzir` Traduz o conteúdo atual da caixa de entrada para inglês.

## Configurações de Conversa

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configurações do Modelo

As configurações do modelo sincronizam-se com os parâmetros de `Configurações do Modelo` nas configurações do assistente, consulte [Configurações do Assistente](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
Nas configurações de conversa, apenas esta configuração do modelo aplica-se ao assistente atual, enquanto as demais são globais. Exemplo: após definir o estilo de mensagem como balão, ele será aplicado em qualquer tópico de qualquer assistente.
{% endhint %}

### Configurações de Mensagem

#### <mark style="color:blue;">**`Linha de Separação de Mensagens`**</mark>:

Utiliza uma linha de separação para dividir o corpo da mensagem da barra de operações.

{% tabs %}
{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar Fonte Serifada`**</mark>：

Alterna entre estilos de fonte; você também pode alterar a fonte através de [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Exibir Números de Linha no Código`**</mark>：

Exibe números de linha nos blocos de código gerados pelo modelo.

{% tabs %}
{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Blocos de Código Dobráveis`**</mark>：

Ativado, blocos de código longos serão automaticamente dobrados.

#### <mark style="color:blue;">**`Quebra de Linha em Código`**</mark>：

Ativado, linhas longas de código (que excedam a janela) quebrarão automaticamente.

#### <mark style="color:blue;">**`Dobrar Conteúdo de Raciocínio Automaticamente`**</mark>：

Ativado, modelos com suporte a raciocínio irão dobrar automaticamente o processo de raciocínio após concluí-lo.

#### <mark style="color:blue;">**`Estilo da Mensagem`**</mark>：

Alterna entre estilo de balão ou lista na interface de conversa.

#### <mark style="color:blue;">**`Estilo do Código`**</mark>：

Altera o estilo visual dos blocos de código.

#### <mark style="color:blue;">**`Renderizador de Fórmulas Matemáticas`**</mark>：

* KaTeX tem velocidade de renderização mais rápida, pois foi otimizado especificamente para desempenho;
* MathJax é mais lento, mas oferece recursos mais completos e suporta mais símbolos e comandos matemáticos.

#### <mark style="color:blue;">**`Tamanho da Fonte das Mensagens`**</mark>：

Ajusta o tamanho da fonte na interface de conversa.

### Configurações de Entrada

#### <mark style="color:blue;">**`Exibir Estimativa de Tokens`**</mark>：

Exibe na caixa de entrada a quantidade estimada de tokens consumidos pelo texto inserido (não representa tokens reais do contexto, apenas referência).

#### <mark style="color:blue;">**`Colar Texto Longo como Arquivo`**</mark>：

Ao colar textos longos copiados de outros lugares, eles são exibidos como arquivos para reduzir interferência na digitação subsequente.

#### <mark style="color:blue;">**`Renderizar Markdown nas Mensagens Enviadas`**</mark>：

Desativado, apenas as respostas do modelo são renderizadas em Markdown; mensagens enviadas não são renderizadas.

{% tabs %}
{% tab title="Desativado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Ativado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traduzir com 3 Espaços Rápidos`**</mark>：

Após inserir uma mensagem na caixa de diálogo, pressione a barra de espaço três vezes rapidamente para traduzir o conteúdo para inglês.

{% hint style="warning" %}
Aviso: esta ação substituirá o texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma de Destino`**</mark>：

Define o idioma de destino para o botão de tradução e para a função de três espaços.

## Configurações do Assistente

Na interface do assistente, selecione o nome do <mark style="background-color:yellow;">assistente</mark> desejado → selecione a configuração correspondente no <mark style="background-color:yellow;">menu de contexto</mark>

### Editar Assistente

{% hint style="info" %}
As configurações do assistente aplicam-se a todos os tópicos sob este assistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configurações de Prompt

#### <mark style="color:blue;">**`Nome`**</mark>：

Define um nome personalizado para identificação do assistente.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Corresponde ao prompt, que pode ser editado seguindo os exemplos na página de Agentes.

#### Configurações do Modelo

#### <mark style="color:blue;">**`Modelo Padrão`**</mark>：

Define um modelo fixo para este assistente. Ao adicionar pela página de Agentes ou copiar o assistente, o modelo inicial será este. Sem esta configuração, o modelo inicial será o modelo padrão global (consulte [Modelo Padrão do Assistente](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
Existem dois modelos padrão para o assistente: um é o [Modelo Padrão Global de Conversa](settings/default-models.md#mo-ren-zhu-shou-mo-xing), outro é o modelo padrão do assistente. O modelo padrão do assistente tem prioridade maior que o modelo padrão global. Quando não definido, o modelo padrão do assistente é igual ao modelo padrão global.
{% endhint %}

#### <mark style="color:blue;">**`Redefinir Modelo Automaticamente`**</mark>：

Ativado - ao criar um novo tópico após alterar o modelo durante uma conversa, o novo tópico redefinirá para o modelo padrão do assistente. Desativado, o novo tópico manterá o modelo usado no tópico anterior.

> Exemplo: se o modelo padrão do assistente for gpt-3.5-turbo, e durante o tópico 1 eu alterar para gpt-4o:
>
> Com redefinição automática ativada: ao criar o tópico 2, o modelo padrão será gpt-3.5-turbo;
>
> Com redefinição automática desativada: ao criar o tópico 2, o modelo padrão será gpt-4o.

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark> ：

Controla o grau de aleatoriedade e criatividade na geração de texto (valor padrão: 0,7). Manifesta-se como:

* Valores baixos (0-0,3):
  * Saída mais determinada e focada
  * Adequado para geração de código, análise de dados
  * Tende a selecionar palavras mais prováveis
* Valores médios (0,4-0,7):
  * Equilíbrio entre criatividade e coerência
  * Adequado para diálogos cotidianos e escrita geral
  * Recomendado para chatbots (em torno de 0,5)
* Valores altos (0,8-1,0):
  * Gera saídas mais criativas e diversificadas
  * Adequado para escrita criativa e brainstorming
  * Pode reduzir a coerência textual

#### <mark style="color:blue;">**`Top P (Amostragem Núcleo)`**</mark>：

Valor padrão 1. Valores menores tornam a saída mais repetitiva e previsível; valores maiores aumentam a diversidade lexical.

A amostragem núcleo controla o limiar de probabilidade das palavras:

* Valores baixos (0,1-0,3):
  * Considera apenas palavras de maior probabilidade
  * Saída mais conservadora e controlada
  * Adequado para comentários de código e documentação técnica
* Valores médios (0,4-0,6):
  * Equilíbrio entre diversidade e precisão
  * Adequado para diálogos e tarefas gerais de escrita
* Valores altos (0,7-1,0):
  * Considera um leque mais amplo de palavras
  * Gera conteúdo mais rico e diversificado
  * Adequado para escrita criativa que exige expressão variada

{% hint style="info" %}
- Esses parâmetros podem ser usados individualmente ou combinados
- Escolha valores adequados conforme o tipo de tarefa
- Recomenda-se experimentar para encontrar a combinação ideal
- Os valores sugeridos são orientativos; consulte a documentação específica de cada modelo
{% endhint %}

#### <mark style="color:blue;">**`Quantidade de Contexto (Context Window)`**</mark>

Quantidade de mensagens mantidas no contexto. Valores maiores consomem mais tokens:

* 5-10: adequado para diálogos comuns
* >10: necessário para tarefas complexas que exigem memória estendida (ex.: gerar textos longos seguindo um esboço, garantindo coerência lógica)
* > Observação: mais mensagens consomem mais tokens

#### <mark style="color:blue;">**`Ativar Limite de Comprimento de Mensagem (MaxToken)`**</mark>

Número máximo de [tokens](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) por resposta. Em modelos de linguagem, max token é um parâmetro crucial que afeta diretamente qualidade e comprimento das respostas.

> Exemplo: ao testar a conectividade do modelo no CherryStudio após inserir a chave, basta verificar se há resposta válida sem conteúdo específico; neste caso, defina MaxToken como 1.

A maioria dos modelos tem limite máximo de 32k tokens, embora existam modelos com 64k ou mais; verifique a documentação específica.

O valor adequado depende das necessidades específicas, mas segue-se esta orientação:

{% hint style="success" %}
Recomendações:

* Conversas comuns: 500-800
* Geração de textos curtos: 800-2000
* Geração de código: 2000-3600
* Geração de textos longos: 4000 ou mais (requer suporte do modelo)
{% endhint %}

{% hint style="warning" %}
Normalmente as respostas do modelo são limitadas pelo MaxToken, porém podem ocorrer cortes (ex.: em códigos longos) ou respostas incompletas. Em casos especiais, ajustes manuais podem ser necessários.
{% endhint %}

#### <mark style="color:blue;">**`Saída em Fluxo (Stream)`**</mark>

Saída em fluxo permite transmitir dados continuamente em vez de enviar tudo de uma vez, melhorando tempo real e eficiência.

No CherryStudio, isso corresponde ao efeito "máquina de escrever".

Desativado (não fluxo): o modelo envia toda a resposta de uma só vez após concluí-la (semelhante ao WhatsApp);

Ativado: exibe caractere por caractere à medida que o modelo gera.

{% hint style="info" %}
Para modelos que não suportam saída em fluxo (ex.: **inicialmente** o1-mini), desative este recurso.
{% endhint %}

#### <mark style="color:blue;">**`Parâmetros Personalizados`**</mark>

Adiciona parâmetros extras ao corpo da requisição, como campos `presence_penalty`, normalmente desnecessários para usuários comuns.

> Os parâmetros mencionados acima (top-p, maxtokens, stream etc.) são exemplos destes parâmetros.

Formato: nome do parâmetro—tipo (texto, número etc.)—valor. Consulte: [Documentação](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Cada provedor possui parâmetros exclusivos; consulte sua documentação específica
{% endhint %}

{% hint style="info" %}
* Parâmetros personalizados têm prioridade sobre parâmetros internos. Se houver conflito, o parâmetro personalizado substitui o interno.

> Exemplo: ao definir `model` como `gpt-4o` nos parâmetros personalizados, o modelo gpt-4o será usado independentemente da seleção feita durante a conversa.

* Use <kbd>nome_do_parâmetro:undefined</kbd> para excluir um parâmetro.
{% endhint %}