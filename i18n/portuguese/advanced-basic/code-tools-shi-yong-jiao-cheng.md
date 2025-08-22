---
description: Tools
icon: code
---
# Tutorial de Uso do Code Tools


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




A versão v1.5.7 do Cherry Studio introduziu a funcionalidade Code Agent, que é poderosa e de operação simples, permitindo iniciar e gerenciar diretamente múltiplos agentes de programação de IA. Este tutorial irá guiá-lo através do processo completo de configuração e inicialização.

***

### Passos de Operação

#### 1. Atualize o Cherry Studio

Primeiro, certifique-se de que o seu Cherry Studio está atualizado para a versão **v1.5.7** ou superior. Você pode ir para [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) ou o site oficial para baixar a versão mais recente.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### 2. Ajuste a Posição da Barra de Navegação

Para facilitar o uso da funcionalidade de abas superiores, recomendamos ajustar a barra de navegação para o topo.

* Caminho de operação: `Configurações` -> `Configurações de exibição` -> `Configurações da barra de navegação`
* Defina a opção "Posição da barra de navegação" para **`Topo`**.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Crie uma Nova Aba

Clique no ícone "+" no topo da interface para criar uma nova aba em branco.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 4. Abra a Função Code Agent

Na nova aba, clique no ícone `Code` (ou `</>`) para entrar na interface de configuração do Code Agent.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Selecione a Ferramenta CLI

Com base nas suas necessidades e na chave de API que possui, selecione uma ferramenta Code Agent para usar. Atualmente, são suportadas as seguintes:

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Selecione o Modelo Chamado pelo Agent

Na lista suspensa de modelos, selecione um modelo compatível com a ferramenta CLI que escolheu. _(Para uma explicação detalhada da compatibilidade de modelos, consulte as "Observações Importantes" abaixo.)_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Especifique o Diretório de Trabalho

Clique no botão "Selecionar diretório" para especificar um diretório de trabalho para o Agent. O Agent terá permissão para acessar todos os arquivos e subdiretórios nesse diretório, a fim de entender o contexto do projeto, ler arquivos e executar código.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Configure as Variáveis de Ambiente

* **Configuração automática**: As escolhas feitas na Etapa 6 (modelo) e Etapa 7 (diretório de trabalho) gerarão automaticamente as variáveis de ambiente correspondentes.
* **Adição personalizada**: Se o seu Agent ou projeto exigir outras variáveis de ambiente específicas (por exemplo, `PROXY_URL`), você pode adicioná-las personalizadas nesta área.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Opções de Atualização

* **Arquivos executáveis integrados**: O Cherry Studio já integrou todos os executáveis do Code Agent acima para você; na maioria dos casos, você pode usá-los diretamente sem necessidade de internet.
* **Atualização automática**: Se desejar que o Agent sempre esteja na versão mais recente, você pode marcar a opção **`Verificar atualizações e instalar a versão mais recente`**. Ao marcar, o programa verificará a internet e atualizará a ferramenta Agent toda vez que for iniciado.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Inicie o Agent

Após concluir todas as configurações, clique no botão **`Iniciar`**. O Cherry Studio chamará automaticamente a ferramenta Terminal (Terminal) do seu sistema, carregará todas as variáveis de ambiente nela e executará o Code Agent selecionado. Agora você pode interagir com o AI Agent na janela de terminal que aparecer.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Observações Importantes

1. **Explicação da Compatibilidade de Modelos**:
   * **Claude Code**: É necessário escolher um modelo que suporte o formato Anthropic API Endpoint. Atualmente, os modelos suportados oficialmente incluem:
     * Modelos da série Claude
     * DeepSeek V3.1 (plataforma de API oficial)
     * Kimi K2 (plataforma de API oficial)
     * GLM 4.5 da Zhipu (plataforma de API oficial)
     * **Nota**: Atualmente, muitos provedores de serviços terceirizados (como One API, New API, etc.) oferecem APIs para DeepSeek, Kimi, GLM que suportam principalmente o formato OpenAI Chat Completions, podendo não ser compatíveis diretamente com o Claude Code, sendo necessário aguardar a adaptação gradual por parte dos provedores.
   * **Gemini CLI**: É necessário escolher um modelo da série Gemini do Google.
   * **Qwen Code**: Suporta modelos com o formato OpenAI Chat Completions API, e recomenda-se fortemente usar a série de modelos **`Qwen3 Coder`** para obter os melhores resultados de geração de código.
   * **OpenAI Codex**: Suporta modelos da série GPT (como `gpt-4o`, `gpt-5`, etc.).
2. **Conflitos de Dependências e Ambiente**:
   * O Cherry Studio integra internamente um ambiente de execução Node.js independente, executáveis do Code Agent e configurações de variáveis de ambiente, visando fornecer um ambiente limpo pronto para uso.
   * Se você encontrar conflitos de dependências ou erros estranhos ao iniciar o Agent, considere **desinstalar ou desativar temporariamente as dependências relacionadas instaladas no sistema** (como o Node.js instalado globalmente ou cadeia de ferramentas específica) para eliminar conflitos.
3. **Aviso de Consumo de Token de API**:
   * **O Code Agent consome tokens de API em grande quantidade**. Ao lidar com tarefas complexas, o Agent pode gerar uma grande quantidade de solicitações para pensar, planejar e gerar código, resultando em um rápido consumo de tokens.
   * Certifique-se de agir **dentro de suas capacidades** com base na sua cota de API e orçamento, e monitore de perto o uso de tokens para evitar estouros orçamentários.

Esperamos que este tutorial ajude você a começar rapidamente com a poderosa funcionalidade Code Agent do Cherry Studio!