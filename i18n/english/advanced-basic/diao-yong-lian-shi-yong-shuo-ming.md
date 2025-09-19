---
icon: route
---
# Call Chain Usage Guide


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




## Feature Introduction

The call chain (also known as "trace") provides users with insights into conversations, helping them understand the specific performance of models, knowledge bases, MCP, network search, and other components during a conversation. It is an observability tool implemented based on [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), visualizing data collected, stored, and processed on the client side, providing quantitative evaluation basis for problem localization and effect optimization.

Each conversation corresponds to a trace data, and a trace is composed of multiple spans. Each span corresponds to a program processing logic within Cherry Studio, such as calling a model session, calling MCP, calling a knowledge base, or calling a network search. The trace is displayed in a tree structure, with spans as tree nodes. The main data includes time consumption and token usage. Of course, the specific input and output can also be viewed in the span details.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Enable Trace

By default, Trace is hidden after Cherry Studio is installed. It needs to be enabled in "Settings" - "General Settings" - "Developer Mode", as shown in the figure below:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Trace records will not be generated for previous sessions; they will only be generated after new questions and answers occur. The generated records are stored locally. If you need to completely clear the Trace, you can do so via "Settings" - "Data Settings" - "Data Directory" - "Clear Cache", or by manually deleting files under `~/.cherrystudio/trace`, as shown in the figure below:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Scenario Introduction

### Full Link View

Click on the call chain in the Cherry Studio dialog box to view the full link data of the call chain. Whether a model, network search, knowledge base, or MCP was called during the conversation, the full link call data can be viewed in the call chain window.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### View Models in the Link

If you want to view the details of the model in the call chain, you can click on the model call node to see its input and output details.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### View Network Search in the Link

If you want to view the details of the network search in the call chain, you can click on the network search call node to see its input and output details. In the details, you can see the question queried by the network search and its returned results.

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### View Knowledge Base in the Link

If you want to view the details of the knowledge base in the call chain, you can click on the knowledge base call node to see its input and output details. In the details, you can see the question queried by the knowledge base and its returned answer.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### View MCP Calls in the Link

If you want to view the details of MCP in the call chain, you can click on the MCP call node to see its input and output details. In the details, you can see the input parameters for calling this MCP Server tool and the tool's return.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Questions and Suggestions

This feature is provided by the Alibaba Cloud [EDAS](https://www.aliyun.com/product/edas) team. If you have any questions or suggestions, please join the DingTalk group (Group ID: 21958624) to communicate directly with the developers.