---
icon: message
---
# Chat Interface


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Assistants and Topics

### Assistants

`Assistant` refers to applying personalized settings to a selected model, such as preset prompts and parameter presets. These settings allow the chosen model to perform more in line with your expectations.

The `System Default Assistant` comes with a general parameter preset (no prompt). You can use it directly or find the preset you need on the [Agents page](agents.md).

### Topics

`Assistant` is the parent of `Topic`. Multiple topics (i.e., conversations) can be created under a single assistant. All `Topics` share the assistant's parameter settings and model settings like preset words (prompt).

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Buttons in the Chat Box

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `New Topic` creates a new topic within the current assistant.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Upload Image or Document` requires model support for image uploads. Document uploads will automatically be parsed into text and provided to the model as context.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Web Search` requires configuring web search-related information in the settings. Search results are returned to the large language model as context. See [Web Search](../../websearch/) for details.

![](../../.gitbook/assets/对话界面/知识库.png) `Knowledge Base` enables the knowledge base. See [Knowledge Base Tutorial](../../knowledge-base/knowledge-base.md) for details.

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `MCP Server` enables the MCP server function. See [MCP Usage Tutorial](../../advanced-basic/mcp/) for details.

![](../../.gitbook/assets/对话界面/生成图片.png) `Generate Image` is not shown by default. For models that support image generation (e.g., Gemini), you need to manually activate it to generate images.

{% hint style="info" %}
Due to technical reasons, you must manually activate the button to generate images. This button will be removed once this feature is optimized.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Select Model` switches to the specified model for the subsequent conversation, while preserving context.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Quick Phrase` requires pre-setting common phrases in the settings to be called and directly entered here, supporting variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Clear Messages` deletes all content under this topic.

![](../../.gitbook/assets/对话界面/展开.png) `Expand` makes the chat box larger to accommodate long text input.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Clear Context` truncates the context available to the model without deleting content, meaning the model will "forget" previous conversation content.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimated Token Count` displays the estimated token count. The four values represent `Current Context Count`, `Maximum Context Count` (∞ indicates infinite context), `Current Input Box Message Count`, and `Estimated Token Count`.

{% hint style="info" %}
This function is only for estimating Token count. The actual Token count varies for each model; please refer to the data provided by the model provider.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Translate` translates the content in the current input box into English.

## Chat Settings

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Model Settings

Model settings are synchronized with the `Model Settings` in Assistant Settings. See [Assistant Settings](chat.md#bian-ji-zhu-shou) for details.

{% hint style="info" %}
In chat settings, only the model settings apply to the current assistant; other settings apply globally. For example, if you set the message style to bubble, it will be a bubble style for any topic in any assistant.
{% endhint %}

### Message Settings

#### <mark style="color:blue;">**`Message Separator`**</mark>:

Use a separator to separate the message body from the action bar.

{% tabs %}
{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Use Serif Font`**</mark>:

Font style switching. You can also change the font via [Custom CSS](../../personalization-settings/).

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

#### <mark style="color:blue;">**`Foldable Code Blocks`**</mark>:

When enabled, code blocks will automatically fold if the code snippet is too long.

#### <mark style="color:blue;">**`Word Wrap Code Blocks`**</mark>:

When enabled, single-line code within code snippets will automatically wrap if it exceeds the window width.

#### <mark style="color:blue;">**`Auto-fold Thought Content`**</mark>:

When enabled, models that support "thinking" will automatically fold the thinking process once completed.

#### <mark style="color:blue;">**`Message Style`**</mark>:

Allows switching the chat interface to bubble or list style.

#### <mark style="color:blue;">**`Code Style`**</mark>:

Allows switching the display style of code snippets.

#### <mark style="color:blue;">**`Math Formula Engine`**</mark>:

*   KaTeX renders faster because it is specifically optimized for performance;
*   MathJax renders slower but is more comprehensive, supporting more mathematical symbols and commands.

#### <mark style="color:blue;">**`Message Font Size`**</mark>:

Adjusts the font size of the chat interface.

### Input Settings

#### <mark style="color:blue;">**`Show Estimated Token Count`**</mark>:

Displays the estimated number of Tokens consumed by the input text in the input box (not the actual context consumption, for reference only).

#### <mark style="color:blue;">**`Paste Long Text as File`**</mark>:

When copying and pasting a long block of text from elsewhere into the input box, it will automatically display as a file, reducing interference during subsequent input.

#### <mark style="color:blue;">**`Markdown Render Input Messages`**</mark>:

When turned off, only the model's reply messages are rendered, not the sent messages.

{% tabs %}
{% tab title="When Off" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="When On" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Translate by Hitting Space 3 Times Quickly`**</mark>:

After entering a message in the chat interface's input box, hitting the spacebar three times quickly will translate the input content into English.

{% hint style="warning" %}
Note: This operation will overwrite the original text.
{% endhint %}

#### <mark style="color:blue;">**`Target Language`**</mark>:

Sets the target language for the translate button in the input box and for the "Translate by Hitting Space 3 Times Quickly" feature.

## Assistant Settings

In the assistant interface, select the desired <mark style="background-color:yellow;">Assistant Name</mark> → select the corresponding settings from the <mark style="background-color:yellow;">right-click menu</mark>.

### Edit Assistant

{% hint style="info" %}
Assistant settings apply to all topics under that assistant.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Prompt Settings

#### <mark style="color:blue;">**`Name`**</mark>:

Customizable assistant name for easy identification.

#### <mark style="color:blue;">**`Prompt`**</mark>:

The prompt, which can be edited by referring to the prompt writing style on the Agents page.

#### Model Settings

#### <mark style="color:blue;">**`Default Model`**</mark>:

You can fix a default model for this assistant. When adding from the Agents page or duplicating an assistant, the initial model will be this one. If not set, the initial model will be the global initial model (i.e., [Default Assistant Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
There are two types of default models for assistants: one is the [Global Default Chat Model](settings/default-models.md#mo-ren-zhu-shou-mo-xing), and the other is the assistant's default model. The assistant's default model has higher priority than the global default chat model. If the assistant's default model is not set, then the assistant's default model = the global default chat model.
{% endhint %}

#### <mark style="color:blue;">**`Auto-reset Model`**</mark>:

When enabled - If you switch to another model during use within this topic, creating a new topic will reset the new topic to the assistant's default model. When this item is disabled, the model for a new topic will follow the model used in the previous topic.

> For example, if the assistant's default model is gpt-3.5-turbo, and I create Topic 1 under this assistant, then during the conversation in Topic 1, I switch to using gpt-4o. In this case:
>
> If auto-reset is enabled: When creating Topic 2, the default selected model for Topic 2 will be gpt-3.5-turbo;
>
> If auto-reset is not enabled: When creating Topic 2, the default selected model for Topic 2 will be gpt-4o.

#### <mark style="color:blue;">**`Temperature`**</mark>:

The temperature parameter controls the degree of randomness and creativity in the text generated by the model (default value is 0.7). Specifically:

*   Low temperature values (0-0.3):
    *   Output is more deterministic, more focused
    *   Suitable for scenarios requiring accuracy, such as code generation and data analysis
    *   Tends to choose the most probable words for output
*   Medium temperature values (0.4-0.7):
    *   Balances creativity and coherence
    *   Suitable for daily conversations, general writing
    *   Recommended for chatbot conversations (around 0.5)
*   High temperature values (0.8-1.0):
    *   Produces more creative and diverse outputs
    *   Suitable for creative writing, brainstorming scenarios
    *   But may reduce text coherence

#### <mark style="color:blue;">**`Top P (Nucleus Sampling)`**</mark>:

The default value is 1. The smaller the value, the more monotonous and easier to understand the AI-generated content; the larger the value, the wider and more diverse the range of vocabulary in the AI's response.

Nucleus sampling affects the output by controlling the probability threshold for vocabulary selection:

*   Smaller values (0.1-0.3):
    *   Only considers the highest probability vocabulary
    *   Output is more conservative, more controllable
    *   Suitable for scenarios like code comments, technical documentation
*   Medium values (0.4-0.6):
    *   Balances vocabulary diversity and accuracy
    *   Suitable for general conversation and writing tasks
*   Larger values (0.7-1.0):
    *   Considers a wider range of vocabulary choices
    *   Produces richer and more diverse content
    *   Suitable for creative writing and other scenarios requiring diverse expression

{% hint style="info" %}
- These two parameters can be used independently or in combination.
- Choose appropriate parameter values based on the specific task type.
- It is recommended to experiment to find the most suitable parameter combination for a particular application scenario.
- The above content is for reference and conceptual understanding only; the given parameter ranges may not be suitable for all models. Please refer to the model's documentation for specific parameter recommendations.
{% endhint %}

#### <mark style="color:blue;">**`Context Window`**</mark>

The number of messages to retain in the context. A larger value means a longer context and consumes more tokens:

*   5-10: Suitable for general conversations
*   \>10: For complex tasks requiring longer memory (e.g., tasks that generate long texts step-by-step according to a writing outline, needing to ensure logical coherence of the generated context)
*   > Note: More messages consume more tokens

#### <mark style="color:blue;">**`Enable Message Length Limit (MaxToken)`**</mark>

The maximum number of [Tokens](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) for a single response. In large language models, max token is a key parameter that directly affects the quality and length of the model's generated response.

> For example: When testing if a model is connected after filling in the key in CherryStudio, you only need to know if the model returns a message correctly, not specific content. In this case, setting MaxToken to 1 is sufficient.

The MaxToken limit for most models is 32k Tokens, but some have 64k or even more. Specific details should be checked on the corresponding introduction page.

The exact setting depends on your needs, but you can also refer to the suggestions below.

{% hint style="success" %}
Suggestions:

*   General chat: 500-800
*   Short text generation: 800-2000
*   Code generation: 2000-3600
*   Long text generation: 4000 and above (requires model support)
{% endhint %}

{% hint style="warning" %}
Generally, the model's generated response will be limited to the MaxToken range. However, it may sometimes be truncated (e.g., when writing long code) or incomplete. In special cases, flexible adjustments may be needed based on actual circumstances.
{% endhint %}

#### <mark style="color:blue;">**`Stream Output`**</mark>

Stream output is a data processing method that allows data to be transmitted and processed in a continuous stream, rather than sending all data at once. This method allows data to be processed and output immediately after it is generated, greatly improving real-time performance and efficiency.

In environments like the CherryStudio client, it essentially means a typewriter effect.

When disabled (non-streaming): The model generates the information and outputs the entire segment at once (imagine receiving a message on WeChat);

When enabled: Outputs character by character. You can think of it as the large model sending you each character immediately after it's generated, until all are sent.

{% hint style="info" %}
If certain special models do not support streaming output, this switch needs to be turned off, such as o1-mini and others that **initially** only supported non-streaming.
{% endhint %}

#### <mark style="color:blue;">**`Custom Parameters`**</mark>

Adds extra request parameters to the request body, such as `presence_penalty` fields. Most people generally don't need this.

> The top-p, maxtokens, stream, and other parameters mentioned above are some of these parameters.

Fill-in method: Parameter Name — Parameter Type (text, number, etc.) — Value. Reference documentation: [Click to go](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Each model provider may have its own unique parameters, and you will need to find usage instructions in the provider's documentation.
{% endhint %}

{% hint style="info" %}
*   Custom parameters take precedence over built-in parameters. That is, if a custom parameter duplicates a built-in parameter, the custom parameter will overwrite the built-in parameter.

> For example: If `model` is set to `gpt-4o` in custom parameters, then `gpt-4o` will be used for conversations regardless of which model is selected.

*   Using the setting <kbd>Parameter Name:undefined</kbd> can exclude a parameter.
{% endhint %}