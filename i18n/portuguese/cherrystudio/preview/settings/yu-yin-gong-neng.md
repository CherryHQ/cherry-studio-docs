---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Recursos de Voz

```
Manual de Recursos de Voz do Cherry Studio

1. Visão Geral dos Recursos de Voz

O Cherry Studio oferece três módulos principais de recursos de voz: TTS (Conversão de Texto em Fala), ASR (Reconhecimento de Fala) e Chamada de Voz. Essas funcionalidades permitem que você interaja naturalmente com a IA por voz, melhorando sua experiência.

- TTS (Conversão de Texto em Fala): Converte respostas de texto da IA em saída de áudio
- ASR (Reconhecimento de Fala): Converte sua fala em entrada de texto
- Chamada de Voz: Combina TTS e ASR para uma experiência de diálogo semelhante ao ChatGPT

2. TTS (Conversão de Texto em Fala)

1. Tipos de Serviços Suportados

O Cherry Studio suporta quatro tipos de serviços TTS:

- OpenAI: Utiliza a API TTS da OpenAI, requer chave de API
- TTS do Navegador: Usa a síntese de voz integrada do navegador, gratuito e sem configuração
- SiliconFlow: Usa o serviço TTS da SiliconFlow, requer chave de API
- TTS Online Gratuito: Serviço TTS gratuito online, não requer chave de API

2. Método de Configuração

1) Acesse a página de configurações, selecione a aba "Recursos de Voz"
2) Na subaba "TTS":
   - Ative a função TTS (ligue a alternância)
   - Selecione o tipo de serviço TTS
   - Configure os parâmetros conforme o serviço escolhido:
     - OpenAI: Preencha chave de API, endereço da API, selecione tom de voz e modelo
     - TTS do Navegador: Selecione tom de voz
     - SiliconFlow: Preencha chave de API, endereço da API, selecione tom de voz, modelo, formato de resposta e velocidade
     - TTS Online Gratuito: Selecione tom de voz e formato de saída
3) Configure filtros TTS (opcional):
   - Filtrar processo de raciocínio
   - Filtrar marcações Markdown
   - Filtrar blocos de código
4) Defina se exibirá a barra de progresso do TTS
5) Clique em "Testar TTS" para verificar a configuração

3. Modo de Uso

- Quando ativado, as respostas da IA são convertidas automaticamente em áudio
- Botões de reprodução aparecem abaixo de cada resposta no chat
- Clique para reproduzir/pausar o áudio
- Textos longos são sintetizados em segmentos e reproduzidos continuamente

3. ASR (Reconhecimento de Fala)

1. Tipos de Serviços Suportados

Três tipos de serviços ASR:

- OpenAI: Usa o modelo Whisper da OpenAI, requer chave de API
- Navegador: Utiliza o reconhecimento de voz integrado, gratuito e sem configuração
- Servidor Local: Conecta-se a servidor WebSocket local

2. Método de Configuração

1) Na página de configurações, aba "Recursos de Voz"
2) Na subaba "ASR":
   - Ative a função ASR (ligue a alternância)
   - Selecione o tipo de serviço ASR
   - Configure parâmetros conforme o serviço:
     - OpenAI: Preencha chave de API, endereço da API, selecione modelo
     - Navegador: Sem configuração adicional
     - Servidor Local: Defina se inicia automaticamente com aplicativo
   - Selecione idioma do ASR (padrão: chinês)
3) Clique em "Testar ASR" para verificar

3. Modo de Uso

- Botão de microfone aparece ao lado da caixa de entrada
- Clique para iniciar gravação
- A fala é convertida em texto na caixa de entrada
- Clique novamente para parar gravação
- Reconhece múltiplas frases em modo contínuo

4. Chamada de Voz

1. Características

- Combina TTS e ASR para diálogos como ChatGPT
- Interface em janela flutuante arrastável
- Modo "Pressione para Falar"
- Atalhos personalizáveis
- Modelo específico para chamadas de voz
- Prompts personalizados

2. Método de Configuração

1) Na aba "Recursos de Voz"
2) Na subaba "Chamada":
   - Ative chamada de voz (ligue a alternância)
   - Clique "Selecionar Modelo" para escolher IA de chamadas
   - Personalize prompts de voz (opcional)
   - Clique "Salvar" ou "Redefinir"

3. Modo de Uso

1) Clique no ícone de telefone ao lado da caixa de chat
2) A janela de chamada abre com saudação de voz
3) Pressione "Pressione para Falar" para gravar (ou use atalho)
4) Solte para enviar para IA
5) IA responde via TTS
6) Controles:
   - Mudo: Silencia saída TTS
   - Pausa/Continuar: Controla fluxo
   - Configurações: Define atalhos
   - Recolher: Minimiza janela
7) Clique no "X" para finalizar

4. Configuração de Atalhos

1) Na janela de chamada, clique em ⚙️
2) Em "Atalhos", clique em "Definir"
3) Pressione a tecla desejada (ex: Espaço, Shift)
4) Salve configurações

5. Problemas Comuns e Soluções

1. Problemas TTS

- Sem áudio: Verifique ativação, tipo de serviço e parâmetros
- Qualidade ruim: Experimente outro serviço ou tom de voz
- Erros: Verifique chave de API e conexão

2. Problemas ASR

- Não reconhece: Verifique ativação e configurações
- Baixa precisão: Altere tipo de serviço ou ajuste microfone
- Falha de conexão: Verifique servidor local ou reinicie app

3. Problemas de Chamada

- Janela não abre: Verifique ativação e configurações TTS/ASR
- Botão não responde: Verifique permissões de microfone
- Sem saída de voz: Verifique mutismo e configurações TTS

6. Configurações Avançadas

1. TTS Avançado

- Opções de filtragem: Processo mental, marcações, códigos
- Barra de progresso: Exibir/ocultar
- Tons e modelos personalizados

2. ASR Avançado

- Início automático do servidor
- Seleção de idioma

3. Chamada Avançada

- Personalização de prompts
- Modelo dedicado de voz
- Atalhos personalizados

7. Sugestões de Uso

1. Serviços TTS:
   - Qualidade premium: OpenAI ou SiliconFlow
   - Zero configuração: TTS do Navegador ou Online Gratuito

2. Serviços ASR:
   - Alta precisão: OpenAI
   - Sem configuração: Navegador

3. Otimizar chamadas:
   - Use headphones para evitar eco
   - Ambientes silenciosos melhoram reconhecimento
   - Personalize prompts para respostas de voz

4. Use conforme necessidade:
   - TTS somente para respostas em áudio
   - ASR somente para entrada por voz
   - Chamada completa para diálogos

Esperamos que este manual ajude a aproveitar os recursos de voz do Cherry Studio para uma interação natural com IA!
```