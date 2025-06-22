
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Configuração e Uso do MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Abra as configurações do Cherry Studio.
2. Encontre a opção `Servidor MCP`.
3. Clique em `Adicionar Servidor`.
4. Preencha os parâmetros relevantes do MCP Server ([link de referência](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Os campos que podem ser necessários incluem:
   * Nome: Personalize um nome, por exemplo `fetch-server`
   * Tipo: Selecione `STDIO`
   * Comando: Preencha `uvx`
   * Parâmetros: Preencha `mcp-server-fetch`
   * (Pode haver outros parâmetros dependendo do servidor específico)
5. Clique em `Salvar`.

{% hint style="success" %}
Após concluir a configuração acima, o Cherry Studio irá baixar automaticamente o MCP Server necessário - `fetch server`. Após o download ser concluído, podemos começar a usar! Observação: Se a configuração do mcp-server-fetch não for bem-sucedida, tente reiniciar o computador.
{% endhint %}

### Ativar o serviço MCP na caixa de chat

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Servidor MCP adicionado com sucesso nas configurações

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Demonstração do efeito de uso**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Como pode ser visto na imagem acima, após combinar a funcionalidade `fetch` do MCP, o Cherry Studio consegue entender melhor a intenção de consulta do usuário, obter informações relevantes da internet e fornecer respostas mais precisas e abrangentes.