
{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Infini-AI Cloud

Have you ever experienced: saving 26 insightful articles in WeChat that you never open again, storing over 10 scattered files in a "Study Materials" folder on your computer, or trying to recall a theory you read half a year ago only to remember fragmented keywords? And when daily information exceeds your brain's processing limit, 90% of valuable knowledge gets forgotten within 72 hours.  
Now, by leveraging the Infini-AI large model service platform API + Cherry Studio to build a personal knowledge base, you can transform dust-collecting WeChat articles and fragmented course content into structured knowledge for precise retrieval.

### 1. Building Personal Knowledge Base

#### 1. Infini-AI API Service: The Stable "Thinking Hub" of Knowledge Bases  
Serving as the "thinking hub" of knowledge bases, the Infini-AI large model service platform offers robust API services including full-capacity DeepSeek R1 and other model versions. **Currently free to use without barriers after registration.** Supports mainstream embedding models (bge, jina) for knowledge base construction. **The platform continuously updates with the latest, most powerful open-source models**, covering multiple modalities like images, videos, and audio.

<figure><img src="../../.gitbook/assets/1280X1280 (1) (1).PNG" alt=""><figcaption></figcaption></figure>

#### 2. Cherry Studio: Zero-Code Knowledge Base Setup  
Compared to RAG knowledge base development requiring 1-2 months deployment time, Cherry Studio offers a significant advantage: **zero-code operation**. Instantly import multiple formats like Markdown/PDF/web pages – parsing 40MB files in 1 minute. Easily add local folders, saved WeChat articles, and course notes.

<figure><img src="../../.gitbook/assets/output (1).png" alt=""><figcaption></figcaption></figure>

### II. 3 Steps to Build Your Personal Knowledge Manager

#### Step 1: Basic Preparation  
1. Download the suitable version from Cherry Studio official site ([https://cherry-ai.com/](https://cherry-ai.com/))  
2. Register account: Log in to Infini-AI platform ([https://cloud.infini-ai.com/genstudio/model?cherrystudio](https://cloud.infini-ai.com/genstudio/model?cherrystudio))  

<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

* Get API key: Select "deepseek-r1" in Model Square, create and copy the API key + model name  
<figure><img src="../../.gitbook/assets/output (1).png" alt=""><figcaption></figcaption></figure>

#### Step 2: CherryStudio Settings  
Go to model services → Select Infini-AI → Enter API key → Activate Infini-AI service  

<figure><img src="../../.gitbook/assets/1280X1280 (2) (1).png" alt=""><figcaption></figcaption></figure>

After setup, select the large model during interaction to use Infini-AI API in CherryStudio.  
*Optional: Set as default model for convenience*  
<figure><img src="../../.gitbook/assets/01445ab7-b863-4155-b517-2b6c3c581f47.png" alt=""><figcaption></figcaption></figure>

#### Step 3: Add Knowledge Base  
Choose any version of bge-series or jina-series embedding models from Infini-AI platform  

<figure><img src="../../.gitbook/assets/1 (1).png" alt=""><figcaption></figcaption></figure>  
<figure><img src="../../.gitbook/assets/2 (2).png" alt=""><figcaption></figcaption></figure>

### III. Real User Scenario Test  
* After importing study materials, query: "Outline core formula derivations in Chapter 3 of 'Machine Learning'"  

<figure><img src="../../.gitbook/assets/6bbdbd0d-5db4-4440-b840-3bb3f422b831.gif" alt=""><figcaption></figcaption></figure>  

**Result Demonstration**  
<figure><img src="../../.gitbook/assets/3.gif" alt=""><figcaption></figcaption></figure>