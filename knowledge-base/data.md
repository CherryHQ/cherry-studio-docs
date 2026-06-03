---
icon: database
---

# 知识库背后是怎么工作的

如果你只想用知识库，**这一页不必看**；这是给好奇心强的读者讲背后原理的。

## 一句话原理

你放进去的文档会被**切成小片段 → 用嵌入模型转成"数字指纹" → 存进本地数据库**。之后你提问时，知识库会算一下你的问题的"数字指纹"，去找最像的那些片段，把它们塞进 AI 的视野里。

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

## 数据存在哪？

**全部存在本地**，不会发到云端（除非你用的嵌入模型本身是云服务，那么文本片段会在嵌入时短暂经过该服务）。

* **macOS**：`~/Library/Application Support/CherryStudio`
* **Windows**：`%APPDATA%\CherryStudio`
* **Linux**：`~/.config/CherryStudio`

## 数据隐私建议

如果资料特别敏感（合同、医疗、内部代码）：

* 用**本地嵌入模型**（如通过 [Ollama](../pre-basic/providers/ollama.md) 或 [LM Studio](../pre-basic/providers/lm-studio.md) 跑 `bge-m3`），整个流程完全离线
* 对话模型也尽量选本地（同上方案）
* 配合 [修改存储位置](../pre-basic/personalization-settings/storage.md) 把数据放到加密磁盘

## 想看具体技术细节？

* 向量数据库（libSQL / Turso）：[https://turso.tech/libsql](https://turso.tech/libsql)
* 嵌入相关原理：搜索"vector embedding"、"RAG"概念
