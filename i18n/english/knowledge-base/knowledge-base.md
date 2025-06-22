---
icon: book-open-cover
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Knowledge Base Tutorial

In version 0.9.1, Cherry Studio introduces the long-awaited knowledge base feature. Below is the step-by-step guide to using Cherry Studio's knowledge base.

## Add Embedding Models
1. Find models in the Model Management Service. You can quickly filter by clicking "Embedding Models".
2. Locate the required model and add it to My Models.

<figure><img src="../.gitbook/assets/image.webp" alt=""><figcaption></figcaption></figure>

## Create Knowledge Base
1. Access: Click the Knowledge Base icon in Cherry Studio's left toolbar to enter the management page.
2. Add Knowledge Base: Click "Add" to start creating.
3. Naming: Enter a name for the knowledge base and add an embedding model (e.g., bge-m3) to complete creation.

<figure><img src="../.gitbook/assets/image-1 (1).webp" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image-2 (1).webp" alt=""><figcaption></figcaption></figure>

## Add Files and Vectorize
1. Add Files: Click the "Add Files" button to open file selection.
2. Select Files: Choose supported file formats (pdf, docx, pptx, xlsx, txt, md, mdx, etc.) and open.
3. Vectorization: The system automatically vectorizes files. A green checkmark (✓) indicates completion.

<figure><img src="../.gitbook/assets/image-3.webp" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image-4.webp" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image-5.webp" alt=""><figcaption></figcaption></figure>

## Add Data from Multiple Sources
Cherry Studio supports adding data through:
1. Folder Directories: Entire directories where supported format files are auto-vectorized.
2. URL Links: e.g., `https://docs.siliconflow.cn/introduction`
3. Sitemaps: XML format sitemaps, e.g., `https://docs.siliconflow.cn/sitemap.xml`
4. Plain Text Notes: Custom content input.

{% hint style="info" %}
Tips:
1. Illustrations in documents cannot currently be vectorized automatically - convert to text manually.
2. URL-based imports may fail due to anti-scraping mechanisms (login requirements, etc.). Always test after creation.
3. Most websites provide sitemaps (e.g., Cherry Studio's [sitemap](https://docs.cherry-ai.com/sitemap-pages.xml)). Try `/sitemap.xml` at root address (e.g., `example.com/sitemap.xml`).
4. For custom sitemaps, use publicly accessible direct links (local files unsupported):
   > 1) Generate sitemaps using AI tools;
   > 2) Use OSS direct links or upload via [ocoolAI's tool](https://one.ocoolai.com/login).
{% endhint %}

## Search Knowledge Base
After vectorization:
1. Click "Search Knowledge Base" at bottom of page.
2. Enter query content.
3. View search results.
4. Matching scores are displayed per result.

<figure><img src="../.gitbook/assets/image-7.webp" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image-8.webp" alt=""><figcaption></figcaption></figure>

## Reference Knowledge Base in Conversations
1. Create new topic > Click "Knowledge Base" in toolbar > Select target knowledge base.
2. Enter question > Model generates answer using retrieved knowledge.
3. Data sources appear below answer for quick reference.

<figure><img src="../.gitbook/assets/image-9.webp" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image-10.webp" alt=""><figcaption></figcaption></figure>