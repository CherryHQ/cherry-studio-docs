---
icon: cloud-check
---
# Model Service Settings


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




This page only introduces the interface functions. For configuration tutorials, please refer to the [Provider Configuration](../../../pre-basic/providers/) tutorial in the basic tutorials.

{% hint style="info" %}
*   When using built-in providers, you only need to fill in the corresponding secret key.
*   Different providers may use different names for the secret key. Secret key, Key, API Key, Token, etc., all refer to the same thing.
{% endhint %}

### API Secret Key

In Cherry Studio, a single provider supports multiple keys used in a round-robin fashion, cycling through the list from first to last.

*   Multiple keys should be added separated by English commas. For example:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Must use **English** commas.
{% endhint %}

### API Address

When using built-in providers, you generally don't need to fill in the API address. If you need to modify it, please strictly follow the address provided in the official documentation.

> If the address provided by the provider is in the format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, you only need to fill in the root address part (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio will automatically append the remaining path (<mark style="background-color:green;">/v1/chat/completions</mark>). Not filling it in as required may lead to abnormal usage.

{% hint style="info" %}
Note: Most providers' large language model routes are unified, so generally the following operations are not necessary. If the provider's API path is v2, v3/chat/completions, or another version, you can manually enter the corresponding version in the address bar ending with "`/`"; when the provider's request route is not the standard <mark style="background-color:green;">/v1/chat/completions</mark>, use the complete address provided by the provider and end it with `#`.

That is:

*   When the API address ends with `/`, only "<mark style="background-color:green;">chat/completions</mark>" is appended.
*   When the API address ends with `#`, no concatenation operation is performed; only the entered address is used.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Add Model

Generally, clicking the `Manage` button in the bottom left corner of the provider configuration page will automatically fetch all models supported by that provider. You can then click the `+` sign from the fetched list to add them to the model list.

{% hint style="info" %}
Not all models in the pop-up list will be added when clicking the manage button. You need to click the `+` on the right side of the model to add it to the model list on the provider configuration page before it can appear in the model selection list.
{% endhint %}

### Connectivity Check

Click the check button next to the API Secret Key input box to test if the configuration is successful.

{% hint style="info" %}
During model checking, the last conversational model from the added model list is used by default. If the check fails, please verify if there are incorrect or unsupported models in the model list.
{% endhint %}

{% hint style="danger" %}
After successful configuration, be sure to turn on the switch in the upper right corner, otherwise the provider will remain disabled, and the corresponding models will not be found in the model list.
{% endhint %}