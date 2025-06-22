---
icon: message
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Chat Interface

## Assistants and Topics

### Assistant

An `Assistant` is a personalized configuration of a selected model, including settings like prompt presets and parameter presets. These settings allow the selected model to better meet your expected work requirements.

The `System Default Assistant` has a fairly general parameter preset (no prompt), which you can use directly or go to the [Agent Page](agents.md) to find a preset that suits your needs.

### Topic

An `Assistant` is a parent set to a `Topic`. Multiple topics (i.e., conversations) can be created under a single assistant. All `Topics` share the `Assistant`'s parameter settings, preset words (prompt), and other model settings.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Buttons in the Chat Box

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `New Topic` Creates a new topic within the current assistant.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Upload Image or Document` Uploading images requires model support. Uploaded documents will be automatically parsed into text and provided to the model as context.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Web Search` Requires configuring web search-related information in the settings. The search results are returned to the large model as context. For details, see [Web Search Mode](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Knowledge Base` Enables the knowledge base. For details, see [Knowledge Base Tutorial](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP Server` Enables the MCP server function. For details, see [MCP Usage Tutorial](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Generate Image` Not displayed by default. For models that support image generation (like Gemini), you need to manually activate it to generate images.

{% hint style="info" %}
For technical reasons, you must manually activate the button to generate images. This button will be removed after this feature is optimized.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Select Model` Switches to the specified model for the subsequent conversation while retaining the context.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Quick Phrases` You need to preset common phrases in the settings first. They can be invoked here and entered directly, with support for variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Clear Messages` Deletes all content under the current topic.

![](../../.gitbook/assets/对话界面/展开.png) `Expand` Makes the chat box larger for entering long texts.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Clear Context` Truncates the context available to the model without deleting the content, meaning the model will "forget" the previous conversation.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimate Token Count` Displays the estimated token count. The four data points are `Current Context Count`, `Max Context Count` (∞ means infinite context), `Character Count in Current Input Box`, and `Estimated Token Count`.

{% hint style="info" %}
This feature is only for estimating token count. The actual token count varies for each model. Please refer to the data provided by the model provider.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Translate` Translates the content in the current input box into English.

## Conversation Settings

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Model Settings

Model settings are synchronized with the `Model Settings` parameters in the assistant settings. For details, see [Assistant Settings](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
In the conversation settings, only the model settings apply to the current assistant; other settings are global. For example, if you set the message style to bubbles, it will be the bubble style in any topic of any assistant.
{% endhint %}

### Message Settings

#### <mark style="color:blue;">**`Message Divider`**</mark>:

Separates the message body from the action bar with a divider.

{% tabs %}
{% tab title="On" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Off" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Use Serif Font`**</mark>:

Switches the font style. You can now also change the font via [custom CSS](../../personalization-settings/).

#### <mark style="color:blue;">**`Show Line Numbers in Code`**</mark>:

Displays line numbers in code blocks when the model outputs code snippets.

{% tabs %}
{% tab title="Off" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="On" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Collapsible Code Blocks`**</mark>:

When enabled, long code snippets will be automatically collapsed.

#### <mark style="color:blue;">**`Wrap Lines in Code Blocks`**</mark>:

When enabled, long single lines of code (exceeding the window) will automatically wrap.

#### <mark style="color:blue;">**`Auto-collapse Thinking Process`**</mark>:

When enabled, models that support showing their thinking process will automatically collapse it after completion.

#### <mark style="color:blue;">**`Message Style`**</mark>:

You can switch the chat interface to either bubble style or list style.

#### <mark style="color:blue;">**`Code Style`**</mark>:

You can switch the display style of code snippets.

#### <mark style="color:blue;">**`Math Formula Engine`**</mark>:

*   KaTeX renders faster as it is specifically designed for performance optimization.
*   MathJax renders slower but is more feature-complete, supporting more mathematical symbols and commands.

#### <mark style="color:blue;">**`Message Font Size`**</mark>:

Adjusts the font size of the chat interface.

### Input Settings

#### <mark style="color:blue;">**`Show Estimated Token Count`**</mark>:

Displays the estimated token consumption of the input text in the input box (not the actual context token consumption, for reference only).

#### <mark style="color:blue;">**`Paste Long Text as File`**</mark>:

When pasting a long text from another source into the input box, it will automatically be displayed as a file style to reduce interference with subsequent input.

#### <mark style="color:blue;">**`Render Input Messages with Markdown`**</mark>:

When off, only the model's reply messages are rendered, not the messages you send.

{% tabs %}
{% tab title="Off" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="On" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Triple-press Space to Translate`**</mark>:

After typing a message in the chat input box, pressing the spacebar three times consecutively will translate the input into English.

{% hint style="warning" %}
Note: This action will overwrite the original text.
{% endhint %}

#### <mark style="color:blue;">**`Target Language`**</mark>:

Sets the target language for the translate button in the input box and the triple-press space translation feature.

## Assistant Settings

In the assistant interface, select the <mark style="background-color:yellow;">assistant name</mark> you want to configure → choose the corresponding setting from the <mark style="background-color:yellow;">right-click context menu</mark>.

### Edit Assistant

{% hint style="info" %}
Assistant settings apply to all topics under that assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Prompt Settings

#### <mark style="color:blue;">**`Name`**</mark>:

You can customize the assistant's name for easy identification.

#### <mark style="color:blue;">**`Prompt`**</mark>:

This is the `prompt`. You can refer to the prompt writing style on the agent page to edit the content.

#### Model Settings

#### <mark style="color:blue;">**`Default Model`**</mark>:

You can set a fixed default model for this assistant. When adding from the agent page or copying an assistant, the initial model will be this one. If this is not set, the initial model will be the global initial model (i.e., the [Default Assistant Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
There are two types of default models for an assistant: the [Global Default Chat Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing) and the assistant's default model. The assistant's default model has a higher priority than the global default chat model. When the assistant's default model is not set, it equals the global default chat model.
{% endhint %}

#### <mark style="color:blue;">**`Auto Reset Model`**</mark>:

When on - If you switch to another model during a conversation in a topic, creating a new topic will reset the model for the new topic to the assistant's default model. When this option is off, the model for a new topic will follow the model used in the previous topic.

> For example, if the assistant's default model is gpt-3.5-turbo, and I create Topic 1 under this assistant, and during the conversation in Topic 1, I switch to gpt-4o, then:
>
> If auto-reset is on: When creating Topic 2, the default model for Topic 2 will be gpt-3.5-turbo.
>
> If auto-reset is off: When creating Topic 2, the default model for Topic 2 will be gpt-4o.

#### <mark style="color:blue;">**`Temperature`**</mark> :

The temperature parameter controls the degree of randomness and creativity in the text generated by the model (default is 0.7). Specifically:

*   Low temperature value (0-0.3):
    *   Output is more deterministic and focused
    *   Suitable for scenarios requiring accuracy, like code generation and data analysis
    *   Tends to select the most likely words
*   Medium temperature value (0.4-0.7):
    *   Balances creativity and coherence
    *   Suitable for daily conversations and general writing
    *   Recommended for chatbot conversations (around 0.5)
*   High temperature value (0.8-1.0):
    *   Produces more creative and diverse output
    *   Suitable for creative writing, brainstorming, etc.
    *   May reduce the coherence of the text

#### <mark style="color:blue;">**`Top P (Nucleus Sampling)`**</mark>:

The default value is 1. The smaller the value, the more monotonous and easier to understand the AI-generated content is. The larger the value, the wider and more diverse the vocabulary of the AI's response.

Nucleus sampling affects the output by controlling the probability threshold for vocabulary selection:

*   Smaller value (0.1-0.3):
    *   Considers only the highest probability words
    *   Output is more conservative and controllable
    *   Suitable for code comments, technical documentation, etc.
*   Medium value (0.4-0.6):
    *   Balances vocabulary diversity and accuracy
    *   Suitable for general conversation and writing tasks
*   Larger value (0.7-1.0):
    *   Considers a wider range of vocabulary choices
    *   Produces richer and more diverse content
    *   Suitable for creative writing and other scenarios requiring diverse expression

{% hint style="info" %}
- These two parameters can be used independently or in combination.
- Choose appropriate parameter values based on the specific task type.
- It is recommended to experiment to find the best parameter combination for a specific application scenario.
- The above content is for reference and conceptual understanding only. The given parameter ranges may not be suitable for all models. Please refer to the parameter recommendations in the relevant model documentation.
{% endhint %}

#### <mark style="color:blue;">**`Context Window`**</mark>

The number of messages to keep in the context. The larger the value, the longer the context and the more tokens are consumed:

*   5-10: Suitable for normal conversations
*   \>10: For complex tasks requiring longer memory (e.g., generating a long article step-by-step according to an outline, which requires ensuring the generated context is logically coherent)
*   > Note: The more messages, the greater the token consumption

#### <mark style="color:blue;">**`Enable Message Length Limit (MaxToken)`**</mark>

The maximum number of [Tokens](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) for a single response. In large language models, max tokens is a key parameter that directly affects the quality and length of the generated response.

> For example: When testing if a model is connected after filling in the key in CherryStudio, you only need to know if the model returns a message correctly without specific content. In this case, setting MaxToken to 1 is sufficient.

The MaxToken limit for most models is 32k Tokens, but some have 64k or even more. You need to check the corresponding introduction page for specifics.

The specific setting depends on your needs, but you can also refer to the following suggestions.

{% hint style="success" %}
Suggestions:

*   Normal chat: 500-800
*   Short article generation: 800-2000
*   Code generation: 2000-3600
*   Long article generation: 4000 and above (requires model support)
{% endhint %}

{% hint style="warning" %}
Generally, the model's response will be limited within the MaxToken range. However, it might be truncated (e.g., when writing long code) or the expression may be incomplete. In special cases, you need to adjust it flexibly according to the actual situation.
{% endhint %}

#### <mark style="color:blue;">**`Streaming Output (Stream)`**</mark>

Streaming output is a data processing method that allows data to be transmitted and processed as a continuous stream, rather than sending all data at once. This method allows data to be processed and output immediately after it is generated, greatly improving real-time performance and efficiency.

In an environment like the CherryStudio client, it's simply a typewriter effect.

When off (non-streaming): The model outputs the entire message at once after generating it (imagine receiving a message on WeChat).

When on: Word-by-word output. You can think of it as the large model sending you each word as it generates it, until the entire message is sent.

{% hint style="info" %}
If some special models do not support streaming output, you need to turn this switch off, such as o1-mini which **initially** only supported non-streaming.
{% endhint %}

#### <mark style="color:blue;">**`Custom Parameters`**</mark>

Adds extra request parameters to the request body, such as `presence_penalty`, which are generally not needed by most users.

> The parameters mentioned above like top-p, maxtokens, stream, etc., are examples of these parameters.

How to fill: Parameter Name—Parameter Type (text, number, etc.)—Value. Refer to the documentation: [Click to go](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Each model provider has more or less its own unique parameters. You need to find their usage methods in the provider's documentation.
{% endhint %}

{% hint style="info" %}
*   Custom parameters have a higher priority than built-in parameters. That is, if a custom parameter conflicts with a built-in parameter, the custom parameter will override the built-in one.

> For example: If you set `model` to `gpt-4o` in the custom parameters, the `gpt-4o` model will be used in the conversation regardless of which model is selected.

*   Using the setting <kbd>Parameter Name:undefined</kbd> can exclude a parameter.
{% endhint %}