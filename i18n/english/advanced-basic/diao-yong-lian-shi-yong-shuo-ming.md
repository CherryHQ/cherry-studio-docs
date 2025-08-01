---
icon: route
---
# Trace Usage Guide


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Feature Introduction

The call chain (also known as "trace") provides users with insight into conversations, helping them understand the specific performance of models, knowledge bases, MCP, web searches, etc., during the conversation process. It is an observability tool implemented based on [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), which enables visualization through client-side data collection, storage, and processing, providing quantitative evaluation basis for problem localization and performance optimization.

Each conversation corresponds to a trace data, and a trace consists of multiple spans. Each span corresponds to a program processing logic in Cherry Studio, such as calling a model session, calling MCP, calling a knowledge base, or calling a web search. Traces are displayed in a tree structure, with spans as tree nodes. Key data includes time consumption and token usage. Of course, the specific input and output can also be viewed in the span details.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Enabling Trace

By default, after Cherry Studio is installed, Trace is in a hidden state. It needs to be enabled in "Settings" - "General Settings" - "Developer Mode", as shown below:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Also, Trace records will not be generated for previous sessions; they will only be generated after new Q&A occurs. The generated records are stored locally. If you need to thoroughly clear Trace, you can do so by going to "Settings" - "Data Settings" - "Data Directory" - "Clear Cache", or by manually deleting files under \~/.cherrystudio/trace, as shown below:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Scenario Introduction

### Full Link View

In the Cherry Studio dialog box, click on the call chain to view the full link data of the call chain. Whether a model, web search, knowledge base, or MCP was called during the conversation, you can view the full link call data in the call chain window.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Viewing Models in the Trace

To view the details of a model in the call chain, you can click on the model call node to see its input and output details.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Viewing Web Search in the Trace

To view the details of web search in the call chain, you can click on the web search call node to see its input and output details. In the details, you can see the query used for the web search and its returned results.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Viewing Knowledge Base in the Trace

To view the details of a knowledge base in the call chain, you can click on the knowledge base call node to see its input and output details. In the details, you can see the query used for the knowledge base and its returned answer.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Viewing MCP Calls in the Trace

To view the details of MCP in the call chain, you can click on the MCP call node to see its input and output details. In the details, you can see the parameters passed to this MCP Server tool and the tool's return value.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Questions and Suggestions

This feature is currently provided by the Alibaba Cloud [EDAS](https://www.aliyun.com/product/edas) team. If you have any questions or suggestions, please join the DingTalk group (Group ID: 21958624) for in-depth communication with the developers.