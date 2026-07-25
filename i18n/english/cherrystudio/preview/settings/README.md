---
description: Understand the Cherry Studio V2 Settings structure and quickly find configuration for models, tools, data, and productivity features.
icon: gear
---

# Software Settings

Cherry Studio V2 brings model connections, tool services, application preferences, data management, and productivity features together in Settings. This page is a navigation guide and does not repeat every switch in detail. Find the relevant section for your goal, then open the corresponding topic page.

## Open Settings

Click the **Settings** icon in the lower-left corner of the main window.

Settings opens **Model Providers** by default. The left sidebar is divided into:

1. Model connections;
2. Tool services;
3. Application settings;
4. Productivity tools;
5. System information.

{% hint style="info" %}
Labels and positions may differ slightly by operating system, window size, or version. If a feature is missing, first confirm the version under **About** and check whether it is available only on a specific platform.
{% endhint %}

## Model Connections

| Setting | Purpose | Related documentation |
| --- | --- | --- |
| Model Providers | Add or manage model providers, API Keys, API addresses, connection methods, and model lists | [Model Provider Settings](providers.md) |
| Models | Set default chat, vision, embedding, rerank, translation, and other models | [Default Model Settings](default-models.md) |
| API Server | Expose Cherry Studio model capabilities to other applications through a local OpenAI-compatible API | [API Server](../../../advanced-basic/api-server.md) |

For first-time setup, use this order:

1. Enable a provider under **Model Providers** and complete a connection check;
2. Confirm that the models you need appear in the model list;
3. Set each type of default model under **Models**;
4. Return to the chat page and send a test message.

API Keys for model providers are sensitive credentials. Do not put real keys in screenshots, public documentation, or feedback reports.

## Tool Services

| Setting | Purpose | Related documentation |
| --- | --- | --- |
| MCP Servers | Install and manage MCP tools that connect assistants or agents to external capabilities | [Using MCP](../../../advanced-basic/mcp/) |
| Web Search | Select keyword search and URL retrieval providers, and configure result count, compression, and the blacklist | [Web Search](../../../websearch/) |
| Document Processing | Configure file parsing for PDFs, Office documents, image OCR, and similar formats | [Document Processing](../../../pre-basic/settings/doc-process.md) |
| Integrations | Connect external knowledge tools such as Obsidian, Notion, SiYuan, Yuque, and Joplin | [Data Settings](../../../data-settings/) |
| Plugins | View and manage application plugins supported by the current version | No dedicated topic page yet |

Tool availability usually depends on all of the following:

- The feature itself is configured;
- The current model supports tool calling or the relevant input type;
- The assistant or agent has permission to use the tool;
- The local network and third-party service are accessible.

Do not assume that a feature is ready just because a switch appears in the interface. After configuring it, perform one minimal test in an actual conversation.

## Application Settings

| Setting | Purpose | Related documentation |
| --- | --- | --- |
| General Settings | Application preferences such as language, theme, fonts, message display, startup behavior, proxy, and voice | [General Settings](general.md) |
| Data Settings | Local data directory, import and export, backups, WebDAV, S3, and note services | [Data Settings](../../../data-settings/) |

General Settings contains many options. These topics provide more detail:

- [Display Settings](display.md): themes, fonts, layout, and message display;
- [Voice Features](yu-yin-gong-neng.md): voice input and text-to-speech;
- [Personalization Settings](../../../personalization-settings/): custom fonts, CSS, and storage location.

{% hint style="warning" %}
Most appearance options take effect immediately, but language, proxy, storage location, and some system integrations may require reopening the window or restarting the application. Follow the notice beside the setting and the actual interface to determine whether a restart is required.
{% endhint %}

## Productivity Tools

| Setting | Purpose | Related documentation |
| --- | --- | --- |
| Channels | Let agents receive and send messages through external channels such as Feishu and Telegram | [Channels](../../../advanced-basic/agent-channels.md) |
| Scheduled Tasks | Run agent tasks automatically on a schedule | [Scheduled Tasks](../../../advanced-basic/scheduled-tasks.md) |
| Shortcuts | View, change, enable, or disable application and global shortcuts | [Shortcut Settings](key-shortcut.md) |
| Quick Assistant | Open a lightweight question window from a global shortcut or the system tray | [Quick Assistant](../kuai-jie-zhu-shou.md) |
| Selection Assistant | Translate, summarize, explain, or perform other actions on text selected in another application | [Selection Assistant](../selection-assistant.md) |

Channels and scheduled tasks may let agents run outside the main window or while unattended. Before enabling them, review model costs, tool permissions, accessible data, and task stop conditions.

## System Information

The **About** page shows:

- The Cherry Studio version;
- Update status and update channel;
- Links to the official website and open-source repository;
- License and related system information.

Development builds may also show **Component Lab**. It is for developing and testing interface components, is not part of the community edition's everyday workflow, and should not be treated as a formal feature entry point in automation steps.

## Recommended First-Time Setup Order

If you have just installed Cherry Studio, complete the minimum setup in this order:

1. **Model Providers**: enable a provider, enter credentials, and check the connection;
2. **Models**: select a default chat model;
3. **General Settings**: select the language, theme, and startup behavior;
4. **Data Settings**: confirm the data location and create the first backup;
5. **Web Search or Document Processing**: configure only the tools you currently need;
6. **Shortcuts**: avoid conflicts between global key combinations and other applications;
7. **About**: confirm that you are using the expected version.

You do not need to enable every service at once. Stabilize basic chat first, then add Web Search, MCP, channels, and automated tasks one at a time so configuration issues are easier to isolate.

## Check Settings After Changes

Use these checks after changing settings:

| Change | Recommended check |
| --- | --- |
| Model provider or API Key | Run a connection check, then send a short message |
| Default model | Start a new conversation and confirm the model displayed at the top |
| Web Search | Enable the Globe icon and ask a question that requires current information |
| Document processing | Upload a small test file and inspect the parsed result |
| Proxy | Access a service that requires the proxy again; restart the application if necessary |
| Shortcut | Press the key combination once in the target window |
| Data or backup | Create a backup and confirm that the file or remote record was actually created |

## Troubleshooting

### Changed Settings Do Not Take Effect

First confirm that the input has lost focus or that you clicked Save or Check. Reopen the relevant page. For language, network, system permission, or storage path changes, restart Cherry Studio afterward.

### A Setting Mentioned in the Documentation Is Missing

Check:

1. Whether the current Cherry Studio installation is a recent V2 community edition;
2. Whether the feature supports only specific operating systems;
3. Whether a provider, model, or experimental feature must be enabled first;
4. Whether the Settings sidebar can scroll farther;
5. Whether the feature has moved to an assistant, agent, or application page.

### Can Every Setting Be Synchronized to Another Device?

Different backup methods cover different data. Do not assume that every credential and local path will be synchronized just because a backup succeeded. Before migrating, read [Data Settings](../../../data-settings/) and verify model providers, paths, and system permissions on the target device.

***

### Get Help and Submit Feedback

If you encounter a problem in Settings, submit feedback through the official channels listed in [Feedback and Suggestions](../../../question-contact/suggestions.md). Include the Cherry Studio version, operating system, setting name, and sanitized error message.
