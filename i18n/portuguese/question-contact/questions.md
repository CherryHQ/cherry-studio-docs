---
icon: seal-question
---
# Perguntas Frequentes


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Códigos de Erro Comuns

* **4xx (Códigos de status de erro do cliente)**: Geralmente indicam erros de sintaxe na solicitação, falha de autenticação ou falha de autorização que impedem a conclusão da solicitação.
* **5xx (Códigos de status de erro do servidor)**: Geralmente indicam erros do lado do servidor, como servidor inoperante ou tempo limite no processamento da solicitação.

| Código de Erro | Possíveis Cenários                                                   | Solução                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **400** | Corpo da solicitação malformado, etc.                         | <p>Verifique o conteúdo de erro retornado na conversa ou <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">consulte o console</a> para ver o erro e siga as instruções.<br><mark style="color:purple;">[Caso comum 1]</mark>: Para modelos Gemini, pode ser necessário vincular um cartão;<br><mark style="color:purple;">[Caso comum 2]</mark>: Dados excedem o limite, comum em modelos visuais quando imagens ultrapassam o limite de tamanho por solicitação;<br><mark style="color:purple;">[Caso comum 3]</mark>: Parâmetros não suportados ou incorretos - teste com um novo assistente;<br><mark style="color:purple;">[Caso comum 4]</mark>: Contexto excedeu o limite - limpe o histórico ou reduza o número de mensagens.</p> |
| **401** | Falha na autentração: modelo não suportado ou conta do provedor suspensa       | Verifique o status da conta com o provedor                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **403** | Sem permissão para a operação solicitada                             | Aja conforme as informações de erro no console ou na resposta                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **404** | Recurso solicitado não encontrado                                   | Verifique o caminho da solicitação, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **422** | Sintaxe correta, mas erro semântico                                 | Erro de interpretação (ex.: valor nulo onde string é exigida, ou tipo de dado incorreto)                                                                                                                                                                                                                                                                                                                                                                                                                |
| **429** | Limite de taxa de solicitação atingido                              | Taxa de solicitação (TPM/RPM) excedida - aguarde antes de tentar novamente                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **500** | Erro interno do servidor                                           | Contate o provedor se persistir                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **501** | Funcionalidade não implementada no servidor                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **502** | Resposta inválida recebida de servidor remoto (servidor proxy/gateway)     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **503** | Servidor sobrecarregado ou em manutenção (ver cabeçalho Retry-After)      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **504** | Tempo limite de gateway/proxy ao acessar servidor remoto                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

***

## Como Verificar Erros no Console

* Com a janela do cliente Cherry Studio ativa, pressione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- A janela ativa deve ser do Cherry Studio para abrir o console;
- Abra o console antes de iniciar testes/diálogos para coletar informações.
{% endhint %}

* No console: Clique em <mark style="color:blue;">`Network`</mark> → Selecione a última entrada com <mark style="color:red;">`×`</mark> vermelho (<mark style="color:red;">`completions`</mark> para diálogos/tradução ou <mark style="color:red;">`generations`</mark> para arte) → Clique em <mark style="color:blue;">`Response`</mark> para ver detalhes.

> Em caso de dúvidas, compartilhe um print no [grupo oficial](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método aplica-se a diálogos, testes de modelos, adição de bases de conhecimento e geração de arte. Sempre abra o console antes da operação.

{% hint style="info" %}
Nomes variam por cenário:
Diálogos/tradução: <mark style="color:red;">`completions`</mark><br>
Arte: <mark style="color:red;">`generations`</mark><br>
Bases de conhecimento: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Fórmulas Não Renderizadas/Erros na Renderização

* Se fórmulas exibem código fonte, verifique delimitadores:

> **Uso de Delimitadores**
>
> _Fórmulas em linha_
>
> * Cifrão único: `$formula$`
> * ou `\(formula\)`
>
> _Blocos de fórmula_
>
> * Cifrão duplo: `$$formula$$`
> * ou `\[formula\]`
> * Exemplo: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Erros com caracteres chineses: altere o mecanismo de renderização para KateX.

***

## Falha ao Criar Base de Conhecimento/Erro na Dimensão de Embedding

1. Modelo indisponível

> Confira suporte e status do modelo com o provedor.

2. Uso de modelo não compatível com embeddings

***

## Modelo Não Reconhece Imagens/Falha no Upload

* Modelos compatíveis têm ícone de olho 🔍 após o nome.
* Caso incorreto: no painel do provedor, edite o modelo e marque "Suporte a imagem".
* Modelos sem capacidade visual não funcionarão mesmo com a opção ativada.