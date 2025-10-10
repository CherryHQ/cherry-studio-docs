# Infini-AI


{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}




Você já passou por isso: salvou 26 artigos úteis no WeChat mas nunca mais abriu, tem mais de 10 arquivos espalhados na pasta "Materiais de estudo" do computador, tenta encontrar uma teoria que leu há seis meses mas só lembra palavras-chave soltas. E quando o volume diário de informações excede o limite de processamento do cérebro, 90% do conhecimento precioso é esquecido em 72 horas.\
Agora, usando a API da plataforma de serviços de modelos de linguagem Infini-AI + Cherry Studio, você pode criar um banco de conhecimento pessoal para transformar artigos esquecidos do WeChat e conteúdos fragmentados de cursos em conhecimento estruturado, permitindo acesso preciso.\

### 1. Construção do Banco de Conhecimento Pessoal

#### 1. Serviço API Infini-AI: o "centro de pensamento" do banco de conhecimento, eficiente e estável

Como "centro de pensamento" do banco de conhecimento, a plataforma Infini-AI oferece versões como o DeepSeek R1 completo e serviços de API estáveis. **Atualmente, após o registro, o uso é gratuito sem restrições.** Suporta modelos de incorporação populares como bge e jina para construir bancos de conhecimento. **A plataforma também atualiza continuamente os serviços de modelos open-source mais recentes e poderosos**, incluindo múltiplos formatos como imagens, vídeos e áudio.

<figure><img src="../../.gitbook/assets/1280X1280 (1) (1).PNG" alt=""><figcaption></figcaption></figure>

#### 2. Cherry Studio: construa bancos de conhecimento sem código

Cherry Studio é uma ferramenta de IA fácil de usar. Comparado ao desenvolvimento tradicional de bancos de conhecimento RAG (que leva 1-2 meses), esta ferramenta oferece a vantagem de **operações sem código**. Permite importar com um clique formatos como Markdown/PDF/páginas web, analisando arquivos de 40MB em 1 minuto. Além disso, pode adicionar pastas locais, artigos salvos no WeChat e anotações de cursos.\

### 2. 3 passos para construir seu assistente de conhecimento personalizado

#### Passo 1: Preparação básica

1. Acesse o site do Cherry Studio para baixar a versão adequada (https://cherry-ai.com/)
2. Registre uma conta: faça login na plataforma Infini-AI (https://cloud.infini-ai.com/genstudio/model?cherrystudio)

<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

* Obtenha a chave da API: no "Model Square", selecione deepseek-r1, clique em criar e obtenha o APIKEY; copie o nome do modelo

<figure><img src="../../.gitbook/assets/output (1).png" alt=""><figcaption></figcaption></figure>

#### Passo 2: Abra as configurações do CherryStudio, selecione Infini-AI nos serviços de modelo, preencha a chave da API e ative o serviço de modelo Infini-AI

<figure><img src="../../.gitbook/assets/1280X1280 (2) (1).png" alt=""><figcaption></figcaption></figure>

Após completar estes passos, selecione o modelo necessário durante a interação para usar o serviço de API da Infini-AI no CherryStudio.\
Para facilitar o uso, você também pode definir um "modelo padrão"\

<figure><img src="../../.gitbook/assets/01445ab7-b863-4155-b517-2b6c3c581f47.png" alt=""><figcaption></figcaption></figure>

#### Passo 3: Adicione o banco de conhecimento

Selecione qualquer versão dos modelos de incorporação bge ou jina da plataforma Infini-AI

<figure><img src="../../.gitbook/assets/1 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/2 (2).png" alt=""><figcaption></figcaption></figure>

### 3. Teste real em cenário de usuário

* Após importar materiais de estudo, insira "Organize as derivações das fórmulas-chave do Capítulo 3 de *Machine Learning*"

<figure><img src="../../.gitbook/assets/6bbdbd0d-5db4-4440-b840-3bb3f422b831.gif" alt=""><figcaption></figcaption></figure>

**Resultado gerado anexado**

<figure><img src="../../.gitbook/assets/3.gif" alt=""><figcaption></figcaption></figure>