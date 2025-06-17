---
icon: square-info
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Informazioni di riferimento per i modelli di embedding

{% hint style="info" %}
Per prevenire errori, in questo documento i valori di max input per alcuni modelli non sono stati impostati al limite massimo. Ad esempio, quando il valore ufficiale massimo di input è indicato come 8k (senza un numero preciso specificato), in questo documento vengono forniti valori di riferimento come 8191 o 8000, ecc. (Se non è chiaro, si può ignorare: basta utilizzare il valore di riferimento indicato nel documento)
{% endhint %}

### Volcano-Doubao

[Indirizzo di riferimento ufficiale del modello](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| Modello                     | max input |
| --------------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba

[Indirizzo di riferimento ufficiale del modello](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| Modello                      | max input |
| --------------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI

[Indirizzo di riferimento ufficiale del modello](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| Modello                    | max input |
| -------------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu

[Indirizzo di riferimento ufficiale del modello](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| Modello        | max input |
| -------------- | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu

[Indirizzo di riferimento ufficiale del modello](https://bigmodel.cn/console/modelcenter/square)

| Modello         | max input |
| --------------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan

[Indirizzo di riferimento ufficiale del modello](https://cloud.tencent.com/document/product/1729/102832)

| Modello               | max input |
| --------------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan

[Indirizzo di riferimento ufficiale del modello](https://platform.baichuan-ai.com/docs/text-Embedding)

| Modello                      | max input |
| --------------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together

[Indirizzo di riferimento ufficiale del modello](https://docs.together.ai/docs/serverless-models#embedding-models)

| Modello                         | max input |
| ------------------------------ | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina

[Indirizzo di riferimento ufficiale del modello](https://jina.ai/models/jina-embedding-b-en-v1)

| Modello                                | max input |
| -------------------------------------- | --------- |
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

[Indirizzo di riferimento ufficiale del modello](https://siliconflow.cn/zh-cn/models)

| Modello                                  | max input |
| ---------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[Indirizzo di riferimento ufficiale del modello](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| Modello                | max input |
| ---------------------- | --------- |
| text-embedding-004 | 2048      |

### nomic

[Indirizzo di riferimento ufficiale del modello](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| Modello                  | max input |
| ------------------------ | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console

[Indirizzo di riferimento ufficiale del modello](https://console.upstage.ai/docs/capabilities/embeddings)

| Modello              | max input |
| -------------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere

[Indirizzo di riferimento ufficiale del modello](https://docs.cohere.com/docs/models#embed)

| Modello                          | max input |
| ------------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |