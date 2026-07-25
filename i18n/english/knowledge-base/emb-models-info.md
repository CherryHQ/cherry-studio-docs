---
icon: square-info
---

# Embedding Models

An embedding model converts text into vectors, allowing Cherry Studio to compare whether a question and a source passage are semantically related. It handles retrieval only; it does not generate the final answer.

Therefore, strong performance as a chat model does not mean that the model can be used for embedding. A knowledge base requires a model that explicitly supports **Embedding** capability.

## Where the Embedding Model Fits in a Knowledge Base

When building an index:

1. Cherry Studio reads and chunks the sources.
2. It sends each passage to the embedding model.
3. The returned vector and passage are stored together in the local vector database.

During retrieval:

1. The user's question is sent to the same embedding model.
2. Cherry Studio searches for nearby passages in the same vector space.
3. Relevant passages are then sent to the chat model to generate an answer.

{% hint style="warning" %}
Indexing and querying must use compatible embedding models and dimensions. Do not switch an existing knowledge base directly to an incompatible model, or its old vectors cannot be compared correctly.
{% endhint %}

## Add an Embedding Model in Cherry Studio

1. Open **Settings → Model Providers**.
2. Select and configure a provider that supports an embedding API.
3. Retrieve the model list and find a model with the **Embedding** label.
4. Add the model to the current provider and keep it enabled.
5. When creating a knowledge base, select it from the embedding model list.

The knowledge base lists only models that meet both conditions:

* The model is enabled
* The model capabilities include embedding

If the capabilities returned by a provider are inaccurate, open the model details and manually check or correct the capability labels. Embedding and reranking are different capabilities; do not mark a Rerank model as Embedding.

{% hint style="info" %}
Whether popular chat models from DeepSeek, Kimi, GLM, GPT, Claude, and other families appear in the knowledge base list depends on whether the specific model provides embedding capability, not on the brand name. The chat model selected for a conversation can differ from the embedding model used by the knowledge base.
{% endhint %}

## How to Choose

### 1. Language Coverage

Choose a model that covers all languages that might appear in your sources and questions.

* Chinese-only sources: start by testing models optimized for Chinese or Chinese and English
* Mixed Chinese and English sources: choose a multilingual model that explicitly supports both languages
* Sources containing Japanese, Russian, or other languages: choose a multilingual model whose official documentation covers those languages
* Code repositories: choose a model with explicit support for code retrieval

Do not rely only on `multilingual` in the model name. Run retrieval tests with your real sources and questions.

### 2. Input Length

The model's input limit must accommodate one chunk. If a chunk exceeds the limit, the request might fail or be truncated.

Cherry Studio chunks documents first, so you usually do not need the largest possible context length. A sensible chunk size and overlap are more important than simply increasing the model limit.

### 3. Vector Dimensions

Dimensions are the number of values in each vector. In general:

* Higher dimensions can preserve more information
* Higher dimensions consume more disk space and memory
* The dimension must be a value that the model actually supports
* Documents and questions within the same knowledge base must use the same dimension

Higher is not always better. For a small collection of sources, model quality, language coverage, and chunking usually matter more than maximizing dimensions.

### 4. Privacy and Deployment Location

When you use an online embedding model, source passages and queries are sent to the provider. For sensitive sources, consider a local model, but also confirm that the document processor, reranking model, and chat model run locally.

See [Knowledge Base Data](data.md) for the detailed data flow.

### 5. Cost, Speed, and Reliability

Building an index processes every passage, and reindexing calls the model again. When selecting an online model, also check:

* Input pricing
* Concurrency and rate limits
* Service region and network latency
* API reliability
* Batch embedding support

Do not judge by per-request price alone. Frequent rate limits or failed requests can substantially increase the time required for large imports.

## How to Set Vector Dimensions

Cherry Studio uses a default dimension when creating a new knowledge base. Open **RAG Settings** at the top of the knowledge base to view the embedding model and dimensions.

The refresh button beside the dimension:

1. Calls the embedding API once using the current provider configuration.
2. Sends a short test string.
3. Reads the actual length of the returned vector.
4. Fills the result into the dimension field.

Refreshing the dimension therefore makes a real model request. It fails if the API endpoint, API key, or model name is incorrect.

{% hint style="warning" %}
After you change the embedding model or dimensions, Cherry Studio starts a rebuild process instead of reusing old vectors with the new configuration. Confirm the model and dimensions before importing sources in bulk.
{% endhint %}

If a provider supports custom output dimensions, consult the model's official documentation first. Do not guess based on another model's default value.

## Common Model Examples

This table illustrates model categories; it is not a complete model list. Providers update, replace, or retire models, so use the live list retrieved by Cherry Studio and the provider's official documentation as the source of truth.

| Scenario | Models to consider testing | Notes |
| --- | --- | --- |
| General cloud embedding | `text-embedding-3-small`, `text-embedding-3-large` | OpenAI officially supports configurable output dimensions |
| Chinese and multilingual sources | `text-embedding-v4`, `qwen3.7-text-embedding` | Alibaba Cloud model capabilities and available dimensions vary by region |
| Local use | `embeddinggemma`, `qwen3-embedding`, `all-minilm` | Embedding model examples listed by Ollama |

Official resources:

* [OpenAI Embeddings](https://developers.openai.com/api/docs/guides/embeddings)
* [Alibaba Cloud Model Studio Text Embeddings](https://help.aliyun.com/zh/model-studio/text-embedding-synchronous-api)
* [Ollama Embeddings](https://docs.ollama.com/capabilities/embeddings)

Models with the same name can have different APIs, versions, dimensions, and prices across providers. When configuring one, confirm the current provider's model ID instead of relying only on its display name.

## Choose a Model with Retrieval Tests

Model leaderboards cannot replace your business data. A more reliable method is to prepare a fixed test set.

### Prepare Samples

Choose 10–30 real questions that cover:

* Questions answered directly in the documents
* Paraphrases and conversational wording
* Keywords such as product names, abbreviations, and identifiers
* Mixed Chinese and English or multilingual questions
* Questions that the documents do not answer

### Comparison Method

1. Create test knowledge bases with the same small set of sources.
2. Keep the chunking and retrieval settings consistent.
3. Build an index separately with each candidate embedding model.
4. Run a retrieval test with the same set of questions.
5. Compare whether the correct passages appear among the first results and how many irrelevant results are returned.

Also record indexing time, query speed, failure rate, and cost. Do not compare only the highest score, because different models can use different scoring scales.

## Change the Model for an Existing Knowledge Base

When you change the model or dimensions under the knowledge base's **RAG Settings**, Cherry Studio creates a new knowledge base indexing workflow.

Before proceeding:

1. Back up the knowledge base and external original files.
2. Confirm that the new model can be called successfully.
3. Use the dimension refresh button to retrieve the actual dimensions.
4. Keep the original knowledge base until the new one finishes indexing and passes retrieval tests.
5. Compare the results using the same questions before deciding whether to delete the old knowledge base.

Rebuilding a large knowledge base calls the document processing and embedding services again, which can incur charges and take considerable time.

## Frequently Asked Questions

### The Model Does Not Appear in the Knowledge Base List

Confirm that the model is enabled, then check its details for embedding capability. Regular chat models and reranking models do not automatically appear in the embedding model list.

### Retrieving Dimensions Fails

Check, in order, whether the provider is enabled, the API endpoint, API key, model ID, network, and account balance. Dimension refresh makes an actual call to the embedding API.

### A Dimension Error Appears During Indexing

Do not use a dimension value from another model. Retrieve the current model's actual dimensions again, then create a compatible index through the rebuild process.

### Mixed Chinese and English Retrieval Performs Poorly

Confirm that the model officially supports the relevant languages, then investigate with retrieval tests. You can also adjust chunking, search mode, and reranking configuration; do not change only the chat model.

### The Local Model Is Very Slow

Check model size, available memory, CPU/GPU usage, and the concurrency configuration in Ollama or LM Studio. Validate with a small set of sources before importing in bulk.

### Does Changing the API Key Require Reindexing?

Usually not, if you still call the same model with the same dimensions. If the provider routes requests to a different model version, run retrieval tests again.

***

### Get Help and Submit Feedback

If you encounter problems with model detection, dimensions, or indexing, contact the community using the information in [Feedback and Suggestions](../question-contact/suggestions.md).
