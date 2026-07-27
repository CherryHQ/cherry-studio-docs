---
icon: books
---

# Knowledge Base

A knowledge base organizes documents, web pages, and other material into a searchable reference library. During a chat, Cherry Studio retrieves relevant chunks from the knowledge base and sends them to the model to generate an answer.

A knowledge base does not train or modify the model. It is better suited to material that you need to query repeatedly, reuse across chats, or manage in large volumes.

{% hint style="info" %}
This page provides a quick start for knowledge bases. For details about every parameter, see the [complete Knowledge Base guide](../../knowledge-base/knowledge-base.md).
{% endhint %}

## Before you begin

Before creating a knowledge base, enable at least one model with **Embedding** capabilities. An embedding model converts your material and questions into searchable data.

Confirm the following in advance:

* Model Services are configured and the embedding model can be called successfully
* An appropriate document processing method is configured for scanned PDFs or complex documents
* A Rerank model is available if you later need to improve result ordering

See:

* [Embedding model reference](../../knowledge-base/emb-models-info.md)
* [Document preprocessing](../../knowledge-base/zhi-shi-ku-wen-dang-yu-chu-li.md)

## Create a knowledge base

1. Open **Knowledge Base** from the Launchpad.
2. Click the add button on the left and select the option to create a knowledge base.
3. Enter a knowledge base name.
4. Place the knowledge base in an existing group if needed.
5. Select an enabled embedding model and complete the creation.

{% hint style="warning" %}
The embedding model and vector dimensions determine the knowledge base index format. Changing the model or dimensions later requires rebuilding the knowledge base, so choose the configuration before importing material in bulk.
{% endhint %}

## Add material

Open the knowledge base, click the option to add material, and select a source.

| Source | Suitable content | Current behavior |
| --- | --- | --- |
| Files | One or more local files | Supports PDF, DOCX, MD, XLSX, TXT, CSV, and EPUB |
| Folder | A collection of local material | Select a folder to import its files in bulk |
| URL | One web page | Enter a web address and extract the page content |
| Sitemap | Multiple pages on a website | Enter a Sitemap address to discover pages in bulk |
| Note | Manually entered content | Submission is not yet available in the current add dialog |

After submitting the add task, you can close the dialog and continue using the app. Reading, chunking, and embedding continue in the background.

## Wait for indexing to finish

Material progresses through preparation, reading, processing, embedding, and other stages. Intermediate status names can vary by source; the final status should be **Completed**.

| Status | Meaning | Recommended action |
| --- | --- | --- |
| Preparing / Reading / Processing / Embedding | The index is being created | Keep the app running and wait |
| Completed | Available for retrieval and chat | Run a retrieval test first |
| Failed | The current material was not indexed completely | Fix the model, network, or file problem, then reindex |
| Deleting | The material and index are being removed | Wait for cleanup to finish |

Only indexed content can participate reliably in retrieval. You cannot force material that is still being processed to reindex; wait for it to complete or fail first.

## Review and manage material

The knowledge base data source page provides these actions:

* Filter by file, folder, URL, or Sitemap
* Search material names and view the number that are ready
* Preview extracted content
* View chunks created from the material
* Delete an individual chunk
* Reindex completed or failed material
* Select multiple items to reindex or delete them in bulk

If the original file has changed, reindexing replaces the old index with the new content. When you delete material, its retrieval data is also removed asynchronously.

## Run a retrieval test first

Open **Retrieval Test** at the top of the knowledge base and enter a question that a real user might ask.

The results show matching chunks, scores, ranking, and elapsed time. Check:

* Whether the correct material appears among the first few results
* Whether the retrieved chunks contain the information needed to answer the question
* Whether chunks are too long, too short, or split incorrectly
* Whether too many irrelevant results appear

If the retrieval results are inaccurate, the chat model usually cannot provide a reliable answer either. Adjust the material or retrieval configuration before testing the chat experience.

## Use the knowledge base in Chat

### Select a knowledge base temporarily

1. Open **Chat** and enter a conversation.
2. Open the knowledge base selector in the input toolbar.
3. Select one or more knowledge bases.
4. Ask a question about the material.

This entry is available only when the current assistant and tool mode support knowledge bases. Knowledge base selection is disabled when a file is attached to the input box; remove the attachment first.

### Attach it to an assistant

If an assistant needs to use the same material over time, open **Resource Library → Assistants**, edit the assistant, and associate the knowledge base. You will not need to select it again each time you use that assistant.

See [Assistants](agents.md) for more assistant settings.

{% hint style="warning" %}
The knowledge base supplies relevant chunks, but the chat model still generates the final answer. Verify important conclusions against cited chunks and the original material.
{% endhint %}

## Adjust RAG settings

Click the RAG Settings button at the top of the knowledge base to adjust the retrieval pipeline.

| Setting | Purpose | Adjustment guidance |
| --- | --- | --- |
| Document processor | Convert documents into text that can be chunked | Check this first for scans, images, or complex layouts |
| Chunk size and overlap | Define the scope of each retrieved chunk | Existing material must be reindexed after a change |
| Embedding model and dimensions | Generate and store the vector index | A change triggers a rebuild or recovery process |
| Search mode | Choose vector, keyword, or hybrid retrieval | Start with the default hybrid retrieval |
| Number of results | Control how many chunks are returned to the model | Too few may omit information; too many may add noise |
| Similarity threshold | Filter out results with insufficient relevance | Applies only in the corresponding retrieval modes |
| Hybrid weight | Balance semantic and keyword matching | For material with many proper nouns, adjust it with retrieval tests |
| Rerank model | Reorder the initial retrieval results | Adds another model call and more waiting time |

Change only one category of parameters at a time, then repeat the retrieval test with the same questions to determine which adjustment actually helps.

## Troubleshooting

### No embedding model is available during creation

Check that Model Services are enabled, the model has an embedding capability marker, and the API configuration works. Standard chat models do not appear in the embedding model list.

### Material remains in processing or shows Failed

Wait for the current task to finish, then check the network, Model Services, file format, and document processor. After fixing the issue, reindex the failed material.

### A scanned PDF contains no usable text

A scanned PDF usually contains only images and requires a document processing method that supports OCR or image parsing. See [Document preprocessing](../../knowledge-base/zhi-shi-ku-wen-dang-yu-chu-li.md).

### The correct content is not retrieved

First confirm that the material has finished indexing, then use Retrieval Test to locate the problem. Check the source quality, chunk size, search mode, number of results, threshold, and reranking configuration in order.

### Chat does not use the knowledge base

Confirm that the knowledge base is selected in the current chat, the target material has a Completed status, and the assistant and tool mode support knowledge bases. Remove any file attached to the input box.

## Data, privacy, and cost

Cherry Studio manages knowledge base metadata and vector indexes. Depending on the selected document processing, embedding, reranking, and chat services, original or extracted content may be sent to the corresponding provider. Retrieved chunks are also sent to the current chat model when generating an answer.

Before importing sensitive material, review the provider's data policy and deployment method. Indexing, reindexing, reranking, and chat responses may also incur model usage fees.

See [Knowledge Base data](../../knowledge-base/data.md) for related files and cleanup methods.

***

### Get help and submit feedback

If you encounter a problem while configuring or using a knowledge base, contact the community using the information under [Feedback and suggestions](../../question-contact/suggestions.md).
