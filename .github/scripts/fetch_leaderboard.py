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
        'Rank (UB)': '排名 (UB)',
        'Model': '模型',
        'Score': '分数',
        '95% CI (±)': '95% 置信区间 (±)',
        'Votes': '票数',
        'Organization': '组织/公司',
        'License': '许可证'
    }

    df.rename(columns=column_mapping, inplace=True)

    utc_now = datetime.now(pytz.utc)
    beijing_tz = pytz.timezone('Asia/Shanghai')
    beijing_now = utc_now.astimezone(beijing_tz)
    
    utc_time_str = utc_now.strftime('%Y-%m-%d %H:%M:%S %Z')
    beijing_time_str = beijing_now.strftime('%Y-%m-%d %H:%M:%S %Z')

    # to_markdown 会自动处理单元格内的 Markdown 链接
    md_table = df.to_markdown(index=False)

    markdown_content = f"""# LLM Arena 排行榜 (实时更新)

这是一个基于 Chatbot Arena (lmarena.ai) 数据的排行榜，通过自动化流程生成。

> **数据更新时间**: {utc_time_str} / {beijing_time_str} (北京时间)

## 排行榜

{md_table}

## 说明

- **排名 (UB)**：基于 Bradley-Terry 模型计算的排名。此排名反映了模型在竞技场中的综合表现，并提供了其 Elo 分数的 **上界** 估计，帮助理解模型的潜在竞争力。
- **模型**：大型语言模型 (LLM) 的名称。部分模型名称可能已嵌入相关链接。
- **分数**：模型在竞技场中通过用户投票获得的 Elo 评分。Elo 评分是一种相对排名系统，分数越高表示模型表现越好。
- **95% 置信区间 (±)**：模型 Elo 评分的95%置信区间（例如：`±6`）。这个区间越小，表示模型的评分越稳定和可靠。
- **票数**：该模型在竞技场中收到的总投票数量。投票数越多，通常意味着其评分的统计可靠性越高。
- **组织/公司**：提供该模型的组织或公司。
- **许可证**：模型的许可协议类型，例如专有 (Proprietary)、Apache 2.0、MIT 等。

## 数据来源与更新频率

本排行榜数据由自动化脚本直接从 <sup>1</sup> [<sup>2</sup>](https://lmarena.ai/) 官方网站获取。此排行榜由 GitHub Actions 每天自动更新。

## 免责声明

本报告仅供参考。排行榜数据是动态变化的，并基于特定时间段内用户在 Chatbot Arena 上的偏好投票。数据的完整性和准确性取决于上游数据源。不同模型可能采用不同的许可协议，使用时请务必参考模型提供商的官方说明。
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
