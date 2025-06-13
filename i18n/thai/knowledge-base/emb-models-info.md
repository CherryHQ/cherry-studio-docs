---
icon: square-info
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# ข้อมูลอ้างอิงโมเดลฝังตัว

{% hint style="info" %}
เพื่อป้องกันข้อผิดพลาด ในเอกสารนี้ค่าอินพุตสูงสุดของโมเดลบางรุ่นไม่ได้ถูกตั้งค่าเป็นค่าสูงสุดสุดท้าย ตัวอย่างเช่น เมื่อผู้ผลิตระบุค่าอินพุตสูงสุดเป็น 8k (ไม่ได้ระบุตัวเลขที่ชัดเจน) ค่าอ้างอิงในเอกสารนี้จะเป็น 8191 หรือ 8000 เป็นต้น (หากไม่เข้าใจให้ข้ามไปและใช้ค่าอ้างอิงในเอกสารได้เลย)
{% endhint %}

### Volcano-Doubao  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| ชื่อ                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| ชื่อ                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| ชื่อ                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| ชื่อ           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://bigmodel.cn/console/modelcenter/square)

| ชื่อ          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://cloud.tencent.com/document/product/1729/102832)

| ชื่อ                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://platform.baichuan-ai.com/docs/text-Embedding)

| ชื่อ                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://docs.together.ai/docs/serverless-models#embedding-models)

| ชื่อ                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://jina.ai/models/jina-embedding-b-en-v1)

| ชื่อ                                 | max input |
| ---------------------------------- | --------- |
| jina-embedding-b-en-v1             | 512       |
| jina-embeddings-v2-base-en         | 8191      |
| jina-embeddings-v2-base-zh         | 8191      |
| jina-embeddings-v2-base-de         | 8191      |
| jina-embeddings-v2-base-code       | 8191      |
| jina-embeddings-v2-base-es         | 8191      |
| jina-colbert-v1-en                 | 8191      |
| jina-reranker-v1-base-en           | 8191      |
| jina-reranker-v1-turbo-en          | 8191      |
| jina-reranker-v1-tiny-en           | 8191      |
| jina-clip-v1                       | 8191      |
| jina-reranker-v2-base-multilingual | 8191      |
| reader-lm-1.5b                     | 256000    |
| reader-lm-0.5b                     | 256000    |
| jina-colbert-v2                    | 8191      |
| jina-embeddings-v3                 | 8191      |

### SiliconFlow  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://siliconflow.cn/zh-cn/models)

| ชื่อ                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| ชื่อ                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### nomic  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| ชื่อ                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://console.upstage.ai/docs/capabilities/embeddings)

| ชื่อ                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere  
[ที่อยู่ข้อมูลอ้างอิงโมเดลอย่างเป็นทางการ](https://docs.cohere.com/docs/models#embed)

| ชื่อ                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |