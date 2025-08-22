---
icon: seal-question
---
# Perguntas Frequentes


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




## Códigos de Erro Comuns

* **4xx (Códigos de status de erro do cliente)**: Geralmente ocorrem devido a erros de sintaxe de solicitação, falha de autenticação ou problemas de autorização que impedem o processamento da solicitação.
* **5xx (Códigos de status de erro do servidor)**: Normalmente indicam erros do lado do servidor, como servidor inativo, tempo limite de processamento, etc.

| Código de Erro | Possíveis Cenários                                                    | Solução                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **400**       | Formato incorreto do corpo da solicitação, etc.                         | <p>Verifique o conteúdo de erro retornado ou consulte o<a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a> para ver detalhes do erro e siga as orientações.</p><p><mark style="color:purple;">[Caso comum 1]</mark>: Modelos Gemini podem exigir vinculação de cartão;<br><mark style="color:purple;">[Caso comum 2]</mark>: Dados excedem limites de tamanho (common em modelos visuais);<br><mark style="color:purple;">[Caso comum 3]</mark>: Parâmetros não suportados ou configurados incorretamente;<br><mark style="color:purple;">[Caso comum 4]</mark>: Limite de contexto excedido.</p> |
| **401**       | Falha na autenticação: modelo não suportado ou conta suspensa, etc.                | Verifique o estado da conta com o provedor de serviços                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **403**       | Sem permissão para realizar operação                                    | Aja conforme as informações de erro no console                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **404**       | Recurso solicitado não encontrado                                     | Verifique o caminho de solicitação                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **422**       | Formato correto, mas erro semântico                                   | Erros semânticos JSON (valores vazios, tipo incorreto, etc.)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **429**       | Limite de taxa de solicitação atingido                               | Aguarde e tente novamente depois                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **500**       | Erro interno do servidor                                              | Contate o provedor de serviços se persistir                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **501**       | Funcionalidade não suportada pelo servidor                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **502**       | Resposta inválida de servidor remoto                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **503**       | Servidor sobrecarregado/inoperante (consulte cabeçalho Retry-After)     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **504**       | Tempo limite de gateway/proxy                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

***

## Como Verificar Erros no Console

* Pressione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (macOS: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>) com a janela do Cherry Studio ativa

{% hint style="info" %}
- Janela do Cherry Studio deve estar em foco
- Abra o console antes de iniciar operações para capturar informações
{% endhint %}

* No console: Clique em <mark style="color:blue;">`Network`</mark> → Busque por <mark style="color:red;">`completions`</mark> (diálogos/tradução) ou <mark style="color:red;">`generations`</mark> (arte) com ícone de erro (✗) → Verifique <mark style="color:blue;">`Response`</mark>

> Se não conseguir identificar o erro, compartilhe screenshot no [grupo oficial](https://t.me/CherryStudioAI)

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método funciona para diálogos, verificação de modelos, vetorização e arte. Sempre inicie o console antes da operação.

{% hint style="info" %}
Nomeação varia conforme cenário:
- Diálogo/tradução: <mark style="color:red;">`completions`</mark>
- Arte: <mark style="color:red;">`generations`</mark>
- Vetorização: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Fórmulas Não Renderizadas/Com Erro

* Se fórmulas aparecerem como código: verifique delimitadores
> **Delimitadores**:  
> - *Inline*: `$fórmula$` ou `\(fórmula\)`  
> - *Bloco*: `$$fórmula$$` ou `\[fórmula\]`
* Erros de renderização com caracteres chineses: altere mecanismo para KateX

***

## Falha na Criação de Base de Conhecimento

1. Modelo indisponível  
   > Verifique compatibilidade e status no provedor
2. Uso de modelo não embedding

***

## Modelos Não Reconhecem Imagens

* Verifique ícone de "olho" 🔍 no nome do modelo
* Modelos visuais habilitam upload de imagem
* Em modelos não visuais, ativar imagem é inútil
* Consulte informações específicas no provedor do modelo