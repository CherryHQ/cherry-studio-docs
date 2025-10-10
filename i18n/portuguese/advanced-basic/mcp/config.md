# Configuração e Uso do MCP


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1.  Abra as configurações do Cherry Studio.
2.  Encontre a opção `Servidor MCP`.
3.  Clique em `Adicionar servidor`.
4.  Preencha os parâmetros relevantes do MCP Server ([link de referência](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Os campos necessários podem incluir:
    *   Nome: Defina um nome personalizado, por exemplo `fetch-server`
    *   Tipo: Selecione `STDIO`
    *   Comando: Preencha `uvx`
    *   Parâmetros: Preencha `mcp-server-fetch`
    *   (Outros parâmetros podem existir dependendo do servidor específico)
5.  Clique em `Salvar`.

{% hint style="success" %}
Após completar a configuração acima, o Cherry Studio baixará automaticamente o servidor MCP necessário - `fetch server`. Após o download concluído, podemos começar a utilizá-lo! Observação: Se a configuração do mcp-server-fetch falhar, tente reiniciar o computador.
{% endhint %}

### Ativando o serviço MCP na caixa de chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

*   Servidor MCP adicionado com sucesso nas configurações

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demonstração dos efeitos de uso**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Como mostrado na imagem acima, ao combinar a função `fetch` do MCP, o Cherry Studio consegue compreender melhor a intenção da consulta do usuário, obtendo informações relevantes da internet para fornecer respostas mais precisas e abrangentes.