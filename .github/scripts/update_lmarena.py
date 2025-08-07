# scripts/update_lmarena_leaderboard.py

import requests
import pandas as pd
import os
from datetime import datetime, timedelta, timezone
import hashlib
import logging

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_file_hash(file_path):
    """
    计算文件的MD5哈希值
    """
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for {file_path}: {e}")
        return None

def update_leaderboard_data():
    """
    从 fboulnois/llm-leaderboard-csv 项目下载排行榜数据，
    处理后生成 Markdown 文件。
    """
    csv_url = 'https://github.com/fboulnois/llm-leaderboard-csv/releases/latest/download/lmarena_text.csv'
    output_file_path = 'other/model_rank/lmarena.md'

    logging.info(f'Attempting to download CSV from: {csv_url}')
    try:
        response = requests.get(csv_url)
        response.raise_for_status() # 如果请求失败，抛出异常

        from io import StringIO
        df = pd.read_csv(StringIO(response.text))
        logging.info(f'Successfully downloaded CSV with {len(df)} rows.')

        # 原始 CSV 列名
        original_columns = [
            'rank',
            'rank_stylectrl',
            'model',
            'arena_score',
            '95_pct_ci',
            'votes',
            'organization',
            'license',
            'knowledge_cutoff',
            'url' # 保留 url 列，用于嵌入到 model 列中
        ]

        # 确保所有原始列都存在
        for col in original_columns:
            if col not in df.columns:
                logging.error(f"Missing expected column in CSV: {col}. Please check the CSV structure.")
                return False

        df_selected = df[original_columns].copy() # 使用 .copy() 避免 SettingWithCopyWarning

        # --- 数据处理和格式化 ---

        # 将 'Unknown' 翻译为 '暂无数据'
        df_selected['knowledge_cutoff'] = df_selected['knowledge_cutoff'].replace('Unknown', '暂无数据')

        # 将 URL 嵌入到 'model' 列中，并创建新的 '模型名' 列
        # 格式：[模型名](链接)
        df_selected['model'] = df_selected.apply(
            lambda row: f"[{row['model']}]({row['url']})" if pd.notna(row['url']) else row['model'],
            axis=1
        )
        
        # 删除原始的 'url' 列，因为它已经嵌入到 'model' 中了
        df_selected = df_selected.drop(columns=['url'])

        # 格式化数值列
        df_selected['arena_score'] = df_selected['arena_score'].round(2)
        df_selected['votes'] = df_selected['votes'].apply(lambda x: f'{x:,}')

        # 定义最终的中文列名
        df_selected.columns = [
            '排名(UB)',
            '排名(StyleCtrl)',
            '模型名', # 现在包含链接
            '分数',
            '置信区间', # 简化列名
            '票数',
            '服务商',
            '许可协议',
            '知识截止日期'
        ]
        
        # --- 时间处理 ---
        # 获取当前 UTC 时间 
        utc_time = datetime.now(timezone.utc)
        # 定义北京时间时区 (GMT+8)
        cst_timezone = timezone(timedelta(hours=8))
        # 将 UTC 时间转换为北京时间
        cst_time = utc_time.astimezone(cst_timezone)

        update_time_utc = utc_time.strftime('%Y-%m-%d %H:%M:%S UTC')
        update_time_cst = cst_time.strftime('%Y-%m-%d %H:%M:%S CST (北京时间)')

        # --- 生成 Markdown 表格并调整对齐 ---
        table = df_selected.to_markdown(index=False)
        
        # 分割表格为行
        table_lines = table.split('\n')
        
        # 第二行是表头分隔线
        header_separator_line = table_lines[1]
        
        # 修改表头分隔线以强制所有列左对齐 (:---)
        modified_separator_parts = [':---' for _ in header_separator_line.split('|') if _]
        modified_separator_line = '|' + '|'.join(modified_separator_parts) + '|'
        
        # 用修改后的分隔线替换原始分隔线
        table_lines[1] = modified_separator_line
        
        # 将所有行重新组合成最终的 Markdown 表格字符串
        final_table_string = '\n'.join(table_lines)

        # --- 生成最终 Markdown 内容 ---
        markdown_content = f'''# LLM Arena 排行榜 (实时更新)

这是一个基于 Chatbot Arena (lmarena.ai) 数据的排行榜，通过自动化流程生成。

> **数据更新时间**: {update_time_utc} / {update_time_cst}

{{% hint style="info" %}}
点击排行榜中的 **模型名称** 可跳转至其详细信息或试用页面。
{{% endhint %}}

## 排行榜

{final_table_string}

## 说明

- **排名(UB)**：基于 Bradley-Terry 模型计算的排名。此排名反映了模型在竞技场中的综合表现，并提供了其 Elo 分数的 **上界** 估计，帮助理解模型的潜在竞争力。
- **排名(StyleCtrl)**：经过对话风格控制后的排名。此排名旨在减少因模型回复风格（例如冗长、简洁）带来的偏好偏差，更纯粹地评估模型的核心能力。
- **模型名**：大型语言模型 (LLM) 的名称。此列已嵌入模型相关链接，点击可跳转。
- **分数**：模型在竞技场中通过用户投票获得的 Elo 评分。Elo 评分是一种相对排名系统，分数越高表示模型表现越好。该分数是动态变化的，反映了模型在当前竞争环境中的相对实力。
- **置信区间**：模型 Elo 评分的95%置信区间（例如：`+6/-6`）。这个区间越小，表示模型的评分越稳定和可靠；反之，区间越大可能意味着数据量不足或模型表现波动较大。它提供了对评分准确性的量化评估。
- **票数**：该模型在竞技场中收到的总投票数量。投票数越多，通常意味着其评分的统计可靠性越高。
- **服务商**：提供该模型的组织或公司。
- **许可协议**：模型的许可协议类型，例如专有 (Proprietary)、Apache 2.0、MIT 等。
- **知识截止日期**：模型训练数据的知识截止日期。**暂无数据** 表示相关信息未提供或未知。

## 数据来源与更新频率

本排行榜数据由 [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) 项目自动生成并提供，该项目从 [lmarena.ai](https://lmarena.ai/) 获取并处理数据。此排行榜由 GitHub Actions 每天自动更新。

## 免责声明

本报告仅供参考。排行榜数据是动态变化的，并基于特定时间段内用户在 Chatbot Arena 上的偏好投票。数据的完整性和准确性取决于上游数据源及 `fboulnois/llm-leaderboard-csv` 项目的更新和处理。不同模型可能采用不同的许可协议，使用时请务必参考模型提供商的官方说明。
'''
        
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        
        current_hash = get_file_hash(output_file_path)
        new_hash = hashlib.md5(markdown_content.encode('utf-8')).hexdigest()

        if current_hash == new_hash:
            logging.info('No changes detected. Skipping file write.')
            return False
        else:
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            logging.info(f'Successfully updated {output_file_path}')
            return True

    except requests.exceptions.RequestException as e:
        logging.error(f'Error downloading CSV: {e}')
        return False
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
        return False

if __name__ == "__main__":
    if update_leaderboard_data():
        exit(0)
    else:
        exit(1)
