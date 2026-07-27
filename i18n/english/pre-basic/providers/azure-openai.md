---
icon: cloud
---

# Azure OpenAI

Cherry Studio V2's built-in Azure OpenAI template connects to models deployed on Microsoft Azure. It selects either Azure Responses or deployment-based requests according to the **API Version**, so the Base URL, API Version, and model ID must match the configuration of your Azure resource.

{% hint style="info" %}
Azure OpenAI and the official OpenAI API are separate services. Do not enter an Azure resource's Endpoint, API Key, API Version, or deployment name in the OpenAI template.
{% endhint %}

## Before you begin

Prepare the following information in the [Azure Portal](https://portal.azure.com/):

- The Endpoint for your Azure AI Foundry or Azure OpenAI resource;
- The API Key for that resource;
- An API Version currently supported by the resource;
- At least one callable model deployment.

If you use a date-based API Version, you also need the **deployment name** of each model. You assign deployment names in Azure, and they may differ from the underlying model names.

## Configure Azure OpenAI

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**, then select **Azure OpenAI**;
3. Enter the Azure resource's API Key;
4. Enter the resource Endpoint as the Base URL, for example, `https://<resource>.openai.azure.com`;
5. Enter an API Version currently supported by the Azure resource;
6. Turn on the provider switch at the top of the page;
7. Add and enable the models you plan to use;
8. Run the connection check and model health check.

{% hint style="warning" %}
Enter only the resource Endpoint as the Base URL. Do not append `/openai`, `/v1`, `/chat/completions`, or a deployment path; Cherry Studio completes the request path based on the current configuration.
{% endhint %}

{% hint style="danger" %}
Do not include your Azure API Key in chat messages, documents, code repositories, or issue screenshots. If a key is exposed, regenerate it immediately in the Azure Portal.
{% endhint %}

## Choose an API Version

Cherry Studio selects the request method according to the API Version:

| API Version | How Cherry Studio handles it | Model configuration |
| --- | --- | --- |
| `v1` or `preview` | Uses Azure Responses | Configure the model route provided by the current Azure resource |
| A date-based version, such as `2024-xx-xx-preview` | Uses an Azure deployment URL | The model ID must match the deployment name in Azure |

The API Version must be one that your Azure resource actually supports. Examples in the interface only demonstrate the format and do not guarantee that the version works with your resource.

If an existing connection suddenly returns 404 after an upgrade, check the current Endpoint, API Version, and deployment name in the Azure Portal or the [Azure OpenAI documentation](https://learn.microsoft.com/azure/ai-services/openai/) before changing Cherry Studio.

## Add and enable models

Click **Add** in the model list, review the sync preview, and apply the changes. If Azure does not return a usable list, click **Custom** to enter models manually.

When using a date-based API Version:

- Enter the Azure deployment name as the **Model ID**;
- Do not enter only the underlying model family name unless it is also the deployment name;
- Add multiple deployments separately;
- If you delete or rename a deployment in Azure, update the model in Cherry Studio as well.

For example, if a model is deployed in Azure as `support-prod`, enter `support-prod` as the model ID in Cherry Studio instead of guessing from the underlying model name.

## Check the connection

1. Confirm that the Base URL does not include an API path;
2. Confirm that the API Key comes from the same Azure resource;
3. Confirm that the resource supports the API Version;
4. Select a model that has been added and enabled;
5. Run the connection check;
6. Run the model health check;
7. Return to the chat interface and send a simple message.

A successful connection check only confirms that the credentials and basic request work. If you plan to use images, reasoning, or tool calls, verify that the corresponding model and deployment support each capability.

## Manage multiple resources or deployments

If different Azure resources use different Endpoints, keys, or API Versions, duplicate the Azure OpenAI provider and configure each copy separately:

- Give each copy an easily recognizable name;
- Keep only the deployments that actually exist in that resource;
- Do not mix keys or deployment names from another resource into one copy;
- When upgrading the API Version, test one copy before updating the other connections.

This keeps production, testing, or regional resources isolated and makes quota and permission issues easier to identify.

## Troubleshooting

### Response code 401

The API Key is invalid or incomplete, or the key and Base URL do not belong to the same Azure resource. Verify them again on the resource's Keys and Endpoint page.

### Response code 404

Check the Base URL, API Version, and model deployment name in that order. Common causes include an extra path, an unsupported date-based version, or using the underlying model name instead of the deployment name.

### Response code 429

The current resource, region, or deployment has reached a rate or quota limit. Check quota and usage in the Azure Portal; changing the model name in Cherry Studio does not bypass resource limits.

### Models do not sync

Some Azure configurations do not return a model list that can be used directly. Click **Custom**, add models according to the actual deployments in Azure, and then run a health check.

### Should I choose `v1`, `preview`, or a date-based version?

Use a method currently supported by your Azure resource and the official documentation. `v1` or `preview` uses Responses, while a date-based version uses a deployment URL. Do not change the API Version based only on the model name.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
