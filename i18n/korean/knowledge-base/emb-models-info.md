---
icon: square-info
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# 임베딩 모델 참조 정보

{% hint style="info" %}
오류 방지를 위해 본 문서에서는 일부 모델의 max input 값을 극한값으로 작성하지 않았습니다. 예를 들어, 공식적으로 최대 입력값이 8k(명확한 수치 미제공)로 공개된 경우 본 문서에서는 8191 또는 8000 등의 참조값을 제시합니다. (이해되지 않는 경우 무시하고 문서의 참조값을 따르시면 됩니다)
{% endhint %}

### 화산-두바오

[공식 모델 정보 참조 주소](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| 모델명                      | max input |
| ------------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### 알리바바

[공식 모델 정보 참조 주소](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| 모델명                      | max input |
| ------------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI  

[공식 모델 정보 참조 주소](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| 모델명                     | max input |
| ------------------------ | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### 바이두

[공식 모델 정보 참조 주소](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| 모델명         | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### 지푸AI

[공식 모델 정보 참조 주소](https://bigmodel.cn/console/modelcenter/square)

| 모델명        | max input |
| ------------ | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### 혼위안

[공식 모델 정보 참조 주소](https://cloud.tencent.com/document/product/1729/102832)

| 모델명              | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### 바이촨

[공식 모델 정보 참조 주소](https://platform.baichuan-ai.com/docs/text-Embedding)

| 모델명                      | max input |
| ------------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together

[공식 모델 정보 참조 주소](https://docs.together.ai/docs/serverless-models#embedding-models)

| 모델명                        | max input |
| --------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina  

[공식 모델 정보 참조 주소](https://jina.ai/models/jina-embedding-b-en-v1)

| 모델명                                 | max input |
| ------------------------------------ | --------- |
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

### 실리콘플로우

[공식 모델 정보 참조 주소](https://siliconflow.cn/zh-cn/models)

| 모델명                                    | max input |
| --------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[공식 모델 정보 참조 주소](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| 모델명               | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### nomic

[공식 모델 정보 참조 주소](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| 모델명                    | max input |
| ----------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console

[공식 모델 정보 참조 주소](https://console.upstage.ai/docs/capabilities/embeddings)

| 모델명              | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere

[공식 모델 정보 참조 주소](https://docs.cohere.com/docs/models#embed)

| 모델명                            | max input |
| ------------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |