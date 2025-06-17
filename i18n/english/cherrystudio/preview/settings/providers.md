---
icon: cloud-check
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Provider Settings

This page only introduces the interface functions. For configuration tutorials, please refer to the [Provider Configuration](../../../pre-basic/providers/) tutorial in the basic tutorials.

{% hint style="info" %}
*   When using built-in providers, you only need to fill in the corresponding key.
*   Different providers may have different names for the key. Secret, Key, API Key, Token, etc., all refer to the same thing.
{% endhint %}

### API Key

In Cherry Studio, a single provider supports using multiple keys in a round-robin fashion. The rotation method is a list loop from front to back.

*   Add multiple keys separated by English commas. For example:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
You must use **English** commas.
{% endhint %}

### API Address

When using built-in providers, you generally do not need to fill in the API address. If you need to modify it, please strictly follow the address provided in the corresponding official documentation.

> If the address provided by the provider is in the format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, you only need to fill in the base URL part (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio will automatically append the remaining path (<mark style="background-color:green;">/v1/chat/completions</mark>). Failure to fill it in as required may result in it not working correctly.

{% hint style="info" %}
Note: The large language model routes for most providers are standardized, so the following operations are generally not necessary. If the provider's API path is v2, v3/chat/completions, or another version, you can manually enter the corresponding version in the address field, ending with a `/`. When the provider's request route is not the standard <mark style="background-color:green;">/v1/chat/completions</mark>, use the complete address provided by the provider and end it with a `#`.

That is:

*   If the API address ends with `/`, only "<mark style="background-color:green;">chat/completions</mark>" will be appended.
*   If the API address ends with `#`, no appending operation is performed; only the entered address will be used.

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Add Models

Usually, clicking the `Manage` button at the bottom left of the provider configuration page will automatically fetch all models supported by that provider. Click the `+` sign from the fetched list to add them to the model list.

{% hint style="info" %}
When you click the manage button, not all models in the pop-up list will be added. You need to click the `+` to the right of a model to add it to the provider's model list on the configuration page for it to appear in the model selection list.
{% endhint %}

### Connectivity Check

Click the check button after the API Key input box to test if the configuration is successful.

{% hint style="info" %}
The model check uses the last chat model from the added model list by default. If the check fails, please verify that there are no incorrect or unsupported models in the model list.
{% endhint %}

{% hint style="danger" %}
After successful configuration, be sure to turn on the switch in the upper right corner. Otherwise, the provider will remain disabled, and you will not be able to find the corresponding models in the model list.
{% endhint %}