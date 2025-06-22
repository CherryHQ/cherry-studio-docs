---
icon: book-bookmark
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Knowledge Popularization

## What are Tokens?

Tokens are the basic units of text processed by AI models, understood as the smallest units of model "thinking". They are not entirely equivalent to the characters or words as we understand them, but rather a special way the model segments text itself.

#### 1. Chinese Tokenization
* A Chinese character is typically encoded as 1-2 tokens
* For example: `"你好"` ≈ 2-4 tokens

#### 2. English Tokenization
* Common words are typically 1 token
* Longer or uncommon words are decomposed into multiple tokens
* For example:
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Special Characters
* Spaces, punctuation, etc. also consume tokens
* Line breaks are typically 1 token

{% hint style="info" %}
Tokenizers vary across different service providers, and even different models from the same provider may have different tokenizers. This knowledge is solely for clarifying the concept of tokens.
{% endhint %}

***

## What is a Tokenizer?

A Tokenizer is the tool that converts text into tokens for AI models. It determines how to split input text into the smallest units that models can understand.

### Why do different models have different Tokenizers?

#### 1. Different Training Data
* Different corpora lead to different optimization directions
* Variations in multilingual support levels
* Specialized optimization for specific domains (medical, legal, etc.)

#### 2. Different Tokenization Algorithms
* BPE (Byte Pair Encoding) - OpenAI GPT series
* WordPiece - Google BERT
* SentencePiece - Suitable for multilingual scenarios

#### 3. Different Optimization Goals
* Some focus on compression efficiency
* Others on semantic preservation
* Others on processing speed

### Practical Impact
The same text may have different token counts across models:
```
Input: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## What is an Embedding Model?

**Basic Concept:** An embedding model is a technique that converts high-dimensional discrete data (text, images, etc.) into low-dimensional continuous vectors. This transformation allows machines to better understand and process complex data. Imagine it as simplifying a complex puzzle into a simple coordinate point that still retains the puzzle's key features. In the large model ecosystem, it serves as a "translator," converting human-understandable information into AI-computable numerical forms.

**Working Principle:** Taking natural language processing as an example, an embedding model maps words to specific positions in vector space. In this space:
* Vectors for "King" and "Queen" will be very close
* Pet-related words like "cat" and "dog" will cluster together
* Semantically unrelated words like "car" and "bread" will be distant

**Main Application Scenarios:**
* Text analysis: Document classification, sentiment analysis
* Recommendation systems: Personalized content recommendations
* Image processing: Similar image retrieval
* Search engines: Semantic search optimization

**Core Advantages:**
1. Dimensionality reduction: Simplifies complex data into manageable vector forms
2. Semantic preservation: Retains key semantic information from original data
3. Computational efficiency: Significantly improves training and inference efficiency

**Technical Value:** Embedding models are fundamental components of modern AI systems, providing high-quality data representations for machine learning tasks, and are key technologies driving advances in natural language processing, computer vision, and other fields.

***

## How Embedding Models Work in Knowledge Retrieval

**Basic Workflow:**
1. **Knowledge Base Preprocessing Stage**
   * Split documents into appropriately sized chunks
   * Use embedding models to convert each chunk into vectors
   * Store vectors and original text in a vector database

2. **Query Processing Stage**
   * Convert user questions into vectors
   * Retrieve similar content from the vector database
   * Provide retrieved context to the LLM

***

## What is MCP (Model Context Protocol)?

MCP is an open-source protocol designed to provide context information to large language models (LLMs) in a standardized way.

* **Analogy:** Think of MCP as a "USB drive" for AI. Just as USB drives can store various files and be plugged into computers for immediate use, MCP servers can "plug in" various context-providing "plugins". LLMs can request these plugins from MCP servers as needed to obtain richer context information and enhance their capabilities.
* **Comparison with Function Tools:** Traditional function tools provide external capabilities to LLMs, but MCP is a higher-level abstraction. Function tools focus on specific tasks, while MCP provides a more universal, modular context acquisition mechanism.

### Core Advantages of MCP
1. **Standardization:** Provides unified interfaces and data formats for seamless collaboration between LLMs and context providers.
2. **Modularity:** Allows developers to decompose context information into independent modules (plugins) for easy management and reuse.
3. **Flexibility:** Enables LLMs to dynamically select required context plugins for smarter, more personalized interactions.
4. **Extensibility:** Supports adding new types of context plugins in the future, providing unlimited possibilities for LLM capability expansion.

***