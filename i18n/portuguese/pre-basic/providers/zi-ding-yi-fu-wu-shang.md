# Provedores Personalizados

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

## Provedores Personalizados

O Cherry Studio não apenas integra os principais serviços de modelos de IA, mas também oferece poderosas capacidades de personalização. Com o recurso **Provedores Personalizados de IA**, você pode integrar facilmente qualquer modelo de IA que necessitar.

### Por que usar Provedores Personalizados de IA?

* **Flexibilidade:** Liberte-se das limitações da lista pré-definida de provedores e escolha livremente os modelos de IA mais adequados às suas necessidades.
* **Diversidade:** Experimente modelos de IA de várias plataformas para explorar seus pontos fortes exclusivos.
* **Controle:** Gerencie diretamente suas chaves de API e endereços de acesso, garantindo segurança e privacidade.
* **Personalização:** Integre modelos implantados de forma privada para atender a cenários comerciais específicos.

### Como adicionar um Provedor Personalizado de IA?

Siga estes passos simples para adicionar seu provedor personalizado no Cherry Studio:

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Abra as Configurações:** Na barra de navegação esquerda do Cherry Studio, clique em "Configurações" (ícone de engrenagem).
2. **Acesse Serviços de Modelos:** Na página de configurações, selecione a aba "Serviços de Modelos".
3. **Adicione Provedor:** Na página "Serviços de Modelos", você verá a lista de provedores existentes. Clique no botão "+ Adicionar" abaixo da lista para abrir o pop-up "Adicionar Provedor".
4. **Preencha as Informações:** No pop-up, preencha:
   * **Nome do Provedor:** Dê um nome identificável (ex: MyCustomOpenAI).
   * **Tipo de Provedor:** Selecione na lista suspensa. Atualmente suportado:
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Salve a Configuração:** Após preencher, clique em "Adicionar" para salvar.

### Configurando o Provedor Personalizado

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Após adicionar, encontre seu provedor na lista e configure:

1. **Status de Ativação:** O interruptor à direita da lista ativa/desativa o serviço.
2. **Chave da API:**
   * Insira sua chave de API (API Key) fornecida pelo provedor.
   * Clique em "Verificar" à direita para validar a chave.
3. **Endereço da API:**
   * Insira o endereço de acesso da API (Base URL).
   * Consulte a documentação oficial do provedor para obter o endereço correto.
4.  **Gerenciamento de Modelos:**

    * Clique em "+ Adicionar" para incluir manualmente os IDs dos modelos que deseja usar (ex: `gpt-3.5-turbo`, `gemini-pro`).

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    \* Consulte a documentação oficial se não souber os nomes exatos.\
    \* Clique em "Gerenciar" para editar ou excluir modelos adicionados.

### Começando a Usar

Após a configuração, selecione seu provedor e modelo no chat do Cherry Studio para iniciar conversas com a IA!

### Usando o vLLM como Provedor Personalizado

O vLLM é uma biblioteca de inferência de LLM rápida e fácil de usar, similar ao Ollama. Siga estes passos para integrá-lo ao Cherry Studio:

1.  **Instale o vLLM:** Siga o guia oficial ([https://docs.vllm.ai/en/latest/getting\_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm  # Se usar pip
    uv pip install vllm  # Se usar uv
    ```
2.  **Inicie o Serviço vLLM:** Use a interface compatível com OpenAI:

    * Via `vllm.entrypoints.openai.api_server`:

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Via `uvicorn`:

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

    O serviço rodará na porta padrão `8000`. Use `--port` para especificar outra porta.
3. **Adicione o vLLM no Cherry Studio:**
   * Siga os passos anteriores para adicionar novo provedor.
   * **Nome do Provedor:** `vLLM`
   * **Tipo de Provedor:** Selecione `OpenAI`.
4. **Configure o vLLM:**
   * **Chave da API:** Deixe em branco ou insira qualquer conteúdo (vLLM não requer chave).
   * **Endereço da API:** Insira o endereço do vLLM (padrão: `http://localhost:8000/`).
   * **Gerenciamento de Modelos:** Adicione o nome do modelo carregado (ex: `gpt2` para o exemplo acima).
5. **Inicie as Conversas:** Selecione o provedor vLLM e o modelo (ex: `gpt2`) para conversar com o LLM via vLLM!

### Dicas e Truques

* **Leia a Documentação:** Antes de adicionar provedores, consulte a documentação oficial sobre chaves de API, endereços e nomes de modelos.
* **Verifique as Chaves:** Use o botão "Verificar" para validar chaves rapidamente.
* **Endereços Precisos:** Diferentes provedores e modelos podem ter endereços distintos.
* **Modelos Necessários:** Adicione apenas modelos que realmente utilizará para evitar excessos.
