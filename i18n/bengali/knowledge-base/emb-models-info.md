---
icon: square-info
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# এম্বেডিং মডেল রেফারেন্স তথ্য

{% hint style="info" %}
ত্রুটি এড়ানোর জন্য, এই ডকুমেন্টে কিছু মডেলের max input-এর মান সীমাবদ্ধতার মাত্রায় লেখা হয়নি। উদাহরণস্বরূপ: অফিসিয়ালভাবে সর্বাধিক ইনপুট মান 8k দেওয়া থাকলে (নির্দিষ্ট সংখ্যা উল্লেখ না করলে), এই ডকুমেন্টে সংকেত মান 8191 বা 8000 ইত্যাদি দেওয়া হতে পারে। (বুঝতে অসুবিধা হলে উপেক্ষা করুন, কেবল ডকুমেন্টের সংকেত মান অনুযায়ী পূরণ করুন)
{% endhint %}

### ভলকানো ডুবাও (Volcano Doubao)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| নাম                     | max input |
| ---------------------- | --------- |
| Doubao-embedding       | 4095      |
| Doubao-embedding-vision| 8191      |
| Doubao-embedding-large | 4095      |

### আলিবাবা (Alibaba)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| নাম                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI&#x20;

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| নাম                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### বাইদু (Baidu)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| নাম           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### ঝিপু AI (Zhipu AI)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://bigmodel.cn/console/modelcenter/square)

| নাম          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### হুনইউয়ান (Hunyuan)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://cloud.tencent.com/document/product/1729/102832)

| নাম                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### বাইচুয়ান (Baichuan)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://platform.baichuan-ai.com/docs/text-Embedding)

| নাম                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### টুগেদার (Together)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://docs.together.ai/docs/serverless-models#embedding-models)

| নাম                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### জিনা AI (Jina AI)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://jina.ai/models/jina-embedding-b-en-v1)

| নাম                                 | max input |
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

### সিলিকনফ্লো (SiliconFlow)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://siliconflow.cn/zh-cn/models)

| নাম                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### জেমিনি (Gemini)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| নাম                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### নমিক (Nomic)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| নাম                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### কনসোল (Console)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://console.upstage.ai/docs/capabilities/embeddings)

| নাম                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### কোহিয়ার (Cohere)

[দাপ্তরিক মডেল তথ্য রেফারেন্স](https://docs.cohere.com/docs/models#embed)

| নাম                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |