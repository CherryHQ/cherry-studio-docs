
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

```markdown
---
icon: cherries
---

# PPIO 派欧云

## Cherry Studio integração com a API LLM da PPIO

### Visão Geral do Tutorial

Cherry Studio é um cliente de desktop multi-modelo, atualmente suportando pacotes de instalação para computadores Windows, Linux e MacOS. Ele agrega modelos LLM mainstream e fornece assistência para vários cenários. Os usuários podem melhorar sua eficiência de trabalho por meio de gerenciamento inteligente de sessões, personalização de código aberto e interface de múltiplos temas.

Cherry Studio agora está profundamente adaptado ao **canal de API de alto desempenho da PPIO** — garantindo poder computacional de nível empresarial, alcançando **resposta rápida do DeepSeek-R1/V3** e **99.9% de disponibilidade de serviço**, proporcionando uma experiência rápida e suave.

O tutorial abaixo inclui um plano de integração completo (incluindo configuração de chave), permitindo que você inicie o modo avançado de "Agendamento Inteligente do Cherry Studio + API de Alto Desempenho da PPIO" em 3 minutos.

### 1. Acesse o CherryStudio e adicione "PPIO" como provedor de modelos

Primeiro, acesse o site oficial para baixar o Cherry Studio: [https://cherry-ai.com/download](https://cherry-ai.com/download) (se não conseguir acessar, você pode abrir o link abaixo do Quark Netdisk para baixar a versão necessária: [https://pan.quark.cn/s/c8533a1ec63e#/list/share)

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(1) Primeiro, clique em **Configurações** no canto inferior esquerdo, defina o nome do provedor como: `PPIO`, e clique em "OK"

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

(2) Acesse o [Gerenciamento de Chaves de API da PPIO Computing Cloud](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), clique em **【Avatar do Usuário】—【Gerenciamento de Chaves de API】** para entrar no painel de controle

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

Clique no botão **【+ Criar】** para criar uma nova chave de API. Personalize um nome para a chave, **a chave gerada é exibida apenas no momento da geração, certifique-se de copiá-la e salvá-la em um documento para evitar afetar o uso posterior.**

(3) No CherryStudio, preencha a chave: clique em **Configurações**, selecione **【PPIO 派欧云】**, insira a chave de API gerada no site oficial e clique em **【Verificar】**

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Selecione o modelo: deepseek/deepseek-r1/community como exemplo. Se precisar mudar para outros modelos, você pode fazer isso diretamente.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

As versões DeepSeek R1 e V3 community são apenas para experimentação, são modelos de parâmetros completos e de alta performance, sem diferenças em estabilidade e eficácia. Se precisar de muitas chamadas, você deve **recarregar e mudar para a versão não community**.

### 2. Configuração de Uso do Modelo

(1) Clique em **【Verificar】** e, uma vez exibido o sucesso da conexão, você pode usar normalmente

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Por fim, clique em **【@】**, selecione o modelo **DeepSeek R1** adicionado recentemente sob o provedor PPIO, e você pode começar a conversar com sucesso~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Parte do material de origem: [Chen En](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### 3. Tutorial em Vídeo de Uso do PPIO×Cherry Studio

Se você prefere um aprendizado visual, preparamos um tutorial em vídeo no Bilibili. Com ensino passo a passo, ajudamos você a dominar rapidamente o método de configuração do "PPIO API+Cherry Studio". Clique no link abaixo para acessar diretamente o vídeo e iniciar uma experiência de desenvolvimento suave → [《【Ainda está frustrado com o DeepSeek carregando loucamente?】 PPIO + DeepSeek versão de alta performance =? Sem mais congestionamentos, decole imediatamente》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Fonte do material de vídeo: sola】
```