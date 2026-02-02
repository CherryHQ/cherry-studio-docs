# 金价暴跌看懵了？我用 Kimi K2.5 + Cherry Studio 做了个“复盘神器”（附 Agent 设计+完整教程）

最近黄金一跳水，很多人第一反应是：要不要跑？要不要抄？\
但回头看，黄金这种资产最擅长的就是“给市场上强度”。它的剧烈波动，其实经常能看到历史的影子：

* **宏观预期突然转向**（利率/通胀/美元走强），黄金容易快速回撤
* **风险事件升温**（冲突、金融系统压力），避险需求又会推高价格
* **流动性紧张**时，甚至会出现“先跌后涨”的反直觉走势

问题是：刷十条新闻，得到的是情绪；但你需要的是**证据链**。\
恰好，最近 月之暗面发布并开源了 **Kimi K2.5** 模型。——它是 Kimi 迄今最智能、最全能的开源模型，在 **Agent、代码、图像/视频** 等任务上达到开源 SOTA。

\
**于是，我产生了一个大胆的想法：** 既然人脑处理不过来这么多杂乱的信息，**能不能让 Kimi K2.5 住在 Cherry Studio 的 Agent 里，帮我把这次“黄金暴跌”扒个底朝天？**&#x4ECA;天这篇，不是枯燥的说明书，而是带你用最新的模型、最硬核的 Agent 技能，给自己配一个 24 小时待命的金融分析团队。文末会提供这个 Agent 的文件夹 `Kimi Agent`。你下载后，配置 3 分钟，就能跑。下面，我把设计逻辑、文件夹结构、组件拆解、运行流程，全扒给你看，如果你盯着 K 线纠结“要不要抄底”，或者被新闻轰炸却找不到真因，那你需要这个。<br>

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=NGNlY2IxYjE3MzQ2MzMxOTg0NDIyYzY5YmM3YmFjN2RfbkFmU0pJWnpFYjhRV21IQmE0MmNkeUl1Q1pKT3RodzBfVG9rZW46WHlURGI3NWk5b1FKaEt4bnZZdGNEUjM1blhjXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

### **为什么这样设计？（3 条硬逻辑，不绕弯）**

1. **数据真实第一，零容忍编造**：金融分析最怕“AI 幻觉”。所以强制每步标注来源 + 时间戳，抓不到就报错（不猜）。公开源（如 Kitco、Investing.com）确保零 API Key 门槛。
2. **任务拆模块化 + 并行**：Kimi K2.5 的亮点是“Agent 集群”（自主分身、并行 1500 步）。我们用 Cherry Studio 的 Skills + Sub-agents 模拟：数据抓取、新闻搜集、报告生成三路并进，效率翻倍。
3. **输出现代化**：不吐 Markdown（谁还看纯文字？），直接生成 HTML（Chart.js 图表 + 响应式布局），对标 Kimi K2.5 的代码生成能力。

结果：一份报告 = 近一年走势图 + 暴跌时间线 + 三情景预测 + 全来源链接。发给老板/群里，直接可用。<br>

### **📁 文件夹结构：为什么兼容 Claude Code？**

核心是 `.claude/` 目录——Cherry Studio 认这个，能自动加载 Skills 和配置。完整结构来自你的 `06-DIRECTORY_STRUCTURE.md`：

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=MjBiZGMwYzM4MTFmMzlkMzdmNTc1OTk1MWU0M2ViYjZfM0RXbkhKVWoyTTlGeG9NVFNUMXZ3S0wwU3dCZkdkZFFfVG9rZW46S1ZKSWJ6WHFjbzNYZkJ4MnR3QmNiQkNIbjRmXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

```python
Kimi Agent/                           # 项目根目录
├── .claude/                          # Cherry Studio Agent 核心配置区
│   ├── prompts/                      # 系统提示词（双语）
│   │   ├── system_prompt_cn.md       # 中文版：定义 Agent 行为 + 数据真实规则
│   │   └── system_prompt_en.md       # 英文版
│   ├── skills/                       # 3 个核心 Skills（自动识别）
│   │   ├── skill_financial_data_fetcher.md     # 数据抓取 + 验证
│   │   ├── skill_geopolitical_analyst.md       # 事件分析 + 时间线
│   │   └── skill_financial_report_generator.md # HTML 报告生成
│   ├── agents/                       # Sub-agents 配置
│   │   ├── subagent_financial_intelligence.md  # 量化分析子模块
│   │   └── subagents_usage_strategy.md         # 协作策略
│   ├── config/                       # 路径/工具配置
│   │   └── paths.conf
│   ├── settings.json                 # 主配置：模型 + 提示词路径 + 工具列表
│   └── mcp.json                      # MCP（工具服务器）配置
├── docs/                             # 文档备份（README、数据源、更新日志）
├── start-gold-agent.sh               # 一键启动脚本（可选）
├── USER_PROMPT_EXAMPLE.md            # 示例指令
└── 备份目录（core_config/ skills/ 等）# 原始文件备份，不参与运行
```

**为什么这样分？**

* `.claude/` 是 Cherry Studio 的标准识别路径：选中工作目录，它自动加载 Skills（文件名 `skill_*.md` → Skill 名 `financial-data-fetcher`）。
* 备份区防丢：原始 Skills 在根目录 skills/，运行时用 `.claude/skills/`。

<br>

### **🔧 核心组件拆解：3 个 Skills + 插件 + Sub-agents**<br>

#### **🧩 三大核心 Skills 设计详情**

我们来看看这三个“分身”具体是如何设计的，以及为什么要这么设计。

1. **Skill A：`financial-data-fetcher` (数据猎手) —— 拒绝幻觉**

* **设计痛点**：通用 LLM 最容易“瞎编”价格。你问金价，它可能编个 2023 年的数据给你。
* **Skill 逻辑**：
  * **硬约束**：我们在 Prompt 里写死了规则——_“禁止使用训练数据中的价格，必须调用工具”_。
  * **工具链**：配备了 `WebFetch`。它不是去“搜”百度，而是直接去“爬”指定的数据源网页（如 Kitco, GoldPrice.org, LBMA）。
  * **数据清洗**：它会将爬下来的乱七八糟的 HTML 清洗为干净的 `JSON` 格式（时间戳、开盘、收盘、涨跌幅）。
* **Kimi K2.5 的作用**：利用其强大的**长文档抽取能力**，从几万行网页代码中精准定位到那个 `$2,xxx.xx` 的数字。

2. **Skill B：`geopolitical-analyst` (地缘逻辑库) —— 拒绝噪音**

* **设计痛点**：黄金暴跌原因很多（美元涨？打仗？抛售？）。普通搜索会把营销号的假新闻也吸进来。
* **Skill 逻辑**：
  * **多源交叉**：不仅搜“金价”，还并行搜索“美元指数(DXY)”、“美联储会议纪要”、“地缘局势”。
  * **时间对齐**：它会执行一个核心逻辑——**“TimeStamp Matching”**。
    * _发现：_ 黄金在 UTC 14:30 暴跌。
    * _搜索：_ UTC 14:30 发生了什么？
    * _匹配：_ 发现美国在 UTC 14:30 发布了超预期的 CPI 数据。
    * _结论：_ 暴跌由通胀数据引发。
* **Kimi K2.5 的作用**：利用其 **Agent 集群（分身）能力**，它能模拟“同时阅读 20 篇新闻”，并过滤掉情绪化噪音，只保留事实。

3. **Skill C：`financial-report-generator` (前端工程师) —— 拒绝平庸**

* **设计痛点**：也是 Cherry Studio 最惊艳的一步。大多数 Agent 只会给你吐一段 Markdown 文字，甚至表格都歪歪扭扭。
* **Skill 逻辑**：
  * **代码优先**：这个 Skill 被训练为“只说代码语言”。它不写文章，它写 HTML + CSS + JavaScript。
  * **动态交互**：即使你没有编程基础，这个组件也会调用 `Chart.js` 库，把组件 A 抓到的数据变成可缩放、可悬停查看的 K 线图。
  * **视觉集成**：它会将组件 B 的分析结论，以“卡片”或“时间轴”的形式，嵌入到网页布局中。
* **Kimi K2.5 的作用**：利用其升级的 **Code（编程）** 能力，特别是前端构建能力。Kimi K2.5 生成的代码健壮性极高，几乎不需要人工 Debug 就能在浏览器跑通。

<br>

2. ### **Sub-agent 在这套 Agent 里的定位是什么？🧩**

下面把 **Kimi Agent（黄金市场分析 Agent）** 里“Sub-agent（子代理）”这一层讲清楚：它们是什么、为什么要用、怎么协作、你在文件夹里能看到什么。

> _先把话说透：_ _**Skills** 更像“可复用的流程模块”；**Sub-agent** 更像“带独立工作说明书的专职角色”。_

\
主 Agent（你在 Cherry Studio 里创建的 `Gold Market Analysis Agent`）负责三件事：

1. **拆任务**：把“分析黄金走势/复盘暴跌/写报告”分成若干独立子任务
2. **派任务**：把子任务分发给不同 Sub-agent（每个子代理有明确边界与输出格式）
3. **验收与汇总**：检查数据是否有来源、时间戳，是否出现缺口；最后交给报告生成模块产出 HTML

为什么不让一个 Agent 一把梭？

* 因为“搜数据、读新闻、算指标、写前端报告”对上下文和工具调用的要求不同，揉成一个 Prompt，最容易跑偏。
* 拆开后，每个子代理的规则可以写得更死：**允许用哪些工具、输出什么结构、遇到失败怎么处理**。

\
**这套配置里有哪些 Sub-agent？分别干什么？✅**&#x8FD9;个包里 Sub-agent 主要是三类（两类是系统预置，一类是自定义）：

#### **A. 系统预置：**`search-specialist`**（搜索与资料整理）**

* **name**: `search-specialist`
* **职责**：高级搜索、筛选结果、跨来源验证、整理引用
* **输出特点**：会给出搜索策略、来源 URL、关键引用（适合做“暴跌触发因素时间线”）

用在黄金分析里，它通常负责：

* “暴跌”的相关新闻源头、发布时间、关键句
* 央行、宏观数据发布（如 CPI、利率决议）对应的官方/权威来源页面
* 同一指标的多源校验（比如 Kitco vs GoldPrice vs Investing）

#### **B. 系统预置：**`business-analyst`**（指标与相关性分析）**

它的工具是 `Read, Write, Bash`，很适合做**结构化分析**：

* 相关性（黄金 vs DXY、黄金 vs 实际利率）
* ETF 持仓变化（如 SPDR Gold Trust）
* KPI 计算（年化波动率、回撤等——前提是拿到了真实数据）

它的价值在于：**把“看起来像分析”的描述，变成“可计算、有中间过程”的结论。**

#### **C. 自定义 Sub-agent：**`financial-intelligence-agent`**（历史数据/技术指标/预测）**

路径：`.claude/agents/subagent_financial_intelligence.md`它覆盖了更偏“量化流水线”的工作：

* 拉取历史数据（OHLCV、经济指标、利率、通胀等）
* 计算 RSI / MACD / 布林带 / 均线 / 波动率
* 输出一组可追溯的中间文件：CSV、JSON（例如 `gold_technical_indicators.csv`、`correlation_analysis.json`、`gold_price_forecast_12m.csv`）

> _这一层特别关键：它把“技术分析”从聊天内容里剥离出来，变成可落盘的产物。之后复用、对比、发给别人，都方便。_

<br>

2. ### **Sub-agent 是怎么被“调度”的？（并行策略）⚙️**

这套系统优先走 **并行**，因为黄金复盘天然是多源信息任务。

#### **Phase 1：并行收集（减少等待）**

* `search-specialist`：搜“暴跌当天关键新闻/数据发布时间线”
* `financial-intelligence-agent`：拉取近一年价格序列 + 计算指标
* `business-analyst`：计算相关性、整理 ETF/宏观的解释框架

#### **Phase 2：串行计算（有依赖的放后面）**

* 只有当历史数据落盘后，才计算指标/波动率/支撑阻力等
* 若发现数据缺口，再回到 `search-specialist` 补来源

#### **Phase 3：汇总交付**

* 主 Agent把三路结果“对齐时间戳、对齐口径”
* 再调用报告生成模块输出 HTML（含图表、时间线、引用清单）

这就是为什么这套 Agent 在“热点场景”更能打： **黄金暴跌=信息密集+口径混乱**，并行搜证 + 校验 + 汇总，能显著降低“看了很多但更迷糊”的情况。

***

4. ### **Sub-agent 和 Skills 的关系：别搞混了🤝**

在你的包里，两者是互补的：

* **Sub-agent**：更像“专用工作模式”，解决“谁来做、怎么做、用哪些工具、输出什么格式”的问题
* **Skills（.claude/skills/）**：更像“可重复调用的流程模块”，解决“这一步怎么稳定执行”的问题 例如：
  * `financial-data-fetcher`：强调多源校验、禁止编数字、输出结构化数据
  * `geopolitical-analyst`：强调事件分类、因果机制、时间线格式
  * `financial-report-generator`：强调 HTML 模板、Chart.js、来源列表、可打印样式

简单说： **Sub-agent 负责把工作分出去；Skills 负责让每一步更稳、更可复用。**<br>

5. ### **你在文件夹里怎么确认 Sub-agent “真的生效了”？🔍**

看两个地方就够了：

1. **目录是否标准**
   1. `.claude/agents/` 里有 `subagent_financial_intelligence.md`
2. **运行日志**（Cherry Studio 内）
   1. 你会看到工具调用和任务分派痕迹（WebSearch/WebFetch/Bash/Write）
   2. 最后能落地生成文件：例如 `gold_analysis_report.html`、若配置包含中间产物也会输出 CSV/JSON

如果你希望“更显眼”，可以在主 Prompt 里加一句硬约束：

> _“请在报告附录列出本次调用了哪些 sub-agent / skills，以及各自产出的文件名。”_

这样读者一眼就能看出：这不是聊天，这是流水线。<br>

#### **🛠️ 实战教程：三步复刻你的专属 Agent**

不用写代码，不用配环境。我打包了一&#x4E2A;**“Kimi Agent”文件夹**，你只要会“复制粘贴”就能用。

**Step 1：模型配置（月之暗面 的 `kimi-K2.5` + Anthropic 端点）**

这是让 AI 变聪明的核心。

1. 打开 Cherry Studio → **模型服务** → 点击 **月之暗面**

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=MjAxNTk2NmU2Mjc4YTEwMmI5MGNjNzc2MmQ1MDk1NTBfOFdwVExLZ3I3SFBqaUlrUWg4OXE5dWdIS3RpUWlDdEZfVG9rZW46SmY1ZmJQS1ZjbzhVY3F4dEZxSmM0V0dRbnZnXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

2. 跳转 月之暗面 开放平台获取 **API Key**（模型调用需要；数据抓取不需要额外 Key）

**⚠️ 高能预警（必做）：** 在 Cherry Studio 的配置里，把 **“端点类型 (Endpoint Type)”** 必须改为 `Anthropic`。

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=MDA0NGM2ZDRjNDgwZGNjNzQxZjgyOWVkODY2ZmI3OTZfdklZWlZDa3B6VnI4bEFhVjN5REQ2WXA2SDNvemJVcERfVG9rZW46SDc1OGIxZ1N1b1d2TkF4MXZiRWNPcmpnbktoXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

* _为什么要改？_ 因为 Cherry Studio 的 Agent 协议需要在 Anthropic 端点模式下运行，这样才能让 Kimi K2.5 完美调度上面提到的那些 Skills。

\
<br>

**Step 2：创建 Agent（直接挂载文件夹 `Kimi Agent`）**

> 文末我为你准备好了名为 `Kimi Agent` 的文件夹，里面预装了所有技能，你不需要手动重复写 Skills/Sub-agent。

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=Yzc5MGJkZGM3Y2UwZTdiMGRlZTM0ZDY2NTIwZGM4MzdfdnNFZFdNSURUNE5sWGI4ZmY3ekxmSGJwdjVLNDlIV1ZfVG9rZW46UzNvQmIxdFpmb3RkQ1J4dlZzT2NLbUZLbmJnXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

1. Cherry Studio → 助手列表旁点 **+** → **创建 Agent**
2. 名称：`Gold Market Analysis Agent`(或者你喜欢的名字)。
3. 模型：选择刚配置的 **月之暗面 /** `kimi-K2.5`
4. 工作目录：选择你下载并解压的 `Kimi Agent` 文件夹

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2E0NTY1NTYwZTQwY2VjNmY5N2UyOTA4M2EwNzcyM2VfQWtKM0thc0d0RnV1U3RLS0prajhoc3dqTllPSnVoME1fVG9rZW46RVFZWGJ3VkxJb2lKWkh4TThscmN6b1ZPbm5mXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

5. 打开文件夹里的系统提示词（例如 `.claude/prompts/system_prompt_cn.md`），粘贴到 Cherry Studio 的 **系统提示词**框。

<br>

### **Step 3：打开工具权限 + 插件 + Skills（照单全勾）**

<br>

1. **权限开启**：在 Agent 配置里开启权限并授权工具（少一个都可能卡住）：

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=YWRiMDYzOGQxNzZiNzliNDI0ZDc1M2E4MzYyZmM2MWRfdHRrajdjdmFsaGI5ekpnek9OM2tDaFVtbkgzTjNxdnRfVG9rZW46UnkzVGJrUjFTb21XQUp4NlpwRmM5dkFybmloXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

* `bash`
* `fetch`
* `edit`
* `multiedit`
* `webfetch`
* `web search`
* `write`

2. **配置插件：**

添加系统预置 plugin：

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=MTE0NzBiZjI2NTk0YjI5M2E3MjI2ZjNiMDM0YTM0NDZfRTlUMDFQbU5hdmNmanNkaWUwRTVyaDM2Tnd0WnZMZkFfVG9rZW46T3huTWJGQlo3b3NuNmJ4SnNHQWNIME50bjBmXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

* `business-analyst`
* `search-specialist`

系统 skills：

* `Excel Analysis`

<br>

**第三步：见证“魔法”**

一切就绪。打开文件夹里的 `USER_PROMPT_EXAMPLE.md`，里面有一段写好的**深度指令**，直接复制发送给 Agent。**这段指令会让 Agent 做三件事：**

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=M2NmYmVmNmY4YWQzMDRkYzhlYWFjZTQ4MjE4NWI4YmVfVWFEY1YyOFF3RnVTSEcxcjZkY1VOaEw1blUwRDFnUlpfVG9rZW46WnpyU2JhbDZvbzBmT0F4UGFaUWNSR1RCbmVqXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>



1. **查**：搜索黄金暴跌的具体跌幅和发生时间。
2. **找**：利用 Kimi K2.5 的联网能力，寻找月之暗面官方关于新模型的特性介绍（不准瞎编）。
3. **比**：寻找历史上类似的暴跌形态，分析是否有“影射”关系。



#### **📊 最终效果呈现：它交出了什么？**

点击发送，你会看到 Agent 开始疯狂运转。 日志里会显示：`Thinking...` -> `Searching News...` -> `Calculating...`一段时间后，你不会得到一句废话，而是会收到一份 **HTML 格式的深度研报**：

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjQ1YzkzY2ExNjBkOTFkZDhjMTdhNTc5ZGU2MzhiNzlfN2t2SFZobTdrMFpMWWhVVm9OZkx4dWJGd1ZUVUNjcmhfVG9rZW46TVRFZmJSR2tPb2Z3dE14cUdmZWN4RTJabkRoXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

* 📈 **近一年黄金走势可视化**（图表 + 表格）
* 🧷 **关键暴涨/暴跌区间标注**（尤其是“暴跌”）
* 🗓️ **事件时间线**（每条事件带来源链接，可复核）
* 📊 **技术指标/相关性分析**（有数据就计算；缺失就明确说明）
* 🔮 **三情景预测**（条件、区间、风险提示写清楚）
* 🧾 **数据来源清单**（URL + 抓取时间戳）

\
**最终，你会得到一个** `gold_analysis.html` **文件，打开即看：**<br>

<figure><img src="https://mcnnox2fhjfq.feishu.cn/space/api/box/stream/download/asynccode/?code=OWIyMjhlYzU2NjExYjE4MTgzMmFkMmU3YjhjNzEyZGFfVGZtbEVLNG41NE5hZkQ0S0tGMTZQSDB2YTM5ZDVra25fVG9rZW46SzRTbGI5VXRLb0o5d2J4aE9nV2MwMDRsblJlXzE3NzAwMTUyNzY6MTc3MDAxODg3Nl9WNA" alt=""><figcaption></figcaption></figure>

***

#### **💭 写在最后**

这次体验让我最震惊的，不是 Kimi K2.5 变得多强，也不是 Cherry Studio 有多好用。 而是 **“确定性”**。在金融市场，信息就是金钱。 以前我们靠猜，现在我们靠 Agent。

通过把 Kimi K2.5 装进 Cherry Studio，我们其实是给自己雇了一&#x4E2A;**“绝对理性、24小时联网、数据可溯源”**&#x7684;超级员工。

**这次黄金暴跌也许你没躲过，但如果学会了这套 Agent 玩法，至少在认知的维度上，你已经赚回来了。**\
\
当你掌握&#x4E86;**“把复杂任务拆解为 Skills 组件”**&#x8FD9;一核心逻辑，再加上 **Kimi K2.5** 在任务规划、工具调用上的质变，你会发现，你以前觉得“AI 做不到”的事情，现在都可以交付给 Agent 了：

* **🕵️♂️ 市场侦察兵**： 不想手动刷竞品网页？让 Agent 自动抓取 10 个竞品的最新价格与功能更新，清洗去重，每天早上 9 点把整理好的 Excel 对比表推送到你桌面。
* **💻 影子程序员**： 代码写不完？不仅是补全代码，你可以让 Agent 读取整个项目文件夹，根据需求自动编写功能模块、运行本地测试、修复 Bug，并顺手生成一份完美的 API 文档。
* **✈️ 极致旅行家**： 拒绝流水账攻略。让 Agent 根据你的预算实时比价机票酒店，综合天气与当地活动评价，规划一条精确到分钟的行程，甚至生成 PDF 路书。

\
**Agent 的真正魅力，不在于它能陪你聊多久，而在于它的自主性和交付力**——它能像今天的黄金分析师一样，在你喝咖啡的时候，默默把活儿干完。

这&#x79CD;**“任务自动化”**&#x7684;感觉，一旦体验过，就回不去了。我们诚挚地邀请你跳出框架，去探索更多硬核、有趣、实用的场景。无论是工作流优化，还是生活黑科技，请将你的奇思妙想和 Agent 配置文件分享出来。

📩 **投稿与交流**：[support@cherry-ai.com](mailto:support@cherry-ai.com)\
**别等未来了。属于你的 AI Agent 时代，从这一刻，已经开始。**

\
👇 **现在就下载，接入 Kimi K2.5，构建你的第一支数字化团队：**&#xD83D;� **附：Kimi Agent 配置文件夹下载链接 ：**&#x68;ttps://pan.quark.cn/s/1ef986d1a9f&#x66;_(请确保已安装 Cherry Studio v1.7.0+ 版本)_\
\
\
\
<br>
