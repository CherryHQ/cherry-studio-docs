---
icon: square-info
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# एम्बेडिंग मॉडल संदर्भ जानकारी

{% hint style="info" %}
त्रुटियों से बचने के लिए, इस दस्तावेज़ में कुछ मॉडलों के max input मान सीमा मान के रूप में नहीं लिखे गए हैं। उदाहरण के लिए: जब आधिकारिक तौर पर अधिकतम इनपुट मान 8k दिया गया हो (सटीक संख्या स्पष्ट न हो), तो इस दस्तावेज़ में संदर्भ मान 8191 या 8000 आदि दिया गया है। (अगर समझ में न आए तो अनदेखा करें, बस दस्तावेज़ में दिए संदर्भ मान का उपयोग करें)
{% endhint %}

### वॉलकैन-डौबाओ

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| नाम                      | अधिकतम इनपुट |
| ----------------------- | ------------ |
| Doubao-embedding        | 4095         |
| Doubao-embedding-vision | 8191         |
| Doubao-embedding-large  | 4095         |

### अलीबाबा

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| नाम                      | अधिकतम इनपुट |
| ----------------------- | ------------ |
| text-embedding-v3       | 8192         |
| text-embedding-v2       | 2048         |
| text-embedding-v1       | 2048         |
| text-embedding-async-v2 | 2048         |
| text-embedding-async-v1 | 2048         |

### OpenAI

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| नाम                     | अधिकतम इनपुट |
| ---------------------- | ------------ |
| text-embedding-3-small | 8191         |
| text-embedding-3-large | 8191         |
| text-embedding-ada-002 | 8191         |

### बैडू

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| नाम         | अधिकतम इनपुट |
| ---------- | ------------ |
| Embedding-V1 | 384          |
| tao-8k       | 8192         |

### झीपू

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://bigmodel.cn/console/modelcenter/square)

| नाम        | अधिकतम इनपुट |
| --------- | ------------ |
| embedding-2 | 1024         |
| embedding-3 | 2048         |

### हुनयुआन

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://cloud.tencent.com/document/product/1729/102832)

| नाम                | अधिकतम इनपुट |
| ----------------- | ------------ |
| hunyuan-embedding | 1024         |

### बाइचुआन

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://platform.baichuan-ai.com/docs/text-Embedding)

| नाम                      | अधिकतम इनपुट |
| ----------------------- | ------------ |
| Baichuan-Text-Embedding | 512          |

### together

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://docs.together.ai/docs/serverless-models#embedding-models)

| नाम                        | अधिकतम इनपुट |
| ------------------------- | ------------ |
| M2-BERT-80M-2K-Retrieval  | 2048         |
| M2-BERT-80M-8K-Retrieval  | 8192         |
| M2-BERT-80M-32K-Retrieval | 32768        |
| UAE-Large-v1              | 512          |
| BGE-Large-EN-v1.5         | 512          |
| BGE-Base-EN-v1.5          | 512          |

### Jina

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://jina.ai/models/jina-embedding-b-en-v1)

| नाम                                 | अधिकतम इनपुट |
| ---------------------------------- | ------------ |
| jina-embedding-b-en-v1             | 512          |
| jina-embeddings-v2-base-en         | 8191         |
| jina-embeddings-v2-base-zh         | 8191         |
| jina-embeddings-v2-base-de         | 8191         |
| jina-embeddings-v2-base-code       | 8191         |
| jina-embeddings-v2-base-es         | 8191         |
| jina-colbert-v1-en                 | 8191         |
| jina-reranker-v1-base-en           | 8191         |
| jina-reranker-v1-turbo-en          | 8191         |
| jina-reranker-v1-tiny-en           | 8191         |
| jina-clip-v1                       | 8191         |
| jina-reranker-v2-base-multilingual | 8191         |
| reader-lm-1.5b                     | 256000       |
| reader-lm-0.5b                     | 256000       |
| jina-colbert-v2                    | 8191         |
| jina-embeddings-v3                 | 8191         |

### सिलिकॉनफ्लो

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://siliconflow.cn/zh-cn/models)

| नाम                                    | अधिकतम इनपुट |
| ------------------------------------- | ------------ |
| BAAI/bge-m3                           | 8191         |
| netease-youdao/bce-embedding-base\_v1 | 512          |
| BAAI/bge-large-zh-v1.5                | 512          |
| BAAI/bge-large-en-v1.5                | 512          |
| Pro/BAAI/bge-m3                       | 8191         |

### Gemini

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| नाम                 | अधिकतम इनपुट |
| ------------------ | ------------ |
| text-embedding-004 | 2048         |

### nomic

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| नाम                    | अधिकतम इनपुट |
| --------------------- | ------------ |
| nomic-embed-text-v1   | 8192         |
| nomic-embed-text-v1.5 | 8192         |
| gte-multilingual-base | 8192         |

### console

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://console.upstage.ai/docs/capabilities/embeddings)

| नाम              | अधिकतम इनपुट |
| ----------------- | ------------ |
| embedding-query   | 4000         |
| embedding-passage | 4000         |

### cohere

[आधिकारिक मॉडल जानकारी संदर्भ पता](https://docs.cohere.com/docs/models#embed)

| नाम                            | अधिकतम इनपुट |
| ----------------------------- | ------------ |
| embed-english-v3.0            | 512          |
| embed-english-light-v3.0      | 512          |
| embed-multilingual-v3.0       | 512          |
| embed-multilingual-light-v3.0 | 512          |
| embed-english-v2.0            | 512          |
| embed-english-light-v2.0      | 512          |
| embed-multilingual-v2.0       | 256          |