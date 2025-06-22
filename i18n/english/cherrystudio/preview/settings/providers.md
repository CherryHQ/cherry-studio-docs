---
icon: cloud-check
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Provider Settings

This page only introduces the interface features. For configuration tutorials, please refer to the [Provider Configuration](../../../pre-basic/providers/) tutorial in the Basic Tutorials.

{% hint style="info" %}
* When using built-in providers, only fill in the corresponding key.
* Different providers may have different names for the key, such as Secret Key, Key, API Key, Token, etc., all referring to the same thing.
{% endhint %}

### API Key

In Cherry Studio, a single provider supports multiple keys for round-robin usage, with the polling method being sequential from front to back.

* Add multiple keys separated by English commas. For example:
```markdown
sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
```

{% hint style="warning" %}
Must use **English** commas.
{% endhint %}

### API Address

When using built-in providers, it's generally not necessary to fill in the API address. If modification is needed, strictly follow the address provided in the official documentation.

> If the provider gives an address in the format <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, only fill in the root address part (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
> 
> Cherry Studio will automatically append the remaining path (<mark style="background-color:green;">/v1/chat/completions</mark>). Failure to comply may result in failure to function properly.

{% hint style="info" %}
Note: Most providers have a unified routing for large language models, so the following operations are generally unnecessary. If the provider's API path is v2, v3/chat/completions or other versions, manually enter the corresponding version ending with '`/`'. When the provider's request route is not the conventional <mark style="background-color:green;">/v1/chat/completions</mark>, use the full address provided by the provider and end it with `#`.

That is:
* When the API address ends with `/`, only "<mark style="background-color:green;">chat/completions</mark>" will be appended
* When the API address ends with `#`, no appending will be performed, only the filled-in address will be used

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Adding Models

Generally, clicking the `Manage` button at the bottom left of the provider configuration page will automatically fetch all supported models. Click `+` in the fetched list to add models to the model list.

{% hint style="info" %}
Models in the popup list won't be automatically added. You must click `+` next to the model to add it to the provider configuration's model list before it appears in the model selection list.
{% endhint %}

### Connectivity Check

Click the check button next to the API Key input box to test whether the configuration is successful.

{% hint style="info" %}
By default, the connectivity check uses the last conversation model in the added model list. If the check fails, please check if there are any incorrect or unsupported models in the model list.
{% endhint %}

{% hint style="danger" %}
After successful configuration, be sure to turn on the switch in the upper right corner. Otherwise the provider will remain disabled and you won't find corresponding models in the model list.
{% endhint %}