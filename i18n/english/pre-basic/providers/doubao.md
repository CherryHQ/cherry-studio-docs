
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# ByteDance (Doubao)

*   Log in to [Volcano Engine](https://console.volcengine.com/)
*   Click [here to go directly](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Get API Key

*   Click on [API Key Management](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) at the bottom of the sidebar.
*   Create an API Key.

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   After successful creation, click the eye icon next to the newly created API Key to reveal and copy it.

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Paste the copied API Key into CherryStudio, then turn on the provider switch.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Activate and Add Models

*   In the [Activation Management](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) at the bottom of the Ark console sidebar, activate the models you need. You can activate models like the Doubao series and DeepSeek as needed.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   In the [Model List Document](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), find the Model ID corresponding to the desired model.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Volcano Engine Model ID list example"><figcaption></figcaption></figure>

*   Open Cherry Studio's [Model Service](../../cherrystudio/preview/settings/providers.md) settings and find Volcano Engine.
*   Click Add, and paste the previously obtained Model ID into the Model ID text box.

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Follow this process to add models one by one.

### API Address

There are two ways to write the API address:

*   The first is the client default: `https://ark.cn-beijing.volces.com/api/v3/`
*   The second way is: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
There is no difference between the two formats. You can keep the default; no modification is needed.

For the difference between endings with `/` and `#`, refer to the API Address section in the provider settings documentation, [click here to go](../../cherrystudio/preview/settings/providers.md#api-di-zhi).
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Official documentation cURL example</p></figcaption></figure>