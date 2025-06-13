
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Provedores Personalizados

Cherry Studio não apenas integra os principais serviços de modelos de IA, mas também oferece recursos de personalização robustos. Com o recurso **Provedores Personalizados de IA**, você pode conectar facilmente qualquer modelo de IA necessário.

## Por que usar provedores personalizados de IA?

* **Flexibilidade:** Livre-se das limitações de fornecedores pré-definidos e escolha livremente os modelos de IA mais adequados às suas necessidades.
* **Diversidade:** Experimente modelos de IA de diferentes plataformas para explorar suas vantagens exclusivas.
* **Controle:** Gerencie diretamente suas chaves de API e endereços de acesso para garantir segurança e privacidade.
* **Personalização:** Conecte modelos implantados de forma privada para atender a cenários comerciais específicos.

## Como adicionar um provedor personalizado de IA?

Adicione seu provedor personalizado de IA ao Cherry Studio em poucos passos:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Acesse as configurações:** Na barra de navegação esquerda do Cherry Studio, clique em "Configurações" (ícone de engrenagem).
2. **Selecione serviços de modelo:** Na página de configurações, escolha a aba "Serviços de Modelo".
3. **Adicione provedor:** Na página "Serviços de Modelo", você verá a lista de provedores existentes. Clique no botão "+ Adicionar" na parte inferior para abrir a janela "Adicionar Provedor".
4. **Preencha as informações:** Na janela, forneça:
   * **Nome do Provedor:** Atribua um nome identificável para seu provedor personalizado (ex: MyCustomOpenAI).
   * **Tipo de Provedor:** Selecione o tipo na lista suspensa. Atualmente compatível com:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Salve a configuração:** Após preencher, clique em "Adicionar" para salvar.

## Configurando provedores personalizados de IA

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Após adicionar, localize seu provedor na lista para configurações detalhadas:

1. **Estado de ativação:** No final da lista de provedores, há um interruptor — ative-o para habilitar o serviço.
2. **Chave de API:**
   * Insira a chave de API (API Key) fornecida pelo seu provedor de IA.
   * Clique no botão "Verificar" à direita para validar a chave.
3. **Endereço da API:**
   * Informe o endereço base da API (Base URL).
   * Consulte sempre a documentação oficial do fornecedor para obter o URL correto.
4. **Gerenciamento de modelos:**
   * Clique em "+ Adicionar" para incluir manualmente os IDs dos modelos que deseja usar (ex: `gpt-3.5-turbo`, `gemini-pro`).

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * Caso não saiba o nome exato do modelo, consulte a documentação do fornecedor.
    * Use o botão "Gerenciar" para editar ou excluir modelos adicionados.

## Iniciando o uso

Após a configuração, selecione seu provedor e modelo personalizados na interface de chat do Cherry Studio para iniciar conversas com IA!

## Usando vLLM como provedor personalizado de IA

O vLLM é uma biblioteca de inferência para LLMs rápida e fácil de usar, semelhante ao Ollama. Veja como integrá-lo ao Cherry Studio:

1. **Instale o vLLM:** Siga a documentação oficial do vLLM ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # se você usa pip
    uv pip install vllm # se você usa uv
    ```
2. **Inicie o serviço vLLM:** Use a interface compatível com OpenAI fornecida pelo vLLM. Duas opções:

    * Iniciar com `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Iniciar com `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Garanta que o serviço inicie corretamente na porta padrão `8000`. Use `--port` para especificar outra porta.

3. **Adicione o vLLM ao Cherry Studio:**
   * Siga os passos anteriores para adicionar um novo provedor.
   * **Nome do Provedor:** `vLLM`
   * **Tipo de Provedor:** Selecione `OpenAI`.
4. **Configure o vLLM:**
   * **Chave de API:** Como o vLLM não requer autenticação, deixe em branco ou insira qualquer valor.
   * **Endereço da API:** Use o URL do serviço vLLM. Padrão: `http://localhost:8000/` (altere se usar outra porta).
   * **Gerenciamento de modelos:** Insira o nome do modelo carregado no vLLM. Ex: `gpt2` para o comando `--model gpt2`.
5. **Inicie conversas:** Selecione o provedor "vLLM" e o modelo configurado para interagir com LLMs via vLLM!

## Dicas e Truques

* **Documentação:** Sempre consulte a documentação oficial do fornecedor sobre chaves de API, URLs e nomes de modelos.
* **Valide chaves:** Use o botão "Verificar" para confirmar a validade das chaves de API.
* **URLs precisos:** Preencha endereços de API corretos conforme especificado pelo fornecedor.
* **Seletividade com modelos:** Adicione apenas modelos que serão utilizados, evitando excessos.