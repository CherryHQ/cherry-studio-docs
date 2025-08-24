---
hidden: True
icon: phone-arrow-up-right
---
# Funcionalidade de Voz


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




{% hint style="warning" %}
Este recurso está suspenso porque o desenvolvedor relevante não continuou a manter o PR.
{% endhint %}

Manual de Uso da Funcionalidade de Voz do Cherry Studio

1.  Visão Geral da Funcionalidade de Voz

O Cherry Studio oferece três módulos principais de funcionalidade de voz: TTS (Texto para Voz), ASR (Reconhecimento de Voz) e chamada de voz. Esses recursos permitem que você interaja naturalmente com a IA através da voz, melhorando sua experiência de uso.

- TTS (Texto para Voz): Converte as respostas de texto da IA em saída de voz
- ASR (Reconhecimento de Voz): Converte sua voz em entrada de texto
- Chamada de voz: Combina TTS e ASR para proporcionar uma experiência de diálogo semelhante ao ChatGPT

2.  Funcionalidade TTS (Texto para Voz)

1.  Tipos de Serviços Suportados

O Cherry Studio suporta quatro tipos de serviço TTS:

- OpenAI: Utiliza a API TTS da OpenAI, requer chave de API
- Navegador TTS: Usa a síntese de voz integrada do navegador, gratuito sem configuração
- Siliconflow: Utiliza o serviço TTS do Siliconflow, requer chave de API
- TTS Online Gratuito: Usa serviços TTS online gratuitos, sem necessidade de chave de API

2.  Método de Configuração

1) Acesse a página de configurações e selecione a aba "Funcionalidade de Voz"
2) Na sub-aba "TTS":
   - Ative a funcionalidade TTS (ligue o interruptor)
   - Selecione o tipo de serviço TTS
   - Configure os parâmetros conforme o serviço selecionado:
     - OpenAI: Preencha a chave de API, endereço da API, selecione voz e modelo
     - Navegador TTS: Selecione a voz
     - Siliconflow: Preencha chave de API, endereço da API, selecione voz, modelo, formato de resposta e velocidade de fala
     - TTS Online Gratuito: Selecione voz e formato de saída
3) Configure opções de filtro TTS (opcional):
   - Filtrar processos de pensamento
   - Filtrar marcadores Markdown
   - Filtrar blocos de código
4) Defina se deseja exibir a barra de progresso do TTS
5) Clique no botão "Testar TTS" para verificar a configuração

3.  Método de Uso

- Ao ativar o TTS, as respostas da IA serão automaticamente convertidas em voz
- Na interface de chat, cada resposta da IA exibirá um botão de reprodução TTS
- Clique para reproduzir/pausar a voz
- Se a barra de progresso estiver ativada, será exibida sob o texto
- Textos longos serão sintetizados e reproduzidos em sequência

3.  Funcionalidade ASR (Reconhecimento de Voz)

1.  Tipos de Serviços Suportados

O Cherry Studio suporta três tipos de serviço ASR:

- OpenAI: Utiliza o modelo Whisper da OpenAI, requer chave de API
- Navegador: Usa o recurso de reconhecimento de voz integrado do navegador, gratuito sem configuração
- Servidor Local: Conecta-se a um servidor WebSocket local para reconhecimento de voz

2.  Método de Configuração

1) Acesse a página de configurações e selecione a aba "Funcionalidade de Voz"
2) Na sub-aba "ASR":
   - Ative a funcionalidade ASR (ligue o interruptor)
   - Selecione o tipo de serviço ASR
   - Configure os parâmetros conforme o serviço selecionado:
     - OpenAI: Preencha chave de API, endereço da API, selecione modelo
     - Navegador: Sem configuração adicional necessária
     - Servidor Local: Defina se o servidor ASR será iniciado automaticamente
   - Selecione o idioma para reconhecimento de voz (padrão: chinês)
3) Clique no botão "Testar ASR" para verificar a configuração

3.  Método de Uso

- Ao ativar o ASR, aparecerá um botão de reconhecimento próximo ao campo de entrada
- Clique para iniciar a gravação
- Após falar, sua voz será convertida em texto no campo
- Clique novamente para encerrar a gravação
- Suporta múltiplas frases consecutivas em modo cumulativo

4.  Funcionalidade de Chamada de Voz

1.  Características Principais

- Combina TTS e ASR para diálogos semelhantes ao ChatGPT
- Interface em janela flutuante arrastável
- Modo "segurar para falar"
- Suporte a atalhos personalizáveis
- Possibilidade de recolher a janela
- Seleção de modelo específico para chamadas
- Suporte a prompts personalizados

2.  Método de Configuração

1) Acesse a página de configurações e selecione a aba "Funcionalidade de Voz"
2) Na sub-aba "Funcionalidade de Chamada":
   - Ative as chamadas de voz (ligue o interruptor)
   - Clique em "Selecionar Modelo" para escolher o modelo de IA
   - Personalize o prompt de chamada (opcional)
   - Salve ou redefina o prompt

3.  Método de Uso

1) Na interface de chat, clique no ícone de telefone
2) A janela de chamada abrirá com voz de boas-vindas
3) Segure o botão "Segurar para Falar" para gravar (ou use atalho)
4) Solte para enviar a gravação à IA
5) A resposta da IA será convertida para voz
6) Use os controles:
   - Mudo/Ativar som
   - Pausar/Continuar
   - Configurações (atalhos)
   - Recolher
7) Clique em fechar para encerrar

4.  Configuração de Atalhos

1) Na janela de chamada, clique no botão de configurações
2) No painel, clique em "Atalhos"
3) Pressione a tecla desejada (espaço, Shift etc.)
4) Salve as configurações
5) Para usar: segure a tecla para gravar, solte para enviar

5.  Problemas Comuns e Soluções

1. Problemas com TTS

- Problema: Sem áudio
  Solução: Verifique TTS ativado, serviço e parâmetros corretos

- Problema: Baixa qualidade
  Solução: Altere serviço ou configurações de voz

- Problema: Erros de exibição
  Solução: Verifique chave de API e conexão

2. Problemas com ASR

- Problema: Sem reconhecimento
  Solução: Confira ASR ativado e configurações

- Problema: Baixa precisão
  Solução: Experimente serviços diferentes ou ajuste microfone

- Problema: Falha na conexão
  Solução: Verifique servidor local e reinicie o app

3. Problemas com Chamadas

- Problema: Janela não abre
  Solução: Verifique recursos TTS/ASR ativados

- Problema: Botão não responde
  Solução: Confira permissões de microfone

- Problema: Sem saída de voz
  Solução: Verifique se o TTS está ativado e não silenciado

6.  Configurações Avançadas

1. TTS Avançado

- Filtros: Processos de pensamento/Markdown/blocos de código
- Barra de progresso
- Personalização de vozes/modelos

2. ASR Avançado

- Início automático do servidor
- Seleção de idioma

3. Chamadas Avançadas

- Prompts personalizados
- Modelos dedicados
- Atalhos personalizáveis

7.  Recomendações de Uso

1. Escolha de serviço TTS:
   - Alta qualidade: OpenAI ou Siliconflow
   - Sem configuração: Navegador ou TTS gratuito

2. Escolha de serviço ASR:
   - Alta precisão: OpenAI
   - Sem configuração: Navegador

3. Otimização de chamadas:
   - Use fones para evitar interferência
   - Ambientes silenciosos melhoram a precisão
   - Prompts personalizados melhoram respostas

4. Configurações conforme necessidade:
   - Só TTS para interações com texto
   - Só ASR para entrada por voz
   - Chamadas completas para diálogo automático

Esperamos que este manual ajude você a aproveitar ao máximo os recursos de voz do Cherry Studio para uma experiência de IA mais natural e intuitiva!