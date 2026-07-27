---
icon: gem
---

# Google Gemini

Cherry Studio V2's built-in Gemini template connects to Google's official Gemini API and uses the native **Google Generate Content** endpoint by default. After configuring an API Key, you can sync the Gemini models available to the current account.

{% hint style="info" %}
The Gemini API and Google Cloud Vertex AI are two different connection methods. This page uses an API Key created in Google AI Studio. If you use a Google Cloud project, region, and service account, see the Vertex AI documentation.
{% endhint %}

## Before you begin

- A Google account that can access Google AI Studio and the Gemini API;
- A location that meets Google's current [available region requirements](https://ai.google.dev/gemini-api/docs/available-regions);
- Acceptance of the relevant Gemini API terms;
- A working API Key and model quota.

Google AI Studio may automatically create a default Google Cloud project and API Key for new users. If you already have a project, you can also import or select it in AI Studio instead of creating another project just for Cherry Studio.

## Create an API Key

1. Open [Google AI Studio API Keys](https://aistudio.google.com/app/apikey);
2. Sign in and select the Google Cloud project you plan to use;
3. Create a new Gemini API Key;
4. Copy the key and save it immediately in a secure location;
5. Return to Cherry Studio to complete the configuration.

{% hint style="danger" %}
Do not include the API Key in chat messages, documents, code repositories, or issue screenshots. Google may block a key that has been publicly exposed or does not meet restriction requirements. If a key is exposed, delete it in AI Studio and create a new one.
{% endhint %}

## Configure Gemini

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**, then select **Gemini**;
3. Enter the API Key created in Google AI Studio;
4. Keep the default Base URL `https://generativelanguage.googleapis.com`;
5. Turn on the provider switch at the top of the page;
6. Click **Add** in the model list, review the sync preview, and apply the changes;
7. Enable the models you plan to use.

The built-in Gemini template uses Google's native endpoint. Do not change the official Gemini API to OpenAI Chat Completions or OpenAI Responses.

## Sync and select models

After you click **Add**, Cherry Studio calls Gemini's model list endpoint and displays the remote results merged with its built-in model information.

- Enable only the models you actually need;
- Verify the complete model ID instead of relying only on the display name;
- Stable, Preview, Latest, and Experimental versions have different stability and life cycles;
- If the endpoint does not return the target model, click **Custom** and enter the model ID from Google's official documentation;
- A model appearing in the list does not guarantee that the current key has permission or remaining quota to call it.

Google continuously changes model versions. Refer to the [Gemini model documentation](https://ai.google.dev/gemini-api/docs/models/gemini) and the actual sync results instead of relying on a fixed list in an old screenshot.

## Check the connection

1. Run the connection check in the API Key section;
2. Select a synced and enabled text model;
3. Confirm that the check succeeds;
4. Run the health check in the model list;
5. Return to the chat interface and send a simple message.

If you plan to use image understanding, image generation, reasoning, or tool calls, test each function separately. Similar model names do not guarantee identical capabilities or request parameters.

## Reasoning and tool calls

Cherry Studio displays reasoning and tool capabilities according to the registered model information and converts thinking parameters for supported Gemini models. The following requirements still apply:

- The current model version supports the capability;
- The API Key has permission and quota for the model;
- The model capability labels match the actual endpoint;
- MCP or other tools are enabled;
- The request parameters do not exceed the model's limits.

If reasoning or tool calls stop working after a model upgrade, sync the models again, then troubleshoot with a simple chat and a single tool separately.

## Connect to a Gemini-compatible gateway

If you are not using Google's official Gemini API:

1. Create a [custom provider](zi-ding-yi-fu-wu-shang.md);
2. Set Google Generate Content as the primary endpoint;
3. Enter the Base URL and API Key supplied by the gateway;
4. Sync or manually add the models actually provided by the gateway;
5. Run the connection check and model health check.

Using a separate custom provider preserves the official Gemini template and prevents gateway paths or model IDs from being mixed into the official configuration.

## Troubleshooting

### Response code 400

The model does not support the current parameters, or the request exceeds its input limit. Test with a short text-only message first, then enable images, reasoning, and tools one at a time.

### Response code 401 or invalid API Key

The key is incomplete, deleted, or blocked. Check its status in Google AI Studio. If the key has been publicly exposed, create a new one.

### Response code 403

The account, project, region, or model permissions do not meet the requirements. Check the current key's project, the [available regions](https://ai.google.dev/gemini-api/docs/available-regions), and the Google account status.

### Response code 404 or model not found

Click **Add** again to sync models, then verify the complete model ID. A Preview, Latest, or Experimental model may have been renamed or discontinued.

### Response code 429

The current project or model has reached a rate or quota limit. Check usage and billing status in Google AI Studio, then try again later or choose a model with available quota.

### Models do not sync

Confirm that you are using a Gemini API Key created in Google AI Studio and that the official Base URL is unchanged. You can also use the official [models endpoint](https://ai.google.dev/api/models) to check whether the key can list models.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
