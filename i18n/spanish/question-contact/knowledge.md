---
icon: book-bookmark
---
# Knowledge Science


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## What are tokens?

Tokens are the fundamental units of text processing in AI models, which can be understood as the smallest units of "thought" for the model. They don't exactly correspond to characters or words as we understand them, but rather represent the model's unique way of segmenting text.

#### 1. Chinese segmentation
* One Chinese character is typically encoded as 1-2 tokens
* Example: `"你好"` ≈ 2-4 tokens

#### 2. English segmentation
* Common words are usually 1 token
* Longer or uncommon words are broken into multiple tokens
* Example:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Special characters
* Spaces, punctuation marks also consume tokens
* Line breaks are typically 1 token

{% hint style="info" %}
Different providers have different Tokenizers, and even different models from the same provider may have variations. This knowledge is solely for clarifying the concept of tokens.
{% endhint %}

***

## What is a Tokenizer?

The Tokenizer is the tool that converts text into tokens for AI models. It determines how to split input text into the smallest units understandable by the model.

### Why do different models have different Tokenizers?

#### 1. Different training data
* Different corpora lead to different optimization directions
* Variations in multilingual support
* Specialized optimization for specific domains (medical, legal, etc.)

#### 2. Different segmentation algorithms
* BPE (Byte Pair Encoding) - OpenAI GPT series
* WordPiece - Google BERT
* SentencePiece - Suitable for multilingual scenarios

#### 3. Different optimization goals
* Some focus on compression efficiency
* Some prioritize semantic preservation
* Others emphasize processing speed

### Practical impact
The same text may have different token counts across models:
```
Input: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## What is an Embedding Model?

**Basic concept:** An embedding model is a technique that converts high-dimensional discrete data (text, images, etc.) into low-dimensional continuous vectors. This transformation allows machines to better understand and process complex data. Imagine simplifying a complex puzzle into a simple coordinate point that still retains the puzzle's key features. In the large model ecosystem, it acts as a "translator," converting human-understandable information into computable numerical forms for AI.

**Working principle:** Taking natural language processing as an example, an embedding model maps words to specific positions in vector space. In this space, semantically similar words automatically cluster together. For instance:
* Vectors for "king" and "queen" will be very close
* Words like "cat" and "dog" will also be nearby
* Semantically unrelated words like "car" and "bread" will be distant

**Main application scenarios:**
* Text analysis: Document classification, sentiment analysis
* Recommendation systems: Personalized content recommendations
* Image processing: Similar image retrieval
* Search engines: Semantic search optimization

**Core advantages:**
1. Dimensionality reduction: Simplifies complex data into manageable vector forms
2. Semantic preservation: Retains key semantic information from original data
3. Computational efficiency: Significantly improves training and inference efficiency for ML models

**Technical value:** Embedding models are foundational components of modern AI systems, providing high-quality data representations for machine learning tasks, serving as key technologies driving advancements in NLP, computer vision, and other fields.

***

## How Embedding Models Work in Knowledge Retrieval

**Basic workflow:**

1. **Knowledge base preprocessing phase**
* Split documents into appropriately sized chunks
* Convert each chunk into vectors using embedding models
* Store vectors and original text in vector databases

2. **Query processing phase**
* Convert user questions into vectors
* Retrieve similar content from vector databases
* Provide retrieved relevant content as context to LLMs

***

## What is MCP (Model Context Protocol)?

MCP is an open-source protocol designed to provide context information to large language models (LLMs) in a standardized manner.

* **Analogy:** Think of MCP as a "USB drive" for the AI field. Just as USB drives store various files that become immediately usable when plugged into a computer, the MCP Server can "plug in" various context-providing "plugins." LLMs can request these plugins from the MCP Server as needed, acquiring richer context information to enhance their capabilities.
* **Comparison with Function Tools:** Traditional Function Tools also provide external capabilities to LLMs, but MCP represents a higher-level abstraction. Function Tools are more task-specific utilities, while MCP offers a more universal, modular context acquisition mechanism.

### Core Advantages of MCP

1. **Standardization:** Provides unified interfaces and data formats enabling seamless collaboration between different LLMs and context providers.
2. **Modularity:** Allows developers to decompose context information into independent modules (plugins) for easy management and reuse.
3. **Flexibility:** LLMs can dynamically select required context plugins based on their needs, enabling smarter and more personalized interactions.
4. **Scalability:** The design supports future addition of more context plugin types, offering unlimited possibilities for expanding LLM capabilities.

***