---
description: Tools
icon: code
---
# Code Tools Usage Tutorial


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




Cherry Studio v1.5.7 introduces an easy-to-operate and powerful Code Agent feature, allowing you to directly launch and manage various AI programming agents. This tutorial will guide you through the complete setup and launch process.

***

### Steps

#### 1. Upgrade Cherry Studio

First, please ensure your Cherry Studio has been upgraded to **v1.5.7** or a higher version. You can visit [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) or the official website to download the latest version.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### 2. Adjust Navigation Bar Position

To facilitate the use of top tab features, we recommend adjusting the navigation bar to the top.

*   Operation path: `Settings` -> `Display Settings` -> `Navigation Bar Settings`
*   Set the "Navigation Bar Position" option to **`Top`**.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Create a New Tab

Click the "+" icon at the top of the interface to create a new blank tab.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 4. Enable Code Agent Feature

In the new tab, click the `Code` (or `</>`) icon to enter the Code Agent configuration interface.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Select CLI Tool

Based on your needs and API Key, select a Code Agent tool to use. Currently, the following are supported:

*   **Claude Code**
*   **Gemini CLI**
*   **Qwen Code**
*   **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Select the Model for Agent Invocation

In the model dropdown list, select a model compatible with your chosen CLI tool. _(For detailed model compatibility instructions, please refer to "Important Notes" below)_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Specify Working Directory

Click the "Select Directory" button to specify a working directory for the Agent. The Agent will have permission to access all files and subdirectories within this directory, allowing it to understand the project context, read files, and execute code.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Set Environment Variables

*   **Automatic Configuration**: Your selections in Step 6 (Model) and Step 7 (Working Directory) will automatically generate the corresponding environment variables.
*   **Custom Addition**: If your Agent or project requires other specific environment variables (e.g., `PROXY_URL`), you can add them custom in this area.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Update Options

*   **Built-in Executables**: Cherry Studio has integrated the executables for all the Code Agents mentioned above, so in most cases, you can use them directly without an internet connection.
*   **Automatic Updates**: If you want the Agent to always stay up-to-date, you can check the **`Check for updates and install the latest version`** option. When checked, the program will connect to the internet to check for and update the Agent tool every time it starts.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Launch Agent

Once all configurations are complete, click the **`Launch`** button. Cherry Studio will automatically invoke your system's built-in Terminal tool, load all environment variables into it, and then run your selected Code Agent. You can now interact with the AI Agent in the popped-up terminal window.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Important Notes

1.  **Model Compatibility Instructions**:
    *   **Claude Code**: Requires selecting models that support the Anthropic API Endpoint format. Officially supported models currently include:
        *   Claude series models
        *   DeepSeek V3.1 (Official API Platform)
        *   Kimi K2 (Official API Platform)
        *   Zhipu GLM 4.5 (Official API Platform)
        *   **Note**: Currently, many third-party service providers (such as One API, New API, etc.) primarily support the OpenAI Chat Completions format for DeepSeek, Kimi, and GLM API interfaces. These may not be directly compatible with Claude Code and require waiting for service providers to gradually adapt.
    *   **Gemini CLI**: Requires selecting Google's Gemini series models.
    *   **Qwen Code**: Supports models with the OpenAI Chat Completions API format. We strongly recommend using the **`Qwen3 Coder`** series models for the best code generation results.
    *   **OpenAI Codex**: Supports GPT series models (e.g., `gpt-4o`, `gpt-5`).
2.  **Dependency and Environment Conflicts**:
    *   Cherry Studio internally integrates an independent Node.js runtime environment, Code Agent executables, and environment variable configurations, aiming to provide a ready-to-use, clean environment.
    *   If you encounter dependency conflicts or strange errors when launching the Agent, consider temporarily **uninstalling or disabling relevant dependencies already installed on your system** (such as globally installed Node.js or specific toolchains) to rule out conflicts.
3.  **API Token Consumption Warning**:
    *   **Code Agent consumes a very large amount of API Tokens**. When handling complex tasks, the Agent may generate numerous requests for thinking, planning, and code generation, leading to rapid Token consumption.
    *   Please be sure to **act within your means** according to your API quota and budget, and closely monitor Token usage to prevent budget overruns.

We hope this tutorial helps you quickly get started with Cherry Studio's powerful Code Agent feature!