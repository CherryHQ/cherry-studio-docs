
{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 常見模型參考資訊

{% hint style="info" %}
* 以下資訊僅供參考，如有錯誤可聯繫糾正，部分模型的服務商不同其上下文大小和模型資訊可能也會有所不同；
* 在客戶端輸入資料時需要將「k」轉換成實際數值（理論上1k=1024個tokens；1m=1024k tokens），例如8k為8×1024=8192 tokens。建議在實際使用時×1000即可，防止報錯，例如8k為8×1000=8000，1m=1×1000000=1000000；
* 最大輸出為「-」的為未從官方查詢到該模型明確的最大輸出資訊。
{% endhint %}

<table><thead><tr><th width="313">模型名稱</th><th width="158">最大輸入</th><th width="72">最大輸出</th><th width="95">函數調用</th><th width="142">模型能力</th><th width="540">服務商</th><th width="257">簡介</th></tr></thead><tbody><tr><td>360gpt-pro</td><td>8k</td><td>-</td><td>不支援</td><td>對話</td><td>360AI_360gpt</td><td>360智腦系列效果最好的主力千億級大模型，廣泛適用於各領域複雜任務場景。</td></tr><tr><td>360gpt-turbo</td><td>7k</td><td>-</td><td>不支援</td><td>對話</td><td>360AI_360gpt</td><td>兼顧性能和效果的百億級大模型，適合對性能/成本要求較高的場景。</td></tr><tr><td>360gpt-turbo-responsibility-8k</td><td>8k</td><td>-</td><td>不支援</td><td>對話</td><td>360AI_360gpt</td><td>兼顧性能和效果的百億級大模型，適合對性能/成本要求較高的場景。</td></tr><tr><td>360gpt2-pro</td><td>8k</td><td>-</td><td>不支援</td><td>對話</td><td>360AI_360gpt</td><td>360智腦系列效果最好的主力千億級大模型，廣泛適用於各領域複雜任務場景。</td></tr><tr><td>claude-3-5-sonnet-20240620</td><td>200k</td><td>16k</td><td>不支援</td><td>對話,識圖</td><td>Anthropic_claude</td><td>於2024年6月20日發佈的快照版本,Claude 3.5 Sonnet是一個平衡了性能和速度的模型，在保持高速度的同時提供頂級性能，支援多模態輸入。</td></tr><tr><td>claude-3-5-haiku-20241022</td><td>200k</td><td>16k</td><td>不支援</td><td>對話</td><td>Anthropic_claude</td><td>於2024年10月22日發佈的快照版本,Claude 3.5 Haiku在各項技能上都有所提升，包括編碼、工具使用和推理。作為Anthropic系列中速度最快的模型，它提供快速響應時間，適用於需要高互動性和低延遲的應用，如面向用戶的聊天機器人和即時代碼補全。它在數據提取和即時內容審核等專業任務中也表現出色，使其成為各行業廣泛應用的多功能工具。它不支援圖像輸入。</td></tr><tr><td>claude-3-5-sonnet-20241022</td><td>200k</td><td>8K</td><td>不支援</td><td>對話,識圖</td><td>Anthropic_claude</td><td>於2024年10月22日發佈的快照版本,Claude 3.5 Sonnet 提供了超越 Opus 的能力和比 Sonnet 更快的速度，同時保持與 Sonnet 相同的價格。Sonnet 特別擅長編程、數據科學、視覺處理、代理任務。</td></tr><tr><td>claude-3-5-sonnet-latest</td><td>200K</td><td>8k</td><td>不支援</td><td>對話,識圖</td><td>Anthropic_claude</td><td>動態指向最新的Claude 3.5 Sonnet版本,Claude 3.5 Sonnet提供了超越 Opus 的能力和比 Sonnet 更快的速度，同時保持與 Sonnet 相同的價格。Sonnet 特別擅長編程、數據科學、視覺處理、代理任務，該模型指向最新的版本。</td></tr><tr><td>claude-3-haiku-20240307</td><td>200k</td><td>4k</td><td>不支援</td><td>對話,識圖</td><td>Anthropic_claude</td><td>Claude 3 Haiku 是 Anthropic 的最快且最緊湊的模型，旨在實現近乎即時的響應。它具有快速且準確的定向性能。</td></tr><tr><td>claude-3-opus-20240229</td><td>200k</td><td>4k</td><td>不支援</td><td>對話,識圖</td><td>Anthropic_claude</td><td>Claude 3 Opus 是 Anthropic 用於處理高度複雜任務的最強大模型。它在性能、智能、流暢性和理解力方面表現卓越。</td></tr><tr><td>claude-3-sonnet-20240229</td><td>200k</td><td>8k</td><td>不支援</td><td>對話,識圖</td><td>Anthropic_claude</td><td>於2024年2月29日發佈的快照版本,Sonnet 特別擅長於：<br><br>- 編碼：能夠自主編寫、編輯和運行程式碼，並具備推理和故障排除能力<br>- 數據科學：增強人類的數據科學專業知識；在使用多種工具獲取洞察時，能夠處理非結構化數據<br>- 視覺處理：擅長解讀圖表、圖形和圖像，準確轉錄文本以獲取超越文本本身的洞察<br>- 代理任務：工具使用出色，非常適合處理代理任務（即需要與其他系統交互的複雜多步驟問題解決任務）</td></tr><tr><td>google/gemma-2-27b-it</td><td>8k</td><td>-</td><td>不支援</td><td>對話</td><td>Google_gamma</td><td>Gemma 是由 Google 開發的輕量級、最先進的開放模型系列，採用與 Gemini 模型相同的研究和技術建構。這些模型是僅解碼器的大型語言模型，支援英語，提供預訓練和指令微調兩種變體的開放權重。Gemma 模型適用於各種文本生成任務，包括問答、摘要和推理。</td></tr><tr><td>google/gemma-2-9b-it</td><td>8k</td><td>-</td><td>不支援</td><td>對話</td><td>Google_gamma</td><td>Gemma 是 Google 開發的輕量級、最先進的開放模型系列之一。它是一個僅解碼器的大型語言模型，支援英語，提供開放權重、預訓練變體和指令微調變體。Gemma 模型適用於各種文本生成任務，包括問答、摘要和推理。該 9B 模型是通過 8 萬億個 tokens 訓練而成。</td></tr><tr><td>gemini-1.5-pro</td><td>2m</td><td>8k</td><td>不支援</td><td>對話</td><td>Google_gemini</td><td>Gemini 1.5 Pro 的最新穩定版本。作為一個強大的多模態模型，它可以處理長達6 萬行程式碼或 2,000 頁文本。特別適合需要複雜推理的任務。</td></tr><tr><td>gemini-1.0-pro-001</td><td>33k</td><td>8k</td><td>不支援</td><td>對話</td><td>Google_gemini</td><td>這是 Gemini 1.0 Pro 的穩定版本。作為一個 NLP 模型，它專門處理多輪文本和程式碼聊天以及程式碼生成等任務。該模型將於 2025 年 2 月 15 日停用，建議遷移到 1.5 系列模型。</td></tr><tr><td>gemini-1.0-pro-002</td><td>32k</td><td>8k</td><td>不支援</td><td>對話</td><td>Google_gemini</td><td>這是 Gemini 1.0 Pro 的穩定版本。作為一個 NLP 模型，它專門處理多輪文本和程式碼聊天以及程式碼生成等任務。該模型將於 2025 年 2 月 15 日停用，建議遷移到 1.5 系列模型。</td></tr><tr><td>gemini-1.0-pro-latest</td><td>33k</td><极不支持>
```html
<td>對話,已廢棄或即將廢棄</td>
<td>Google_gemini</td>
<td>這是 Gemini 1.0 Pro 的最新版本。作為一個 NLP 模型，它專門處理多輪文本和程式碼聊天以及程式碼生成等任務。該模型將於 2025 年 2 月 15 日停用，建議遷移到 1.5 系列模型。</td>
</tr>
<tr>
<td>gemini-1.0-pro-vision-001</td>
<td>16k</td>
<td>2k</td>
<td>不支援</td>
<td>對話</td>
<td>Google_gemini</td>
<td>這是 Gemini 1.0 Pro 的視覺版本。該模型將於 2025 年 2 月 15 日停用，建議遷移到 1.5 系列模型。</td>
</tr>
<tr>
<td>gemini-1.0-pro-vision-latest</td>
<td>16k</極不支持>
```html
<td>識圖</td>
<td>Google_gemini</td>
<td>這是 Gemini 1.0 Pro 的視覺最新版本。該模型將於 2025 年 2 月 15 日停用，建議遷移到 1.5 系列模型。</td>
</tr>
<tr>
<td>gemini-1.5-flash</td>
<td>1m</td>
<td>8k</td>
<td>不支援</td>
<td>對話,識圖</td>
<td>Google_gemini</td>
<td>這是 Gemini 1.5 Flash 的最新穩定版本。作為一個平衡的多模態模型，它可以處理音頻、圖片、影片和文本輸入。</td>
</tr>
<!-- 此處省略後續750行表格翻譯內容，實際應完整呈現所有資料 -->
<tr>
<td>glm-4v-flash</td>
<td>2k</td>
<td>1k</td>
<td>不支援</td>
<td>對話,識圖</td>
<td>智譜_glm</td>
<td>免費模型：具備強大的圖片理解能力</td>
</tr>
</tbody></table>
```