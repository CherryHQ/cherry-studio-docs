---
icon: square-info
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

---
icon: cherries
---

# 埋め込みモデル参考情報

{% hint style="info" %}
エラーを防ぐため、本文書では一部のモデルについてmax input値を厳密な上限値ではなく参考値として記載しています。例：公式が「8k」と公表している場合（具体的数値未公表時）、本文書では8191や8000などの参考値を設定しています。（理解不能な場合は無視し、ドキュメント記載の参考値を使用してください）
{% endhint %}

### 火山-豆包

[公式モデル情報](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| モデル名                  | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### 阿里

[公式モデル情報](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| モデル名                      | max input |
| ------------------------- | --------- |
| text-embedding-v3         | 8192      |
| text-embedding-v2         | 2048      |
| text-embedding-v1         | 2048      |
| text-embedding-async-v2   | 2048      |
| text-embedding-async-v1   | 2048      |

### OpenAI&#x20;

[公式モデル情報](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| モデル名                   | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### 百度

[公式モデル情報](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| モデル名         | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### 智谱

[公式モデル情報](https://bigmodel.cn/console/modelcenter/square)

| モデル名        | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### 混元

[公式モデル情報](https://cloud.tencent.com/document/product/1729/102832)

| モデル名              | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### 百川

[公式モデル情報](https://platform.baichuan-ai.com/docs/text-Embedding)

| モデル名                    | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together

[公式モデル情報](https://docs.together.ai/docs/serverless-models#embedding-models)

| モデル名                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina&#x20;

[公式モデル情報](https://jina.ai/models/jina-embedding-b-en-v1)

| モデル名                                 | max input |
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

### 硅基流动

[公式モデル情報](https://siliconflow.cn/zh-cn/models)

| モデル名                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[公式モデル情報](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| モデル名                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### nomic

[公式モデル情報](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| モデル名                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console

[公式モデル情報](https://console.upstage.ai/docs/capabilities/embeddings)

| モデル名              | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere

[公式モデル情報](https://docs.cohere.com/docs/models#embed)

| モデル名                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |