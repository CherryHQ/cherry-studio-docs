---
icon: cloud-check
---
# Model Service Settings


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




This page only introduces the interface functions. For configuration tutorials, please refer to the [Provider Configuration](../../../pre-basic/providers/) tutorial in the basic tutorials.

{% hint style="info" %}
*   When using built-in service providers, you only need to fill in the corresponding secret key.
*   Different service providers may use different names for the secret key, such as Secret Key, Key, API Key, Token, etc., all refer to the same thing.
{% endhint %}

### API Key

In Cherry Studio, a single service provider supports multi-key round-robin usage, where the keys are rotated from first to last in a list.

*   Add multiple keys separated by English commas, as shown in the example below:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
You must use an **English** comma.
{% endhint %}

### API Address

When using built-in service providers, you generally do not need to fill in the API address. If you need to modify it, please strictly follow the address provided in the official documentation.

> If the address provided by the service provider is in the format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, you only need to fill in the root address part (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio will automatically concatenate the remaining path (<mark style="background-color:green;">/v1/chat/completions</mark>). Not filling it as required may lead to improper functionality.

{% hint style="info" %}
Note: The large language model routes for most service providers are consistent, so the following operations are generally not necessary. If the service provider's API path is v2, v3/chat/completions, or another version, you can manually enter the corresponding version ending with "/" in the address bar; when the service provider's request route is not the conventional <mark style="background-color:green;">/v1/chat/completions</mark>, use the complete address provided by the service provider and end it with "#".

That is:

*   When the API address ends with `/`, only "<mark style="background-color:green;">chat/completions</mark>" is concatenated.
*   When the API address ends with `#`, no concatenation operation is performed; only the entered address is used.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Add Model

Typically, clicking the `Manage` button in the bottom left corner of the service provider configuration page will automatically fetch all models supported by that service provider. You can then click the `+` sign from the fetched list to add them to the model list.

{% hint style="info" %}
Not all models in the pop-up list will be added when you click the `Manage` button. You need to click the `+` sign to the right of each model to add it to the model list on the service provider configuration page before it can appear in the model selection list.
{% endhint %}

### Connectivity Check

Click the check button next to the API Key input box to test if the configuration is successful.

{% hint style="info" %}
During the model check, the last conversation model added to the model list is used by default. If the check fails, please verify if there are any incorrect or unsupported models in the model list.
{% endhint %}

{% hint style="danger" %}
After successful configuration, make sure to turn on the switch in the upper right corner, otherwise, the service provider will remain disabled, and the corresponding models will not be found in the model list.
{% endhint %}