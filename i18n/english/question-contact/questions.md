---
icon: seal-question
---

# Frequently Asked Questions

Use this page to identify the type of issue you are facing and open the relevant troubleshooting topic. When something goes wrong, preserve the original error and your data first. Do not immediately reinstall the app, reset its data, or delete its application directory.

## Start with five checks

1. Record the full Cherry Studio version under **Settings → About**.
2. Record your operating system, chip architecture, and when the issue occurred.
3. Save the complete error shown in the interface. Do not report only that it “does not work.”
4. Narrow the scope with a new chat, a small file, or a simple tool.
5. Determine whether every model fails or only a specific provider, model, or feature.

If the issue appeared after an update, also record the previous version and whether you migrated the data directory.

{% hint style="warning" %}
Resetting data clears the local database and files managed by the app. It is not a general-purpose fix. Do not use it without a usable backup. Clearing the cache also cannot fix account, model, or API configuration errors.
{% endhint %}

## The app cannot be installed or started

### The installer will not open

Confirm that you downloaded the correct operating system and architecture:

* Use the arm64 package on an Apple silicon Mac and the x64 package on an Intel Mac.
* On Windows and Linux, also choose the version that matches your device architecture.
* Download installers from [Download Cherry Studio](../cherrystudio/download.md) or the official releases.

If macOS reports that it cannot verify the developer or that the file is damaged, follow the [macOS installation guide](../pre-basic/installation/macos.md). Do not download a re-signed installer from an unknown source.

### Blank screen, broken layout, or missing buttons after startup

If you have used custom CSS, start with [Clear CSS settings](../personalization-settings/clear-css.md). A bad selector can hide access to settings, but deleting the entire data directory would also remove unrelated content.

If you have not used custom CSS, record the app version and operating system, restart, and reproduce the issue. If it persists, preserve the logs and submit a report.

### The app looks like a fresh installation after an update

Check whether you changed the application data directory, whether an external drive is online, and whether the app started with a new empty directory. Do not immediately create large amounts of data in the new directory or delete the old one. See [Change storage location](../personalization-settings/storage.md).

## Model services

### The API Key is saved but still does not work

Check the following in order:

1. The provider is enabled.
2. The API Key belongs to the current provider and region and contains no extra spaces.
3. The API address uses the root path and endpoint type required by the provider.
4. Your account has access to the target model and has a valid balance, quota, or billing method.
5. The model has been synced or added manually and is enabled in the model list.

A successful connection check usually proves only that one basic request can reach the service. It does not prove that vision, reasoning, tool use, Embedding, or image generation works. Test each capability separately.

See [Model providers](../pre-basic/providers/) for general setup and [Provider quick reference](../pre-basic/providers/quick-reference.md) for links to all provider templates.

### The model list cannot be retrieved

Some compatible services do not provide a standard model list or return only models your account can access. Verify the Base URL, credentials, region, and proxy first. If the provider supports a manually entered Model ID, add it according to the provider’s official documentation.

Do not copy a Model ID from another platform merely because it looks the same. Namespaces, capitalization, and version suffixes may differ.

### The model appears on the provider page but not in Chat

The model must meet all of these conditions:

* Its provider is enabled.
* The model itself is enabled.
* Its model type is valid for the current entry point.

Embedding, Rerank, and image-generation models are not shown as normal chat models. Agents also require a model available through an **Anthropic Messages** endpoint.

### Common HTTP status codes

Providers may define errors differently. Always use the response body and the provider’s documentation as the primary references.

| Status | Common cause | Check first |
| :--- | :--- | :--- |
| `400` | Invalid request parameters, context, or content format | Model endpoint, attachments, context length, custom parameters |
| `401` | Authentication failed | API Key, Authorization method, expired Key |
| `403` | Insufficient account, model, region, or content permissions | Model access, billing, region, organization permissions |
| `404` | Path, deployment, or model does not exist | Base URL, Deployment, Model ID, endpoint type |
| `408` / `504` | Request or upstream timeout | Network, proxy, service status, input size |
| `413` | Request body is too large | Image and file sizes, context, batch input |
| `422` | Parameters can be parsed but cannot be processed | Field types, required values, model-specific parameters |
| `429` | Rate, Token, or quota limit | RPM/TPM, balance, concurrency, retry later |
| `500` / `502` / `503` | Upstream internal error, gateway failure, or overload | Service status, proxy, retry with a smaller request |

If the error occurs only with one model, test another basic text model from the same provider. If every provider fails, then inspect the local network and proxy.

## Chat

### No response after sending a message

Check the actual model and provider shown above the message. In a multi-model chat, one failed model does not mean that every model failed. Inspect each response separately.

You can create a default assistant and an empty chat, then send only this short message:

```text
Reply with: Connection successful
```

If the small request succeeds but the original chat fails, the likely cause is context length, an attachment, a tool, or a custom assistant parameter. See [Chat interface](../cherrystudio/preview/chat.md) for detailed instructions.

### Context is too long or the request body is too large

Reduce message history, disable unneeded context, remove large attachments, or start a new chat. Clearing context changes only the history included in subsequent model requests; it does not delete every message shown in the interface.

### Images cannot be uploaded or the model cannot understand them

Confirm that the model has a vision capability tag and that the current provider endpoint actually accepts images. Selecting the capability manually changes only Cherry Studio’s interface filters and request routing. It cannot add a capability that the server does not support.

When uploading an image in a multi-model chat, every mentioned model should support image input.

### Formulas appear as source text

First confirm that the model produced complete delimiters:

* Inline formulas: `$...$` or `\(...\)`
* Display formulas: `$$...$$` or `\[...\]`

A formula will not render as math if its delimiters are inside a code block, escaped incorrectly, or truncated in the model output. Inspect the original message before concluding that this is a display issue.

## Network and proxy

### The browser can connect, but Cherry Studio cannot

The system browser and an Electron app may use different proxies, certificates, or login sessions. Open [General settings](../cherrystudio/preview/settings/general.md) and verify the proxy mode, proxy address, and whether a restart is required.

Also check:

* Whether a corporate network or firewall blocks the target domain.
* Whether a proxy has replaced the HTTPS certificate.
* Whether the system time is correct.
* Whether the service restricts regions or requires a login.

Do not treat disabling system security software or ignoring certificate errors as a long-term connection fix.

### Every request fails after enabling a proxy

Temporarily switch back to the system proxy or no proxy for comparison. A manual proxy requires the correct protocol, host, and port. HTTP, HTTPS, and SOCKS are not interchangeable merely because they use the same port.

## Knowledge Base

### A Knowledge Base cannot be created or its dimension cannot be retrieved

You need a working Embedding model before creating a Knowledge Base. Check that:

1. The selected model is an Embedding model, not a normal chat model.
2. The provider, API Key, Base URL, and Model ID are correct.
3. The model can complete a real embedding request.
4. The vector dimension returned by the model matches the configuration.

See [Embedding models](../knowledge-base/emb-models-info.md) for detailed troubleshooting.

### A file remains in processing or shows a failure

Wait for the current queue to finish, then inspect the failure state. Common causes include an unreadable file, an inaccessible web page, a document-processor failure, a failed Embedding request, or rate limiting.

After fixing the configuration, reindex the failed source. See the [Knowledge Base guide](../knowledge-base/knowledge-base.md) for the full workflow.

### Chat answers are inaccurate

Use the retrieval test first to check whether the correct chunks were found:

* Incorrect retrieval: adjust the source material, chunking, Embedding, or Rerank configuration.
* Correct retrieval but incorrect answer: inspect the chat model, prompt, and context.

A Knowledge Base supplies retrieved chunks; the chat model still produces the final answer.

## Agents

### A model does not appear in the Agent model picker

Agents require an endpoint type that includes **Anthropic Messages** and exclude Embedding, Rerank, and image-generation models. Check the provider endpoint and capability tags, then verify actual compatibility with a simple tool task.

### The Agent page reports that the service is not running

Click the start button on the page first. If it still fails, open **Settings → API Server** and inspect the port and running state. If another program occupies the port, stop the conflicting process or use an available port.

### An Agent cannot read or write files

Check that the target directory has been added to the accessible paths, the tool is enabled, and permission requests were approved. Do not add your entire user directory or disk merely to bypass an error.

See [Agents](../advanced-basic/agent.md) and [API Server](../advanced-basic/api-server.md) for more troubleshooting.

## MCP

### A Server cannot start

For a local STDIO Server, check Command, Arguments, the runtime environment, and the working directory first. For a remote Server, check the URL, Headers, authentication, and protocol type first.

Open **View logs** in the Server details, disable the Server, then enable it again. This makes the first startup error easier to find. See [MCP FAQ](../advanced-basic/mcp/chang-jian-wen-ti.md) for the complete checklist.

### The Server is connected but has no tools

A successful connection does not guarantee that the Server provides Tools. It may provide only Prompts or Resources. Inspect the capability list in the Server details and look for initialization or `listTools` errors in the logs.

### The model describes a tool but does not call it

Confirm that:

* The current assistant or Agent is connected to the MCP Server.
* The Server is enabled and the target tool is visible.
* The current model and endpoint support tool calling.
* Tool approval was not denied.

## Data, backup, and recovery

### Automatic backups are not being created

Check that the schedule is not set to “Off,” the destination directory or remote service is online, and review the latest error shown on the page. For an external drive, NAS, or remote storage, also verify available space, permissions, and connectivity.

### Images or Knowledge Base files are missing after recovery

If **Compact backup** was enabled, images and Knowledge Base files in the application `Data` directory were skipped. This is expected, and files excluded from a compact backup cannot be restored from it.

### Data from multiple computers is not merged automatically

Backup and recovery overwrite data; they are not real-time, bidirectional sync. Compare versions and timestamps before recovery, and back up the current device first.

See [Data settings](../data-settings/README.md) for details.

## Get logs

Go to **Settings → Data Settings → Data**, then open the log directory from **Application logs**. Reproduce the issue and locate the corresponding file by timestamp.

Before submitting it, remove or obscure:

* API Keys, Tokens, Cookies, and authentication Headers.
* Chats, prompts, Knowledge Base content, and file contents.
* Email addresses, user names, personal directories, and internal network addresses.
* Requests to and responses from third-party services.

A single error may span multiple log lines. Keep the necessary context immediately before and after it, but do not publicly upload the entire application data directory or a backup file.

## What to include in a report

An actionable report includes at least:

```text
Cherry Studio version:
Operating system and architecture:
Provider and model (if relevant):
Time of issue:
Expected result:
Actual result:
Minimal reproduction steps:
Complete error:
Actions already tried:
Redacted log or screenshot:
```

Read [How to ask effectively](ask.md) first, then submit your report through a channel listed under [Feedback and suggestions](suggestions.md). For crashes or data issues, state whether you have a backup, whether you migrated the data directory, and whether you continued writing data after the issue occurred.
