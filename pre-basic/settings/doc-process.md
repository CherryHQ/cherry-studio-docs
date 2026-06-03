---
icon: file-code
---

# 文档处理

文档处理（DocProcess）是 v1.9.x 起独立出来的全局 OCR / 文档解析 pipeline，**所有需要把 PDF、图片、扫描件转换为文本的功能**（[知识库](../../knowledge-base/knowledge-base.md) 导入、对话中拖文件、Agent 读文件等）都会经过这里。

### 配置入口

打开 `设置 → 文档处理`：

<figure><img src="../../.gitbook/assets/cherry-docprocess.png" alt=""><figcaption><p>文档处理设置面板</p></figcaption></figure>

主要分两块：

#### 1. 系统 OCR

* **macOS**：MacOS requires no configuration ✅（自动使用系统 OCR API）
* **Windows**：需手动选择 OCR 引擎，可选 Tesseract / Paddle OCR / OpenVINO / 系统 OCR

#### 2. 文档处理服务商

| 服务商 | 说明 |
|---|---|
| **MinerU**（默认） | 云端文档解析服务，需 API Key。免费额度足够日常使用 |
| **Tesseract** | 离线 OCR，已捆绑在 Cherry Studio 中 |
| **Paddle OCR** | 国产离线 OCR，对中文版式效果较好 |
| **OpenVINO** | Intel 加速的本地 OCR |
| **三方 Provider** | 通过 OpenAI 兼容接口调用三方 Vision 模型 |

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
