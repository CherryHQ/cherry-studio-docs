---
icon: image
---

# Zhipu GLM-4.6V

Cherry Studio recognizes GLM-4.6V and its common variants from multiple providers. It identifies the standard version as a multimodal model that supports images, files, reasoning, and tool calling. The capabilities you can use ultimately depend on the APIs made available by the provider.

{% hint style="warning" %}
This page no longer promises that GLM-4.6V will always be a free trial model from CherryAI or CherryIN. Refer to the model selector, provider console, and actual request results to determine whether the model is free and still available.
{% endhint %}

## Check whether it is already available

1. Open the model selector on the Chats page;
2. Search for `GLM-4.6V`;
3. Confirm the model's provider and check its Vision, File, Reasoning, and Tool capability tags;
4. Select the model and upload an image that contains no sensitive information for testing.

Multiple providers may offer the same model, and its display name, model ID, and capability tags may differ.

## Connect through a provider

If GLM-4.6V does not appear in the model selector:

1. Open `Settings → Model Services`;
2. Select ZhiPu or an aggregation provider that offers the model for your account;
3. Enter the API Key and check the Base URL;
4. Select **Add** and apply the model changes shown in the sync preview;
5. Search for and enable GLM-4.6V;
6. Run a connection check or Model Health Check.

Cherry Studio's model registry recognizes GLM-4.6V identifiers used by multiple providers, but this does not guarantee that your account has access to the model.

## Choose the correct variant

A provider may offer standard, Flash, FP8, or other suffixed versions at the same time. They are separate models, and you should not assume that they have identical capabilities only because their names are similar.

- For image understanding, confirm that the model has the **Vision** or **Image Recognition** capability;
- To upload documents, confirm that the model has the **File Input** capability;
- To use MCP or other tools, confirm that the model has the **Tool Calling** capability;
- For text-only tasks, choose a suitable variant based on the provider's speed, quota, and pricing information.

{% hint style="danger" %}
Do not guess a model ID from this page. Copy the complete ID from the provider console or API documentation. An incorrect ID may return “model not found” or route requests to a different variant.
{% endhint %}

## Use images in a chat

1. Select a GLM-4.6V model with Vision capability;
2. Drag an image into the input area, paste an image, or select the attachment button to add one;
3. Describe the task in the same message, such as extracting a table, explaining a chart, or analyzing an interface;
4. Before sending, check whether the image contains an API Key, personal information, or other sensitive content.

If the input area does not allow you to add images, the current model is usually not recognized as a Vision model. Sync the model again or review its capabilities on the model editing page.

## Troubleshooting

### The uploaded image is not recognized

Confirm that you selected a GLM-4.6V variant with Vision support and that the provider endpoint accepts image input. An identical model name alone does not prove that API capabilities are the same.

### The model can chat but cannot call tools

Check the Tool capability tag, then test with a simple tool. The provider may not have enabled tool calling for this variant or may be using an incompatible API.

### GLM-4.6V does not appear in the synced list

Check the provider console to confirm that the model is available to your account. If the API does not return a model list, select **Custom** and enter the model ID supplied by the provider.

### The provider reports that a file or context is too large

Reduce the number or resolution of images, split long documents, and try again in a new topic. Exact limits depend on the provider and model variant.

For general free-trial rules, see [CherryAI (Free Trial)](../cherryin/README.md). For the provider setup process, see [Model Services](../README.md).
