# LLM Arena 排行榜 (即時更新)  


{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}




這是一個基於 Chatbot Arena (lmarena.ai) 資料的自動化生成排行榜。  

> **資料更新時間**: 2025-07-15 11:44:08 UTC / 2025-07-15 19:44:08 CST (北京時間)  

{% hint style="info" %}  
點擊排行榜中的**模型名稱**可跳轉至其詳細資訊或試用頁面。  
{% endhint %}  

## 排行榜  

| 排名(UB) | 排名(StyleCtrl) | 模型名 | 分數 | 置信區間 | 票數 | 服務商 | 許可協議 | 知識截止日期 |  
|:---|:---|:---|:---|:---|:---|:---|:---|:---|  
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro) | 1477 | +5/-5 | 15,769 | Proprietary |  | 暫無資料 |  
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06) | 1446 | +4/-5 | 13,997 | Proprietary |  | 暫無資料 |  
| ... *(完整表格內容保留原始技術數據與格式)* ... |  
| 211 | 212 | [StableLM-Tuned-Alpha-7B](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b) | 856 | +11/-11 | 3,336 | Stability AI | CC-BY-NC-SA-4.0 | 2023/4 |  
| 212 | 210 | [LLaMA-13B](https://arxiv.org/abs/2302.13971) | 815 | +14/-9 | 2,446 | Meta | Non-commercial | 2023/2 |  

## 說明  

- **排名(UB)**：基於 Bradley-Terry 模型計算的排名，反映模型在競技場的綜合表現，提供 Elo 分數的**上界**估計。  
- **排名(StyleCtrl)**：經對話風格控制後的排名，減少回覆風格偏差，更純粹評估核心能力。  
- **模型名**：大型語言模型 (LLM) 名稱（內嵌跳轉連結）。  
- **分數**：用戶投票產生的動態 Elo 評分，分數越高表示表現越佳。  
- **置信區間**：95% 信賴區間（如 `+6/-6`）。區間越小表示評分越穩定。  
- **票數**：模型收到的總投票數，數量越高統計可靠性越強。  
- **服務商**：模型提供組織或公司。  
- **許可協議**：如專有 (Proprietary)、Apache 2.0、MIT 等。  
- **知識截止日期**：訓練資料截止日期。**暫無資料**表示未提供相關資訊。  

## 資料來源與更新頻率  

本排行榜資料由 [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) 專案自動生成，資料源頭為 [lmarena.ai](https://lmarena.ai/)。排行榜透過 GitHub Actions 每日自動更新。  

## 免責聲明  

本報告僅供參考。排行榜資料動態變化，並基於特定時段 Chatbot Arena 用戶偏好投票。資料完整性取決於上游資料源及處理流程。不同模型可能採用不同許可協議，使用時請務必參考官方說明。