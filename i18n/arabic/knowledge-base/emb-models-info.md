---
icon: square-info
---

{% hint style="warning" %}
تمت ترجمة هذا المستند من الصينية بواسطة الذكاء الاصطناعي ولم تتم مراجعته بعد.
{% endhint %}

# معلومات مرجعية لنماذج التضمين

{% hint style="info" %}
لتفادي الأخطاء، لم يتم كتابة قيم max input لبعض النماذج في هذا المستند كقيم قصوى. على سبيل المثال: عندما تكون القيمة القصوى للإدخال المقدمة رسميًا هي 8k (بدون تحديد قيمة دقيقة)، يتم تقديم قيمة مرجعية في هذا المستند مثل 8191 أو 8000 إلخ. (إذا لم تكن مفهومة، تجاهلها واملأ وفقًا للقيم المرجعية في المستند)
{% endhint %}

### 火山-豆包

[官方模型信息参考地址](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| الاسم                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### 阿里

[官方模型信息参考地址](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| الاسم                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI

[官方模型信息参考地址](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| الاسم                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### 百度

[官方模型信息参考地址](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| الاسم           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### 智谱

[官方模型信息参考地址](https://bigmodel.cn/console/modelcenter/square)

| الاسم          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### 混元

[官方模型信息参考地址](https://cloud.tencent.com/document/product/1729/102832)

| الاسم                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### 百川

[官方模型信息参考地址](https://platform.baichuan-ai.com/docs/text-Embedding)

| الاسم                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together

[官方模型信息参考地址](https://docs.together.ai/docs/serverless-models#embedding-models)

| الاسم                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina

[官方模型信息参考地址](https://jina.ai/models/jina-embedding-b-en-v1)

| الاسم                                 | max input |
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

[官方模型信息参考地址](https://siliconflow.cn/zh-cn/models)

| الاسم                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[官方模型信息参考地址](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| الاسم                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### nomic

[官方模型信息参考地址](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| الاسم                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console

[官方模型信息参考地址](https://console.upstage.ai/docs/capabilities/embeddings)

| الاسم                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere

[官方模型信息参考地址](https://docs.cohere.com/docs/models#embed)

| الاسم                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |