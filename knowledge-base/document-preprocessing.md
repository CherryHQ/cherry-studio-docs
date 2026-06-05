---
icon: face-viewfinder
---

# 知识库文档预处理

知识库文档预处理用于在向量化前对 PDF / 图片等非文本内容做 OCR 与结构解析，让知识库能正确检索这些资料。

{% hint style="warning" %}
**当前版本改动**：文档处理（OCR + Provider 配置）已从"每个知识库内部"迁移到独立的 **`设置 → 文档处理`**。本页流程已按当前版本更新。
{% endhint %}

### 配置OCR服务商

打开 `设置 → 文档处理`，依次配置：

* **系统 OCR**：macOS 用户开箱即用（无需配置）；Windows 需手动选择 OCR 引擎
* **文档处理服务商**：默认 `MinerU`，可填写 `API Key` + `API Host`（默认 `https://mineru.net`）；也可切换为 Tesseract / Paddle OCR / OpenVINO / 三方 Provider

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 11.50.10@2x (1) (1).jpg" alt=""><figcaption></figcaption></figure>

点击获取API KEY后会在浏览器打开申请地址，点击立即申请填写表单后获取API KEY，并将其填入API KEY中。

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 11.51.55@2x (1).jpg" alt=""><figcaption></figcaption></figure>

### 在知识库中启用文档预处理

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 20.01.03@2x (1).jpg" alt=""><figcaption></figcaption></figure>

在创建好的知识库设置中打开 **文档预处理** 开关，即可在添加文件时自动使用上一步配置的 OCR Provider。

### 上传文档

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 12.01.59@2x (1).jpg" alt=""><figcaption></figcaption></figure>

> 可以通过右上角搜索对知识库结果检测

### 在对话中使用

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 14.11.00@2x (1).jpg" alt=""><figcaption></figcaption></figure>

> 知识库使用Tips: 使用**能力较强**的模型时可以将知识库搜索模式修改为意图识别，意图识别可以更准确、广泛的描述您的问题。

### 开启知识库意图识别

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 14.12.47@2x (1).jpg" alt=""><figcaption></figcaption></figure>
