---
icon: square-info
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Thông Tin Tham Khảo về Mô hình Nhúng (Embedding)

{% hint style="info" %}
Để tránh lỗi, giá trị max input của một số mô hình trong tài liệu này không được ghi ở mức giới hạn tuyệt đối. Ví dụ: khi giá trị đầu vào tối đa chính thức là 8k (không xác định rõ số liệu cụ thể), giá trị tham khảo trong tài liệu này là 8191 hoặc 8000, v.v. (Nếu không hiểu có thể bỏ qua, vui lòng điền theo giá trị tham khảo trong tài liệu)
{% endhint %}

### Volcano-Doubao

[Địa chỉ tham khảo thông tin mô hình chính thức](https://console.volcengine.com/ark/region:ark+cn-beijing/model?feature=\&projectName=default\&vendor=Bytedance\&view=LIST_VIEW)

| Tên                      | max input |
| ----------------------- | --------- |
| Doubao-embedding        | 4095      |
| Doubao-embedding-vision | 8191      |
| Doubao-embedding-large  | 4095      |

### Alibaba

[Địa chỉ tham khảo thông tin mô hình chính thức](https://help.aliyun.com/zh/model-studio/user-guide/embedding?spm=a2c4g.11186623.0.i1)

| Tên                      | max input |
| ----------------------- | --------- |
| text-embedding-v3       | 8192      |
| text-embedding-v2       | 2048      |
| text-embedding-v1       | 2048      |
| text-embedding-async-v2 | 2048      |
| text-embedding-async-v1 | 2048      |

### OpenAI

[Địa chỉ tham khảo thông tin mô hình chính thức](https://platform.openai.com/docs/guides/embeddings#embedding-models)

| Tên                     | max input |
| ---------------------- | --------- |
| text-embedding-3-small | 8191      |
| text-embedding-3-large | 8191      |
| text-embedding-ada-002 | 8191      |

### Baidu

[Địa chỉ tham khảo thông tin mô hình chính thức](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/om6070n97#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

| Tên           | max input |
| ------------ | --------- |
| Embedding-V1 | 384       |
| tao-8k       | 8192      |

### Zhipu

[Địa chỉ tham khảo thông tin mô hình chính thức](https://bigmodel.cn/console/modelcenter/square)

| Tên          | max input |
| ----------- | --------- |
| embedding-2 | 1024      |
| embedding-3 | 2048      |

### Hunyuan

[Địa chỉ tham khảo thông tin mô hình chính thức](https://cloud.tencent.com/document/product/1729/102832)

| Tên                | max input |
| ----------------- | --------- |
| hunyuan-embedding | 1024      |

### Baichuan

[Địa chỉ tham khảo thông tin mô hình chính thức](https://platform.baichuan-ai.com/docs/text-Embedding)

| Tên                      | max input |
| ----------------------- | --------- |
| Baichuan-Text-Embedding | 512       |

### together

[Địa chỉ tham khảo thông tin mô hình chính thức](https://docs.together.ai/docs/serverless-models#embedding-models)

| Tên                        | max input |
| ------------------------- | --------- |
| M2-BERT-80M-2K-Retrieval  | 2048      |
| M2-BERT-80M-8K-Retrieval  | 8192      |
| M2-BERT-80M-32K-Retrieval | 32768     |
| UAE-Large-v1              | 512       |
| BGE-Large-EN-v1.5         | 512       |
| BGE-Base-EN-v1.5          | 512       |

### Jina

[Địa chỉ tham khảo thông tin mô hình chính thức](https://jina.ai/models/jina-embedding-b-en-v1)

| Tên                                 | max input |
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

[Địa chỉ tham khảo thông tin mô hình chính thức](https://siliconflow.cn/zh-cn/models)

| Tên                                    | max input |
| ------------------------------------- | --------- |
| BAAI/bge-m3                           | 8191      |
| netease-youdao/bce-embedding-base\_v1 | 512       |
| BAAI/bge-large-zh-v1.5                | 512       |
| BAAI/bge-large-en-v1.5                | 512       |
| Pro/BAAI/bge-m3                       | 8191      |

### Gemini

[Địa chỉ tham khảo thông tin mô hình chính thức](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#text-embedding)

| Tên                 | max input |
| ------------------ | --------- |
| text-embedding-004 | 2048      |

### nomic

[Địa chỉ tham khảo thông tin mô hình chính thức](https://docs.nomic.ai/atlas/embeddings-and-retrieval/text-embedding)

| Tên                    | max input |
| --------------------- | --------- |
| nomic-embed-text-v1   | 8192      |
| nomic-embed-text-v1.5 | 8192      |
| gte-multilingual-base | 8192      |

### console

[Địa chỉ tham khảo thông tin mô hình chính thức](https://console.upstage.ai/docs/capabilities/embeddings)

| Tên                | max input |
| ----------------- | --------- |
| embedding-query   | 4000      |
| embedding-passage | 4000      |

### cohere

[Địa chỉ tham khảo thông tin mô hình chính thức](https://docs.cohere.com/docs/models#embed)

| Tên                            | max input |
| ----------------------------- | --------- |
| embed-english-v3.0            | 512       |
| embed-english-light-v3.0      | 512       |
| embed-multilingual-v3.0       | 512       |
| embed-multilingual-light-v3.0 | 512       |
| embed-english-v2.0            | 512       |
| embed-english-light-v2.0      | 512       |
| embed-multilingual-v2.0       | 256       |