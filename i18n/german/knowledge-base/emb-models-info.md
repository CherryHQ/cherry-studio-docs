---
icon: square-info
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Referenzinformationen für Embedding-Modelle

{% hint style="info" %}
Um Fehler zu vermeiden, sind die max input-Werte für einige Modelle in diesem Dokument nicht als Grenzwerte angegeben. Beispielsweise: Wenn der offizielle maximale Eingabewert mit 8k angegeben ist (ohne genaue Zahl), zeigt dieses Dokument Referenzwerte wie 8191 oder 8000 an. (Bei Unklarheiten einfach die Referenzwerte im Dokument übernehmen)
{% endhint %}

### Volcano-Doubao

[Offizielle Modellinformationen Referenzadresse](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| Name                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba

[Offizielle Modellinformationen Referenzadresse](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| Name                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI

[Offizielle Modellinformationen Referenzadresse](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| Name                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu

[Offizielle Modellinformationen Referenzadresse](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| Name           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu

[Offizielle Modellinformationen Referenzadresse](https://bigmodel.cn/console/modelcenter/square)

| Name          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan

[Offizielle Modellinformationen Referenzadresse](https://cloud.tencent.com/document/product/1729/102832)

| Name                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan

[Offizielle Modellinformationen Referenzadresse](https://platform.baichuan-ai.com/docs/text-Embedding)

| Name                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### Together

[Offizielle Modellinformationen Referenzadresse](https://docs.together.ai/docs/serverless-models#embedding-models)

| Name                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina

[Offizielle Modellinformationen Referenzadresse](https://jina.ai/models/jina-embedding-b-en-v1)

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

### Silicon Flow

[Offizielle Modellinformationen Referenzadresse](https://siliconflow.cn/zh-cn/models)

| Name                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[Offizielle Modellinformationen Referenzadresse](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| Name                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### Nomic

[Offizielle Modellinformationen Referenzadresse](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| Name                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### Console

[Offizielle Modellinformationen Referenzadresse](https://console.upstage.ai/docs/capabilities/embeddings)

| Name                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### Cohere

[Offizielle Modellinformationen Referenzadresse](https://docs.cohere.com/docs/models#embed)

| Name                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |