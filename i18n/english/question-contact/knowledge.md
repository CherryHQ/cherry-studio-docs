---
icon: book-bookmark
---

# AI Concepts

This page explains AI concepts that appear frequently in Cherry Studio. The goal is not to memorize terminology, but to understand why a model may fail, which settings affect the result, and where your data may be sent.

## Models, providers, and APIs

### Model

A model is a computational system that processes input and produces output. Different models may specialize in text, image understanding, image generation, Embedding, Rerank, reasoning, or tool calling.

The same model name may be offered by several providers. A different provider may mean different:

* Model IDs, versions, and context limits.
* Available regions, prices, rate limits, and account permissions.
* OpenAI, Anthropic, Gemini, or other API formats.
* Image, tool, reasoning-parameter, and other capabilities.

Therefore, the same model name does not prove identical API behavior. Test the model with the provider you actually use.

### Provider

A provider supplies the API address, authentication, model list, billing, and request limits. Cherry Studio saves connection settings, organizes requests, and displays results, but it cannot activate a provider account, quota, or model access for you.

See [Model providers](../pre-basic/providers/) for configuration.

### API and endpoint

An API defines request and response formats. Common endpoints include:

* OpenAI Chat Completions
* OpenAI Responses
* Anthropic Messages
* Google Generate Content
* Ollama Chat

“Compatible with an API” usually means that the basic format is similar. It does not guarantee implementation of every advanced capability in that API. Agents additionally require a model that is available through an **Anthropic Messages** endpoint.

## Token and Tokenizer

### What is a Token?

A Token is a piece of text processed by a model. One Token may be:

* A complete word.
* Part of a word.
* One or more characters.
* Punctuation, whitespace, or a special symbol.

Tokens do not equal word counts or a fixed number of characters in any language.

### What is a Tokenizer?

A Tokenizer converts input into the sequence of Tokens used by a model. Models and versions may use different Tokenizers, so the same text may produce different Token counts.

This affects:

* Whether the context limit is exceeded.
* Request speed.
* Input and output cost.
* How long documents are split.

Token counts displayed in Cherry Studio help estimate context size. Final billing and exact usage are determined by the provider’s response.

## Context window

Context is the information a model actually receives in one request. It may include:

* The system prompt and assistant configuration.
* The current user message.
* Retained message history.
* Image, file, or web-page content.
* Chunks retrieved from a Knowledge Base.
* Tool definitions, call parameters, and results.
* Space for the model’s remaining output.

A context window has a limit. With too much content, the provider may reject the request, the app may truncate some content, or the model may attend to only part of it.

### Is a longer context always better?

No. A longer context costs more and takes longer, and irrelevant information may interfere with the task. More effective approaches include:

* Use a separate topic for each project.
* Use **New context** when moving to a new stage.
* Attach only the files required for the task.
* Retrieve only relevant Knowledge Base chunks.
* Put stable rules in an assistant and temporary information in the current message.

See [Chat interface](../cherrystudio/preview/chat.md) for topic and context actions.

## System prompts, assistants, and topics

### System prompt

A system prompt defines a long-term role, behavioral boundaries, and output rules. It cannot change a model’s own knowledge, context limit, or server-side capabilities.

A system prompt that is too long or internally inconsistent consumes context and reduces predictability. Keep only stable rules there; put dates, source material, and the current goal in a user message.

### Assistant

An assistant saves a reusable chat configuration, such as:

* System prompt.
* Default model and parameters.
* Context count.
* Knowledge Bases.
* Web search and MCP.

One assistant can have several topics. The topics share assistant configuration but maintain independent histories. See [Assistant library](../cherrystudio/preview/selection-assistant.md) for details.

## Temperature, Top P, and output parameters

Temperature and Top P commonly adjust generation randomness and the candidate range, but implementations differ across models and providers. Some reasoning models ignore, restrict, or fix these values.

General guidance:

* Keep stable defaults for factual extraction, format conversion, and code edits.
* Increase diversity moderately for creative writing.
* Do not change several parameters drastically and then try to judge one parameter’s effect.
* If a parameter causes an error, restore its default and consult the model’s official documentation.

The maximum output length limits what the model can generate in the current request; it does not expand the input context. If output stops unexpectedly, inspect the output limit, provider restrictions, and request timeout.

## Reasoning models

A reasoning model performs additional computation before answering. It is useful for multi-step analysis, mathematics, planning, and complex coding tasks. Reasoning usually takes more time or costs more.

Keep in mind:

* A “Thinking” indicator does not mean that every model returns reasoning content in the same way.
* Hidden reasoning does not mean the model performed no reasoning.
* Strong reasoning does not guarantee factual correctness.
* Simple tasks do not always need the highest reasoning effort.

Choose a model by evaluating task accuracy, speed, price, and tool compatibility together.

## Tool calling

A model cannot automatically visit a website merely because it “knows” that website. Tool calling usually has three steps:

1. The app tells the model which tools are available and how their parameters are structured.
2. The model returns a structured tool-call request.
3. Cherry Studio or the corresponding Server executes the tool and returns the result to the model.

Accordingly, a tool can fail at several points:

* The model does not select the tool.
* The model produces invalid parameters.
* The user denies permission.
* The tool program or remote service fails.
* The tool result is too large or malformed.

A model saying that it will search does not prove that it called a tool. Inspect the tool record in the message or the [trace](../advanced-basic/diao-yong-lian-shi-yong-shuo-ming.md).

## Web search

Web search may come from:

* A model provider’s native search capability.
* A search service configured in Cherry Studio.
* A search tool supplied through MCP.

A search commonly returns candidate web pages first, then reads selected content for the model. The presence of a citation link does not mean that the citation supports the model’s conclusion. Check its publication date, original source, and quoted content.

See [Web search](../websearch/README.md) for configuration.

## Multimodal models

A multimodal model can process inputs other than text, such as images, audio, or files. Evaluate each capability separately:

| Capability | Description |
| :--- | :--- |
| Vision understanding | Read an image and answer questions about it |
| Image generation | Create or edit an image from a prompt |
| File input | Accept a PDF, document, or other file |
| Audio understanding | Accept and analyze audio |

Vision support does not imply image-generation support. The ability to read images also does not imply support for every file format.

Cherry Studio capability tags control the interface and request routing. Changing a tag manually cannot change the provider’s actual API. Run a minimal test after changing it.

## Hallucination

A “hallucination” is fluent model output that lacks support, conflicts with the input, or is factually wrong. Common causes include:

* The question lacks essential context.
* The model relies on outdated training information.
* Retrieved material is irrelevant or comes from unreliable sources.
* Important information is overlooked in a long context.
* The user insists on an answer, discouraging the model from leaving a gap.

Ways to reduce the risk include:

* Require sources, dates, and input locations.
* Separate facts, inferences, and assumptions.
* Allow an “uncertain” answer.
* Manually sample critical data.
* Have qualified professionals review high-risk decisions.

Web access and Knowledge Bases can supply newer material, but they do not automatically eliminate hallucinations.

## Embedding

An Embedding model converts text into a series of numbers called a vector. Semantically similar text is usually closer in vector space, which enables similarity retrieval.

An Embedding model is not a chat model. It normally returns vectors rather than natural-language answers.

### Dimension

The dimension is the number of values in a vector. Indexing and querying one Knowledge Base require compatible models and dimensions. After changing the model or dimension, you normally need to rebuild the old vectors.

More dimensions do not guarantee better accuracy. Also consider language, text type, input limits, speed, cost, and actual retrieval performance.

See [Embedding models](../knowledge-base/emb-models-info.md) for details.

## Chunking and vector retrieval

When building a Knowledge Base, a long document is split into smaller chunks before a vector is produced for each one.

Chunks that are too large may:

* Contain too many topics.
* Exceed the Embedding input limit.
* Consume too much context when returned.

Chunks that are too small may:

* Lose relationships between sentences.
* Produce excessive indexes and requests.
* Retrieve isolated phrases without enough explanation.

Overlap preserves some context across adjacent chunks, but it increases the number of indexed chunks. The best value depends on document structure and question type and should be selected through retrieval tests.

## Rerank

Vector retrieval first finds candidate chunks. A Rerank model then reorders them for the current question. It can improve candidate order, but it cannot fix:

* An answer that does not exist in the source.
* Incorrect document extraction.
* A candidate stage that retrieves no relevant chunks at all.
* A final chat model that misunderstands the correct chunk.

Embedding and Rerank are different capabilities and are not interchangeable.

## RAG

RAG means Retrieval-Augmented Generation. In a Cherry Studio Knowledge Base, it can be summarized as:

1. Extract and chunk documents.
2. Build an index with Embedding.
3. Convert the user’s question into a query vector.
4. Retrieve similar chunks.
5. Optionally reorder them with Rerank.
6. Give the chunks to the chat model as context.
7. Have the chat model generate an answer.

If retrieval is correct but the answer is wrong, inspect the chat model and prompt. If retrieval itself is wrong, inspect the sources, chunking, Embedding, and Rerank configuration. See the [Knowledge Base guide](../knowledge-base/knowledge-base.md) for the full workflow.

## MCP

MCP (Model Context Protocol) lets AI applications connect to external capabilities through a common interface. A Server may provide:

* **Tools**: execute queries, writes, or API calls.
* **Prompts**: provide reusable prompt templates.
* **Resources**: provide readable content.

MCP is a protocol, not a security sandbox. A STDIO Server may run locally with your user permissions, and a remote Server receives data sent to it. Before installing one, inspect its source, commands, parameters, environment variables, and access scope.

See [MCP](../advanced-basic/mcp/) for usage.

## Skills

A skill is a set of task instructions, workflows, and resources for an Agent. It primarily tells an Agent “how to complete this kind of work,” while MCP mainly provides “what can be called.”

A skill may itself reference scripts, templates, or tools. Read `SKILL.md` and its accompanying files before installation, and enable only trusted sources. See [Skills](../pre-basic/settings/skills.md).

## Assistants and Agents

| | Assistant | Agent |
| :--- | :--- | :--- |
| Primary use | Ongoing chats with a fixed configuration | Multi-step tasks executed under a goal and permissions |
| Local working directory | No Agent-style directory permissions | Can restrict accessible directories |
| File and command tools | Extended through selected MCP Servers and similar integrations | Can use built-in tools, MCP, and skills |
| Best for | Writing, questions and answers, Knowledge Base retrieval | Editing files, running commands, completing workflows |

See [Concepts 101](../advanced-basic/concepts-101.md) when deciding which one to use.

## Local and cloud models

### Cloud models

Requests are sent to a provider. Common advantages include no local deployment and a larger model selection. You must consider the network, account, cost, region, and the provider’s data policies.

### Local models

Model inference runs on your device or a service in your local network. This can reduce model requests sent externally, but it requires sufficient memory, GPU memory, storage, and compute.

“Using a local model” does not mean that the entire workflow is offline. These components may still access external services:

* Web search.
* Remote MCP.
* Cloud Embedding or Rerank.
* Cloud document processors.
* Image generation, channels, and third-party integrations.

When evaluating privacy, inspect the complete data flow component by component instead of looking only at where the chat model runs.

See [Ollama](../pre-basic/providers/ollama.md) and [LM Studio](../pre-basic/providers/lm-studio.md) for local-model configuration.

## Where costs come from

Components that may incur costs include:

* Chat-model input, output, and reasoning Tokens.
* Image, audio, or file processing.
* Embedding and Rerank requests.
* Image generation.
* Search, document processors, MCP, or other third-party APIs.
* Cloud storage and network traffic.

Parallel multi-model requests, repeated retries, long contexts, and frequent scheduled tasks all increase usage. Estimates displayed in Cherry Studio do not replace the provider’s bill.

## Data and privacy

In one workflow, data may pass through:

```text
User input
→ Cherry Studio
→ Document processing / Search / Knowledge Base / MCP
→ Model provider
→ Cherry Studio display or local files
```

The actual path depends on the enabled capabilities. Before use, check:

* Whether data leaves the device.
* Which service processes it.
* Whether requests are retained or used for training.
* Where credentials are stored and how much access they grant.
* Whether logs, backups, and screenshots contain sensitive information.

Do not put API Keys, Tokens, passwords, private keys, or unnecessary personal data in prompts, Knowledge Bases, or documents. Redact highly sensitive material first, and choose models and tools that comply with your organization’s policies.

## Recommended learning path

1. Understand models, providers, Tokens, and context first.
2. Complete a small task in [Chat interface](../cherrystudio/preview/chat.md).
3. Save a stable prompt in an assistant.
4. Create a Knowledge Base and run a retrieval test.
5. Learn MCP when you need external tools.
6. Use Agents and skills when you need local files and multi-step execution.

For an actual failure rather than a conceptual question, start with [Frequently Asked Questions](questions.md).
