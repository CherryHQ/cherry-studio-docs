---
icon: bolt
---

# MiniMax

Cherry Studio V2 includes two built-in providers: **MiniMax CN** and **MiniMax**. Both connect to MiniMax language model endpoints, but they use different platforms, Base URLs, and API Keys.

This page explains how to use the MiniMax M series in Cherry Studio for chat, coding, and Agent tasks. MiniMax uses separate APIs for speech, image, video, and music generation; these are not the language model service described here.

{% hint style="info" %}
Select **MiniMax CN** for the mainland China platform and **MiniMax** for the international platform. Accounts, keys, balances, and subscriptions may be separate between the two platforms. Do not mix them.
{% endhint %}

## Before you begin

Prepare credentials for the platform where your account is registered:

| Platform | Cherry Studio provider | Default Base URL |
| --- | --- | --- |
| Mainland China | MiniMax CN | `https://api.minimaxi.com/v1/` |
| International | MiniMax | `https://api.minimax.io/v1/` |

- Users in mainland China can create an API Key on the [MiniMax Platform](https://platform.minimaxi.com/);
- International users can create an API Key on the [MiniMax API Platform](https://platform.minimax.io/);
- Confirm that the key has pay-as-you-go balance or a valid Token Plan;
- Review the currently available models, context, and rate limits.

Pay-as-you-go API Keys and Token Plan keys use different balances or quotas. If the connection works but returns a quota error, check the billing page associated with the platform where you created the key instead of looking only at the other account's balance.

## Configure MiniMax

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**;
3. Select **MiniMax CN** for a mainland China account or **MiniMax** for an international account;
4. Enter the API Key created on the corresponding platform;
5. Keep the built-in default Base URL;
6. Turn on the provider switch at the top of the page;
7. Click **Add** in the model list, review the sync preview, and apply the changes;
8. Enable only the models you plan to use.

{% hint style="danger" %}
Do not include the API Key in chat messages, documents, code repositories, or issue screenshots. If the key is exposed, delete it immediately on the corresponding MiniMax platform and create a new one.
{% endhint %}

Entering a key from the `.com` platform in the `.io` provider, or the reverse, usually returns unauthorized. First confirm that you selected the correct provider entry instead of overriding the built-in address.

## Select a model

Cherry Studio V2 currently includes the following primary models for both MiniMax providers:

| Model ID | Primary use |
| --- | --- |
| `MiniMax-M3` | Flagship multimodal coding and Agent model with an official 1M context |
| `MiniMax-M2.7` | Coding, tool calls, office work, and complex Agent workflows |
| `MiniMax-M2.7-highspeed` | Same family as M2.7, prioritizing lower output latency |

The synced list may also include M2.5, M2.1, or other models. Use the actual sync results and official MiniMax documentation for model IDs and life cycles instead of relying on the `abab` family names in older documentation.

- Try M3 first for general-purpose tasks;
- For mainly coding and tool calls, compare M3 with M2.7;
- Select `MiniMax-M2.7-highspeed` when output speed matters;
- For reproducible results, record the complete model ID instead of only the display name.

## OpenAI- and Anthropic-compatible endpoints

Both built-in providers include OpenAI Chat Completions- and Anthropic Messages-compatible addresses:

| Platform | OpenAI-compatible | Anthropic-compatible |
| --- | --- | --- |
| Mainland China | `https://api.minimaxi.com/v1/` | `https://api.minimaxi.com/anthropic` |
| International | `https://api.minimax.io/v1/` | `https://api.minimax.io/anthropic` |

Cherry Studio uses OpenAI Chat Completions by default. Keep the default for initial chat and model synchronization.

MiniMax officially recommends the Anthropic-compatible endpoint for thinking blocks and interleaved thinking. If you manually change a model's endpoint type in Cherry Studio, also confirm the following:

- The Base URL matches the account region;
- The model uses the Anthropic Messages protocol;
- The key comes from the same platform;
- Standard chat, thinking display, and tool calls all pass health checks again.

Do not change only the Base URL while keeping an incorrect protocol type. The message structures of the OpenAI- and Anthropic-compatible endpoints are not identical.

## Thinking content and multi-turn tool calls

MiniMax M-series models return reasoning content. Cherry Studio recognizes the M2 series as reasoning models. M3 is newer, so the current V2 version may not yet show every dedicated thinking control.

Recommendations:

- Keep the thinking setting at **Default**;
- Do not force disabled thinking or a custom budget on a fixed-thinking model;
- Use streaming output for long responses;
- Do not arbitrarily change Temperature, Top P, or penalty settings;
- After switching protocols, test again that thinking content displays correctly.

{% hint style="warning" %}
MiniMax multi-turn tool calls depend on the complete assistant message, including thinking content and `tool_calls`. Cherry Studio maintains the chat history. Do not manually delete or rewrite the previous message during tool execution, or the model may lose reasoning continuity.
{% endhint %}

If you see `<think>` tags when using the OpenAI-compatible endpoint, the provider is usually placing thinking content in `content`. Before switching to the Anthropic-compatible endpoint, test it in a separate provider copy to avoid affecting existing chats.

## Tool calls and MCP

Cherry Studio V2 recognizes tool-call capabilities for the MiniMax M2, M2.x, and M3 series, which can be used in MCP and Agent scenarios.

We recommend validating in this order:

1. Select a synced and enabled M3 or M2.7 model;
2. Complete a standard chat;
3. Enable one simple MCP tool;
4. Use a prompt that explicitly requires a tool call;
5. Confirm that the model actually makes the tool call;
6. Then add multiple tools or long-running tasks.

Preserve the complete context in long-running tasks. If the model repeatedly calls the same tool, reduce the number of tools, shorten the system prompt, and state a clear stopping condition.

## Images, videos, and files

MiniMax M3 officially supports text, image, and video input, but Cherry Studio V2's automatic vision-model detection rules may not yet include M3. Therefore:

- If image or video controls appear in the input box, run a health test with a small file first;
- If the controls do not appear, update Cherry Studio and sync the models again;
- Do not fake model capabilities by changing only the display name;
- If the current version still does not work, wait for the client adaptation.

Older M2 models on the MiniMax OpenAI- and Anthropic-compatible endpoints generally support only text and tool calls. Do not add MiniMax's separate image, video, or speech generation models as chat models.

For PDFs, Cherry Studio currently extracts text locally first and then sends the text to MiniMax:

- Text-based PDFs can usually be processed directly;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost during extraction;
- The extracted text consumes context and input usage.

## Multimodal generation models are not chat models

MiniMax also provides speech, image, video, and music generation APIs, but these endpoints have separate request formats and task workflows. A model appearing on the platform does not mean it can be called directly through a Cherry Studio chat provider.

For example, manually adding a video generation model to the chat model list usually produces a parameter or endpoint error. Use a dedicated Cherry Studio interface that supports the capability. Renaming a model cannot replace an integration that is not currently available.

## Knowledge bases and embedding models

The built-in MiniMax providers currently configure language model endpoints and do not provide embedding models. When using a knowledge base or [Global Memory](../../advanced-basic/memory.md):

- You can continue to use MiniMax as the chat model;
- Select the embedding model from another provider;
- The two model types do not need to come from the same provider;
- Run a model health check for each after configuration.

## Check the connection

1. Confirm that you selected the correct mainland China or international provider;
2. Run the connection check in the API Key section;
3. Select a synced and enabled model;
4. Run the health check in the model list;
5. Return to the chat interface and send a simple message;
6. Test long responses, thinking display, and MCP separately.

A successful connection check confirms only that the basic credentials work. It does not mean the key can access every model or that the Token Plan still has available quota.

## Troubleshooting

### Unauthorized or error code 1004

The API Key is invalid or deleted, or it does not match the `.com` / `.io` provider. Confirm the provider region and create a new key.

### Insufficient balance or error code 1008

Check the billing type and account where the current key was created. Pay-as-you-go balance and Token Plan quota must be reviewed separately.

### Rate limit, 1002, or 1041

The request has reached a rate or concurrency limit. Reduce concurrency, shorten the context, and try again later. If the issue persists, check the account tier and official limits.

### Token limit or error code 1039

The current chat, attachment text, and expected output exceed the model context. Start a new chat, reduce attachments, shorten the history, or select a model with a longer context.

### The model list still shows older models

Click **Add** again to sync the list and confirm that the Base URL was not changed incorrectly. If the remote list does not yet return a new model, use the built-in preset model or add its complete official ID manually.

### M3 has no thinking or image controls

M3's official capabilities are newer than Cherry Studio's current automatic detection rules. Update the client and sync again first. If the controls still do not appear, do not override the model type; wait for the client adaptation.

### MCP calls are interrupted or the context is inconsistent

Enable only one tool first and confirm that you are using M3 or M2.7. Do not delete the assistant message immediately before the tool call. Start a new chat and test again if necessary.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For model capabilities, see [MiniMax Models](https://platform.minimax.io/docs/guides/models-intro); for feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
