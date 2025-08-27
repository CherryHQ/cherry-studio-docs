---
icon: route
---
# Trace Usage Guide


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Feature Introduction

Trace provides users with dialogue insights, helping them understand the specific performance of models, knowledge bases, MCP, web search, etc., during the conversation process. It is an observability tool implemented based on [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), which enables visualization through client-side data collection, storage, and processing, providing quantitative evaluation basis for problem localization and performance optimization.

Each conversation corresponds to one trace data, and a trace is composed of multiple spans. Each span corresponds to a program processing logic in Cherry Studio, such as calling a model session, calling MCP, calling a knowledge base, calling web search, etc. Traces are displayed in a tree structure, with spans as tree nodes. The main data includes time consumption and token usage. Of course, the specific input and output can also be viewed in the span details.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Enabling Trace

By default, after Cherry Studio is installed, Trace is hidden. It needs to be enabled in "Settings" - "General Settings" - "Developer Mode", as shown below:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Also, Trace records will not be generated for previous sessions; they will only be generated after new questions and answers occur. The generated records are stored locally. If you need to clear Trace completely, you can do so by going to "Settings" - "Data Settings" - "Data Directory" - "Clear Cache", or by manually deleting files under `~/.cherrystudio/trace`, as shown below:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Scenario Introduction

### View Full Trace

Click "Trace" in the Cherry Studio chat window to view the full trace data. Regardless of whether a model, web search, knowledge base, or MCP was called during the conversation, you can view the full trace data in the trace window.

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### View Model in Trace

If you want to view the details of a model in the trace, click on the model call node to view its input and output details.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### View Web Search in Trace

If you want to view the details of a web search in the trace, click on the web search call node to view its input and output details. In the details, you can see the question queried by the web search and its returned results.

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### View Knowledge Base in Trace

If you want to view the details of a knowledge base in the trace, click on the knowledge base call node to view its input and output details. In the details, you can see the question queried by the knowledge base and its returned answer.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### View MCP Call Details in Trace

If you want to view the details of MCP in the trace, click on the MCP call node to view its input and output details. In the details, you can see the input parameters for calling this MCP Server tool and the tool's return.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Questions and Suggestions

This feature is provided by the Alibaba Cloud [EDAS](https://www.aliyun.com/product/edas) team. If you have any questions or suggestions, please join the DingTalk group (Group ID: 21958624) for in-depth communication with the developers.