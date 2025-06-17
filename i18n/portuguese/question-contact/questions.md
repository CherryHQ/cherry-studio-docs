---
icon: seal-question
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Perguntas Frequentes

## Códigos de Erro Comuns

*   **4xx (Códigos de status de erro do cliente)**: Geralmente indicam erros de sintaxe na solicitação, falha de autenticação ou autorização que impedem a conclusão da solicitação.
*   **5xx (Códigos de status de erro do servidor)**: Geralmente indicam erros do lado do servidor, como servidor inativo, tempo limite no processamento da solicitação, etc.

| Código de erro         | Possíveis cenários                                                   | Solução                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :---------------------- | :-------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4>           | Erro de formato do corpo da solicitação, etc.                           | <p>Verifique o conteúdo de erro retornado na conversa ou consulte o <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a> para ver o conteúdo do erro e siga as instruções.</p><p><mark style="color:purple;">[Caso comum 1]</mark>: Se for um modelo Gemini, pode ser necessário vincular um cartão;<br><mark style="color:purple;">[Caso comum 2]</mark>: Volume de dados excedido, comum em modelos visuais quando o tamanho da imagem excede o limite superior de tráfego por solicitação;<br><mark style="color:purple;">[Caso comum 3]</mark>: Parâmetros não suportados ou preenchidos incorretamente. Tente criar um novo assistente limpo para testar;<br><mark style="color:purple;">[Caso comum 4]</mark>: Contexto excede o limite - limpe o contexto, inicie uma nova conversa ou reduza o número de mensagens de contexto.</p> |
| <h4>401</h4>           | Falha de autenticação: modelo não suportado ou conta do servidor suspensa, etc. | Entre em contato ou verifique o status da conta do provedor de serviço correspondente                                                                                                                                                                                                                                                                                                                                                                       |
| <h4>403</h4>           | Operação solicitada sem permissão                                    | Execute a ação apropriada com base nas informações de erro retornadas na conversa ou no <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">console</a>                                                                                                                                                                                                                                                                                         |
| <h4>404</h4>           | Recurso solicitado não encontrado                                    | Verifique o caminho da solicitação, etc.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>422</h4>           | Formato de solicitação correto, mas erro semântico                    | Erros que o servidor consegue analisar mas não processar. Comuns em erros semânticos JSON (ex.: valor nulo; quando uma string é exigida mas é fornecido número ou booleano).                                                                                                                                                                                                                                                                             |
| <h4>429</h4>           | Limite de taxa de solicitação atingido                               | Taxa de solicitação (TPM ou RPM) atingiu o limite - aguarde um momento antes de tentar novamente                                                                                                                                                                                                                                                                                                                                                             |
| <h4>500</h4>           | Erro interno do servidor, impossível completar a solicitação          | Se persistir, entre em contato com o provedor de serviço                                                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>501</h4>           | O servidor não suporta a função solicitada, impossível completar a solicitação |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>502</h4>           | O servidor, atuando como gateway ou proxy, recebeu uma resposta inválida do servidor remoto ao tentar executar a solicitação |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>503</h4>           | O servidor está temporariamente indisponível para processar solicitações devido a sobrecarga ou manutenção. O tempo de espera pode estar incluso no cabeçalho Retry-After |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <h4>504</h4>           | O servidor, atuando como gateway ou proxy, não obteve a solicitação do servidor remoto a tempo |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

***

## Método para Verificar Erros no Console

* Clique na janela do cliente do Cherry Studio e pressione o atalho <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- A janela ativa deve ser a do cliente Cherry Studio para abrir o console;
- É necessário abrir o console antes de clicar em testar ou iniciar uma conversa para coletar informações da solicitação.
{% endhint %}

* Na janela do console que aparecer, clique em <mark style="color:blue;">`Network`</mark> → Procure o último item marcado com <mark style="color:red;">`×`</mark> chamado <mark style="color:red;">`completions`</mark> _(quando encontrar erros em diálogos, tradução ou verificação de conectividade do modelo)_ ou <mark style="color:red;">`generations`</mark> _(erros em geração de imagens)_ → Clique em <mark style="color:blue;">`Response`</mark> para ver o conteúdo completo retornado (área ④ na imagem).

> Se não conseguir identificar a causa do erro, envie uma captura de tela desta interface no [Grupo de Comunidade Oficial](https://t.me/CherryStudioAI) para obter ajuda.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método funciona não apenas em diálogos, mas também em testes de modelos, adição de bases de conhecimento, geração de imagens, etc. Sempre abra a janela de depuração antes de realizar operações que envolvam solicitações para capturar informações.

{% hint style="info" %}
O nome na coluna Name (área ② acima) varia conforme o cenário:

Diálogo, tradução, verificação de modelo: <mark style="color:red;">`completions`</mark>  
Geração de imagens: <mark style="color:red;">`generations`</mark>  
Criação de base de conhecimento: <mark style="color:red;">`embeddings`</mark>  
{% endhint %}

***

## Fórmula Não Renderizada/Erro de Renderização de Fórmula

* Se a fórmula aparece como código em vez de renderizada, verifique se possui delimitadores

> **Uso de Delimitadores**
>
> _Fórmula inline_
>
> * Use cifrão único: `$fórmula$`
> * Ou use `\(` e `\)`, ex: `\(fórmula\)`
>
> 
>
> _Bloco de fórmula independente_
>
> * Use cifrão duplo: `$$fórmula$$`
> * Ou use `\[fórmula\]`
> * Exemplo: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Erro de renderização/caracteres ilegíveis são comuns quando fórmulas contêm caracteres chineses - tente mudar o mecanismo de renderização para KaTeX.

***

## Não É Possível Criar Base de Conhecimento/Falha ao Obter Dimensões de Embedding

1. Status do modelo indisponível

> Confirme se o provedor suporta o modelo ou verifique o status de serviço do modelo.

2. Uso de modelo não adequado para embeddings

***

## Modelo Não Reconhece Imagens/Não Consegue Fazer Upload ou Selecionar Imagem

Primeiro verifique se o modelo suporta reconhecimento de imagem. Modelos populares são categorizados pelo Cherry Studio - modelos com ícone de olho após o nome suportam reconhecimento visual.

Modelos visuais permitem upload de arquivos de imagem. Se a funcionalidade não estiver corretamente associada, localize o modelo na lista de provedores, clique no botão de configuração após seu nome e marque a opção de imagem.

Para informações detalhadas, consulte as especificações do modelo com o provedor. Assim como modelos de embedding, modelos não visuais não funcionarão mesmo com a opção de imagem habilitada.