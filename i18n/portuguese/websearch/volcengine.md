---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Integração do Volcano Engine com Acesso à Internet

### 1. Acessar/Registrar uma conta do «Volcano Engine» <a href="#rclz7" id="rclz7"></a>

Visite o site oficial: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Site oficial do Volcano Engine</p></figcaption></figure>

### 2. Criar «Meu Aplicativo» com acesso à internet <a href="#gvzaa" id="gvzaa"></a>

2.1. Faça login no Volcano Engine e acesse a página «Volcano Ark»: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Clique sequencialmente em:** <mark style="color:red;">**«Meus Aplicativos» → «Criar Aplicativo» → «Sem Código» → «Bate-papo Individual»**</mark>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Preencher informações e publicar o aplicativo <a href="#zzdfe" id="zzdfe"></a>

**Nome do aplicativo**: Escolha qualquer nome conforme exigido. (Campos com <mark style="color:red;">**\* são obrigatórios**</mark>, outros são opcionais)

<mark style="color:red;">**Chave: Ative o plugin de internet (requer ativação prévia)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Ativar o recurso de plugin de internet (observe custos e uso gratuito) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Clique em "Comprar Agora" e siga até ver esta tela, indicando ativação bem-sucedida.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Verifique o status: ativação concluída</p></figcaption></figure>

Retorne à tela «Preencher Informações do Aplicativo» e continue.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Configurações avançadas de «Busca na Internet» <a href="#sp6uz" id="sp6uz"></a>

Escolha conforme sua necessidade:

* Para controle preciso de entrada/saída: use **«Chamada Personalizada»**;
* Para simplicidade: **«Chamada Automática»** (padrão);
* Se prioriza atualização em tempo real: **«Forçar Ativação»**.

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Publicar o aplicativo <a href="#fe1gf" id="fe1gf"></a>

Clique em **«Publicar»** no canto superior direito para finalizar.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Obter a API Key <a href="#jtqlu" id="jtqlu"></a>

Siga: **«Guia de Chamada de API» → «Selecionar e copiar API Key» → «Ver e Selecionar»**

Copie a API Key e cole-a posteriormente no cherry studio (veja detalhes abaixo).

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

**Nota**: Sem API Key? Clique em **«Criar API Key»** no canto superior direito do pop-up.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Usar a API Key no cherry studio para acesso à internet com deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1. Acesse cherry studio → «Configurações» → «Nome qualquer» → «Tipo: OpenAI» <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Configurar URL e Key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Dica: Se o endereço não for encontrado ou não for do nó de Pequim, verifique aqui (não esqueça "/"):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Adicionar nome do modelo <a href="#qmh3i" id="qmh3i"></a>

**Copie o nome do modelo indicado em texto pequeno**, caso contrário ocorrerá erro.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Visualização do resultado <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>