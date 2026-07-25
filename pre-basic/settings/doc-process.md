---
icon: file-code
---

# 文档处理与 OCR

Cherry Studio V2 已把文件解析拆成两个相邻页面：

* `设置 → 文档处理`：把 PDF、Office 等文档转换成可索引的 Markdown；
* `设置 → OCR`：识别图片、截图和扫描页中的文字。

它们会被对话附件、翻译、知识库和 Agent 的文件工具复用。

## 文档处理

当前 V2 可按平台和配置选择：

* **MinerU**：云端复杂文档解析；
* **Open MinerU**：自部署 MinerU；
* **PaddleOCR**：自部署服务，支持文档解析模型；
* **Doc2X**；
* **Mistral**。

选择服务后按页面要求填写 API Key、API Host 或模型。知识库还可在自己的检索设置中指定处理服务商。

## OCR

当前 V2 的 OCR 候选包括：

* **系统 OCR**；
* **本地 PaddleOCR**：完全离线，首次使用前到 `设置 → 环境依赖` 下载约 140 MB 的模型；
* **Tesseract**：可选择语言包；
* **PaddleOCR**：连接自行部署的服务；
* **Mistral**；
* **Intel OV(NPU) OCR**：仅在兼容环境中显示或可用。

可用项会因操作系统、硬件和依赖安装状态不同而变化。

## 推荐配置

| 场景 | 建议 |
|---|---|
| 普通截图、少量图片 | 系统 OCR |
| Windows/Linux 离线中文识别 | 本地 PaddleOCR |
| 需要自定义语言包 | Tesseract |
| 复杂 PDF、论文、合同 | MinerU / Open MinerU 或其他文档处理服务 |
| 企业内网 | 自部署 PaddleOCR / Open MinerU |

## 与知识库的关系

文档处理和 OCR 负责从原始文件中提取文本；知识库随后再做分块、嵌入和检索。更换处理器不会自动重建旧数据，需在知识库中对相关数据源执行 **重新索引**。

详情见：

* [知识库教程](../../knowledge-base/knowledge-base.md)
* [文档预处理](../../knowledge-base/document-preprocessing.md)

## 常见问题

### 本地 PaddleOCR 不可选

打开 `设置 → 环境依赖` 下载 OCR 模型。下载完成后回到 OCR 页面重新选择。

### 扫描 PDF 只有空白或乱码

先确认 OCR 能单独识别其中一页，再选择适合复杂文档的处理服务，并重新索引。

### API 服务检测失败

检查 API Key、API Host、网络代理和账户状态。不要把真实密钥放入截图或反馈内容。

***

### 💡 获取帮助与提交反馈

如果您在配置或使用过程中遇到疑问，请参考 [反馈与建议](../../question-contact/suggestions.md)。
