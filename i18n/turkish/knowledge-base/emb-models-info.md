---
icon: square-info
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# Gömme Modelleri Referans Bilgileri

{% hint style="info" %}
Hata oluşmasını önlemek için, bu belgede bazı modellerin maksimum girdi (max input) değerleri sınır değer olarak yazılmamıştır. Örneğin: Resmi kaynakta maksimum girdi 8k olarak verildiğinde (spesifik değer belirtilmemişse), bu belgede 8191 veya 8000 gibi referans değerler kullanılmıştır. (Anlaşılamadıysa görmezden gelin, belgedeki referans değerleri kullanın)
{% endhint %}

### Volcano-Doubao

[Resmi Model Bilgisi Referans Adresi](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| Ad                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba

[Resmi Model Bilgisi Referans Adresi](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| Ad                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI

[Resmi Model Bilgisi Referans Adresi](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| Ad                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu

[Resmi Model Bilgisi Referans Adresi](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| Ad           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu

[Resmi Model Bilgisi Referans Adresi](https://bigmodel.cn/console/modelcenter/square)

| Ad          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan

[Resmi Model Bilgisi Referans Adresi](https://cloud.tencent.com/document/product/1729/102832)

| Ad                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan

[Resmi Model Bilgisi Referans Adresi](https://platform.baichuan-ai.com/docs/text-Embedding)

| Ad                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### Together

[Resmi Model Bilgisi Referans Adresi](https://docs.together.ai/docs/serverless-models#embedding-models)

| Ad                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina

[Resmi Model Bilgisi Referans Adresi](https://jina.ai/models/jina-embedding-b-en-v1)

| Ad                                 | max input |
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

[Resmi Model Bilgisi Referans Adresi](https://siliconflow.cn/zh-cn/models)

| Ad                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[Resmi Model Bilgisi Referans Adresi](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| Ad                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### Nomic

[Resmi Model Bilgisi Referans Adresi](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| Ad                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### Console

[Resmi Model Bilgisi Referans Adresi](https://console.upstage.ai/docs/capabilities/embeddings)

| Ad                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### Cohere

[Resmi Model Bilgisi Referans Adresi](https://docs.cohere.com/docs/models#embed)

| Ad                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |