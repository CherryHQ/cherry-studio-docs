
{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# ByteDance (Doubao)

* Faça login no [Volcano Engine](https://console.volcengine.com/)
* Clique diretamente [aqui para acessar](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Obter chave API

* Clique em [Gerenciamento de Chave API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) na barra lateral inferior
* Crie uma Chave API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* Após criar com sucesso, clique no ícone de olho 👁️ ao lado da Chave API e copie

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* Cole a Chave API copiada no CherryStudio e ative o interruptor do provedor.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Ativar e adicionar modelos

* Na barra lateral do Console Ark, acesse [Gerenciamento de Ativação](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) para ativar os modelos necessários. Você pode ativar conforme necessidade os modelos da série Doubao e DeepSeek.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* No [documento da lista de modelos](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), localize o **Model ID** correspondente ao modelo desejado.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Exemplo de lista de Model IDs do Volcano Engine"><figcaption></figcaption></figure>

* Acesse as configurações de [Serviço de Modelos](../../cherrystudio/preview/settings/providers.md) do Cherry Studio, encontre "Volcano Engine"
* Clique em adicionar e cole o **Model ID** obtido anteriormente na caixa de texto Model ID

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* Repita este processo para adicionar modelos sequencialmente

### Endereço da API

Existem duas formas de escrever o endereço da API:

* Primeira (padrão do cliente): `https://ark.cn-beijing.volces.com/api/v3/`
* Segunda: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Ambas as formas são equivalentes. Mantenha o padrão sem modificações.

Para diferenças entre terminações `/` e `#`, consulte a seção de endereço API nas configurações do provedor. [Clique para acessar](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Exemplo de cURL da documentação oficial</p></figcaption></figure>