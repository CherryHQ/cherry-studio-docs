import pandas as pd
from datetime import datetime
import pytz
import os
from io import StringIO
import time
import requests
from bs4 import BeautifulSoup


def fetch_and_parse_leaderboard():
    """
    使用 ScraperAPI 抓取并使用 BeautifulSoup 解析 LMArena 排行榜页面，
    """
    api_key = os.getenv('SCRAPER_API_KEY')
    if not api_key:
        print("错误：SCRAPER_API_KEY 环境变量未设置。")
        raise ValueError("SCRAPER_API_KEY is not set.")

    target_url = "https://lmarena.ai/leaderboard/text"
    base_url = "https://lmarena.ai" # 用于拼接相对链接
    scraperapi_url = f'http://api.scraperapi.com?api_key={api_key}&url={target_url}'

    retries = 3
    delay = 60
    
    for i in range(retries):
        try:
            print(f"Attempt {i+1}/{retries} to fetch data via ScraperAPI...")
            response = requests.get(scraperapi_url, timeout=120) # 增加超时时间
            response.raise_for_status()
            print("Successfully fetched data via ScraperAPI.")

            # --- 使用 BeautifulSoup 解析 ---
            soup = BeautifulSoup(response.text, 'lxml')
            
            table = soup.find('table')
            if not table:
                print("No tables found on the page.")
                return None

            # 提取表头
            headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]
            
            # 提取表格数据行
            rows = []
            for tr in table.find('tbody').find_all('tr'):
                cells = tr.find_all('td')
                row_data = []
                for idx, cell in enumerate(cells):
                    # 检查是否是“Model”列（通常是第二列，索引为1）
                    if idx == 1:
                        link_tag = cell.find('a')
                        if link_tag and link_tag.has_attr('href'):
                            model_name = link_tag.get_text(strip=True)
                            href = link_tag['href']
                            # 拼接成完整的 URL
                            full_url = f"{base_url}{href}" if href.startswith('/') else href
                            # 创建 Markdown 格式的链接
                            markdown_link = f"{model_name} [<sup>1</sup>]({full_url})"
                            row_data.append(markdown_link)
                        else:
                            row_data.append(cell.get_text(strip=True))
                    else:
                        row_data.append(cell.get_text(strip=True))
                rows.append(row_data)

            # 创建 DataFrame
            df = pd.DataFrame(rows, columns=headers)
            return df

        except requests.exceptions.HTTPError as e:
            if i < retries - 1:
                print(f"Attempt {i+1} failed with HTTP error: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2
            else:
                print("All retries failed.")
                raise
        except requests.exceptions.RequestException as e:
            if i < retries - 1:
                print(f"A network error occurred: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2
            else:
                print("All retries failed due to network errors.")
                raise
    
    return None

# --- generate_markdown 函数保持不变（使用上一版的修改） ---

def generate_markdown(df):
    """
    将 DataFrame 转换为带有中文表头和更新版说明的 Markdown 格式。
    """
    if df is None or df.empty:
        return "未能获取或解析排行榜数据。"

    column_mapping = {
        'Rank': '排名',
        'Rank (UB)': '排名 (UB)',
        'Rank Spread': '排名区间',
        'Model': '模型',
        'Score': '分数',
        '95% CI (±)': '95% 置信区间 (±)',
        'Votes': '票数',
        'Organization': '组织/公司',
        'License': '许可证'
    }

    df.rename(columns=column_mapping, inplace=True)

    # The full upstream table contains hundreds of rows and several wide
    # metadata columns. Keep the public docs readable on laptop and mobile
    # screens by showing a concise top-30 snapshot; the complete live table
    # remains available on LMArena.
    preferred_columns = ['排名', '排名 (UB)', '模型', '分数', '票数']
    visible_columns = [column for column in preferred_columns if column in df.columns]
    if visible_columns:
        df = df.loc[:, visible_columns]
    df = df.head(30)

    utc_now = datetime.now(pytz.utc)
    beijing_tz = pytz.timezone('Asia/Shanghai')
    beijing_now = utc_now.astimezone(beijing_tz)
    
    utc_time_str = utc_now.strftime('%Y-%m-%d %H:%M:%S %Z')
    beijing_time_str = beijing_now.strftime('%Y-%m-%d %H:%M:%S %Z')

    # to_markdown 会自动处理单元格内的 Markdown 链接
    md_table = df.to_markdown(index=False)

    markdown_content = f"""# LLM Arena 排行榜

本页展示 [LMArena](https://lmarena.ai/leaderboard/text) 文本榜单前 30 名的每日快照，方便快速了解近期模型表现。完整榜单、筛选项和最新变化请到 LMArena 官网查看。

> **数据更新时间**: {utc_time_str} / {beijing_time_str} (北京时间)

{{% hint style="info" %}}
排行榜反映特定评测和用户投票偏好，不等同于模型在你的任务中一定更好。选择模型时还要考虑价格、速度、上下文、工具调用、隐私和地区可用性。
{{% endhint %}}

## 前 30 名

{md_table}

## 怎么看这张表

* **排名 / 排名 (UB)**：LMArena 根据对战投票估算的相对名次。
* **分数**：相对评分，适合比较同一时刻榜单中的模型。
* **票数**：样本量参考；票数较少时，排名通常更容易波动。

## 选模型时再确认三件事

1. Provider 是否实际提供这个模型，以及你的地区和账户是否可用；
2. API 价格、速率限制和上下文是否适合你的任务；
3. 用 3～5 个真实任务做小规模测试，不要只看总榜名次。

## 数据来源

数据来自 [LMArena 官方文本榜单](https://lmarena.ai/leaderboard/text)，由 GitHub Actions 每天更新。模型价格、许可证和能力请以模型服务商官方信息为准。
"""
    return markdown_content


def main():
    """
    主函数：执行抓取、转换和写入文件的操作。
    """
    output_filepath = "other/model_rank/lmarena.md"
    
    print("Fetching leaderboard data...")
    try:
        leaderboard_df = fetch_and_parse_leaderboard()
        
        if leaderboard_df is not None:
            print("Generating Markdown content...")
            markdown_output = generate_markdown(leaderboard_df)
            
            output_dir = os.path.dirname(output_filepath)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                print(f"Created directory: {output_dir}")
            
            with open(output_filepath, "w", encoding="utf-8") as f:
                f.write(markdown_output)
            print(f"'{output_filepath}' has been updated successfully.")
        else:
            print("Failed to update leaderboard after processing.")
    except Exception as e:
        print(f"An error occurred during the process: {e}")
        exit(1)


if __name__ == "__main__":
    main()
