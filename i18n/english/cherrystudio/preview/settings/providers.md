---
icon: cloud-check
---
# Model Service Settings


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




This page only introduces the interface functions. For configuration tutorials, please refer to the [Provider Configuration](../../../pre-basic/providers/) tutorial in the basic tutorials.

{% hint style="info" %}
* When using built-in service providers, you only need to fill in the corresponding secret key.
* Different service providers may use different names for the secret key, such as secret key, Key, API Key, Token, etc., but they all refer to the same thing.
{% endhint %}

### API Key

In Cherry Studio, a single service provider supports using multiple keys in a polling manner, where the polling method is a list loop from beginning to end.

* Multiple keys should be added separated by English commas. For example, as shown below:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Must use **English** commas.
{% endhint %}

### API Address

When using built-in service providers, you generally do not need to fill in the API address. If you need to modify it, please fill in the address strictly according to the official documentation.

> If the address provided by the service provider is in the format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, you only need to fill in the root address part (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio will automatically append the remaining path (<mark style="background-color:green;">/v1/chat/completions</mark>). Not filling it in as required may lead to abnormal usage.

{% hint style="info" %}
Note: The large language model routes of most service providers are unified, and generally, the following operations are not required. If the service provider's API path is `v2`, `v3/chat/completions`, or other versions, you can manually enter the corresponding version in the address bar ending with `/`; when the service provider's request route is not the standard <mark style="background-color:green;">/v1/chat/completions</mark>, use the complete address provided by the service provider and end it with `#`.

That is:

* When the API address ends with `/`, only "<mark style="background-color:green;">chat/completions</mark>" is appended.
* When the API address ends with `#`, no appending operation is performed, and only the entered address is used.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Add Model

Generally, clicking the `Manage` button in the bottom left corner of the service provider configuration page will automatically retrieve all callable models supported by that service provider. You can then click the `+` sign from the retrieved list to add them to the model list.

{% hint style="info" %}
When clicking the manage button, not all models in the pop-up list will be added automatically. You need to click the `+` on the right side of the model to add it to the model list on the service provider configuration page for it to appear in the model selection list.
{% endhint %}

### Connectivity Check

Click the check button next to the API Key input field to test if the configuration is successful.

{% hint style="info" %}
During model check, the last conversational model added to the model list is used by default. If the check fails, please check if there are any incorrect or unsupported models in the model list.
{% endhint %}

{% hint style="danger" %}
After successful configuration, make sure to turn on the switch in the upper right corner, otherwise the service provider will remain disabled, and the corresponding model will not be found in the model list.
{% endhint %}