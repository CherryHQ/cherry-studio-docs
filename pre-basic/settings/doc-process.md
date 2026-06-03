---
icon: file-code
---

# 文档处理

简单说：**这是 Cherry Studio "把 PDF / 图片 / 扫描件认出文字" 的中央配置。**

举几个例子，下面这些事都依赖它：

* 你把一份扫描的合同 PDF 拖进对话框，想让 AI 读懂内容
* 你把一堆图片格式的发票放进[知识库](../../knowledge-base/knowledge-base.md)，希望以后能搜
* 你的 [Agent](../../advanced-basic/agent.md) 要打开本地文件夹里某张截图分析

这些场景背后都需要先把"图像里的文字"变成"可以被 AI 读的文字"，这一步技术上叫 **OCR**（Optical Character Recognition，光学字符识别）。

v1.9.x 起，OCR 的配置从每个知识库里搬到了**一个统一的设置页**。你在这里配一次，所有用到 OCR 的地方都会用同一套配置。

### 配置入口

打开 `设置 → 文档处理`：

<figure><img src="../../.gitbook/assets/cherry-docprocess.png" alt=""><figcaption><p>文档处理设置面板</p></figcaption></figure>

面板分两块，分别管"图片识字"和"PDF 解析"。

#### 1. 系统 OCR — 给图片认字

* **如果你用 macOS**：什么都不用配，Cherry Studio 直接借用系统自带的"识图"能力，免费、离线、效果还不错 ✅
* **如果你用 Windows**：需要在下方选一个 OCR 引擎。如果你只是日常用，选默认的就行；不放心可以看下面的"选哪个 OCR 引擎"说明。

<details>
<summary>选哪个 OCR 引擎？</summary>

| 引擎 | 适合谁 |
|---|---|
| **系统 OCR** | 优先尝试，免配置 |
| **Tesseract** | 经典开源 OCR，已经内置在 Cherry Studio 里，离线可用 |
| **Paddle OCR** | 中文识别效果更好（百度开源）；处理中文文档优先选 |
| **OpenVINO** | 用了 Intel 显卡能加速的高级用户可选 |

不知道选哪个就用默认。识别效果不满意时再换。
</details>

#### 2. 文档处理服务商 — 给 PDF / 复杂文档做结构化解析

普通文本 PDF 直接读就行，但带表格、多栏、扫描页的 PDF 需要更复杂的处理 —— 这就是**文档处理服务商**的工作。默认用 **MinerU**（一个免费云服务）：

| 服务商 | 简单说明 |
|---|---|
| **MinerU**（默认） | 免费云服务，专门处理复杂版式 PDF（学术论文、合同等），需到 [mineru.net](https://mineru.net) 注册拿一个 API Key |
| **Tesseract / Paddle OCR / OpenVINO** | 离线方案，不联网也能跑 |
| **三方 Provider** | 用你某家 AI 服务商的"看图"模型来识别（更智能但贵） |

### 配置 MinerU（默认方案）

1. 在 **API Key** 字段填入 MinerU 申请到的 key（点击 **Get API Key** 直达申请页）
2. **API Host** 保持默认 `https://mineru.net`
3. 切换到知识库或 Agent 时无需额外配置，会自动使用此处的设置

### 与知识库的关系

* 文档处理仅负责"非文本 → 文本"这一步
* 转换后的文本继续走 [嵌入模型](../../knowledge-base/emb-models-info.md) 向量化、入库
* 详细的"在知识库中启用"流程见 [知识库文档预处理](../../knowledge-base/document-preprocessing.md)

### 何时不需要配置

* 你只用知识库导入纯文本（`.md` / `.txt` / `.docx` 中的纯文字段落）→ 完全不经过文档处理
* 你只用对话功能、不传文件 → 同上

### 提示与技巧

* MinerU 对带表格 / 多栏排版的 PDF 效果显著优于 Tesseract，遇到学术论文等首选
* 离线场景请用 Paddle OCR 或 Tesseract（无网络也能跑）
* 切换处理器后，之前已向量化的资料**不会自动重做** —— 需手动重新导入

如遇问题，请在 [反馈与建议](../../question-contact/suggestions.md) 中提交反馈。
