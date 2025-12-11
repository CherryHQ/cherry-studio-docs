---
icon: database
---

# 知识库数据

在 Cherry Studio 知识库中添加的数据全部存储在本地，在添加过程中会复制一份文档放在 Cherry Studio 数据存储目录

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067 (1).png" alt=""><figcaption><p>知识库处理流程图</p></figcaption></figure>

向量数据库：[https://turso.tech/libsql](https://turso.tech/libsql)

当文档被添加到 Cherry Studio 知识库之后，文件会被切分为若干个片段，然后这些片段会交给嵌入模型进行处理

当使用大模型进行问答的时候，会查询和问题相关的文本片段一并交个大语言模型处理

如果对数据隐私有要求，建议使用本地嵌入数据库和本地大语言模型
