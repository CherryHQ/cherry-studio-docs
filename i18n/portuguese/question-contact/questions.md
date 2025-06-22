---
icon: seal-question
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Perguntas Frequentes

## Códigos de Erro Comuns

* **4xx (Códigos de status de erro do cliente)**: Geralmente indicam erros de sintaxe na solicitação, falha de autenticação ou problemas que impedem o processamento da requisição.
* **5xx (Códigos de status de erro do servidor)**: Geralmente indicam problemas no lado do servidor, como servidor indisponível, tempo limite de processamento, etc.

| Código de Erro          | Possíveis Causas                                                   | Soluções                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <h4>400</h4> | Formato incorreto do corpo da solicitação, entre outros                                   | <p>Verifique o conteúdo do erro na resposta da conversa ou no <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a> para ver detalhes do erro e siga as instruções.</p><p><mark style="color:purple;">[Caso comum 1]</mark>: Para modelos Gemini, pode ser necessário vincular um cartão;<br><mark style="color:purple;">[Caso comum 2]</mark>: Dados excedem o limite de tamanho, comum em modelos visuais. Imagens maiores que o limite superior retornam este erro;<br><mark style="color:purple;">[Caso comum 3]</mark>: Parâmetros não suportados ou incorretos. Teste com um novo assistente limpo;<br><mark style="color:purple;">[Caso comum 4]</mark>: Contexto excede o limite. Limpe o histórico ou inicie uma nova conversa.</p> |
| <h4>401</h4> | Autenticação falhou: modelo não suportado ou conta suspensa no servidor                      | Entre em contato com o provedor de serviços ou verifique o status da conta                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>403</h4> | Sem permissão para a operação solicitada                                                 | Execute ações conforme o erro na resposta da conversa ou informações do [console](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                   |
| <h4>404</h4> | Recurso não encontrado                                                                 | Verifique o caminho da solicitação                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>422</h4> | Sintaxe correta, mas erro semântico                                                     | Erros processáveis mas não executáveis. Comum em erros de semântica JSON (ex: valor nulo; esperado string, mas número/booleano fornecido).                                                                                                                                                                                                                                                                                                    |
| <h4>429</h4> | Limite de taxa de solicitação excedido                                                  | Taxa (TPM/RPM) atingiu o limite máximo. Aguarde antes de tentar novamente                                                                                                                                                                                                                                                                                                                                                                |
| <h4>500</h4> | Erro interno do servidor, solicitação não processada                                      | Contate o provedor se persistir                                                                                                                                                                                                                                                                                                                                                                                                     |
| <h4>501</h4> | Funcionalidade não implementada pelo servidor                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>502</h4> | Resposta inválida recebida de servidor remoto pelo gateway/proxy                         |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>503</h4> | Serviço indisponível (sobrecarga/manutenção). O cabeçalho Retry-After indica tempo de espera. |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <h4>504</h4> | Gateway/proxy não obteve resposta do servidor remoto a tempo                            |                                                                                                                                                                                                                                                                                                                                                                                                                                 |

***

## Como Verificar Erros no Console

* Clique na janela do cliente Cherry Studio e pressione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- A janela ativa deve ser a do cliente Cherry Studio para abrir o console;
- Abra o console ANTES de testar ou iniciar solicitações para coletar informações.
{% endhint %}

* Na janela do console: Clique em <mark style="color:blue;">`Network`</mark> → Selecione a última entrada com <mark style="color:red;">`×`</mark> vermelho em ② (<mark style="color:red;">`completions`</mark> para diálogo/tradução/erros de modelo ou <mark style="color:red;">`generations`</mark> para pintura) → Clique em <mark style="color:blue;">`Response`</mark> para ver o conteúdo completo (área ④).

> Se não conseguir identificar o erro, envie um print desta tela para o [Grupo oficial](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método funciona para diálogos, testes de modelo, criação de bases de conhecimento, pintura, etc. Sempre abra o console ANTES de realizar a operação.

{% hint style="info" %}
Nomes diferentes em "Name" (área ②):

Diálogo/Tradução/Verificação: <mark style="color:red;">`completions`</mark>  
Pintura: <mark style="color:red;">`generations`</mark>  
Criação de Base: <mark style="color:red;">`embeddings`</mark>  
{% endhint %}

***

## Fórmula Não Renderizada/Erro na Renderização

* Fórmulas exibidas como código? Verifique delimitadores:

> **Uso de Delimitadores**
>
> _Fórmula em linha_
>
> * Cifrão simples: `$fórmula$`
> * Ou `\(fórmula\)`
>
> _Bloco de fórmula_
>
> * Cifrão duplo: `$$fórmula$$`
> * Ou `\[fórmula\]`
> * Exemplo: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Erros de renderização com caracteres chineses? Troque o mecanismo para KateX.

***

## Falha ao Criar Base de Conhecimento/Dimensão de Embedding

1. Modelo indisponível

> Confirme suporte do provedor ou status do serviço.

2. Uso de modelo não compatível com embedding

***

## Modelo Não Reconhece Imagens/Falha no Upload/Seleção

Verifique suporte à visão: modelos compatíveis têm ícone de olho 👁️ após o nome.

Modelos visuais permitem upload de imagens. Se a função não estiver ativada:
- Acesse os modelos do provedor
- Clique no ícone de configuração
- Marque a opção de imagem

Modelos sem suporte visual não processarão imagens, mesmo com a opção ativada. Consulte informações específicas com seu provedor.