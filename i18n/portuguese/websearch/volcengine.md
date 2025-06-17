---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Integração do Volc Engine para Acesso à Internet

### 1. Acesse/Registre uma conta no **Volc Engine** <a href="#rclz7" id="rclz7"></a>

Visite o site oficial: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Site oficial do Volc Engine</p></figcaption></figure>

### 2. Crie um **"Meu Aplicativo" com acesso à internet** <a href="#gvzaa" id="gvzaa"></a>

2.1. Faça login no Volc Engine e acesse a página **"Arca Vulcânica"**: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Clique sequencialmente:** <mark style="color:red;">**"Meus Aplicativos" → "Criar Aplicativo" → "Zero Code" → "Chat Individual"**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Preencha as informações e publique o aplicativo <a href="#zzdfe" id="zzdfe"></a>

**Nome do aplicativo**: Qualquer nome conforme os requisitos. (Campos com <mark style="color:red;">**\* são obrigatórios**</mark>, outros podem ficar em branco)

<mark style="color:red;">**Chave: Ative o plugin de internet (prévia ativação necessária)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Ative a função de plugin de internet (note custos e limites gratuitos) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Clique em "Comprar Agora" e siga os passos até ver a tela abaixo, indicando ativação bem-sucedida.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Verifique o status - ativação concluída</p></figcaption></figure>

Retorne à interface de "Preencher Informações do Aplicativo" para continuar.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Configurações avançadas de "Pesquisa na Internet" <a href="#sp6uz" id="sp6uz"></a>

Recomendações pessoais:
* Para controle preciso de entrada/saída: use **"Chamada Personalizada"**;
* Para simplicidade: **"Chamada Automática"** (valor padrão);
* Prioridade máxima de atualização: **"Forçar Ativação"** (requer verificação de custos).

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Publique o aplicativo <a href="#fe1gf" id="fe1gf"></a>

Clique em **"Publicar"** no canto superior direito para concluir a criação.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Obtenha a API Key <a href="#jtqlu" id="jtqlu"></a>

Siga: **"Guia de Chamada de API" → "Selecionar e copiar API Key" → "Visualizar e selecionar"**

Copie a API Key e cole no Cherry Studio. (Detalhes abaixo)

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Caso não haja API Key: **"Criar API Key"** → Copiar a chave gerada.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Use a API Key no Cherry Studio para acesso à internet via DeepSeek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1. Acesse Cherry Studio → **"Configurações"** → "Nome livre" → **"Tipo: OpenAI"** <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Configure URL e Key <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Nota: Se não encontrar o endereço ou usar nó fora de Pequim, consulte o local exato aqui (não esqueça "/"):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Adicione o nome do modelo <a href="#qmh3i" id="qmh3i"></a>

**Copie o nome do modelo** indicado em texto pequeno para evitar erros.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Visualização do resultado <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>