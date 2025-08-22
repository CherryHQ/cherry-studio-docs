---
icon: route
---
# Trace Usage Guide


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Feature Introduction

Trace (also known as "call chain") provides users with insight into conversations, helping them understand the specific performance of models, knowledge bases, MCP, web search, etc., during a conversation. It is an observability tool implemented based on [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), which visualizes data through client-side collection, storage, and processing, providing quantitative evaluation basis for problem localization and performance optimization.

Each conversation corresponds to a trace, and a trace consists of multiple spans. Each span corresponds to a program processing logic in Cherry Studio, such as calling a model session, calling MCP, calling a knowledge base, calling web search, etc. A trace is displayed in a tree structure, with spans as tree nodes. The main data includes time consumption and token usage, and you can also view its specific input and output in the span details.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Enable Trace

By default, after Cherry Studio is installed, Trace is hidden. It needs to be enabled in "Settings" - "General Settings" - "Developer Mode", as shown below:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Furthermore, Trace records will not be generated for previous sessions; they will only be generated after new Q&A interactions occur. The generated records are stored locally. To completely clear the Trace, you can do so by going to "Settings" - "Data Settings" - "Data Directory" - "Clear Cache", or by manually deleting files under ~/.cherrystudio/trace, as shown below:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Scenario Introduction

### View Full Link Trace

In the Cherry Studio dialog box, click on the call chain to view the full link trace data. Whether a model, web search, knowledge base, or MCP was called during the conversation, you can view the full link call data in the call chain window.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### View Model in Trace

To view the details of a model in the call chain, you can click on the model call node to view its input and output details.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### View Web Search in Trace

To view the details of web search in the call chain, you can click on the web search call node to view its input and output details. In the details, you can see the query used for the web search and its returned results.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### View Knowledge Base in Trace

To view the details of the knowledge base in the call chain, you can click on the knowledge base call node to view its input and output details. In the details, you can see the query used for the knowledge base and its returned answer.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### View MCP Call in Trace

To view the details of MCP in the call chain, you can click on the MCP call node to view its input and output details. In the details, you can see the input parameters for calling this MCP Server tool and the tool's return.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Questions and Suggestions

The current functionality is provided by the Alibaba Cloud [EDAS](https://www.aliyun.com/product/edas) team. If you have any questions or suggestions, please join the DingTalk group (Group ID: 21958624) to communicate directly with the developers.