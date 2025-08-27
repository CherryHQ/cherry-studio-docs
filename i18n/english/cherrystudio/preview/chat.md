---
icon: message
---
# Conversation Interface


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Assistants and Topics

### Assistants

An `Assistant` allows you to personalize the selected model with settings such as prompt presets and parameter presets, making the model work more in line with your expectations.

The `System Default Assistant` provides a general parameter preset (no prompt). You can use it directly or find the preset you need on the [Agents Page](agents.md).

### Topics

An `Assistant` is the parent set of `Topics`. Multiple topics (i.e., conversations) can be created under a single assistant. All `Topics` share the `Assistant`'s parameter settings and prompt presets, among other model settings.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Buttons in the Chatbox

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `New Topic` creates a new topic within the current assistant.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Upload Image or Document` requires model support for image uploads. Uploading documents will automatically parse them into text to be provided as context to the model.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Web Search` requires configuring web search related information in the settings. Search results are returned to the large model as context. For details, see [Web Search Mode](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Knowledge Base` enables the knowledge base feature. For details, see [Knowledge Base Tutorial](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP Server` enables the MCP server feature. For details, see [MCP Usage Tutorial](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Generate Image` is not displayed by default. For models that support image generation (e.g., Gemini), it needs to be manually enabled before images can be generated.

{% hint style="info" %}
Due to technical reasons, you must manually enable the button to generate images. This button will be removed after this feature is optimized.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Select Model` switches to the specified model for subsequent conversations while preserving the context.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Quick Phrases` requires pre-setting common phrases in the settings to be called here, allowing direct input and supporting variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Clear Messages` deletes all content under this topic.

![](../../.gitbook/assets/对话界面/展开.png) `Expand` makes the chatbox larger for entering longer texts.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Clear Context` truncates the context available to the model without deleting content, meaning the model will "forget" previous conversation content.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimated Token Count` displays the estimated token count. The four values represent `Current Context Count`, `Maximum Context Count` (∞ indicates unlimited context), `Current Input Box Message Character Count`, and `Estimated Token Count`.

{% hint style="info" %}
This function is only for estimating the token count. The actual token count varies for each model, so please refer to the data provided by the model provider.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Translate` translates the content in the current input box into English.

## Conversation Settings

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Model Settings

Model settings are synchronized with the `Model Settings` parameters in the assistant settings. For details, see [Assistant Settings](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
In the conversation settings, only the model settings apply to the current assistant; other settings apply globally. For example, if you set the message style to bubbles, it will be in bubble style for any topic of any assistant.
{% endhint %}

### Message Settings

#### <mark style="color:blue;">**`Message Separator`**</mark>:

Uses a separator to divide the message body from the action bar.

{% tabs %}
{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Use Serif Font`**</mark>:

Font style toggle. You can now also change fonts via [custom CSS](../../personalization-settings/).

#### <mark style="color:blue;">**`Display Line Numbers for Code`**</mark>:

Displays line numbers for code blocks when the model outputs code snippets.

{% tabs %}
{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Collapsible Code Blocks`**</mark>:

When enabled, code blocks will automatically collapse if the code snippet is long.

#### <mark style="color:blue;">**`Code Block Word Wrap`**</mark>:

When enabled, single lines of code within a code snippet will automatically wrap if they are too long (exceed the window).

#### <mark style="color:blue;">**`Auto-collapse Thinking Content`**</mark>:

When enabled, models that support thinking will automatically collapse the thinking process after completion.

#### <mark style="color:blue;">**`Message Style`**</mark>:

Allows switching the conversation interface to bubble style or list style.

#### <mark style="color:blue;">**`Code Style`**</mark>:

Allows switching the display style of code snippets.

#### <mark style="color:blue;">**`Mathematical Formula Engine`**</mark>:

*   KaTeX renders faster because it is specifically designed for performance optimization.
*   MathJax renders slower but is more comprehensive, supporting more mathematical symbols and commands.

#### <mark style="color:blue;">**`Message Font Size`**</mark>:

Adjusts the font size of the conversation interface.

### Input Settings

#### <mark style="color:blue;">**`Display Estimated Token Count`**</mark>:

Displays the estimated token count consumed by the input text in the input box (not the actual context token consumption, for reference only).

#### <mark style="color:blue;">**`Paste Long Text as File`**</mark>:

When copying and pasting a long block of text from elsewhere into the input box, it will automatically display as a file, reducing interference during subsequent input.

#### <mark style="color:blue;">**`Markdown Render Input Messages`**</mark>:

When disabled, only model replies are rendered, not sent messages.

{% tabs %}
{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Triple Space for Translation`**</mark>:

After entering a message in the conversation interface input box, pressing the spacebar three times consecutively will translate the input content into English.

{% hint style="warning" %}
Note: This operation will overwrite the original text.
{% endhint %}

#### <mark style="color:blue;">**`Target Language`**</mark>:

Sets the target language for the input box translation button and the triple space translation feature.

## Assistant Settings

In the assistant interface, select the <mark style="background-color:yellow;">assistant name</mark> you want to set → select the corresponding setting in the <mark style="background-color:yellow;">right-click menu</mark>.

### Edit Assistant

{% hint style="info" %}
Assistant settings apply to all topics under that assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Prompt Settings

#### <mark style="color:blue;">**`Name`**</mark>:

Customizable assistant name for easy identification.

#### <mark style="color:blue;">**`Prompt`**</mark>:

The prompt itself. You can refer to the prompt writing style on the agent page to edit the content.

#### Model Settings

#### <mark style="color:blue;">**`Default Model`**</mark>:

You can fix a default model for this assistant. When adding from the agent page or copying an assistant, the initial model will be this model. If this item is not set, the initial model will be the global initial model (i.e., [Default Assistant Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
There are two types of default models for assistants: one is the [global default conversation model](settings/default-models.md#mo-ren-zhu-shou-mo-xing), and the other is the assistant's default model. The assistant's default model has a higher priority than the global default conversation model. If the assistant's default model is not set, the assistant's default model will be equal to the global default conversation model.
{% endhint %}

#### <mark style="color:blue;">**`Auto Reset Model`**</mark>:

When enabled - if you switch to another model during use in this topic, creating a new topic will reset the new topic's model to the assistant's default model. When this item is disabled, the model for a new topic will follow the model used in the previous topic.

> For example, if the assistant's default model is gpt-3.5-turbo, and I create Topic 1 under this assistant, then switch to gpt-4o during the conversation in Topic 1:
>
> If auto-reset is enabled: When creating Topic 2, the default model selected for Topic 2 will be gpt-3.5-turbo.
>
> If auto-reset is not enabled: When creating Topic 2, the default model selected for Topic 2 will be gpt-4o.

#### <mark style="color:blue;">**`Temperature`**</mark>:

The temperature parameter controls the degree of randomness and creativity in the text generated by the model (default value is 0.7). Specifically:

*   Low temperature values (0-0.3):
    *   Output is more deterministic and focused.
    *   Suitable for scenarios requiring accuracy, such as code generation and data analysis.
    *   Tends to select the most probable words for output.
*   Medium temperature values (0.4-0.7):
    *   Balances creativity and coherence.
    *   Suitable for daily conversations and general writing.
    *   Recommended for chatbot conversations (around 0.5).
*   High temperature values (0.8-1.0):
    *   Produces more creative and diverse output.
    *   Suitable for creative writing, brainstorming, etc.
    *   May reduce text coherence.

#### <mark style="color:blue;">**`Top P (Nucleus Sampling)`**</mark>:

The default value is 1. A smaller value makes the AI-generated content more monotonous and easier to understand; a larger value gives the AI a wider and more diverse range of vocabulary for replies.

Nucleus sampling affects output by controlling the probability threshold for vocabulary selection:

*   Smaller values (0.1-0.3):
    *   Only consider words with the highest probability.
    *   Output is more conservative and controllable.
    *   Suitable for scenarios like code comments and technical documentation.
*   Medium values (0.4-0.6):
    *   Balances vocabulary diversity and accuracy.
    *   Suitable for general conversations and writing tasks.
*   Larger values (0.7-1.0):
    *   Considers a wider range of vocabulary.
    *   Produces richer and more diverse content.
    *   Suitable for creative writing and other scenarios requiring diverse expression.

{% hint style="info" %}
-   These two parameters can be used independently or in combination.
-   Choose appropriate parameter values based on the specific task type.
-   It is recommended to experiment to find the parameter combination best suited for a particular application scenario.
-   The above content is for reference and conceptual understanding only; the given parameter ranges may not be suitable for all models. Please refer to the parameter recommendations in the model's documentation.
{% endhint %}

#### <mark style="color:blue;">**`Context Window`**</mark>

The number of messages to keep in the context. A larger value means a longer context and consumes more tokens:

*   5-10: Suitable for general conversations.
*   >10: For complex tasks requiring longer memory (e.g., generating long texts step-by-step according to an outline, where generated context needs to ensure logical coherence).
*   > Note: More messages consume more tokens.

#### <mark style="color:blue;">**`Enable Message Length Limit (MaxToken)`**</mark>

The maximum [Token](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) count for a single response. In large language models, `max token` (maximum token count) is a crucial parameter that directly affects the quality and length of the model's generated responses.

> For example, when testing if a model is connected after filling in the key in CherryStudio, if you only need to know if the model returns a message correctly without specific content, you can set MaxToken to 1.

The MaxToken limit for most models is 32k Tokens, but some support 64k or even more; you need to check the relevant introduction page for details.

The specific setting depends on your needs, but you can also refer to the following suggestions.

{% hint style="success" %}
Suggestions:

*   General Chat: 500-800
*   Short Text Generation: 800-2000
*   Code Generation: 2000-3600
*   Long Text Generation: 4000 and above (requires model support)
{% endhint %}

{% hint style="warning" %}
Generally, the model's generated response will be limited within the MaxToken range. However, it may also be truncated (e.g., when writing long code) or expressed incompletely. In special cases, adjustments need to be made flexibly according to the actual situation.
{% endhint %}

#### <mark style="color:blue;">**`Streaming Output (Stream)`**</mark>

Streaming output is a data processing method that allows data to be transmitted and processed in a continuous stream, rather than sending all data at once. This method allows data to be processed and output immediately after it is generated, greatly improving real-time performance and efficiency.

In environments like the CherryStudio client, it basically means a "typewriter effect."

When disabled (non-streaming): The model generates information and outputs the entire segment at once (imagine receiving a message on WeChat).

When enabled: Outputs character by character. This can be understood as the large model sending you each character as soon as it generates it, until all characters are sent.

{% hint style="info" %}
If certain special models do not support streaming output, this switch needs to be turned off, such as o1-mini and others that **initially** only supported non-streaming.
{% endhint %}

#### <mark style="color:blue;">**`Custom Parameters`**</mark>

Adds additional request parameters to the request body, such as `presence_penalty` and other fields. Generally, most users will not need this.

> Parameters like top-p, maxtokens, stream, etc., mentioned above are some of these parameters.

Input format: Parameter Name — Parameter Type (text, number, etc.) — Value. Reference documentation: [Click to go](https://openai.apifox.cn/doc-3222739).

{% hint style="info" %}
Each model provider may have its own unique parameters. You need to consult the provider's documentation for usage methods.
{% endhint %}

{% hint style="info" %}
*   Custom parameters have higher priority than built-in parameters. That is, if a custom parameter conflicts with a built-in parameter, the custom parameter will override the built-in parameter.

> For example: if `model` is set to `gpt-4o` in custom parameters, then `gpt-4o` will be used in the conversation regardless of which model is selected.

*   Settings like <kbd>ParameterName:undefined</kbd> can be used to exclude parameters.
{% endhint %}