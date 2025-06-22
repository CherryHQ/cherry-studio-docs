
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Ollama

Ollama é uma excelente ferramenta de código aberto que permite executar e gerenciar facilmente vários modelos de linguagem grandes (LLMs) localmente. O Cherry Studio agora suporta integração com Ollama, permitindo que você interaja diretamente com LLMs implantados localmente na interface familiar, sem depender de serviços em nuvem!

## O que é Ollama?

Ollama é uma ferramenta que simplifica a implantação e uso de modelos de linguagem grandes (LLMs). Ele possui as seguintes características:

* **Execução local:** Os modelos são executados completamente no seu computador local, sem necessidade de conexão à internet, protegendo sua privacidade e segurança de dados.
* **Simples e fácil de usar:** Com comandos simples de linha de comando, você pode baixar, executar e gerenciar vários LLMs.
* **Riqueza de modelos:** Suporta diversos modelos de código aberto populares como Llama 2, Deepseek, Mistral, Gemma, entre outros.
* **Multiplataforma:** Compatível com macOS, Windows e Linux.
* **API Aberta:** Possui interface compatível com OpenAI e pode ser integrado com outras ferramentas.

## Por que usar Ollama no Cherry Studio?

* **Sem serviços de nuvem:** Não está mais limitado por cotas e custos de API em nuvem, desfrute plenamente do poder dos LLMs locais.
* **Privacidade de dados:** Todos os seus dados de conversa permanecem locais, sem preocupações com vazamento de privacidade.
* **Disponível offline:** Mesmo sem conexão à internet, você pode continuar interagindo com o LLM.
* **Personalização:** Selecione e configure o LLM que melhor atenda às suas necessidades.

## Configurar Ollama no Cherry Studio

### **1. Instalar e executar Ollama**

Primeiro, você precisa instalar e executar o Ollama no seu computador:

* **Baixar Ollama:** Visite o site oficial do Ollama ([https://ollama.com/](https://ollama.com/)) e baixe o pacote correspondente ao seu sistema operacional.  
  No Linux, você pode instalar diretamente via comando:
  
  ```sh
  curl -fsSL https://ollama.com/install.sh | sh
  ```
* **Instalar Ollama:** Siga as instruções do instalador para completar a instalação.
* **Baixar modelos:** Abra o terminal (ou prompt de comando) e use o comando `ollama run` para baixar o modelo desejado. Exemplo para baixar Llama 3.2:
  
  ```sh
  ollama run llama3.2
  ```
  
  O Ollama baixará e executará o modelo automaticamente.
* **Manter Ollama em execução:** Certifique-se de que o Ollama permaneça em execução durante sua interação com os modelos via Cherry Studio.

### **2. Adicionar Ollama como provedor no Cherry Studio**

Adicione o Ollama como provedor personalizado de IA:

* **Abrir configurações:** Na barra lateral do Cherry Studio, clique no ícone de engrenagem "Configurações".
* **Acessar serviços de modelo:** Selecione a aba "Model Services" (Serviços de Modelo).
* **Adicionar provedor:** Clique em "Ollama" na lista.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configurar o provedor Ollama**

Localize o Ollama na lista de provedores e configure:

1. **Status de ativação:**
   * Ative o interruptor à direita para habilitar o serviço.
2. **Chave API:**
   * O Ollama **não requer** chave API por padrão. Deixe este campo vazio ou preencha arbitrariamente.
3. **Endereço API:**
   * Insira o endereço local da API do Ollama (padrão):
   
   ```
   http://localhost:11434/
   ```
   
   Ajuste se você alterou a porta.
4. **Tempo de manutenção ativa:** Define o tempo máximo de inatividade da sessão (em minutos). O Cherry Studio desconectará automaticamente após este período para liberar recursos.
5. **Gerenciamento de modelos:**
   * Clique em "+ Adicionar" para inserir manualmente o nome dos modelos baixados no Ollama (ex: `llama3.2` se baixado via `ollama run llama3.2`).
   * Use o botão "Gerenciar" para editar ou remover modelos.

## Começar a usar

Após a configuração, selecione "Ollama" e seu modelo no painel de chat do Cherry Studio para iniciar conversas com seu LLM local!

## Dicas e sugestões

* **Primeira execução do modelo:** O download inicial dos arquivos pode demorar significativamente.
* **Ver modelos disponíveis:** Execute `ollama list` no terminal para listar modelos instalados.
* **Requisitos de hardware:** Verifique se seu computador possui recursos suficientes (CPU/RAM/GPU) para executar LLMs.
* **Documentação Ollama:** Clique em `View Ollama Documentation and Models` na página de configuração para acessar a documentação oficial.