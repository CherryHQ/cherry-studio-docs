---
description: Tools
icon: code
---
# Code Tools Usage Tutorial


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




Cherry Studio v1.5.7 introduces a simple to operate, powerful Code Agent feature, which can directly launch and manage various AI programming agents. This tutorial will guide you through the complete setup and launch process.

***

### Operation Steps

#### 1. Upgrade Cherry Studio

First, please ensure your Cherry Studio is upgraded to **v1.5.7** or higher. You can go to [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) or the official website to download the latest version.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 2. Adjust Navigation Bar Position

To facilitate the use of the top tab feature, we recommend adjusting the navigation bar to the top.

*   Operation path: `Settings` -> `Display Settings` -> `Navigation Bar Settings`
*   Set the "Navigation Bar Position" option to **`Top`**.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Create New Tab

Click the "+" icon at the top of the interface to create a new blank tab.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. Open Code Agent Function

In the newly created tab, click the `Code` (or `</>`) icon to enter the Code Agent configuration interface.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Select CLI Tool

Based on your needs and API Key, select a Code Agent tool to use. Currently, the following are supported:

*   **Claude Code**
*   **Gemini CLI**
*   **Qwen Code**
*   **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Select Model for Agent Invocation

In the model dropdown list, select a model compatible with your chosen CLI tool. _(For detailed model compatibility instructions, please refer to the 'Important Notes' below)_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Specify Working Directory

Click the "Select Directory" button to specify a working directory for the Agent. The Agent will have access to all files and subdirectories within this directory, allowing it to understand the project context, read files, and execute code.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Set Environment Variables

*   **Automatic Configuration**: Your selections in step 6 (model) and step 7 (working directory) will automatically generate corresponding environment variables.
*   **Custom Addition**: If your Agent or project requires other specific environment variables (e.g., `PROXY_URL`, etc.), you can add them custom in this area.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Update Options

*   **Built-in Executables**: Cherry Studio has integrated the executables for all the above Code Agents for you. In most cases, you can use them directly without an internet connection.
*   **Automatic Updates**: If you want the Agent to always stay updated, you can check the **`Check for updates and install the latest version`** option. When checked, the program will check for updates online and update the Agent tool every time it starts.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Launch Agent

After all configurations are complete, click the **`Launch`** button. Cherry Studio will automatically invoke your system's built-in Terminal tool, load all environment variables into it, and then run your selected Code Agent. You can now interact with the AI Agent in the popped-up terminal window.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Important Notes

1.  **Model Compatibility Instructions:**
    *   **Claude Code**: Requires selecting models that support the Anthropic API Endpoint format. Currently supported official models include:
        *   Claude series models
        *   DeepSeek V3.1 (Official API platform)
        *   Kimi K2 (Official API platform)
        *   Zhipu GLM 4.5 (Official API platform)
        *   **Note**: Many third-party service providers (such as One API, New API, etc.) currently offer API interfaces for DeepSeek, Kimi, and GLM that mostly only support the OpenAI Chat Completions format. These may not be directly compatible with Claude Code and require waiting for service providers to gradually adapt.
    *   **Gemini CLI**: Requires selecting Google's Gemini series models.
    *   **Qwen Code**: Supports models with OpenAI Chat Completions API format, and it is highly recommended to use the **`Qwen3 Coder`** series models for the best code generation results.
    *   **OpenAI Codex**: Supports GPT series models (e.g., `gpt-4o`, `gpt-5`, etc.).
2.  **Dependencies and Environment Conflicts:**
    *   Cherry Studio internally integrates a standalone Node.js runtime environment, Code Agent executables, and environment variable configurations, aiming to provide a ready-to-use, clean environment.
    *   If you encounter dependency conflicts or unusual errors when launching the Agent, consider temporarily **uninstalling or disabling related dependencies already installed on your system** (such as globally installed Node.js or specific toolchains) to eliminate conflicts.
3.  **API Token Consumption Warning:**
    *   **Code Agent consumes a very large amount of API Tokens**. When handling complex tasks, the Agent may generate a large number of requests for thinking, planning, and generating code, leading to rapid Token consumption.
    *   Please be sure to **act within your means** based on your API quota and budget, and closely monitor Token usage to prevent budget overruns.

We hope this tutorial helps you quickly get started with Cherry Studio's powerful Code Agent feature!