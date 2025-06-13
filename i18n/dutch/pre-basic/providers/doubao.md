
{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# ByteDance (Doubao)

* Meld u aan bij [Volcano Engine](https://console.volcengine.com/)
* Klik direct [hier om door te gaan](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### API-sleutel verkrijgen

* Klik op [API Key-beheer](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) in de zijbalk
* Maak een API-sleutel aan

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* Na succesvolle aanmaak, klik op het oog-icoon achter de API-sleutel om deze te tonen en kopieer

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* Plak de gekopieerde API-sleutel in CherryStudio en schakel de aanbieder in.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Modellen activeren en toevoegen

* Activeer benodigde modellen via [Activeringsbeheer](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) in de zijbalk. Activeer naar behoefte Doubao-modellen of DeepSeek.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* Zoek de bijbehorende **Model-ID** in het [modellijstdocument](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Voorbeeld Volcano Engine model-ID-lijst"><figcaption></figcaption></figure>

* Ga naar [Modelinstellingen](../../cherrystudio/preview/settings/providers.md) in Cherry Studio en selecteer Volcano Engine
* Klik op toevoegen en plak de Model-ID in het tekstveld

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* Voeg modellen een voor een op deze manier toe

### API-adres

Er zijn twee schrijfwijzen voor het API-adres:

* Standaard in client: `https://ark.cn-beijing.volces.com/api/v3/`
* Alternatief: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Beide notaties zijn functioneel gelijkwaardig. Het is aanbevolen de standaardinstelling te behouden.

Zie het gedeelte over API-adressen bij aanbiederinstellingen voor verschillen tussen `/` en `#` eindes: [klik hier](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Officiële cURL-voorbeeld</p></figcaption></figure>