---
icon: square-info
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Informasi Referensi Model Embedding

{% hint style="info" %}
Untuk mencegah kesalahan, nilai max input beberapa model dalam dokumen ini tidak ditulis sebagai nilai batas maksimum. Contoh: ketika nilai input resmi maksimum adalah 8k (tanpa nilai pasti), nilai referensi dalam dokumen ini ditetapkan sebagai 8191 atau 8000 dll. (Jika tidak memahami, abaikan saja; isi sesuai nilai referensi dalam dokumen.)
{% endhint %}

### Volcengine - Doubao

[Alamat Referensi Informasi Model Resmi](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| Nama                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba

[Alamat Referensi Informasi Model Resmi](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| Nama                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI

[Alamat Referensi Informasi Model Resmi](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| Nama                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu

[Alamat Referensi Informasi Model Resmi](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| Nama           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu

[Alamat Referensi Informasi Model Resmi](https://bigmodel.cn/console/modelcenter/square)

| Nama          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan

[Alamat Referensi Informasi Model Resmi](https://cloud.tencent.com/document/product/1729/102832)

| Nama                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan

[Alamat Referensi Informasi Model Resmi](https://platform.baichuan-ai.com/docs/text-Embedding)

| Nama                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together

[Alamat Referensi Informasi Model Resmi](https://docs.together.ai/docs/serverless-models#embedding-models)

| Nama                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina

[Alamat Referensi Informasi Model Resmi](https://jina.ai/models/jina-embedding-b-en-v1)

| Nama                                 | max input |
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

[Alamat Referensi Informasi Model Resmi](https://siliconflow.cn/zh-cn/models)

| Nama                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[Alamat Referensi Informasi Model Resmi](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| Nama                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### nomic

[Alamat Referensi Informasi Model Resmi](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| Nama                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console

[Alamat Referensi Informasi Model Resmi](https://console.upstage.ai/docs/capabilities/embeddings)

| Nama                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere

[Alamat Referensi Informasi Model Resmi](https://docs.cohere.com/docs/models#embed)

| Nama                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |