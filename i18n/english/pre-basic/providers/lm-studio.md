# LM Studio

LM Studio lets you download and run local models on macOS, Windows, and Linux. It can provide Cherry Studio with chat, vision, tool-calling, and embedding capabilities through an OpenAI-compatible API.

Cherry Studio V2 includes a built-in LM Studio provider that connects to `http://localhost:1234` by default. Standard chats use the OpenAI-compatible API, and the model list comes from `/v1/models`.

{% hint style="info" %}
Model synchronization in Cherry Studio only reads the models currently visible to LM Studio. It does not download models for you. Download a model from the **Discover** page in LM Studio before starting the local API Server.
{% endhint %}

## Prepare LM Studio

1. Download and install the latest version from the [LM Studio website](https://lmstudio.ai/);
2. Open **Discover**, then search for and download a model;
3. Choose a parameter size and quantization that fit your system memory or VRAM;
4. Open the **Developer** page;
5. Click **Start server** to start the API Server.

The default listening address is:

```text
http://localhost:1234
```

You can also start it from a terminal:

```bash
lms server start
```

For first-time use, load the model and complete one chat in LM Studio to confirm that the model can run before connecting it to Cherry Studio.

## Choose a Model and Quantization

The model file, quantization method, and context length all affect memory usage and speed.

- Larger parameter counts generally provide stronger capabilities but require more RAM or VRAM;
- GGUF models can use a mix of CPU and GPU inference;
- Apple Silicon devices can use compatible MLX models;
- Lower-bit quantization uses less memory but may reduce output quality;
- Longer contexts require more KV Cache memory;
- Vision models must also process image encodings and usually use more memory than text-only models of a similar size.

If you are unsure, start with a small or medium model and a common quantization that your device can load reliably. Increase the parameter count or context length gradually.

The LM Studio CLI can also estimate resource usage:

```bash
lms load --estimate-only <model-key>
```

## Configure Cherry Studio

1. Open `Settings → Model Providers`;
2. Switch the filter on the left to **All Providers**;
3. Select **LM Studio**;
4. Keep the Base URL as `http://localhost:1234`;
5. Leave the API Key empty if authentication is not enabled in LM Studio;
6. Turn on the provider switch at the top of the page;
7. Click **Add** or synchronize models;
8. Review the synchronization preview and apply the changes;
9. Enable only the models you plan to use;
10. Run a model health check before testing it in a chat.

Enter only the host and port in the Base URL; you do not need to append `/v1` manually. Cherry Studio accesses the model list and chat endpoints through the OpenAI-compatible API.

## Why the Model List Changes

LM Studio's `/v1/models` endpoint returns the models currently visible to the server:

| LM Studio setting | Model list behavior |
| --- | --- |
| Just-In-Time Model Loading enabled | Can return all downloaded models and load one automatically on its first request |
| Just-In-Time Model Loading disabled | Usually returns only models that are already loaded in memory |

For this reason, the statement in older tutorials that you must manually load a model before synchronizing no longer applies to every version.

If the model list in Cherry Studio is empty:

1. Confirm that the API Server is running;
2. Open `http://localhost:1234/v1/models` in a browser or terminal;
3. Check whether JIT Loading is enabled in LM Studio;
4. If JIT is disabled, load the model in LM Studio first;
5. Return to Cherry Studio and synchronize again.

{% hint style="warning" %}
Successful model synchronization does not guarantee that your device can load the model. When JIT is enabled, unloaded models may still appear in the list. The first chat triggers loading and may reveal insufficient memory, an excessive context length, or other problems.
{% endhint %}

## API Tokens and Authentication

LM Studio does not require an API Token by default. For local use, you can leave the API Key empty in Cherry Studio.

LM Studio 0.4.0 and later can enable **Require Authentication** under `Developer → Server Settings`:

1. Open **Manage Tokens**;
2. Create a Token and configure its permissions;
3. Copy the new Token;
4. Enter the Token in the LM Studio provider settings in Cherry Studio;
5. Synchronize models again and run a health check.

Cherry Studio sends a non-empty API Key as a Bearer Token. LM Studio also supports authentication headers commonly used by OpenAI- and Anthropic-compatible APIs.

{% hint style="danger" %}
An API Token is displayed in full only when it is created. Do not put a Token in chats, documents, code repositories, or troubleshooting screenshots. Delete and replace it immediately if it is exposed.
{% endhint %}

## Chat, Vision, and MCP

### Standard Chat

Select an instruction model that supports Chat Completions. After basic chat works, test reasoning, images, or tool calls.

The quality of a local model's answers depends on the model, quantization, prompt template, and context settings. Successfully returning content only confirms that the API works; it does not mean the model is suitable for every task.

### Vision

LM Studio's OpenAI-compatible Chat Completions API supports text and images, but the selected model must have vision capabilities.

1. Download a version explicitly marked as a vision model;
2. Load it in LM Studio or allow JIT to load it;
3. Synchronize it to Cherry Studio;
4. Confirm that the model shows image support;
5. Start by sending one small image as a test.

Similar model names do not mean that every quantization or variant supports images. If Cherry Studio does not detect vision support, check the model ID and runtime support first. Do not change only the display name.

### Tool Calling and MCP

Cherry Studio MCP requires a model to produce structured Tool Calling output. LM Studio provides native or compatible modes based on the model template, but actual reliability still depends on the model.

Test in this order:

1. Complete a standard chat first;
2. Enable only one simple MCP tool;
3. Explicitly ask the model to call that tool;
4. Check whether it produces a structured call;
5. Confirm that the tool result is returned to the model;
6. Add more tools gradually.

Small models may only output text saying that they are about to call a tool without making an actual call. If this happens, prefer a model marked with native Tool Use, a larger parameter count, or more extensive tool training.

Cherry Studio MCP and LM Studio's own MCP integration are separate paths. If you only use Cherry Studio MCP, you do not need to configure the same tool again in LM Studio.

## Reasoning Models and Structured Output

Whether LM Studio can process reasoning parameters or structured output depends on the model template and its OpenAI-compatible implementation.

- Prefer models and templates that LM Studio explicitly supports;
- Reasoning switches and effort parameters are not interchangeable across models;
- If enabling reasoning causes a parameter error, restore the default or turn reasoning off;
- If JSON or structured output fails, test the same model in LM Studio first;
- Do not change a model's display name to imitate another capability.

## Model Loading, JIT, and VRAM

With JIT Loading enabled, LM Studio can automatically load a model into memory or VRAM when Cherry Studio calls it for the first time. The first response will be noticeably slower than later requests.

LM Studio 0.4+ also provides:

- **Idle TTL**: how long an idle model remains loaded before it is unloaded automatically;
- **Auto-Evict**: automatically unload a model previously loaded by JIT before loading a new one;
- **Only Keep Last JIT Loaded Model**: keep only the most recently used JIT model loaded.

The LM Studio provider page in Cherry Studio also shows **Keep Alive Time**. Whether and when memory is released also depends on LM Studio's JIT, TTL, Auto-Evict, and manual loading state. When troubleshooting, use LM Studio's loaded model list and server settings as the source of truth.

For manual control, use:

```bash
lms load <model-key> --context-length 8192 --gpu max
lms unload <model-key>
lms unload --all
```

Do not load several large models that are each close to your device's limit. When switching models frequently, enabling Auto-Evict is usually more stable than keeping models loaded continuously.

## Context Length

A model's maximum supported context and the context actually loaded are not the same. The Context Length configured when LM Studio loads a model determines the range available to that running instance.

An excessive context length may cause:

- Insufficient RAM or VRAM;
- Longer initial load times;
- Slower prompt processing;
- Truncated requests or limit errors;
- More failures in vision and long-document tasks.

If Cherry Studio's model information shows a larger value than the context actually loaded in LM Studio, follow the LM Studio runtime configuration. Start with a shorter context to confirm stability, then increase it as needed.

## Knowledge Bases and Embedding Models

LM Studio provides an OpenAI-compatible `/v1/embeddings` endpoint that can run dedicated embedding models.

1. Download an embedding model;
2. Load it in LM Studio or allow JIT to load it;
3. Synchronize the model in Cherry Studio;
4. Confirm that it is recognized as an embedding model;
5. Select it in a knowledge base and detect its dimensions;
6. Run a health check before importing documents.

LM Studio does not support reranking models in Cherry Studio. Choose another provider if you need Rerank.

Do not casually change the embedding model or dimensions after using them in an existing knowledge base. Doing so usually requires rebuilding the vector index.

## PDFs and Attachments

V2 does not currently send the original PDF file directly to LM Studio. Cherry Studio extracts the PDF text locally before sending it to the model:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes context;
- Images in a PDF must be sent separately to a vision model.

## Code Tools and the Anthropic-Compatible API

Cherry Studio's LM Studio preset also retains an Anthropic-compatible address for certain Code Tools. Its default is still `http://localhost:1234`.

LM Studio provides `/v1/messages`. If a Code Tool requires an Anthropic-compatible service:

1. Confirm that you are using a recent version of LM Studio;
2. Start the API Server;
3. Confirm that the target model supports the required tool capabilities;
4. Enter the same Token if authentication is enabled;
5. Use the actual model identifier from LM Studio;
6. Test with a simple task before granting file or command permissions.

Support for the Messages API does not mean every local model can reliably complete coding-agent tasks. Model capabilities, context, tool-calling quality, and device performance all affect the result.

## Connect to LM Studio over a LAN or Remotely

If Cherry Studio and LM Studio are not on the same device:

1. Enable **Serve on Local Network** in LM Studio's Server Settings;
2. Enable **Require Authentication** and create a Token;
3. Confirm that the system firewall permits the server port;
4. Enter the LAN address of the LM Studio host in Cherry Studio;
5. Enter the Token;
6. Open `/v1/models` first, then run a health check.

The CLI can also listen on all network interfaces:

```bash
lms server start --bind 0.0.0.0
```

Do not expose an unauthenticated LM Studio port directly to the public internet. For remote access over the internet, use a VPN or a reverse proxy with properly configured HTTPS, authentication, and access control.

In Docker, virtual machine, WSL, or remote desktop environments, `localhost` points to the system running Cherry Studio and may not be the LM Studio host. Use an address that is actually reachable.

## Troubleshooting

### Cannot Connect to `localhost:1234`

The LM Studio API Server is not running, the port has changed, or a firewall is blocking it. Confirm that the Developer page shows the server as running.

### The Model List Is Empty

Check whether `/v1/models` returns content. If JIT is disabled, load the model first. If JIT is enabled, confirm that the model has been downloaded and is visible to the server.

### Models Synchronize, but Chats Return an Error

The model may not have loaded successfully, resources may be insufficient, the context may be too large, or the API template may be incompatible. Check the LM Studio server logs and loading status.

### The First Response Is Slow

JIT is loading the model. Later requests are usually faster. You can preload the model, but it will continue to occupy memory or VRAM.

### Insufficient Memory or VRAM

Use a smaller model or a more compressed quantization and shorten the context. Increase GPU Offload only when your device has enough headroom, and unload other models.

### Images or MCP Do Not Work

Working standard chats do not mean that the model supports vision or tools. Check the model version, template, Cherry Studio capability detection, and LM Studio logs.

### Invalid API Token

Confirm that Require Authentication is enabled in LM Studio, the Token has not been deleted, its permissions are correct, and there are no extra spaces in Cherry Studio.

### Remote Connection Is Refused

Confirm that Serve on Local Network is enabled, the port is reachable, and the firewall and reverse proxy path are correct. Do not solve public-internet connectivity problems by disabling every security control.

For more general settings, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For LM Studio servers, compatible APIs, and model management, see the [official documentation](https://lmstudio.ai/docs). To send feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
