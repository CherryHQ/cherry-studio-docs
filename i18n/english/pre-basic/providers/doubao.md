# ByteDance (Doubao)


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




*   Log in to [Volcano Engine](https://console.volcengine.com/)
*   Click [here to go directly](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Obtain API Key

*   Click [API Key Management](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) at the bottom of the sidebar.
*   Create an API Key

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   After successful creation, click the eye icon next to the created API Key to view and copy it.

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Paste the copied API Key into CherryStudio, then enable the provider switch.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Activate and Add Models

*   In the Ark console, at the very bottom of the sidebar, navigate to [Open Management](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) to activate the models you want to use. Here, you can activate Doubao series and DeepSeek models as needed.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   In the [Model List Documentation](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), find the Model ID corresponding to the desired model.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Example of Volcano Engine Model ID column"><figcaption></figcaption></figure>

*   Open Cherry Studio's [Model Service](../../cherrystudio/preview/settings/providers.md) settings and find Volcano Engine.
*   Click "Add", then copy the previously obtained Model ID into the Model ID text box.

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Add models one by one following this process.

### API Address

There are two ways to write the API address:

*   The default client setting is: `https://ark.cn-beijing.volces.com/api/v3/`
*   The second way to write it is: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
There is no significant difference between the two forms. It is fine to keep the default and no modification is needed.

For the difference between `/` and `#` endings, please refer to the API Address section of the provider settings documentation, [click to go there](../../cherrystudio/preview/settings/providers.md#api-di-zhi).
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Official documentation cURL example</p></figcaption></figure>