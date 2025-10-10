---
icon: square-info
---
# Referencia de Modelos de Embedding


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




{% hint style="info" %}
Para prevenir errores, en este documento algunos valores de max input no están escritos como valores límite. Por ejemplo: cuando el valor máximo de entrada oficial es 8k (sin especificar un valor exacto), este documento proporciona valores de referencia como 8191 u 8000. (Si no lo entiende, ignore y utilice los valores de referencia del documento)
{% endhint %}

### Volcano Doubao

[Enlace oficial de referencia del modelo](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| Nombre                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba

[Enlace oficial de referencia del modelo](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| Nombre                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI&#x20;

[Enlace oficial de referencia del modelo](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| Nombre                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu

[Enlace oficial de referencia del modelo](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| Nombre           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu

[Enlace oficial de referencia del modelo](https://bigmodel.cn/console/modelcenter/square)

| Nombre          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan

[Enlace oficial de referencia del modelo](https://cloud.tencent.com/document/product/1729/102832)

| Nombre                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan

[Enlace oficial de referencia del modelo](https://platform.baichuan-ai.com/docs/text-Embedding)

| Nombre                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together

[Enlace oficial de referencia del modelo](https://docs.together.ai/docs/serverless-models#embedding-models)

| Nombre                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina&#x20;

[Enlace oficial de referencia del modelo](https://jina.ai/models/jina-embedding-b-en-v1)

| Nombre                                 | max input |
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

### Silicon Flow

[Enlace oficial de referencia del modelo](https://siliconflow.cn/zh-cn/models)

| Nombre                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[Enlace oficial de referencia del modelo](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| Nombre                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### nomic

[Enlace oficial de referencia del modelo](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| Nombre                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console

[Enlace oficial de referencia del modelo](https://console.upstage.ai/docs/capabilities/embeddings)

| Nombre                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere

[Enlace oficial de referencia del modelo](https://docs.cohere.com/docs/models#embed)

| Nombre                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |