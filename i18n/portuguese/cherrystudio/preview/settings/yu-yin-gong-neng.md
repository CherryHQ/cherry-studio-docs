---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Funcionalidades de Voz

```
Manual de Uso das Funcionalidades de Voz do Cherry Studio

1. Visão Geral das Funcionalidades de Voz

O Cherry Studio oferece três módulos principais de funcionalidade de voz: TTS (texto para voz), ASR (reconhecimento de voz) e chamada de voz. Esses recursos permitem que você se comunique naturalmente com a IA através de voz, melhorando sua experiência de uso.

- TTS (Texto para Voz): Converte respostas de texto da IA em saída de voz
- ASR (Reconhecimento de Voz): Converte sua fala em entrada de texto
- Chamada de Voz: Combina TTS e ASR para uma experiência de conversa semelhante ao ChatGPT

2. Funcionalidade TTS (Texto para Voz)

1. Tipos de serviço suportados

O Cherry Studio suporta quatro tipos de serviço TTS:

- OpenAI: Usa a API TTS da OpenAI, requer chave de API
- TTS do Navegador: Utiliza a síntese de voz integrada do navegador, gratuito sem configuração
- Siliconflow: Usa o serviço TTS do Siliconflow, requer chave de API
- TTS Online Gratuito: Utiliza serviços TTS gratuitos online, não requer chave de API

2. Método de configuração

1) Acesse a página de configurações, selecione a aba "Funcionalidades de Voz"
2) Na subaba "TTS":
   - Ative a função TTS (ligue o interruptor)
   - Selecione o tipo de serviço TTS
   - Configure os parâmetros conforme o tipo de serviço selecionado:
     - OpenAI: Preencha a chave de API, endereço da API, selecione voz e modelo
     - TTS do Navegador: Selecione a voz
     - Siliconflow: Preencha chave de API, endereço da API, selecione voz, modelo, formato de resposta e velocidade
     - TTS Online Gratuito: Selecione voz e formato de saída
3) Configure filtros TTS (opcional):
   - Filtrar processos de pensamento
   - Filtrar marcações Markdown
   - Filtrar blocos de código
4) Defina se deseja exibir a barra de progresso do TTS
5) Clique no botão "Testar TTS" para verificar a configuração

3. Método de uso

- Com o TTS ativado, as respostas da IA são automaticamente convertidas em voz
- Na interface de chat, botões de reprodução TTS aparecem abaixo de cada resposta da IA
- Clique no botão para reproduzir/pausar a voz
- Se habilitado, a barra de progresso será exibida abaixo do texto
- Textos longos são sintetizados em segmentos e reproduzidos continuamente

3. Funcionalidade ASR (Reconhecimento de Voz)

1. Tipos de serviço suportados

O Cherry Studio suporta três tipos de serviço ASR:

- OpenAI: Usa o modelo Whisper da OpenAI, requer chave de API
- Navegador: Utiliza o reconhecimento de voz integrado do navegador, gratuito sem configuração
- Servidor Local: Conecta-se a um servidor WebSocket local para reconhecimento de voz

2. Método de configuração

1) Acesse a página de configurações, selecione a aba "Funcionalidades de Voz"
2) Na subaba "ASR":
   - Ative a função ASR (ligue o interruptor)
   - Selecione o tipo de serviço ASR
   - Configure os parâmetros conforme o tipo de serviço selecionado:
     - OpenAI: Preencha chave de API, endereço da API, selecione modelo
     - Navegador: Nenhuma configuração adicional necessária
     - Servidor Local: Configure se deseja iniciar automaticamente ao iniciar o aplicativo
   - Selecione o idioma de reconhecimento (padrão: chinês)
3) Clique no botão "Testar ASR" para verificar a configuração

3. Método de uso

- Com o ASR ativado, um botão de reconhecimento de voz aparece ao lado da caixa de entrada
- Clique no botão para iniciar a gravação
- Após falar, a voz é convertida em texto e inserida na caixa de entrada
- Clique novamente para parar a gravação
- Suporte para reconhecimento contínuo de múltiplas frases em modo acumulativo

4. Funcionalidade de Chamada de Voz

1. Características

- Combina TTS e ASR para experiência de conversa semelhante ao ChatGPT
- Interface de janela flutuante arrastável
- Modo de "pressionar para falar"
- Suporte a atalhos personalizados
- Suporte a recolhimento da janela
- Seleção de modelo dedicado para chamadas de voz
- Suporte a prompts personalizados

2. Método de configuração

1) Acesse a página de configurações, selecione a aba "Funcionalidades de Voz"
2) Na subaba "Chamada de Voz":
   - Ative a função de chamada de voz (ligue o interruptor)
   - Clique em "Selecionar Modelo" para escolher o modelo de IA para chamadas
   - Personalize o prompt no campo de texto (opcional)
   - Clique em "Salvar" para manter ou "Redefinir" para restaurar o padrão

3. Método de uso

1) Na interface de chat, clique no ícone de telefone à direita da caixa de entrada
2) A janela de chamada abrirá com uma mensagem de boas-vindas
3) Pressione e segure o botão "Pressionar para Falar" para gravar (ou use o atalho)
4) Solte o botão para enviar o áudio para processamento
5) A IA responde via TTS
6) Controles na janela:
   - Mudo: Controla a saída de áudio
   - Pausa/Continua: Interrompe ou retoma a conversa
   - Configurações: Personaliza atalhos
   - Recolher: Minimiza a janela mantendo apenas a barra de falar
7) Clique em fechar para encerrar a chamada

4. Configuração de atalhos

1) Na janela de chamada, clique em configurações
2) No painel que aparece, clique no botão de atalhos
3) Pressione a tecla desejada (ex: barra de espaço, Shift)
4) Clique em "Salvar"
5) Use: Pressione o atalho para gravar, solte para enviar

5. Problemas Comuns e Soluções

1. Problemas relacionados ao TTS

- Problema: Sem som no TTS
  Solução: Verifique se o TTS está ativado e os parâmetros configurados corretamente

- Problema: Qualidade de áudio ruim
  Solução: Experimente outro serviço TTS ou voz diferente

- Problema: Erros durante reprodução
  Solução: Verifique chave de API e conexão de rede

2. Problemas relacionados ao ASR

- Problema: Não reconhece voz
  Solução: Verifique se ASR está ativado e parâmetros corretos

- Problema: Baixa precisão de reconhecimento
  Solução: Tente outro serviço ASR ou ajuste microfone

- Problema: Falha na conexão do servidor ASR
  Solução: Verifique se o servidor local está ativo ou reinicie o aplicativo

3. Problemas relacionados à chamada de voz

- Problema: Janela não abre
  Solução: Verifique função ativada e configurações de TTS/ASR

- Problema: Sem resposta ao pressionar para falar
  Solução: Verifique permissões do microfone ou reinicie a chamada

- Problema: Sem saída de voz nas respostas
  Solução: Verifique se TTS está ativado e não está mudo

6. Configurações Avançadas e Opções Personalizadas

1. Configurações avançadas de TTS

- Filtros: Oculta processos de pensamento, marcações Markdown e blocos de código
- Barra de progresso: Controla exibição
- Vozes e modelos personalizados: Adicione vozes e modelos personalizados

2. Configurações avançadas de ASR

- Inicialização automática: Inicia servidor ao abrir aplicativo
- Seleção de idioma: Escolha diferentes idiomas de reconhecimento

3. Configurações avançadas de chamada de voz

- Prompts personalizados: Oriente o comportamento da IA em modo de voz
- Modelo dedicado: Selecione modelo exclusivo para chamadas
- Atalhos personalizados: Defina teclas para controle de gravação

7. Recomendações de Uso

1. Escolha de serviço TTS:
   - Para alta qualidade: OpenAI ou Siliconflow
   - Sem configuração: TTS do Navegador ou TTS Online Gratuito

2. Escolha de serviço ASR:
   - Para alta precisão: OpenAI
   - Sem configuração: Reconhecimento do navegador

3. Otimização de chamadas:
   - Use fones para evitar eco
   - Ambientes silenciosos melhoram a precisão
   - Prompts personalizados tornam respostas mais naturais

4. Personalização conforme necessidades:
   - Para comunicação textual: Ative apenas TTS
   - Para entrada por voz: Ative apenas ASR
   - Para diálogo completo: Ative chamada de voz

Esperamos que este manual ajude você a aproveitar ao máximo as funcionalidades de voz do Cherry Studio, desfrutando de uma interação mais natural e conveniente com a IA!
```