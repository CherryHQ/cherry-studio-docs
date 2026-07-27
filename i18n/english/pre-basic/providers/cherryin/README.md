---
icon: gift
---

# CherryAI (Free Trial)

CherryAI is a cloud trial service built into Cherry Studio. It is enabled automatically with the app and does not require you to enter an API Key first, making it suitable for quickly trying Chats and model selection after installation.

{% hint style="info" %}
CherryAI is an in-app trial service. [CherryIN](../cherryin-1.md) is a model provider that accepts a configured API Key. Their names are similar, but their entry points, quotas, and setup methods differ.
{% endhint %}

## Start using it

1. Open the [Chats page](../../../cherrystudio/preview/chat.md);
2. Select the model name in the input area or Assistant title bar to open the model selector;
3. Search for `CherryAI`, or use the **Free** tag to filter available trial models;
4. Select a model and send a message.

CherryAI models display a trial-service indicator in the model selector. Available models may change with the app version and service status, so refer to the current list in the app.

## Why CherryAI does not appear under Model Services

This is expected. V2 adds CherryAI as an available model source but deliberately hides it from the regular provider list under `Settings → Model Services`. Users also cannot change its API Key or Base URL.

For stable use of your own account and quota, follow the steps under [Model Services](../README.md) to configure CherryIN, an official model API, a local model, or another gateway.

## Free quota

CherryAI requests use trial quota. When the quota is exhausted, the app displays a corresponding notice. You can:

- Wait for the trial quota to recover;
- Switch to another configured and enabled model;
- Follow the notice to configure your own API Key with the corresponding provider.

{% hint style="warning" %}
Free quota, recovery times, and available models may change. This page does not promise a fixed quota, and the trial service is not recommended for production tasks, long-running automation, or use as your only available model.
{% endhint %}

## Usage limitations

- **No setup does not mean offline operation**: Messages are still sent to the CherryAI cloud API;
- **Model capabilities vary**: Refer to model tags and actual responses for capabilities such as vision, reasoning, web access, and tool calling;
- **The provider page is not editable**: Seeing CherryAI in the model selector but not in Model Services settings is expected behavior;
- **Trial models may change**: If a model saved to an Assistant is removed, reopen the model selector and choose a replacement.

## Use it with your own models

You can first use CherryAI for your initial trial, then configure your own provider. After configuration:

1. Enable the target provider and model on the Model Services page;
2. Return to the model selector and choose the new model;
3. As needed, select default, quick, translation, or topic-naming models under [Default Model settings](../../../cherrystudio/preview/settings/default-models.md).

This lets you switch directly to your own model even when trial quota is temporarily unavailable.

If CherryAI does not appear in the model selector or requests fail for every trial model, first check your network and restart the app. If the issue persists, submit the Cherry Studio version, operating system, and sanitized error details. See [Feedback and Suggestions](../../../question-contact/suggestions.md) for contact options.
