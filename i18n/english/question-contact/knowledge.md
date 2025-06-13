---
icon: book-bookmark
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# AI Concepts

## What are tokens?

Tokens are the basic units that AI models use to process text. You can think of them as the smallest unit of "thought" for the model. They are not exactly equivalent to characters or words as we understand them, but rather a special way the model segments text.

#### 1. Chinese Tokenization

*   A Chinese character is usually encoded as 1-2 tokens.
*   For example: `"你好"` ≈ 2-4 tokens

#### 2. English Tokenization

*   Common words are usually 1 token.
*   Longer or less common words are broken down into multiple tokens.
*   For example:
    *   `"hello"` = 1 token
    *   `"indescribable"` = 4 tokens

#### 3. Special Characters

*   Spaces, punctuation marks, etc., also consume tokens.
*   A newline character is usually 1 token.

{% hint style="info" %}
The tokenizers of different service providers are not the same, and even the tokenizers of different models from the same provider can vary. This information is only intended to clarify the concept of a token.
{% endhint %}

***

## What is a Tokenizer?

A Tokenizer is the tool an AI model uses to convert text into tokens. It determines how to split the input text into the smallest units that the model can understand.

### Why do different models have different Tokenizers?

#### 1. Different Training Data

*   Different corpora lead to different optimization directions.
*   Varying degrees of multilingual support.
*   Specialized optimizations for specific domains (e.g., medical, legal).

#### 2. Different Tokenization Algorithms

*   BPE (Byte Pair Encoding) - OpenAI GPT series
*   WordPiece - Google BERT
*   SentencePiece - Suitable for multilingual scenarios

#### 3. Different Optimization Goals

*   Some focus on compression efficiency.
*   Some focus on semantic preservation.
*   Some focus on processing speed.

### Practical Impact

The same text may have a different number of tokens in different models:

```
Input: "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## What is an Embedding Model?

**Basic Concept:** An embedding model is a technique that converts high-dimensional discrete data (text, images, etc.) into low-dimensional continuous vectors. This transformation allows machines to better understand and process complex data. Imagine it as simplifying a complex puzzle into a simple coordinate point that still retains the key features of the puzzle. In the large model ecosystem, it acts as a "translator," converting human-understandable information into a numerical form that AI can compute.

**How it Works:** Taking natural language processing as an example, an embedding model can map words to specific positions in a vector space. In this space, words with similar meanings will automatically cluster together. For example:

*   The vectors for "king" and "queen" will be very close.
*   Pet-related words like "cat" and "dog" will also be near each other.
*   Words with unrelated meanings, like "car" and "bread," will be far apart.

**Main Application Scenarios:**

*   Text analysis: document classification, sentiment analysis
*   Recommendation systems: personalized content recommendations
*   Image processing: similar image retrieval
*   Search engines: semantic search optimization

**Core Advantages:**

1.  Dimensionality Reduction: Simplifies complex data into easy-to-process vector form.
2.  Semantic Preservation: Retains key semantic information from the original data.
3.  Computational Efficiency: Significantly improves the training and inference efficiency of machine learning models.

**Technical Value:** Embedding models are fundamental components of modern AI systems. They provide high-quality data representations for machine learning tasks and are a key technology driving progress in fields like natural language processing and computer vision.

***

## How Embedding Models Work in Knowledge Retrieval

**Basic Workflow:**

1.  **Knowledge Base Preprocessing Stage**
    *   Split documents into appropriately sized chunks.
    *   Use an embedding model to convert each chunk into a vector.
    *   Store the vectors and the original text in a vector database.

2.  **Query Processing Stage**
    *   Convert the user's question into a vector.
    *   Retrieve similar content from the vector database.
    *   Provide the retrieved relevant content to the LLM as context.

***

## **What is MCP (Model Context Protocol)?**

MCP is an open-source protocol designed to provide contextual information to Large Language Models (LLMs) in a standardized way.

*   **Analogy:** You can think of MCP as the "USB drive" of the AI world. We know that a USB drive can store various files and be used directly after being plugged into a computer. Similarly, various "plugins" that provide context can be "plugged" into an MCP Server. An LLM can request these plugins from the MCP Server as needed to obtain richer contextual information and enhance its capabilities.
*   **Comparison with Function Tools:** Traditional Function Tools can also provide external functionalities for LLMs, but MCP is more like a higher-dimensional abstraction. A Function Tool is more of a tool for specific tasks, whereas MCP provides a more general, modular mechanism for acquiring context.

### **Core Advantages of MCP**

1.  **Standardization:** MCP provides a unified interface and data format, allowing different LLMs and context providers to collaborate seamlessly.
2.  **Modularity:** MCP allows developers to break down contextual information into independent modules (plugins), making them easier to manage and reuse.
3.  **Flexibility:** LLMs can dynamically select the required context plugins based on their needs, enabling more intelligent and personalized interactions.
4.  **Extensibility:** MCP's design supports the future addition of more types of context plugins, offering limitless possibilities for expanding the capabilities of LLMs.

***