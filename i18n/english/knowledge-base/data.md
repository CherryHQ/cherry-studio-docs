---
icon: database
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Data Storage Explanation

All data added to the Cherry Studio knowledge base is stored locally. During the addition process, a copy of the document will be placed in the Cherry Studio data storage directory.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Knowledge Base Processing Flowchart</p></figcaption></figure>

Vector Database: [https://turso.tech/libsql](https://turso.tech/libsql)

After a document is added to the Cherry Studio knowledge base, the file will be split into several chunks, and then these chunks will be processed by an embedding model.

When using a large model for Q&A, text chunks related to the question will be retrieved and sent to the large language model for processing.

If you have data privacy requirements, it is recommended to use a local embedding database and a local large language model.