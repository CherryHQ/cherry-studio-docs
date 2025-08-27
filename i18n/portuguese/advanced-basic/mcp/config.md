# Configuração e Uso do MCP


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1.  Abra as configurações do Cherry Studio.
2.  Localize a opção `Servidor MCP`.
3.  Clique em `Adicionar Servidor`.
4.  Preencha os parâmetros do MCP Server ([Link de referência](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Os campos podem incluir:
    *   Nome: Defina um nome personalizado, por exemplo `fetch-server`
    *   Tipo: Selecione `STDIO`
    *   Comando: Preencha com `uvx`
    *   Parâmetros: Preencha com `mcp-server-fetch`
    *   (Outros parâmetros podem ser necessários dependendo do servidor)
5.  Clique em `Salvar`.

{% hint style="success" %}
Após esta configuração, o Cherry Studio baixará automaticamente o MCP Server necessário - `fetch server`. Após o download, você poderá começar a usar! Observação: Se a configuração do mcp-server-fetch falhar, tente reiniciar o computador.
{% endhint %}

### Ativar serviço MCP na caixa de chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

*   Quando o servidor MCP for adicionado com sucesso em `Servidores MCP`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demonstração de resultados**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Como mostra a imagem acima, ao combinar a função `fetch` do MCP, o Cherry Studio compreende melhor a intenção das consultas dos usuários, obtém informações relevantes da internet e fornece respostas mais precisas e abrangentes.