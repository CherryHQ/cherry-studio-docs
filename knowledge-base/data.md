---
icon: database
---

# 知识库工作原理

本页面向希望了解知识库底层工作机制的用户。若只需要使用知识库，可直接参考 [知识库教程](knowledge-base.md)。

## 核心原理

加入知识库的文档会被**切分为小片段 → 由嵌入模型转换为数字向量 → 存入本地数据库**。提问时，知识库会将问题转换为同类向量，检索最相似的片段，并将这些片段提供给对话模型作为上下文。

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067 (1).png" alt=""><figcaption><p>知识库处理流程图</p></figcaption></figure>

## 详细一点

1. **入库前的准备**
   - 文档（PDF、Word、网页等）先经过 [文档预处理](document-preprocessing.md)（OCR 等），变成纯文本
   - 纯文本被切成 200-500 字左右的小片段（chunk），方便检索

2. **嵌入与存储**
   - 每个片段交给 [嵌入模型](emb-models-info.md) 处理，得到一组数字（向量）
   - 这些数字 + 原文片段都存在 Cherry Studio 本地的数据库里（基于开源的 libSQL）

3. **查询**
   - 你提问时，问题文本同样被嵌入模型转成数字
   - 系统找出"和问题数字最像"的若干片段
   - 这些片段连同问题一起送给对话模型，由它生成最终答案

## 数据存储位置

**所有数据保存在本地**，不会上传到云端（若使用的嵌入模型本身是云服务，文本片段会在嵌入处理过程中短暂经过该服务）。

* **macOS**：`~/Library/Application Support/CherryStudio`
* **Windows**：`%APPDATA%\CherryStudio`
* **Linux**：`~/.config/CherryStudio`

## 数据隐私建议

如资料涉及敏感信息（合同、医疗、内部代码等）：

* 使用**本地嵌入模型**（如通过 [Ollama](../pre-basic/providers/ollama.md) 或 [LM Studio](../pre-basic/providers/lm-studio.md) 运行 `bge-m3`），全流程离线
* 对话模型同样建议选择本地部署
* 可配合 [修改存储位置](../pre-basic/personalization-settings/storage.md) 将数据存放至加密磁盘

## 延伸阅读

* 向量数据库（libSQL / Turso）：[https://turso.tech/libsql](https://turso.tech/libsql)
* 嵌入与检索增强生成：可查阅"vector embedding"、"RAG"相关资料
