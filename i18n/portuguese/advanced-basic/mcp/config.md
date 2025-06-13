
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configuração e Uso do MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Abra as configurações do Cherry Studio.
2. Encontre a opção `MCP 服务器` (Servidores MCP).
3. Clique em `添加服务器` (Adicionar servidor).
4. Preencha os parâmetros relevantes do MCP Server ([link de referência](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Os campos podem incluir:
   * Nome: Um nome personalizado, por exemplo `fetch-server`
   * Tipo: Selecione `STDIO`
   * Comando: Preencha com `uvx`
   * Parâmetros: Preencha com `mcp-server-fetch`
   * (Pode haver outros parâmetros dependendo do servidor específico)
5. Clique em `保存` (Salvar).

{% hint style="success" %}
Após concluir a configuração acima, o Cherry Studio baixará automaticamente o MCP Server necessário - `fetch server`. Após o download, podemos começar a usar! Observação: Se a configuração do mcp-server-fetch não for bem-sucedida, tente reiniciar o computador.
{% endhint %}

### Ativando o serviço MCP no chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Após adicionar com sucesso um servidor MCP nas configurações de `MCP 服务器`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demonstração de uso**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Como mostra a imagem acima, após integrar a funcionalidade `fetch` do MCP, o Cherry Studio consegue entender melhor a intenção da consulta do usuário, obtém informações relevantes da internet e fornece respostas mais precisas e abrangentes.