---
icon: book-open-cover
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Knowledge Base Tutorial

In version 0.9.1, CherryStudio introduced the long-awaited knowledge base feature.

Below, we will provide detailed instructions for using CherryStudio step-by-step.

## Add Embedding Model

1.  In the Model Management service, find a model. You can click "Embedding Model" to filter quickly;
2.  Find the model you need and add it to "My Models".

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Create a Knowledge Base

1.  Knowledge Base Entry: On the left toolbar of CherryStudio, click the knowledge base icon to enter the management page;
2.  Add Knowledge Base: Click "Add" to start creating a knowledge base;
3.  Naming: Enter a name for the knowledge base and add an embedding model, for example, bge-m3, to complete the creation.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Add Files and Vectorize

1.  Add Files: Click the "Add Files" button to open the file selector;
2.  Select Files: Choose supported file formats like pdf, docx, pptx, xlsx, txt, md, mdx, etc., and open them;
3.  Vectorization: The system will automatically perform vectorization. When it shows "Completed" (green ✓), it means vectorization is finished.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Add Data from Multiple Sources

CherryStudio supports adding data in multiple ways:

1.  Folder Directory: You can add an entire folder directory. Files in supported formats within this directory will be automatically vectorized;
2.  URL Link: Supports website URLs, such as [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3.  Sitemap: Supports XML-formatted sitemaps, such as [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4.  Plain Text Note: Supports inputting custom content as plain text.

{% hint style="info" %}
Tip:

1.  Illustrations in documents imported into the knowledge base are not yet supported for vector conversion and need to be manually converted to text;
2.  Using a website URL as a knowledge base source may not always be successful. Some websites have strict anti-scraping mechanisms (or require login, authorization, etc.), so this method may not retrieve accurate content. It is recommended to test by searching after creation.
3.  Most websites provide a sitemap, like CherryStudio's [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml). Generally, you can get related information by adding /sitemap.xml after the root address (URL) of the website, e.g., `aaa.com/sitemap.xml`.
4.  If a website does not provide a sitemap or the URLs are complex, you can create your own sitemap.xml file. The file must be provided as a direct link that is publicly accessible on the internet; local file links will not be recognized.

> 1) You can ask an AI to generate a sitemap file or write an HTML sitemap generator tool;
> 2) Direct links can be generated using methods like OSS direct links or cloud storage direct links. If you don't have a ready-made tool, you can go to the [ocoolAI](https://one.ocoolai.com/login) official website, log in, and use the free file upload tool in the top bar to generate a direct link.
{% endhint %}

## Search the Knowledge Base

Once files and other materials have been vectorized, you can start querying:

1.  Click the "Search Knowledge Base" button at the bottom of the page;
2.  Enter your query;
3.  The search results will be displayed;
4.  And the match score for each result will be shown.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Referencing the Knowledge Base to Generate Replies in a Conversation

1.  Create a new topic. In the conversation toolbar, click on the knowledge base icon. A list of created knowledge bases will expand. Select the one you want to reference;
2.  Enter and send your question. The model will return an answer generated from the search results;
3.  Additionally, the referenced data sources will be attached below the answer, allowing for quick access to the source files.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>