---
icon: message
---
# Conversation Interface


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Assistants and Topics

### Assistants

`Assistants` are used to apply personalized settings to a selected model, such as preset prompts and parameter presets. These settings allow the chosen model to better meet your expected workflow.

The `System Default Assistant` presets a common parameter (no prompt). You can use it directly or go to the [Agents page](agents.md) to find the preset you need.

### Topics

`Assistants` are the parent of `Topics`. Multiple topics (i.e., conversations) can be created under a single assistant. All `Topics` share the assistant's parameter settings and model settings like preset words (prompts).

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Buttons within the Chat Box

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `New Topic` creates a new topic within the current assistant.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Upload Image or Document` requires model support for image uploads. Document uploads will be automatically parsed into text and provided to the model as context.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Web Search` requires configuring web search-related information in the settings. Search results are returned to the large model as context. See [Web Search Mode](../../websearch/) for details.

![](../../.gitbook/assets/对话界面/知识库.png) `Knowledge Base` enables the knowledge base feature. See [Knowledge Base Tutorial](../../knowledge-base/knowledge-base.md) for details.

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP Server` enables the MCP server feature. See [MCP Usage Tutorial](../../advanced-basic/mcp/) for details.

![](../../.gitbook/assets/对话界面/生成图片.png) `Generate Image` is not displayed by default. For models that support image generation (e.g., Gemini), you need to manually toggle it on to generate images.

{% hint style="info" %}
Due to technical reasons, you must manually toggle the button to generate images. This button will be removed once this feature is optimized.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Select Model` switches to the specified model for the subsequent conversation, while retaining the context.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Quick Phrases` requires pre-setting common phrases in the settings, which can then be invoked and directly inserted here, supporting variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Clear Messages` deletes all content under this topic.

![](../../.gitbook/assets/对话界面/展开.png) `Expand` enlarges the chat box for entering long texts.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Clear Context` truncates the context available to the model without deleting the content, meaning the model will "forget" previous conversation content.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimated Token Count` displays the estimated Token count. The four data points are `current context count`, `maximum context count` (∞ means infinite context), `character count in current input box`, and `estimated Token count`.

{% hint style="info" %}
This feature is only for estimating Token counts. The actual Token count varies for each model, please refer to the data provided by the model provider.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Translate` translates the content in the current input box into English.

## Conversation Settings

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Model Settings

Model settings are synchronized with the `Model Settings` in Assistant Settings. See [Assistant Settings](chat.md#bian-ji-zhu-shou) for details.

{% hint style="info" %}
In Conversation Settings, only the model settings apply to the current assistant; other settings apply globally. For example, if you set the message style to bubble, it will be bubble style in any topic of any assistant.
{% endhint %}

### Message Settings

#### <mark style="color:blue;">**`Message Separator`**</mark>:

Uses a separator to distinguish the message body from the operation bar.

{% tabs %}
{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Use Serif Font`**</mark>:

Font style toggle. You can also change the font via [custom CSS](../../personalization-settings/).

#### <mark style="color:blue;">**`Show Line Numbers for Code`**</mark>:

Displays line numbers for code blocks when the model outputs code snippets.

{% tabs %}
{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Collapsible Code Blocks`**</mark>:

When enabled, code blocks will automatically collapse if the code snippet is too long.

#### <mark style="color:blue;">**`Code Blocks Word Wrap`**</mark>:

When enabled, single-line code within code snippets will automatically wrap if it exceeds the window width.

#### <mark style="color:blue;">**`Auto-collapse Thinking Content`**</mark>:

When enabled, models that support "thinking" will automatically collapse the thinking process after completion.

#### <mark style="color:blue;">**`Message Style`**</mark>:

Allows switching the conversation interface to bubble style or list style.

#### <mark style="color:blue;">**`Code Style`**</mark>:

Allows switching the display style of code snippets.

#### <mark style="color:blue;">**`Math Formula Engine`**</mark>:

*   KaTeX renders faster because it is specifically optimized for performance.
*   MathJax renders slower but is more comprehensive, supporting more mathematical symbols and commands.

#### <mark style="color:blue;">**`Message Font Size`**</mark>:

Adjusts the font size of the conversation interface.

### Input Settings

#### <mark style="color:blue;">**`Show Estimated Token Count`**</mark>:

Displays the estimated Token count for the input text in the input box (not the actual context consumed, for reference only).

#### <mark style="color:blue;">**`Paste Long Text as File`**</mark>:

When copying and pasting a long paragraph from elsewhere into the input box, it will automatically display as a file, reducing interference when entering subsequent content.

#### <mark style="color:blue;">**`Render Input Messages as Markdown`**</mark>:

When disabled, only the model's reply messages are rendered, not the sent messages.

{% tabs %}
{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Translate by Tapping Space 3 Times`**</mark>:

After entering a message in the conversation interface's input box, tapping the spacebar three times in quick succession will translate the input content into English.

{% hint style="warning" %}
Note: This operation will overwrite the original text.
{% endhint %}

#### <mark style="color:blue;">**`Target Language`**</mark>:

Sets the target language for the input box translate button and for translating by tapping space 3 times.

## Assistant Settings

In the assistant interface, select the desired <mark style="background-color:yellow;">assistant name</mark> → choose the corresponding setting from the <mark style="background-color:yellow;">right-click menu</mark>.

### Edit Assistant

{% hint style="info" %}
Assistant settings apply to all topics under that assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Prompt Settings

#### <mark style="color:blue;">**`Name`**</mark>:

Customizable assistant name for easy identification.

#### <mark style="color:blue;">**`Prompt`**</mark>:

The prompt itself. You can refer to the prompt writing style on the Agents page to edit the content.

#### Model Settings

#### <mark style="color:blue;">**`Default Model`**</mark>:

You can fix a default model for this assistant. When adding from the Agents page or duplicating an assistant, the initial model will be this model. If this is not set, the initial model will be the global initial model (i.e., [Default Assistant Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
There are two types of default models for assistants: one is the [Global Default Conversation Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing), and the other is the assistant's default model; the assistant's default model takes precedence over the global default conversation model. If the assistant's default model is not set, then the assistant's default model = the global default conversation model.
{% endhint %}

#### <mark style="color:blue;">**`Auto Reset Model`**</mark>:

When enabled - if you switch to another model during use within this topic, creating a new topic will reset the new topic's model to the assistant's default model. When this is disabled, the new topic's model will follow the model used in the previous topic.

> For example, if the assistant's default model is gpt-3.5-turbo, and I create Topic 1 under this assistant, then switch to gpt-4o during the conversation in Topic 1:
>
> If auto-reset is enabled: when creating Topic 2, the default model selected for Topic 2 will be gpt-3.5-turbo;
>
> If auto-reset is not enabled: when creating Topic 2, the default model selected for Topic 2 will be gpt-4o.

#### <mark style="color:blue;">**`Temperature`**</mark>:

The temperature parameter controls the randomness and creativity of the text generated by the model (default value is 0.7). Specifically:

*   Low temperature values (0-0.3):
    *   Output is more certain and focused
    *   Suitable for scenarios requiring accuracy, such as code generation, data analysis
    *   Tends to select the most probable words for output
*   Medium temperature values (0.4-0.7):
    *   Balances creativity and coherence
    *   Suitable for daily conversations, general writing
    *   Recommended for chatbot conversations (around 0.5)
*   High temperature values (0.8-1.0):
    *   Produces more creative and diverse output
    *   Suitable for creative writing, brainstorming, etc.
    *   But may reduce text coherence

#### <mark style="color:blue;">**`Top P (Nucleus Sampling)`**</mark>:

The default value is 1. The smaller the value, the more monotonous and easier to understand the AI-generated content; the larger the value, the wider and more diverse the vocabulary range of the AI's response.

Nucleus sampling affects the output by controlling the probability threshold for vocabulary selection:

*   Smaller values (0.1-0.3):
    *   Only considers the highest probability words
    *   Output is more conservative and controllable
    *   Suitable for code comments, technical documents, etc.
*   Medium values (0.4-0.6):
    *   Balances vocabulary diversity and accuracy
    *   Suitable for general conversations and writing tasks
*   Larger values (0.7-1.0):
    *   Considers a wider range of vocabulary choices
    *   Produces richer and more diverse content
    *   Suitable for creative writing and other scenarios requiring diverse expressions

{% hint style="info" %}
- These two parameters can be used independently or in combination.
- Choose appropriate parameter values based on the specific task type.
- It is recommended to experiment to find the most suitable parameter combination for a specific application scenario.
- The above content is for reference and conceptual understanding only. The given parameter ranges may not be suitable for all models. Please refer to the model's documentation for specific parameter recommendations.
{% endhint %}

#### <mark style="color:blue;">**`Context Window`**</mark>

The number of messages to retain in the context. A larger value means a longer context and consumes more tokens:

*   5-10: Suitable for general conversations
*   >10: For complex tasks requiring longer memory (e.g., tasks that generate long texts step by step according to a writing outline, needing to ensure logical coherence of the generated context)
*   > Note: More messages consume more tokens.

#### <mark style="color:blue;">**`Enable Message Length Limit (MaxToken)`**</mark>

The maximum number of [Tokens](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) for a single response. In large language models, max token is a key parameter that directly affects the quality and length of the model's generated responses.

> For example, when testing if a model is connected after filling in the key in CherryStudio, you only need to know if the model returns a message correctly, not specific content. In this case, setting MaxToken to 1 is sufficient.

Most models have a MaxToken limit of 32k Tokens, but there are also 64k, or even more. You need to check the corresponding introduction page for details.

How much to set depends on your needs. Of course, you can also refer to the following suggestions.

{% hint style="success" %}
Suggestions:

*   General chat: 500-800
*   Short text generation: 800-2000
*   Code generation: 2000-3600
*   Long text generation: 4000 and above (requires model support)
{% endhint %}

{% hint style="warning" %}
Generally, the model's generated response will be limited to the MaxToken range. However, it may also be truncated (e.g., when writing long code) or expressed incompletely. In special cases, flexible adjustments may be needed based on actual circumstances.
{% endhint %}

#### <mark style="color:blue;">**`Streaming Output (Stream)`**</mark>

Streaming output is a data processing method that allows data to be transmitted and processed in a continuous stream, rather than sending all data at once. This method allows data to be processed and output immediately after it is generated, greatly improving real-time performance and efficiency.

In environments like the CherryStudio client, it basically means a typewriter effect.

When disabled (non-streaming): The model generates information and then outputs the entire paragraph at once (imagine receiving a message on WeChat);

When enabled: It outputs character by character. You can think of it as the large model sending you each character as soon as it generates it, until all are sent.

{% hint style="info" %}
If certain special models do not support streaming output, this switch needs to be turned off, such as o1-mini, which **initially** only supported non-streaming.
{% endhint %}

#### <mark style="color:blue;">**`Custom Parameters`**</mark>

Adds additional request parameters to the request body, such as `presence_penalty` and other fields. Generally, most people won't need this.

> The top-p, maxtokens, stream, and other parameters mentioned above are among these parameters.

Filling method: Parameter Name — Parameter Type (text, number, etc.) — Value. Reference documentation: [Click to go](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Each model provider may have its own unique parameters. You need to look for usage instructions in the provider's documentation.
{% endhint %}

{% hint style="info" %}
*   Custom parameters have higher priority than built-in parameters. That is, if a custom parameter duplicates a built-in parameter, the custom parameter will override the built-in parameter.

> For example, if `model` is set to `gpt-4o` in custom parameters, then `gpt-4o` will be used in the conversation regardless of which model is selected.

*   Setting <kbd>Parameter Name:undefined</kbd> can exclude a parameter.
{% endhint %}