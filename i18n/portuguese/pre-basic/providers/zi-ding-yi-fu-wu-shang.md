# Provedores Personalizados


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Cherry Studio não apenas integra os principais serviços de modelos de IA, mas também oferece recursos poderosos de personalização. Com o recurso **Provedores de IA Personalizados**, você pode integrar facilmente qualquer modelo de IA que desejar.

## Por que usar provedores de IA personalizados?

* **Flexibilidade:** Não fique limitado à lista de provedores pré-definidos, escolha livremente os modelos de IA que melhor atendem às suas necessidades.
* **Diversidade:** Experimente modelos de IA de várias plataformas diferentes e descubra suas vantagens únicas.
* **Controle:** Gerencie diretamente suas chaves de API e endereços de acesso, garantindo segurança e privacidade.
* **Personalização:** Integre modelos implantados de forma privada para atender às necessidades de cenários de negócios específicos.

## Como adicionar um provedor de IA personalizado?

Em apenas alguns passos simples, você pode adicionar seu provedor de IA personalizado no Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Abrir configurações:** Na barra de navegação esquerda do Cherry Studio, clique em "Configurações" (ícone de engrenagem).
2. **Acessar serviços de modelo:** Na página de configurações, selecione a guia "Serviços de Modelo".
3. **Adicionar provedor:** Na página "Serviços de Modelo", você verá a lista de provedores existentes. Clique no botão "+ Adicionar" abaixo da lista para abrir o pop-up "Adicionar Provedor".
4. **Preencher informações:** No pop-up, preencha os seguintes campos:
   * **Nome do provedor:** Dê um nome identificável ao seu provedor personalizado (ex: MyCustomOpenAI).
   * **Tipo de provedor:** Selecione o tipo na lista suspensa. Atualmente suportados:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Salvar configuração:** Após preencher, clique em "Adicionar" para salvar sua configuração.

## Configurar provedor de IA personalizado

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Após adicionar, encontre seu provedor na lista e faça a configuração detalhada:

1. **Status de ativação:** No extremo direito da lista de provedores personalizados há um interruptor de ativação. Ative para habilitar o serviço personalizado.
2. **Chave de API:**
   * Insira a chave de API (API Key) fornecida pelo seu provedor de IA.
   * Clique no botão "Verificar" à direita para validar a chave.
3. **Endereço da API:**
   * Insira o endereço base da API (Base URL).
   * Consulte sempre a documentação oficial do seu provedor de IA para obter o endereço correto.
4. **Gerenciamento de modelos:**
   * Clique em "+ Adicionar" para incluir manualmente os IDs dos modelos que deseja usar neste provedor (ex: `gpt-3.5-turbo`, `gemini-pro`).

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * Consulte a documentação oficial do seu provedor de IA se não souber os nomes exatos dos modelos.
    * Clique em "Gerenciar" para editar ou remover modelos já adicionados.

## Começando a usar

Após completar as configurações, você poderá selecionar seu provedor de IA personalizado e modelo na interface de chat do Cherry Studio para iniciar conversas com a IA!

## Usando vLLM como provedor de IA personalizado

vLLM é uma biblioteca de inferência para LLMs rápida e fácil de usar, similar ao Ollama. Veja como integrá-lo ao Cherry Studio:

1. **Instalar vLLM:** Siga a documentação oficial do vLLM ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)) para instalação.

    ```sh
    pip install vllm # se você usa pip
    uv pip install vllm # se você usa uv
    ```
2. **Iniciar serviço vLLM:** Use a interface compatível com OpenAI fornecida pelo vLLM. Duas formas principais:

    * Usando `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Usando `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Certifique-se que o serviço iniciou corretamente na porta padrão `8000`. Você pode especificar outra porta usando o parâmetro `--port`.

3. **Adicionar provedor vLLM no Cherry Studio:**
   * Siga os passos anteriores para adicionar um novo provedor de IA personalizado.
   * **Nome do provedor:** `vLLM`
   * **Tipo de provedor:** Selecione `OpenAI`.
4. **Configurar provedor vLLM:**
   * **Chave de API:** Como vLLM não requer chave, deixe em branco ou insira qualquer valor.
   * **Endereço da API:** Insira o endereço da API do vLLM. Padrão: `http://localhost:8000/` (ajuste se usar porta diferente).
   * **Gerenciamento de modelos:** Adicione o nome do modelo carregado no vLLM. No exemplo `python -m vllm.entrypoints.openai.api_server --model gpt2`, insira `gpt2`.
5. **Iniciar conversa:** Selecione agora o provedor vLLM e o modelo `gpt2` no Cherry Studio para conversar com o LLM acionado pelo vLLM!

## Dicas e boas práticas

* **Revise a documentação:** Sempre consulte a documentação oficial do seu provedor de IA antes de adicioná-lo.
* **Verifique a chave API:** Use o botão "Verificar" para evitar falhas devido a chaves inválidas.
* **Atenção ao endereço API:** Diferentes provedores e modelos podem exigir endereços distintos.
* **Adição seletiva de modelos:** Adicione apenas modelos que realmente utilizará, evitando excessos.