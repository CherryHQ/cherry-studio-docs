---
icon: square-info
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 埋め込みモデル参考情報

{% hint style="info" %}
エラー防止のため、本文書では一部モデルのmax input値を限界値ではなく安全側に設定しています（例：公式の最大入力値が8k（具体的な数値未記載）の場合、本文書では8191や8000など控えめな参考値を表示）。内容が理解できなくても問題ありません。ドキュメント記載の参考値に従って入力してください。
{% endhint %}

### Volcano-Doubao

[公式モデル情報参照先](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| 名称                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba

[公式モデル情報参照先](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| 名称                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI&#x20;

[公式モデル情報参照先](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| 名称                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu

[公式モデル情報参照先](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| 名称           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu AI

[公式モデル情報参照先](https://bigmodel.cn/console/modelcenter/square)

| 名称          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan

[公式モデル情報参照先](https://cloud.tencent.com/document/product/1729/102832)

| 名称                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan

[公式モデル情報参照先](https://platform.baichuan-ai.com/docs/text-Embedding)

| 名称                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### Together

[公式モデル情報参照先](https://docs.together.ai/docs/serverless-models#embedding-models)

| 名称                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina&#x20;

[公式モデル情報参照先](https://jina.ai/models/jina-embedding-b-en-v1)

| 名称                                 | max input |
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

[公式モデル情報参照先](https://siliconflow.cn/zh-cn/models)

| 名称                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[公式モデル情報参照先](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| 名称                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### Nomic

[公式モデル情報参照先](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| 名称                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### Upstage Console

[公式モデル情報参照先](https://console.upstage.ai/docs/capabilities/embeddings)

| 名称                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### Cohere

[公式モデル情報参照先](https://docs.cohere.com/docs/models#embed)

| 名称                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |