
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# ByteDance (Doubao)

* Log in to [Volcano Engine](https://console.volcengine.com/)
* Or click [here to go directly](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Obtaining the API Key

* Click [API Key Management](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) in the sidebar
* Create an API Key

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* After creation, click the eye icon next to the created API Key to reveal and copy it

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* Paste the copied API Key into Cherry Studio and then toggle the provider switch to ON

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Enabling and Adding Models

* Enable the models you need at the bottom of the sidebar in the Ark console under [Enablement Management](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false). You can enable the Doubao series, DeepSeek, and other models as required

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* In the [Model List Documentation](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), find the model ID corresponding to the desired model

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Volcano Engine Model ID List Example"><figcaption></figcaption></figure>

* Open Cherry Studio's [Model Services](../../cherrystudio/preview/settings/providers.md) settings and locate Volcano Engine
* Click Add, then paste the previously obtained model ID into the model ID text field

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* Follow this process to add models one by one

### API Address

There are two ways to write the API address:
* First, the default in the client: `https://ark.cn-beijing.volces.com/api/v3/`
* Second: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
There is no significant difference between the two formats; you can keep the default and no modification is needed.

For the difference between ending with `/` and `#`, refer to the API Address section in the provider settings documentation. [Click to go there](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Official Documentation cURL Example</p></figcaption></figure>