---
icon: database
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Data Storage Instructions

Data added to the Cherry Studio knowledge base is entirely stored locally. During the addition process, a copy of the document will be placed in the Cherry Studio data storage directory.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Knowledge Base Processing Flowchart</p></figcaption></figure>

Vector Database: [https://turso.tech/libsql](https://turso.tech/libsql)

After documents are added to the Cherry Studio knowledge base, they are segmented into multiple fragments. These fragments are then processed by the embedding model.

When using large models for Q&A, relevant text fragments matching the query will be retrieved and processed together by the large language model.

If you have data privacy requirements, it is recommended to use local embedding databases and local large language models.