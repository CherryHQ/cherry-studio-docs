import os
import re
import time
from datetime import datetime
from io import StringIO

import pandas as pd
import pytz
import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# 榜单配置
# ---------------------------------------------------------------------------
# 原 lmarena.ai 已更名为 Arena AI，新域名为 https://arena.ai/。
# 模型榜单现为一个目录，包含以下子榜单。
BASE_URL = "https://arena.ai"
OUTPUT_DIR = "other/model_rank"

# 每个榜单的配置：
#   slug          : 输出文件名（不含扩展名）与 README 链接标识
#   url           : Arena AI 榜单地址
#   title         : 页面标题
#   description   : 简短说明
#   model_col     : 表格中 "Model" 所在列的索引（0 基）
#   preferred     : 期望保留并翻译的英文列名（顺序即展示顺序）
#   top_n         : 快照展示的行数
LEADERBOARDS = [
    {
        "slug": "agent",
        "url": f"{BASE_URL}/leaderboard/agent",
        "title": "Agent 智能体榜单",
        "description": "评测模型在多轮工具调用 / 智能体任务上的综合表现，涵盖净改进率、确认成功率、赞踩比、可控性、Bash 恢复率、工具幻觉率等维度。",
        "model_col": 1,
        "preferred": [
            "Rank",
            "Model",
            "Net Improvement",
            "Confirmed Success",
            "Praise vs Complaint",
            "Steerability",
            "Bash Recovery",
            "Tool Hallucination",
            "Sessions",
        ],
        "top_n": 30,
    },
    {
        "slug": "text",
        "url": f"{BASE_URL}/leaderboard/text",
        "title": "文本榜单",
        "description": "Arena AI 最核心的文本对战榜单，根据人类盲投对战估算模型相对实力。",
        "model_col": 2,
        "preferred": ["Rank", "Rank Spread", "Model", "Score", "Votes", "Price $/M", "Context"],
        "top_n": 30,
    },
    {
        "slug": "search",
        "url": f"{BASE_URL}/leaderboard/search",
        "title": "搜索榜单",
        "description": "评测模型在联网搜索 / 信息检索类任务上的表现。",
        "model_col": 2,
        "preferred": ["Rank", "Rank Spread", "Model", "Score", "Votes", "Price $/M", "Context"],
        "top_n": 30,
    },
    {
        "slug": "vision",
        "url": f"{BASE_URL}/leaderboard/vision",
        "title": "视觉榜单",
        "description": "评测多模态模型在图像理解类任务上的表现。",
        "model_col": 2,
        "preferred": ["Rank", "Rank Spread", "Model", "Score", "Votes", "Price $/M", "Context"],
        "top_n": 30,
    },
    {
        "slug": "code-webdev",
        "url": f"{BASE_URL}/leaderboard/code/webdev",
        "title": "代码 / Web 开发榜单",
        "description": "评测模型在 Web 前端开发（HTML/CSS/JS）任务上的实际表现。",
        "model_col": 2,
        "preferred": ["Rank", "Rank Spread", "Model", "Score", "Votes", "Price $/M", "Context"],
        "top_n": 30,
    },
    {
        "slug": "text-to-image",
        "url": f"{BASE_URL}/leaderboard/text-to-image",
        "title": "文生图榜单",
        "description": "评测文生图模型根据文本提示生成图像的能力。",
        "model_col": 2,
        "preferred": ["Rank", "Rank Spread", "Model", "Score", "Votes"],
        "top_n": 30,
    },
]

# ---------------------------------------------------------------------------
# 表头中英文映射
# ---------------------------------------------------------------------------
# 覆盖当前所有榜单的英文表头，翻译为中文以便文档展示。
COLUMN_MAPPING = {
    # 通用列
    "Rank": "排名",
    "Rank Spread": "排名区间",
    "Model": "模型",
    "Score": "分数",
    "Votes": "票数",
    "Price $/M": "价格 $/百万Token",
    "Context": "上下文",
    # Agent 专属列
    "Net Improvement": "净改进率",
    "Confirmed Success": "确认成功率",
    "Praise vs Complaint": "赞踩比",
    "Steerability": "可控性",
    "Bash Recovery": "Bash 恢复率",
    "Tool Hallucination": "工具幻觉率",
    "Sessions": "会话数",
}


# ---------------------------------------------------------------------------
# 抓取与解析
# ---------------------------------------------------------------------------
def fetch_page_html(url, api_key):
    """
    使用 ScraperAPI 抓取指定 URL 的 HTML（启用渲染以获取 JS 渲染后的表格）。
    带重试与指数退避。
    """
    scraperapi_url = (
        f"http://api.scraperapi.com?api_key={api_key}&url={url}&render=true"
    )

    retries = 3
    delay = 60
    last_exc = None

    for i in range(retries):
        try:
            print(f"  Attempt {i + 1}/{retries} to fetch {url} via ScraperAPI...")
            response = requests.get(scraperapi_url, timeout=180)
            response.raise_for_status()
            print("  Successfully fetched page.")
            return response.text
        except requests.exceptions.HTTPError as e:
            last_exc = e
            if i < retries - 1:
                print(f"  HTTP error: {e}. Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                print("  All retries failed with HTTP errors.")
        except requests.exceptions.RequestException as e:
            last_exc = e
            if i < retries - 1:
                print(f"  Network error: {e}. Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                print("  All retries failed due to network errors.")

    if last_exc:
        raise last_exc
    return None


def parse_leaderboard_table(html, config):
    """
    解析页面 HTML 中的排行榜表格，返回 pandas DataFrame。

    - 自动定位 Model 列并保留其中的外链，转为 Markdown 超链接。
    - 其余单元格取纯文本。
    """
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table")
    if not table:
        print("  No <table> found on the page.")
        return None

    thead = table.find("thead")
    if not thead:
        print("  No <thead> found.")
        return None

    headers = [th.get_text(strip=True) for th in thead.find_all("th")]

    tbody = table.find("tbody")
    if not tbody:
        print("  No <tbody> found.")
        return None

    model_col = config["model_col"]
    # Rank 列在表头中的位置（用于只取排名数字、排除变化趋势等附加信息）
    rank_col = headers.index("Rank") if "Rank" in headers else None

    rows = []
    for tr in tbody.find_all("tr", recursive=False):
        cells = tr.find_all("td")
        if not cells:
            continue
        row_data = []
        for idx, cell in enumerate(cells):
            if idx == model_col:
                # Model 列：取其中的 <a> 标签文本与外链，转 Markdown 超链接
                link_tag = cell.find("a")
                if link_tag and link_tag.get_text(strip=True):
                    model_name = link_tag.get_text(strip=True)
                    href = link_tag.get("href", "")
                    if href:
                        full_url = (
                            f"{BASE_URL}{href}" if href.startswith("/") else href
                        )
                        row_data.append(f"{model_name} [<sup>1</sup>]({full_url})")
                    else:
                        row_data.append(model_name)
                else:
                    row_data.append(cell.get_text(strip=True))
            elif rank_col is not None and idx == rank_col:
                # Rank 列：单元格内可能同时包含排名数字与变化趋势，
                # 只取第一个排名数字（首个 <span>），排除附带的趋势数字。
                first_span = cell.find("span")
                if first_span:
                    rank_text = first_span.get_text(strip=True)
                    # 仅保留开头的数字部分，避免误带入其它文本
                    m = re.match(r"\d+", rank_text)
                    row_data.append(m.group(0) if m else rank_text)
                else:
                    txt = cell.get_text(strip=True)
                    m = re.match(r"\d+", txt)
                    row_data.append(m.group(0) if m else txt)
            else:
                row_data.append(cell.get_text(strip=True))
        # 行的列数可能与表头数不完全一致（合并单元格等），按表头对齐截断/补齐
        if len(row_data) < len(headers):
            row_data += [""] * (len(headers) - len(row_data))
        elif len(row_data) > len(headers):
            row_data = row_data[: len(headers)]
        rows.append(row_data)

    df = pd.DataFrame(rows, columns=headers)
    return df


# ---------------------------------------------------------------------------
# Markdown 生成
# ---------------------------------------------------------------------------
def _normalize_score(val):
    """清理 Score 单元格中的附加说明文本。

    Arena AI 的 Score 单元格会把分数、置信区间和标签拼在一起，例如：
      '1712+20/-20Preliminary' -> '1712 (+20/-20) Preliminary'
      '1385±5'                 -> '1385 (±5)'
      '1271±6Preliminary'       -> '1271 (±6) Preliminary'
    """
    if not isinstance(val, str):
        return val

    s = val.strip()
    if not s:
        return s

    # 提取开头的分数
    m = re.match(r"^(\d+)", s)
    if not m:
        return s
    base = m.group(1)
    rest = s[len(base):].strip()

    parts = [base]

    # 情况 1：+hi/-lo 格式（如 +20/-20）
    m_pm = re.match(r"^\s*([+\-]?\d+)\s*/\s*([+\-]?\d+)\s*(.*)$", rest)
    if m_pm:
        hi, lo, extra = m_pm.groups()
        parts.append(f"(+{hi}/{'+' + lo if lo and lo[0] != '-' else lo})")
        rest = extra.strip()
    else:
        # 情况 2：±n 格式（如 ±5）
        m_pm2 = re.match(r"^\s*±\s*(\d+)\s*(.*)$", rest)
        if m_pm2:
            ci, extra = m_pm2.groups()
            parts.append(f"(±{ci})")
            rest = extra.strip()
        else:
            # 情况 3：单独的 +n 或 -n
            m_pm3 = re.match(r"^\s*([+\-]\d+)\s*(.*)$", rest)
            if m_pm3:
                ci, extra = m_pm3.groups()
                parts.append(f"({ci})")
                rest = extra.strip()

    if rest:
        parts.append(rest)

    return " ".join(parts)


def generate_markdown(df, config, utc_now, beijing_now):
    """
    将 DataFrame 转换为带中文表头和说明的 Markdown 内容。
    """
    if df is None or df.empty:
        return "未能获取或解析排行榜数据。\n"

    df = df.copy()

    # 仅保留期望展示的列（按配置顺序），缺失的列自动跳过
    preferred = config["preferred"]
    visible_columns = [c for c in preferred if c in df.columns]
    if visible_columns:
        df = df.loc[:, visible_columns]

    # 清理 Score 列的附加文本
    if "Score" in df.columns:
        df["Score"] = df["Score"].apply(_normalize_score)

    # 重命名为中文表头
    df.rename(columns={c: COLUMN_MAPPING.get(c, c) for c in df.columns}, inplace=True)

    df = df.head(config["top_n"])

    utc_time_str = utc_now.strftime("%Y-%m-%d %H:%M:%S %Z")
    beijing_time_str = beijing_now.strftime("%Y-%m-%d %H:%M:%S %Z")

    md_table = df.to_markdown(index=False)

    url = config["url"]
    title = config["title"]
    description = config["description"]

    markdown_content = f"""# {title}

本页展示 [Arena AI]({url}) 榜单前 {config['top_n']} 名的每日快照，方便快速了解近期模型表现。完整榜单、筛选项和最新变化请到 Arena AI 官网查看。

{description}

> **数据更新时间**: {utc_time_str} / {beijing_time_str} (北京时间)

{{% hint style="info" %}}
排行榜反映特定评测和用户投票偏好，不等同于模型在你的任务中一定更好。选择模型时还要考虑价格、速度、上下文、工具调用、隐私和地区可用性。
{{% endhint %}}

## 前 {config['top_n']} 名

{md_table}

## 怎么看这张表

* **排名 / 排名区间**：Arena AI 根据对战投票估算的相对名次；排名区间表示在置信范围内的名次波动。
* **分数**：相对评分，适合比较同一时刻榜单中的模型。
* **票数 / 会话数**：样本量参考；样本较少时，排名通常更容易波动。
* **价格 $/百万Token**：输入 / 输出每百万 Token 的参考价格。
* **上下文**：模型支持的最大上下文长度。

## 选模型时再确认三件事

1. Provider 是否实际提供这个模型，以及你的地区和账户是否可用；
2. API 价格、速率限制和上下文是否适合你的任务；
3. 用 3～5 个真实任务做小规模测试，不要只看总榜名次。

## 数据来源

数据来自 [Arena AI 官方{title}]({url})，由 GitHub Actions 每天更新。模型价格、许可证和能力请以模型服务商官方信息为准。
"""
    return markdown_content


def generate_readme():
    """
    生成模型榜单目录页 README.md，列出所有子榜单。
    """
    lines = []
    lines.append("# 模型榜单\n")
    lines.append(
        "模型榜单用于辅助比较不同模型的相对表现，不应单独作为选型结论。数据来自 [Arena AI](https://arena.ai/)，由 GitHub Actions 每日自动更新。\n"
    )
    lines.append("选择模型时还应综合考虑任务类型、上下文长度、多模态与工具调用能力、速度、价格、地区可用性和数据政策。排行榜与价格会动态变化，请以页面标注的更新时间和模型服务商官方信息为准。\n")
    lines.append("## 榜单目录\n")
    for cfg in LEADERBOARDS:
        lines.append(f"* [{cfg['title']}]({cfg['slug']}.md)：{cfg['description']}")
    lines.append("")
    lines.append("***\n")
    lines.append("### 💡 获取帮助与提交反馈\n")
    lines.append(
        "如果您在配置或使用过程中遇到任何疑问、Bug 或有功能改进建议，请参考 [反馈与建议](../../question-contact/suggestions.md) 中提供的官方渠道。\n"
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def main():
    api_key = os.getenv("SCRAPER_API_KEY")
    if not api_key:
        print("错误：SCRAPER_API_KEY 环境变量未设置。")
        raise ValueError("SCRAPER_API_KEY is not set.")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    utc_now = datetime.now(pytz.utc)
    beijing_tz = pytz.timezone("Asia/Shanghai")
    beijing_now = utc_now.astimezone(beijing_tz)

    updated_files = []

    # 1. 生成各子榜单
    for cfg in LEADERBOARDS:
        print(f"\n=== Processing {cfg['slug']} ({cfg['url']}) ===")
        try:
            html = fetch_page_html(cfg["url"], api_key)
            df = parse_leaderboard_table(html, cfg)
            markdown_output = generate_markdown(df, cfg, utc_now, beijing_now)

            output_path = os.path.join(OUTPUT_DIR, f"{cfg['slug']}.md")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown_output)
            print(f"  Updated: {output_path}")
            updated_files.append(output_path)
        except Exception as e:
            print(f"  Failed to update {cfg['slug']}: {e}")

    # 2. 生成 / 更新目录页 README.md
    readme_path = os.path.join(OUTPUT_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(generate_readme())
    print(f"\nUpdated index: {readme_path}")
    updated_files.append(readme_path)

    # 3. 删除旧的 lmarena.md（已更名为 Arena AI 多榜单）
    old_file = os.path.join(OUTPUT_DIR, "lmarena.md")
    if os.path.exists(old_file):
        os.remove(old_file)
        print(f"Removed obsolete file: {old_file}")

    print("\nAll leaderboards updated.")
    print("Updated files:")
    for path in updated_files:
        print(f"  - {path}")


if __name__ == "__main__":
    main()
