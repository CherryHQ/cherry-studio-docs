---
description: Tools
icon: code
---
# Code Tools Usage Tutorial


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




Cherry Studio v1.5.7 introduces an easy-to-use yet powerful Code Agent feature, allowing you to directly launch and manage various AI programming agents. This tutorial will guide you through the complete setup and launch process.

***

### Operating Steps

#### 1. Upgrade Cherry Studio

First, please ensure your Cherry Studio is upgraded to **v1.5.7** or a higher version. You can download the latest version from [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) or the official website.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 2. Adjust Navigation Bar Position

To facilitate the use of the top tab feature, we recommend adjusting the navigation bar to the top.

*   Path: `Settings` -> `Display Settings` -> `Navigation Bar Settings`
*   Set the "Navigation Bar Position" option to **`Top`**.

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Create a New Tab

Click the "+" icon at the top of the interface to create a new blank tab.

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. Open Code Agent Function

In the newly created tab, click the `Code` (or `</>`) icon to enter the Code Agent configuration interface.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Select CLI Tool

Based on your needs and available API Key, choose a Code Agent tool to use. The following are currently supported:

*   **Claude Code**
*   **Gemini CLI**
*   **Qwen Code**
*   **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Select the Model Called by the Agent

From the model dropdown list, select a model compatible with your chosen CLI tool. _(For detailed model compatibility instructions, please refer to the "Important Notes" section below.)_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Specify Working Directory

Click the "Select Directory" button to specify a working directory for the Agent. The Agent will have access to all files and subdirectories within this directory, allowing it to understand project context, read files, and execute code.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Set Environment Variables

*   **Automatic Configuration**: Your choices in step 6 (Model) and step 7 (Working Directory) will automatically generate corresponding environment variables.
*   **Custom Addition**: If your Agent or project requires other specific environment variables (e.g., `PROXY_URL` etc.), you can add them custom in this area.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Update Options

*   **Built-in Executables**: Cherry Studio has integrated executables for all the Code Agents mentioned above, so in most cases, you can use them directly without an internet connection.
*   **Automatic Updates**: If you want the Agent to always stay up-to-date, you can check the option **`Check for updates and install the latest version`**. When checked, the program will check for and update the Agent tool online every time it starts.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Launch Agent

Once all configurations are complete, click the **`Launch`** button. Cherry Studio will automatically invoke your system's built-in Terminal tool, load all environment variables, and then run your selected Code Agent. You can now interact with the AI Agent in the pop-up terminal window.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Important Notes

1.  **Model Compatibility Description**:
    *   **Claude Code**: Requires selecting a model that supports the Anthropic API Endpoint format. Currently officially supported models include:
        *   Claude series models
        *   DeepSeek V3.1 (Official API platform)
        *   Kimi K2 (Official API platform)
        *   Zhipu GLM 4.5 (Official API platform)
        *   **Note**: Many third-party service providers (such as One API, New API, etc.) currently only support OpenAI Chat Completions format for DeepSeek, Kimi, and GLM API interfaces. These might not be directly compatible with Claude Code and may require waiting for service providers to adapt.
    *   **Gemini CLI**: Requires selecting Google's Gemini series models.
    *   **Qwen Code**: Supports OpenAI Chat Completions API format models, **`Qwen3 Coder`** series models are highly recommended for optimal code generation results.
    *   **OpenAI Codex**: Supports GPT series models (e.g., `gpt-4o`, `gpt-5`, etc.).
2.  **Dependencies and Environment Conflicts**:
    *   Cherry Studio integrates an independent Node.js runtime environment, Code Agent executables, and environment variable configurations, aiming to provide a pure out-of-the-box environment.
    *   If you encounter dependency conflicts or strange errors when launching the Agent, consider temporarily **uninstalling or disabling related dependencies already installed on your system** (such as globally installed Node.js or specific toolchains) to rule out conflicts.
3.  **API Token Consumption Warning**:
    *   **Code Agent consumes a very large amount of API Tokens**. When handling complex tasks, the Agent may generate a large number of requests for thinking, planning, and code generation, leading to rapid Token consumption.
    *   Please be sure to **act within your means** based on your API quota and budget, and closely monitor Token usage to prevent budget overruns.

We hope this tutorial helps you quickly get started with Cherry Studio's powerful Code Agent functionality!