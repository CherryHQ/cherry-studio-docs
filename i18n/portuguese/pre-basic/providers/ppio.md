
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# PPIO PiO Cloud

## Cherry Studio integra a API LLM da PPIO

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)Visão Geral do Tutorial <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio é um cliente de desktop multi-modelo, atualmente compatível com pacotes de instalação para sistemas Windows, Linux e macOS. Ele agrega modelos LLM líderes, oferecendo assistência em diversos cenários. Os usuários podem melhorar sua eficiência através de gerenciamento inteligente de conversas, personalização de código aberto e interface multi-tema.

O Cherry Studio agora possui integração profunda com o **canal de API de alto desempenho da PPIO** — garantindo capacidade computacional corporativa para **resposta ultrarrápida do DeepSeek-R1/V3** e **99,9% de disponibilidade de serviço**, proporcionando uma experiência fluida e eficiente.

O tutorial abaixo contém o plano completo de integração (incluindo configuração de chaves), permitindo ativar o modo avançado de "Inteligência de Agendamento do Cherry Studio + API de Alto Desempenho da PPIO" em apenas 3 minutos.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Acesse o Cherry Studio e adicione "PPIO" como fornecedor de modelo <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Primeiro, faça o download do Cherry Studio no site oficial: [ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) (se não conseguir acessar, utilize o link alternativo do Quark Pan: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Clique em "Configurações" no canto inferior esquerdo, defina o nome do fornecedor como `PPIO` e clique em "Confirmar"

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Acesse [Gerenciamento de Chaves de API do PPIO Infra](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), clique no ícone do usuário → "Gerenciamento de Chaves de API" para entrar no painel de controle

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Clique no botão [+ Criar] para gerar uma nova chave de API. Defina um nome para a chave. **A chave gerada só será exibida uma vez — copie-a e salve-a para uso futuro**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) No Cherry Studio, insira a chave: vá para "Configurações", selecione [PPIO PiO Cloud], insira a chave de API gerada no site oficial e clique em [Verificar]

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Selecione o modelo: usando `deepseek/deepseek-r1/community` como exemplo. Se necessário, outros modelos podem ser alternados diretamente.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

As versões DeepSeek R1 e V3 community são para testes exploratórios com todos os parâmetros habilitados, sem diferenças em estabilidade ou desempenho. Para uso intensivo, **recarregue créditos e alterne para versões não-community**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. Configuração de Uso do Modelo <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) Após clicar em [Verificar] e confirmar a conexão bem-sucedida, o uso normal está habilitado

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Finalmente, clique em [@], selecione o modelo DeepSeek R1 adicionado sob o fornecedor PPIO e inicie a conversa!

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

[Parte do material fonte: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)]

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. Tutorial em Vídeo PPIO × Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Se preferir aprendizagem visual, preparamos um tutorial em vídeo no Bilibili. Com instruções passo a passo, você dominará rapidamente a configuração "API PPIO + Cherry Studio". Clique no link abaixo para acessar o vídeo e iniciar uma experiência de desenvolvimento fluida → [《[Frustrado com o DeepSeek travando?] PPIO Cloud + DeepSeek Full Power = Zero congestionamento, decolagem imediata》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

[Material de vídeo: sola]