---
icon: book-open-cover
---
# Knowledge Base Tutorial


{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}




In version 0.9.1, CherryStudio introduces the long-awaited knowledge base feature.

Below, we will present detailed instructions for using CherryStudio step-by-step.

## Add Embedding Model

1.  Find the model in the model management service, you can quickly filter by clicking "Embedding Model";
2.  Find the required model and add it to My Models.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Create Knowledge Base

1.  Knowledge Base Entry: On the left toolbar of CherryStudio, click the knowledge base icon to enter the management page;
2.  Add Knowledge Base: Click "Add" to start creating a knowledge base;
3.  Name: Enter the name of the knowledge base and add an embedding model. Taking bge-m3 as an example, you can complete the creation.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Add Files and Vectorize

1.  Add Files: Click the "Add files" button to open the file selection;
2.  Select Files: Choose supported file formats, such as pdf, docx, pptx, xlsx, txt, md, mdx, etc., and open them;
3.  Vectorization: The system will automatically perform vectorization. When it shows "Completed" (green ✓), it means vectorization is finished.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Add Data from Multiple Sources

CherryStudio supports multiple ways to add data:

1.  Folder Directory: You can add an entire folder directory, and supported format files within that directory will be automatically vectorized;
2.  Website Link: Supports URL links, such as [https://docs.siliconflow.cn/introduction](https://docs.siliconflow.cn/introduction);
3.  Sitemap: Supports XML-format sitemaps, such as [https://docs.siliconflow.cn/sitemap.xml](https://docs.siliconflow.cn/sitemap.xml);
4.  Plain Text Note: Supports entering custom content in plain text.

{% hint style="info" %}
Tips:

1.  Illustrations in documents imported into the knowledge base currently do not support conversion to vectors and need to be manually converted to text;
2.  Using a website as a knowledge base source may not always succeed. Some websites have strict anti-crawling mechanisms (or require login, authorization, etc.), so this method may not always obtain accurate content. It is recommended to test with a search after creation.
3.  Most websites provide a sitemap, such as CherryStudio's [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml). Generally, you can get relevant information by adding `/sitemap.xml` after the website's root address (i.e., URL). For example, `aaa.com/sitemap.xml`.
4.  If a website does not provide a sitemap or if the URLs are scattered, you can combine an XML sitemap file yourself. For now, the file needs to be filled in as a publicly accessible direct link; local file links will not be recognized.

> 1) You can have AI generate sitemap files or have AI write a sitemap HTML generator tool;
> 2) Direct links can be generated using OSS direct links or cloud drive direct links. If there is no existing tool, you can go to the [ocoolAI](https://one.ocoolai.com/login) official website, log in, and use the free file upload tool in the website's top bar to generate direct links.
{% endhint %}

## Search Knowledge Base

Once files and other data are vectorized, you can query them:

1.  Click the "Search Knowledge Base" button at the bottom of the page;
2.  Enter the query content;
3.  The search results will be displayed;
4.  And the matching score for each result will be shown.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Cite Knowledge Base in Conversation to Generate Replies

1.  Create a new topic. In the conversation toolbar, click "Knowledge Base," which will expand the list of created knowledge bases. Select the knowledge base you want to cite;
2.  Enter and send your question, and the model will return an answer generated from the retrieval results;
3.  At the same time, the cited data source will be attached below the answer, allowing quick access to the source file.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>