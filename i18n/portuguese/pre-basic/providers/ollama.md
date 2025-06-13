
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Ollama

Ollama é uma excelente ferramenta de código aberto que permite executar e gerenciar facilmente diversos modelos de linguagem grandes (LLMs) localmente. O Cherry Studio agora oferece suporte à integração com Ollama, permitindo que você interaja diretamente com LLMs implantados localmente na interface familiar, sem depender de serviços em nuvem!

## O que é Ollama?

Ollama é uma ferramenta que simplifica a implantação e o uso de modelos de linguagem grandes (LLMs). Ele apresenta as seguintes características:

* **Execução local:** Os modelos funcionam inteiramente no seu computador local, sem necessidade de internet, protegendo sua privacidade e segurança de dados.
* **Simples e fácil de usar:** Comandos simples de terminal permitem baixar, executar e gerenciar diversos LLMs.
* **Ampla variedade de modelos:** Suporta modelos open-source populares como Llama 2, Deepseek, Mistral, Gemma e muitos outros.
* **Multiplataforma:** Compatível com macOS, Windows e Linux.
* **API aberta:** Oferece interface compatível com OpenAI, permitindo integração com outras ferramentas.

## Por que usar Ollama no Cherry Studio?

* **Sem dependência de nuvem:** Livre de cotas e custos de APIs em nuvem, explore todo o potencial dos LLMs locais.
* **Privacidade de dados:** Todas suas conversas permanecem localmente armazenadas, sem riscos de vazamento.
* **Funcionamento offline:** Interaja com LLMs mesmo sem conexão à internet.
* **Personalização:** Selecione e configure o LLM mais adequado às suas necessidades específicas.

## Configurando Ollama no Cherry Studio

### **1. Instalando e executando Ollama**

Primeiro, você precisa instalar e executar o Ollama no seu computador. Siga estes passos:

*   **Baixe o Ollama:** Visite o site oficial ([https://ollama.com/](https://ollama.com/)) e baixe o pacote correspondente ao seu sistema operacional.\
    No Linux, instale diretamente via comando:

    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```
* **Instale o Ollama:** Siga as instruções do instalador.
*   **Baixe um modelo:** Abra o terminal e use `ollama run` para baixar o modelo desejado. Exemplo para Llama 2:

    ```sh
    ollama run llama3.2
    ```

    O Ollama baixará e executará o modelo automaticamente.
* **Mantenha o Ollama em execução:** Certifique-se que o Ollama permaneça ativo durante suas interações via Cherry Studio.

### **2. Adicionando Ollama como provedor no Cherry Studio**

Adicione o Ollama como provedor personalizado no Cherry Studio:

* **Acesse Configurações:** Na barra lateral esquerda, clique em "Configurações" (ícone de engrenagem).
* **Selecione Modelos:** No menu de configurações, acesse "Modelos".
* **Adicione provedor:** Clique em Ollama na lista.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configurando o provedor Ollama**

Localize o Ollama na lista de provedores e ajuste as configurações:

1. **Status de ativação:**
   * Ative o interruptor ao lado do provedor Ollama.
2. **Chave da API:**
   * Ollama **não requer** chave API por padrão. Deixe em branco ou insira qualquer valor.
3. **Endereço da API:**
   * Insira o endereço local do Ollama. Normalmente:
       ```
       http://localhost:11434/
       ```
       Ajuste se alterar a porta padrão.
4. **Tempo de atividade:** Tempo máximo de inatividade (em minutos) antes da desconexão automática.
5. **Gerenciamento de modelos:**
   * Clique em "+ Adicionar" para incluir modelos previamente baixados no Ollama.
   * Exemplo: Após `ollama run llama3.2`, insira `llama3.2`.
   * Use "Gerenciar" para editar ou remover modelos adicionados.

## Começando a usar

Após a configuração, selecione o provedor Ollama e seu modelo no painel de chat do Cherry Studio para iniciar conversas locais com LLMs!

## Dicas úteis

* **Primeira execução:** O download inicial do modelo pode demorar — aguarde pacientemente.
* **Lista de modelos:** Execute `ollama list` no terminal para ver modelos disponíveis.
* **Requisitos de hardware:** Verifique se seu computador atende aos requisitos de CPU, RAM e GPU do modelo escolhido.
* **Documentação:** Clique em `Ver documentação e modelos do Ollama` nas configurações para acessar o site oficial.