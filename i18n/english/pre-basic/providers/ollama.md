---
icon: server
---

# Ollama

Ollama can run local models on macOS, Windows, and Linux, and it can call cloud models through Ollama Cloud. Cherry Studio V2 uses Ollama's native Chat API and syncs models visible to the current instance from `/api/tags`.

When running locally, model inference and chat requests are processed on your device by default. If you select a Cloud model, the Ollama cloud API, or Web Search capabilities, the request still leaves your device.

{% hint style="info" %}
Clicking **Add** or syncing models in Cherry Studio reads only the existing Ollama model list; it does not download model weights. Pull the model in Ollama first, then return to Cherry Studio to sync it.
{% endhint %}

## Choose a connection method

| Method | Base URL | API Key |
| --- | --- | --- |
| Ollama on the same computer | `http://localhost:11434` | Leave blank |
| Self-hosted Ollama on a LAN or remote server | Actual server address | Depends on the reverse proxy |
| Direct Ollama Cloud connection | `https://ollama.com` | Ollama API Key |
| Local Ollama proxying a Cloud model | `http://localhost:11434` | Usually blank after signing in locally |

The local API does not require authentication by default. When the API Key is not empty, Cherry Studio sends `Authorization: Bearer ...`, which can be used for Ollama Cloud or a reverse proxy configured with Bearer authentication.

## Install Ollama

Visit the [Ollama website](https://ollama.com/) to download and install the version for your operating system.

On Linux, you can also use the official installation script:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

After installation, confirm that the service is running:

```bash
ollama list
```

If the command returns a model list, the Ollama CLI and local service are basically working.

## Pull models

Select a model and tag from the [Ollama model library](https://ollama.com/library), then run:

```bash
ollama pull <model>:<tag>
```

For example:

```bash
ollama pull gemma3
```

Common management commands:

```bash
ollama list
ollama ps
ollama stop <model>
ollama rm <model>:<tag>
```

- `ollama list`: View models that have been pulled;
- `ollama ps`: View currently loaded models and CPU/GPU usage;
- `ollama stop`: Unload a model from RAM or VRAM;
- `ollama rm`: Delete local model files.

A model tag affects parameter size, quantization, context, and disk usage. Do not consider only the model family name; select a specific tag based on RAM, VRAM, and the task.

## Configure in Cherry Studio

1. Open `Settings → Model Providers`;
2. Set the filter on the left to **All Providers**;
3. Select **Ollama**;
4. For local use, keep the Base URL `http://localhost:11434`;
5. Leave the API Key blank for the local service;
6. Turn on the provider switch at the top of the page;
7. Click **Add** to read the Ollama model list;
8. Review the sync preview and apply the changes;
9. Enable only the models you plan to use.

Cherry Studio normalizes `http://localhost:11434`, an address containing `/v1`, or an address containing `/api` to Ollama's native `/api` path. To reduce confusion, enter the host address without a specific endpoint.

If a model you just pulled does not appear, first confirm that `ollama list` shows the exact same tag, then click **Add** again.

## API Keys and Cloud models

### Use Cloud models through local Ollama

Sign in through Ollama first:

```bash
ollama signin
```

Then pull or run a model with `:cloud` according to the official instructions. Cherry Studio remains connected to `http://localhost:11434`, while local Ollama handles cloud authentication.

### Connect directly to Ollama Cloud

1. Create an API Key in your Ollama account;
2. Change the Base URL to `https://ollama.com`;
3. Enter the key in the API Key field;
4. Sync the available cloud models;
5. Run the connection and model health checks.

{% hint style="warning" %}
Do not include an API Key in chat messages, documents, code repositories, or issue screenshots. If a Cloud key is exposed, revoke it immediately in your Ollama account and create a new one.
{% endhint %}

A local model does not automatically become a cloud model. Confirm the model tag and the Ollama host currently connected to avoid misunderstanding where the data is actually processed.

## Select chat, vision, and tool models

Ollama model capabilities are determined by the model and its tag. Cherry Studio recognizes common capabilities from the model ID.

### Standard chat

Any generation model that supports the Ollama Chat API can be used for basic chat. The first request must load the weights and may be noticeably slower than later requests.

### Vision understanding

Select a model explicitly marked as supporting Vision in the Ollama model library. After syncing, check whether Cherry Studio displays image capabilities, then upload a small image for testing.

- Similar model names do not mean they all support images;
- Different tags may have different capabilities;
- Images increase context and memory usage;
- If the model ID is not recognized automatically, do not fake capabilities by changing only the display name.

### Tool calls and MCP

The model must natively support Tool Calling for Cherry Studio to use MCP reliably.

1. Select a model explicitly marked as supporting tool calls in the model library;
2. Complete a standard chat first;
3. Enable only one simple MCP tool;
4. Explicitly ask the model to call the tool;
5. Confirm that the model actually makes the call;
6. Then add more tools.

Some small models output text saying they “plan to call a tool” but do not generate a structured call. In that case, choose a model with stronger tool capabilities instead of repeatedly adding more prompt instructions.

## Configure thinking mode

The Ollama Chat API uses the `think` parameter to control thinking:

- For models that support GPT-OSS tiered reasoning, Cherry Studio can send Low, Medium, or High;
- Other thinking models usually accept only enabled or disabled;
- Selecting **Off** sends `think: false`;
- With Default or enabled, actual behavior still depends on the model.

If a model does not support `think` and returns a parameter error, disable thinking or use the correct model tag. Do not apply one model's thinking options directly to every local model.

## Context and hardware usage

Ollama's actual context depends on the model, server settings, and available memory. A longer context significantly increases RAM or VRAM usage.

You can set the default context when starting Ollama:

```bash
OLLAMA_CONTEXT_LENGTH=8192 ollama serve
```

To see whether a model is running on the GPU:

```bash
ollama ps
```

The `PROCESSOR` column shows the CPU, GPU, or mixed loading ratio.

If the model context entered in Cherry Studio is larger than the actual Ollama configuration, the server may still truncate the input or return a limit error. Use the Ollama runtime configuration and logs as the source of truth.

## Model loading and concurrency

Ollama unloads models after they become idle by default to release resources. You can adjust this behavior with `OLLAMA_KEEP_ALIVE`, `OLLAMA_MAX_LOADED_MODELS`, `OLLAMA_NUM_PARALLEL`, and `OLLAMA_MAX_QUEUE`.

- Keeping a model loaded reduces the wait for the first response but continues to occupy RAM or VRAM;
- Higher parallelism requires more context memory for each model;
- Loading multiple large models at once may trigger queuing or unloading;
- The server may return 503 when the queue is full.

Do not increase concurrency parameters alone. First use `ollama ps` and system monitoring to confirm available hardware resources.

## Knowledge bases and embedding models

Ollama can provide local embedding models for knowledge bases and [Global Memory](../../advanced-basic/memory.md).

1. Pull a dedicated embedding model from the model library;
2. Return to Cherry Studio and sync the models;
3. Confirm that the model is recognized as an embedding model;
4. Select it in the knowledge base;
5. Detect the dimensions and run a health check;
6. Then import documents.

Cherry Studio does not support Ollama reranking models. Select another provider when you need Rerank.

Once an embedding model is used in an existing knowledge base, do not casually change the model or dimensions; otherwise, you generally need to rebuild the vector index.

## PDFs and attachments

The current V2 version does not send PDFs directly to Ollama. Cherry Studio extracts the PDF text locally before passing it to the model:

- Text-based PDFs can usually be processed;
- Scanned documents require OCR first;
- Tables, complex layouts, and image information may be lost;
- Extracted text consumes the model context;
- Images in a PDF must be sent separately to a vision model.

## Connect to remote Ollama

Ollama listens only on `127.0.0.1:11434` by default. To connect from Cherry Studio on another device, configure the listening address on the Ollama host. For example:

```bash
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

The method for setting environment variables and restarting the service differs by operating system. See the [Ollama FAQ](https://docs.ollama.com/faq).

{% hint style="danger" %}
Do not expose an unauthenticated Ollama port directly to the public internet. Use a firewall even on a LAN. For public internet access, use a VPN or a reverse proxy with HTTPS and authentication.
{% endhint %}

When connecting to Ollama in Docker, a virtual machine, or WSL, `localhost` refers to the system where Cherry Studio is running, which is not necessarily the container or virtual machine. Use a host address that is reachable and check the port mapping.

## Check the connection

1. Run `ollama list` on the Ollama host;
2. Confirm that the target model has been pulled;
3. Run the provider connection check in Cherry Studio;
4. Click **Add** to sync the models;
5. Run the model health check;
6. Return to the chat interface and send a simple message;
7. Then test thinking, images, MCP, or the knowledge base.

If the local command also fails, fix Ollama first. If only Cherry Studio fails, focus on the Base URL, network, and model tag.

## Troubleshooting

### Cannot connect to `localhost:11434`

Ollama is not running, the port was changed, or a firewall is blocking it. Run `ollama list` first and check the Ollama logs.

### The model list is empty

The current Ollama host has no pulled models, or Cherry Studio is connected to the wrong host. `ollama list` and Cherry Studio must point to the same instance.

### A newly downloaded model is missing

Click **Add** again to sync the list and use the complete name and tag shown by `ollama list`. Cherry Studio synchronization does not download models for you.

### The first response is slow

Ollama is loading the model into RAM or VRAM. Use `ollama ps` to check where it is loaded; subsequent requests are usually faster.

### Out of memory, crashes, or constant queuing

Select a model with fewer parameters or higher quantization, shorten the context, reduce concurrency, and stop other loaded models.

### Response code 503

The server load is too high or the queue is full. Reduce concurrency, wait for the current request to finish, or adjust the Ollama queue configuration.

### Images or MCP are unavailable

Confirm that the specific model tag supports the corresponding capability and that Cherry Studio recognizes it correctly. Standard chat working does not mean the model supports vision or tools.

### Remote connection refused

Confirm that Ollama is listening on a non-local address, the port is open, and the reverse proxy path is correct. Do not solve public internet connectivity by disabling every security measure.

For general configuration, see [Model Providers](README.md) and [Model Provider Settings](../../cherrystudio/preview/settings/providers.md). For the Ollama API, see the [official documentation](https://docs.ollama.com/api/introduction); for feedback, see [Feedback and Suggestions](../../question-contact/suggestions.md).
