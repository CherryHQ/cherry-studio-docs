---
description: Tools
icon: code
---
# Tutorial de Uso do Code Tools


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




A versão Cherry Studio v1.5.7 introduziu a funcionalidade poderosa e de operação simples do Code Agent, que permite iniciar e gerenciar diretamente diversos agentes de programação de IA. Este tutorial irá guiá-lo através do processo completo de configuração e inicialização.

***

### Passos de Operação

#### 1. Atualize o Cherry Studio

Primeiro, certifique-se de que seu Cherry Studio está atualizado para a versão **v1.5.7** ou superior. Você pode baixar a versão mais recente em [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) ou no site oficial.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 2. Ajuste a Posição da Barra de Navegação

Para facilitar o uso da funcionalidade de abas superiores, recomendamos ajustar a barra de navegação para o topo.

* Caminho da operação: `Configurações` -> `Configurações de Exibição` -> `Configurações da Barra de Navegação`
* Defina a opção "Posição da Barra de Navegação" como **`Topo`**.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Crie uma Nova Aba

Clique no ícone "+" na parte superior da interface para criar uma nova aba em branco.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. Ative a Função Code Agent

Na nova aba criada, clique no ícone `Code` (ou `</>`) para acessar a interface de configuração do Code Agent.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Selecione a Ferramenta CLI

De acordo com suas necessidades e a chave de API disponível, selecione uma ferramenta Code Agent para usar. Atualmente, são suportadas as seguintes opções:

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Selecione o Modelo para o Agent

Na lista suspensa de modelos, selecione um modelo compatível com a ferramenta CLI escolhida. _(Para detalhes sobre compatibilidade de modelos, consulte a seção "Observações Importantes" abaixo)_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Especifique o Diretório de Trabalho

Clique no botão "Selecionar Diretório" para definir um diretório de trabalho para o Agent. O Agent terá acesso a todos os arquivos e subdiretórios nesse diretório, permitindo que ele compreenda o contexto do projeto, leia arquivos e execute códigos.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Configure Variáveis de Ambiente

* **Configuração Automática**: Suas seleções na etapa 6 (modelo) e etapa 7 (diretório de trabalho) gerarão automaticamente as variáveis de ambiente correspondentes.
* **Adição Personalizada**: Se seu Agent ou projeto exigir variáveis de ambiente específicas adicionais (por exemplo, `PROXY_URL`), você pode adicioná-las personalizadamente nesta área.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Opções de Atualização

* **Arquivos Executáveis Integrados**: O Cherry Studio já inclui arquivos executáveis para todos os Code Agents mencionados acima. Na maioria dos casos, você pode usá-los diretamente sem conexão à internet.
* **Atualização Automática**: Se desejar que o Agent esteja sempre na versão mais recente, marque a opção **`Verificar atualizações e instalar a versão mais recente`**. Quando marcada, o programa verificará e atualizará a ferramenta Agent a cada inicialização.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Inicie o Agent

Após concluir todas as configurações, clique no botão **`Iniciar`**. O Cherry Studio chamará automaticamente a ferramenta Terminal do seu sistema, carregará todas as variáveis de ambiente e executará o Code Agent selecionado. Agora você pode interagir com o AI Agent na janela de terminal aberta.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Observações Importantes

1. **Explicações sobre Compatibilidade de Modelos**:
   * **Claude Code**: Requer modelos compatíveis com o formato Anthropic API Endpoint. Atualmente, os modelos suportados oficialmente incluem:
     * Modelos da série Claude
     * DeepSeek V3.1 (plataforma de API oficial)
     * Kimi K2 (plataforma de API oficial)
     * GLM 4.5 da Zhipu (plataforma de API oficial)
     * **Atenção**: Atualmente, muitos provedores de terceiros (como One API, New API, etc.) oferecem APIs para DeepSeek, Kimi e GLM principalmente no formato OpenAI Chat Completions, o que pode não ser diretamente compatível com Claude Code. É necessário aguardar adaptação gradual dos provedores.
   * **Gemini CLI**: Requer modelos da série Gemini do Google.
   * **Qwen Code**: Suporta modelos com formato de API OpenAI Chat Completions. Recomenda-se fortemente usar modelos da série **`Qwen3 Coder`** para os melhores resultados de geração de código.
   * **OpenAI Codex**: Suporta modelos da série GPT (por exemplo, `gpt-4o`, `gpt-5`, etc.).
2. **Conflitos de Dependências e Ambiente**:
   * O Cherry Studio integra internamente um ambiente Node.js independente, arquivos executáveis do Code Agent e configurações de variáveis de ambiente, visando fornecer um ambiente limpo pronto para uso.
   * Se encontrar conflitos de dependência ou erros incomuns ao iniciar o Agent, considere **desinstalar ou desativar temporariamente as dependências relevantes instaladas globalmente no sistema** (como Node.js ou cadeias de ferramentas específicas) para eliminar conflitos.
3. **Aviso sobre Consumo de API Token**:
   * **O Code Agent consome uma quantidade muito grande de tokens de API**. Ao processar tarefas complexas, o Agent pode gerar numerosas solicitações para pensar, planejar e gerar código, resultando em consumo rápido de tokens.
   * Certifique-se de **atuar conforme sua capacidade**, monitorar de perto o uso de tokens de acordo com sua cota e orçamento de API, para evitar estouro de orçamento.

Esperamos que este tutorial o ajude a dominar rapidamente a poderosa funcionalidade Code Agent do Cherry Studio!