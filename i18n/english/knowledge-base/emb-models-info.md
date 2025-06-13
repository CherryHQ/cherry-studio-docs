---
icon: square-info
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# Embedding Model Reference Information

{% hint style="info" %}
To prevent errors, the 'max input' values for some models in this document are not set to their absolute limits. For instance, when the official documentation states a maximum input of 8k (without specifying the exact number), this document may list the reference value as 8191 or 8000. (Feel free to ignore this note if it's unclear; simply use the reference values provided in the document.)
{% endhint %}

### Volcengine-Doubao

[Official Model Information Reference](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| Name                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba

[Official Model Information Reference](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| Name                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI

[Official Model Information Reference](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| Name                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu

[Official Model Information Reference](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| Name           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu

[Official Model Information Reference](https://bigmodel.cn/console/modelcenter/square)

| Name          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan

[Official Model Information Reference](https://cloud.tencent.com/document/product/1729/102832)

| Name                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan

[Official Model Information Reference](https://platform.baichuan-ai.com/docs/text-Embedding)

| Name                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together

[Official Model Information Reference](https://docs.together.ai/docs/serverless-models#embedding-models)

| Name                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina

[Official Model Information Reference](https://jina.ai/models/jina-embedding-b-en-v1)

| Name                                 | max input |
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

[Official Model Information Reference](https://siliconflow.cn/zh-cn/models)

| Name                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[Official Model Information Reference](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| Name                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### nomic

[Official Model Information Reference](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| Name                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console

[Official Model Information Reference](https://console.upstage.ai/docs/capabilities/embeddings)

| Name                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere

[Official Model Information Reference](https://docs.cohere.com/docs/models#embed)

| Name                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |