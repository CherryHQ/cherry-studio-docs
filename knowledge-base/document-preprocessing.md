---
icon: face-viewfinder
---

# 文档预处理

知识库文档预处理用于在向量化前对 PDF / 图片等非文本内容做 OCR 与结构解析，让知识库能正确检索这些资料。

### 先配好解析引擎

文档预处理用到的解析引擎（默认 MinerU）在设置里统一配置一次即可：

* 到 [文档处理](../pre-basic/settings/doc-process.md) 选好文档解析引擎、填好 API 密钥；
* 如需识别**图片 / 扫描件**里的文字，再到 [OCR](../pre-basic/settings/ocr.md) 配好 OCR 引擎。

配好后回到知识库，按下面选用它即可。

### 在知识库中选择文档处理引擎

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 20.01.03@2x.jpg" alt=""><figcaption></figcaption></figure>

在知识库的**设置**里，把 **文档处理** 选成你配好的解析引擎（默认未选；选定后，添加文件时就会用它做预处理）。

### 上传文档

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 12.01.59@2x.jpg" alt=""><figcaption></figcaption></figure>

> 可以用右上角的**召回测试**验证检索效果。

### 在对话中使用

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 14.11.00@2x.jpg" alt=""><figcaption></figcaption></figure>

***

### 获取帮助与提交反馈

如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../question-contact/suggestions.md) 中提供的官方渠道。
