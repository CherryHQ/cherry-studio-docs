---
icon: face-viewfinder
---

# Document Preprocessing

Document preprocessing converts PDFs, Word documents, spreadsheets, and other files into Markdown text that is more suitable for retrieval before chunking and vectorization. It is primarily useful for scans, complex layouts, tables, and multicolumn documents.

If a document already has a clear text layer, Cherry Studio's built-in reader will usually work. Do not enable an online processor for every file by default simply because it seems “more advanced.” First compare actual results with a small set of sources.

## Processing Workflow

When no document processor is selected:

1. Cherry Studio reads supported files directly.
2. It extracts and chunks the text.
3. It calls the embedding model to build an index.

After selecting a document processor:

1. Cherry Studio sends the document to the selected processor.
2. The processor outputs Markdown.
3. The app manages the Markdown as a processing artifact.
4. Cherry Studio then chunks it and builds the index.

{% hint style="info" %}
The document processor “turns a file into searchable text,” the embedding model “turns text into vectors,” and the chat model “answers using retrieved passages.” These are separate stages.
{% endhint %}

## Documents That Need Preprocessing

Consider using a document processor first when:

* A scanned PDF has no selectable text
* A PDF contains complex tables, multicolumn layouts, or many formulas
* Built-in parsing produces a disorganized structure for Word, Excel, or similar files
* Key content is contained in images or the page layout
* Retrieved passages contain garbled text, incorrect ordering, or substantial omissions

Additional processing is usually unnecessary when:

* Plain text, Markdown, CSV, or another text file already has a clear structure
* A PDF has a complete text layer and a simple layout
* Built-in parsing already produces correct previews and retrieval test results

Preprocessing cannot solve every problem automatically. Handwriting, low-resolution scans, complex formulas, and nested tables can still be recognized incorrectly.

## Processing Capabilities Supported in V2

Cherry Studio divides file processing into two categories:

| Capability | Input | Output | Relationship to knowledge bases |
| --- | --- | --- | --- |
| Document to Markdown | Document file | Markdown | Can be selected in knowledge base RAG Settings |
| Image to text | Image | Text | Used for other image OCR scenarios; it is not the same as knowledge base document processing |

The current knowledge base add interface does not accept an image as a standalone data source. To process a PDF or Office document that contains images, select a processor that supports **Document to Markdown**.

## Available Document Processors

In the current V2 `main` branch, knowledge bases can use these Document to Markdown processors:

| Processor | Deployment | Common configuration |
| --- | --- | --- |
| Mistral OCR | Online API | API Key, API Host, model |
| MinerU | Online API | API Key, API Host |
| Doc2X | Online API | API Key, API Host |
| Open MinerU | Self-hosted service | Local or private-network API Host |
| PaddleOCR | API service or self-hosted deployment | API Key, API Host, parsing model |

The items shown depend on the current system and app version. Provider endpoints, models, and application procedures can change; use the live interface under **Settings → Document Processing** as the source of truth.

{% hint style="warning" %}
Online processors usually require uploading the original file. Before importing contracts, internal material, or personal information, review the provider's data policy, deployment region, and deletion mechanism. Prefer a local or self-hosted processor for sensitive sources.
{% endhint %}

## Configure a Document Processor

1. Open **Settings → Document Processing**.
2. Select a processor that supports Document to Markdown from the left side.
3. Enter the API Key required by the processor.
4. Check the API Host. For a self-hosted service, enter an address that is actually accessible.
5. If the interface provides a model option, select a model deployed on the server.
6. Click **Set as Default** to use it as the default processor for general document processing.

The API Key field can manage multiple keys. Do not include keys in documentation, screenshots, or feedback logs.

### Online Processors

An online processor requires:

* A valid API Key and an account in good standing
* An API Host that matches the account's region
* Network access to the service
* A model that currently supports document parsing
* Files whose size and format comply with the provider's limits

### Open MinerU

Open MinerU connects to a self-hosted MinerU service. The default address is suitable only for local testing. If the service runs in a container, on a remote host, or on another port, enter a complete address that can be reached from the device running Cherry Studio.

### PaddleOCR

PaddleOCR supports configuring a parsing model. The model name must match one deployed on the server. A preset in the app interface does not mean that the corresponding model is installed on your server.

## Image OCR and Knowledge Base Document Processing

The Settings page might also show image-to-text processors such as system OCR, Tesseract, PaddleOCR, Mistral, and OpenVINO OCR.

* System OCR appears only on supported platforms
* Tesseract supports selecting recognition languages
* OpenVINO OCR appears only when the runtime environment meets its requirements
* PaddleOCR and Mistral might support both image and document capabilities

These image OCR settings do not automatically replace the Document to Markdown selection in a knowledge base. When processing PDF, DOCX, XLSX, or other documents, select a document processor in that knowledge base's RAG Settings.

## Enable It in a Knowledge Base

1. Open the target knowledge base.
2. Click **RAG Settings** at the top.
3. Under **File Processor**, select a configured document processor.
4. Save the settings.
5. Add a test document and wait for its status to become Completed.

A new knowledge base does not require a file processor by default. Only after you select one will supported document files enter the Document to Markdown workflow.

{% hint style="warning" %}
Changing the file processor does not automatically rewrite sources that have already completed processing. To use the new processor with an existing source, reindex that data source.
{% endhint %}

## Verify Processing Results

Do not rely only on a “Completed” status. Perform at least these three checks.

### 1. Preview the Source

Select **Preview Source** from the More menu on the data source row, then check:

* Whether headings and paragraphs are in the correct order
* Whether tables retain their row and column relationships
* Whether page headers and footers introduce excessive noise
* Whether key numbers, proper nouns, and formulas are recognized correctly
* Whether pages are missing, blank, or garbled

### 2. Review the Chunks

Open the chunk details and check whether content is split at sensible positions. Even if the parsed result is complete, poor chunking can still affect retrieval.

### 3. Run a Retrieval Test

Test retrieval with questions that are actually answered in the document:

* Specific values from tables
* Information that spans paragraphs
* Proper nouns and identifiers
* Text that OCR might easily confuse

If the correct text was not extracted, switch processors or improve the original file first. If the text is correct but retrieval performs poorly, adjust chunking and retrieval settings.

## Compare Processors

Choose three to five representative documents and run the same tests with each candidate processor.

| Dimension | Result to observe |
| --- | --- |
| Completeness | Whether pages, paragraphs, or tables are missing |
| Order | Whether multicolumn content and page numbers are ordered correctly |
| Accuracy | Whether numbers, symbols, and proper nouns are correct |
| Structure | Whether headings, lists, and tables are preserved |
| Speed | Processing time for one document and for a batch |
| Reliability | Whether timeouts or failures occur frequently |
| Privacy and cost | Whether original content is uploaded and how usage is billed |

The same processor can perform differently across document types. Contracts, papers, reports, and scanned receipts do not need to use the same configuration.

## Frequently Asked Questions

### No File Processor Option Appears in the Knowledge Base

Confirm that you opened RAG Settings at the top of the knowledge base and check the app version. A knowledge base lists only processors that support Document to Markdown, not processors with image OCR capability only.

### Document Processing Keeps Waiting

A remote processor might use a background task. Keep the app running, then check the network and provider task status. After a timeout, the source shows a Failed status; fix the configuration and reindex it.

### An API Key or Host Error Appears

Check whether the key has extra spaces, the Host includes the correct protocol, the account region matches, and the self-hosted service is reachable from the current device.

### A Scanned PDF Is Still Empty After Processing

Confirm that you selected a Document to Markdown processor rather than a processor that supports only image to text. Also check the scan resolution, page orientation, and languages supported by the provider.

### Table Parsing Is Disorganized

Use Preview Source to confirm that the problem comes from document processing rather than chunking. You can switch to a processor that handles complex layouts better or export critical tables to a simpler file structure before importing them.

### Results Do Not Change After Switching Processors

Changing the processor affects only subsequent processing. Reindex existing data sources and wait for the new processing task to complete.

### Does Regular Markdown Use the Online Processor?

Document preprocessing starts only for files recognized as document types when a processor is selected for the knowledge base. Text and Markdown files proceed directly to reading and indexing.

## Privacy and Costs

Online document processing can incur upload, parsing, and storage charges. After processing, Cherry Studio still calls the embedding model. If reranking and an online chat model are enabled, later retrieval and answers can also incur charges.

For the complete data flow and backup guidance, see [Knowledge Base Data](data.md).

***

### Get Help and Submit Feedback

If you encounter problems during document processing, OCR, or knowledge base indexing, contact the community using the information in [Feedback and Suggestions](../question-contact/suggestions.md).
