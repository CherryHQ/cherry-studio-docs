---
icon: square-info
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Справочная информация о моделях внедрения (Embedding Models)

{% hint style="info" %}
Во избежание ошибок, в данном документе значения max input для некоторых моделей указаны не как предельные. Например: когда официально указано максимальное входное значение 8k (без точного указания конкретного числа), в этом документе приведены справочные значения вроде 8191 или 8000. (Если непонятно, игнорируйте это и просто используйте справочные значения из документа)
{% endhint %}

### Volcano-Doubao

[Официальная справочная информация по моделям](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| Название                      | max input |
| ---------------------------- | --------- |
| Doubao-embedding             | 4095      |
| Doubao-embedding-vision      | 8191      |
| Doubao-embedding-large       | 4095      |

### Alibaba

[Официальная справочная информация по моделям](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| Название                      | max input |
| ---------------------------- | --------- |
| text-embedding-v3            | 8192      |
| text-embedding-v2            | 2048      |
| text-embedding-v1            | 2048      |
| text-embedding-async-v2      | 2048      |
| text-embedding-async-v1      | 2048      |

### OpenAI

[Официальная справочная информация по моделям](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| Название                     | max input |
| --------------------------- | --------- |
| text-embedding-3-small      | 8191      |
| text-embedding-3-large      | 8191      |
| text-embedding-ada-002       | 8191      |

### Baidu

[Официальная справочная информация по моделям](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| Название        | max input |
| -------------- | --------- |
| Embedding-V1    | 384       |
| tao-8k         | 8192      |

### Zhipu

[Официальная справочная информация по моделям](https://bigmodel.cn/console/modelcenter/square)

| Название      | max input |
| ------------ | --------- |
| embedding-2  | 1024      |
| embedding-3  | 2048      |

### Hunyuan

[Официальная справочная информация по моделям](https://cloud.tencent.com/document/product/1729/102832)

| Название            | max input |
| ------------------ | --------- |
| hunyuan-embedding  | 1024      |

### Baichuan

[Официальная справочная информация по моделям](https://platform.baichuan-ai.com/docs/text-Embedding)

| Название                    | max input |
| -------------------------- | --------- |
| Baichuan-Text-Embedding    | 512       |

### Together

[Официальная справочная информация по моделям](https://docs.together.ai/docs/serverless-models#embedding-models)

| Название                       | max input |
| ----------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval      | 2048      |
| M2-BERT-80M-8K-Retrieval      | 8192      |
| M2-BERT-80M-32K-Retrieval     | 32768     |
| UAE-Large-v1                  | 512       |
| BGE-Large-EN-v1.5             | 512       |
| BGE-Base-EN-v1.5              | 512       |

### Jina

[Официальная справочная информация по моделям](https://jina.ai/models/jina-embedding-b-en-v1)

| Название                               | max input |
| ------------------------------------- | --------- |
| jina-embedding-b-en-v1                | 512       |
| jina-embeddings-v2-base-en            | 8191      |
| jina-embeddings-v2-base-zh            | 8191      |
| jina-embeddings-v2-base-de            | 8191      |
| jina-embeddings-v2-base-code          | 8191      |
| jina-embeddings-v2-base-es            | 8191      |
| jina-colbert-v1-en                    | 8191      |
| jina-reranker-v1-base-en              | 8191      |
| jina-reranker-v1-turbo-en             | 8191      |
| jina-reranker-v1-tiny-en              | 8191      |
| jina-clip-v1                          | 8191      |
| jina-reranker-v2-base-multilingual    | 8191      |
| reader-lm-1.5b                        | 256000    |
| reader-lm-0.5b                        | 256000    |
| jina-colbert-v2                       | 8191      |
| jina-embeddings-v3                    | 8191      |

### SiliconFlow

[Официальная справочная информация по моделям](https://siliconflow.cn/zh-cn/models)

| Название                                 | max input |
| --------------------------------------- | --------- |
| BAAI/bge-m3                             | 8191      |
| netease-youdao/bce-embedding-base\_v1   | 512       |
| BAAI/bge-large-zh-v1.5                  | 512       |
| BAAI/bge-large-en-v1.5                  | 512       |
| Pro/BAAI/bge-m3                         | 8191      |

### Gemini

[Официальная справочная информация по моделям](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| Название                | max input |
| ---------------------- | --------- |
| text-embedding-004     | 2048      |

### Nomic

[Официальная справочная информация по моделям](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| Название                  | max input |
| ------------------------ | --------- |
| nomic-embed-text-v1      | 8192      |
| nomic-embed-text-v1.5    | 8192      |
| gte-multilingual-base    | 8192      |

### Console

[Официальная справочная информация по моделям](https://console.upstage.ai/docs/capabilities/embeddings)

| Название              | max input |
| -------------------- | --------- |
| embedding-query      | 4000      |
| embedding-passage    | 4000      |

### Cohere

[Официальная справочная информация по моделям](https://docs.cohere.com/docs/models#embed)

| Название                              | max input |
| ------------------------------------ | --------- |
| embed-english-v3.0                   | 512       |
| embed-english-light-v3.0             | 512       |
| embed-multilingual-v3.0              | 512       |
| embed-multilingual-light-v3.0        | 512       |
| embed-english-v2.0                   | 512       |
| embed-english-light-v2.0             | 512       |
| embed-multilingual-v2.0              | 256       |