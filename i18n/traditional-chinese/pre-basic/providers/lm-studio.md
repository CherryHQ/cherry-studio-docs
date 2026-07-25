# LM Studio

LM Studio 可在 macOS、Windows 和 Linux 上下載並執行本機模型，並透過 OpenAI 相容 API 向 Cherry Studio 提供對話、視覺、工具呼叫和嵌入功能。

Cherry Studio V2 內建 LM Studio 服務商，預設連線至 `http://localhost:1234`。一般對話使用 OpenAI 相容介面，模型清單來自 `/v1/models`。

{% hint style="info" %}
Cherry Studio 中的模型同步只會讀取 LM Studio 目前可見的模型，不會替你下載模型。請先在 LM Studio 的 **Discover** 頁面下載模型，再啟動本機 API Server。
{% endhint %}

## 準備 LM Studio

1. 從 [LM Studio 官網](https://lmstudio.ai/)下載並安裝最新版本；
2. 開啟 **Discover**，搜尋並下載模型；
3. 根據裝置記憶體或顯示記憶體選擇參數規模和量化版本；
4. 開啟 **Developer** 頁面；
5. 點選 **Start server** 啟動 API Server。

預設監聽位址為：

```text
http://localhost:1234
```

也可以在終端機啟動：

```bash
lms server start
```

首次使用時，建議先在 LM Studio 內完成一次載入和對話，確認模型本身能夠執行，再連線至 Cherry Studio。

## 選擇模型與量化

模型檔案、量化方式和上下文長度都會影響記憶體占用與速度。

- 參數規模越大，通常能力越強，但需要更多 RAM 或 VRAM；
- GGUF 模型可以使用 CPU 與 GPU 混合推論；
- Apple Silicon 可使用相容的 MLX 模型；
- 較低位元量化占用較小，但可能降低輸出品質；
- 上下文越長，KV Cache 占用越高；
- 視覺模型還需要處理圖片編碼，占用通常高於同規模的純文字模型。

不確定時，先選擇裝置能夠穩定載入的中小型模型和常見量化版本，再逐步增加參數規模或上下文。

LM Studio CLI 也可以估算資源占用：

```bash
lms load --estimate-only <model-key>
```

## 在 Cherry Studio 設定

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇 **LM Studio**；
4. 保留 Base URL `http://localhost:1234`；
5. LM Studio 未啟用驗證時，將 API Key 留空；
6. 開啟頁面頂部的服務商開關；
7. 點選**新增**或同步模型；
8. 檢查同步預覽並套用變更；
9. 只啟用準備使用的模型；
10. 執行模型健康檢查，再進入對話測試。

建議在 Base URL 中填寫主機和連接埠，不必手動附加 `/v1`。Cherry Studio 會透過 OpenAI 相容介面存取模型清單和對話介面。

## 模型清單為什麼會變化

LM Studio 的 `/v1/models` 會傳回伺服器目前可見的模型：

| LM Studio 設定 | 模型清單行為 |
| --- | --- |
| 開啟 Just-In-Time Model Loading | 可以傳回所有已下載模型，並在首次請求時自動載入 |
| 關閉 Just-In-Time Model Loading | 通常只傳回已載入記憶體的模型 |

因此，舊版教學中「必須先手動 Load 才能同步」的說法已不再適用於所有版本。

如果 Cherry Studio 中的模型清單是空的：

1. 確認 API Server 已啟動；
2. 在瀏覽器或終端機存取 `http://localhost:1234/v1/models`；
3. 檢查 LM Studio 是否已開啟 JIT Loading；
4. 關閉 JIT 時，先在 LM Studio 載入模型；
5. 返回 Cherry Studio 重新同步。

{% hint style="warning" %}
模型同步成功不代表裝置一定能夠載入該模型。開啟 JIT 後，未載入的模型也可能出現在清單中；首次對話才會觸發載入，並顯示記憶體不足、上下文過大等問題。
{% endhint %}

## API Token 與驗證

LM Studio 預設不要求 API Token。在本機使用時，Cherry Studio 的 API Key 可以留空。

LM Studio 0.4.0 及以上版本可以在 `Developer → Server Settings` 開啟 **Require Authentication**：

1. 開啟 **Manage Tokens**；
2. 建立 Token 並設定權限；
3. 複製新的 Token；
4. 在 Cherry Studio 的 LM Studio 服務商中填入該 Token；
5. 重新同步模型並執行健康檢查。

Cherry Studio 會將非空白的 API Key 作為 Bearer Token 傳送。LM Studio 也支援 OpenAI 與 Anthropic 相容介面常見的驗證標頭。

{% hint style="danger" %}
API Token 只會在建立時完整顯示。不要將 Token 寫入聊天、文件、程式碼儲存庫或問題截圖；外洩後應立即刪除並重新建立。
{% endhint %}

## 對話、視覺與 MCP

### 一般對話

選擇支援 Chat Completions 的指令模型。基礎對話正常後，再測試思考、圖片或工具呼叫。

本機模型的回答品質取決於模型、量化、提示範本和上下文設定。能夠成功傳回內容，只代表介面可用，並不表示模型適合所有工作。

### 視覺理解

LM Studio 的 OpenAI 相容 Chat Completions 支援文字和圖片，但具體模型必須具備視覺能力。

1. 下載明確標記為視覺模型的版本；
2. 在 LM Studio 中載入或允許 JIT 載入；
3. 同步到 Cherry Studio；
4. 確認模型顯示圖片能力；
5. 先傳送一張尺寸較小的圖片測試。

模型名稱相近不代表每個量化或變體都支援圖片。如果 Cherry Studio 未識別出視覺能力，應先確認模型 ID 和執行階段支援，不要只修改顯示名稱。

### 工具呼叫與 MCP

Cherry Studio 的 MCP 依賴模型輸出結構化 Tool Calling。LM Studio 會根據模型範本提供原生或相容模式，但實際穩定性仍由模型決定。

建議依下列順序測試：

1. 先完成一般對話；
2. 只啟用一個簡單的 MCP 工具；
3. 明確要求模型呼叫該工具；
4. 檢查是否產生結構化呼叫；
5. 確認工具結果能夠傳回給模型；
6. 再逐步增加工具數量。

小型模型可能只輸出「準備呼叫工具」的文字，而沒有真正發起呼叫。遇到這種情況，優先改用帶有原生 Tool Use 標記、參數規模更大或工具訓練更充分的模型。

Cherry Studio MCP 與 LM Studio 伺服器本身的 MCP 整合是兩條不同的鏈路。只使用 Cherry Studio MCP 時，不需要在 LM Studio 中重複設定同一個工具。

## 思考模型與結構化輸出

LM Studio 能否處理思考參數或結構化輸出，取決於模型範本和 OpenAI 相容實作。

- 優先使用 LM Studio 已明確支援的模型與範本；
- 不同模型的思考開關和強度參數並不通用；
- 如果啟用思考後傳回參數錯誤，先恢復預設或關閉思考；
- JSON 或結構化輸出失敗時，先在 LM Studio 中使用同一模型驗證；
- 不要透過修改模型顯示名稱偽裝成另一種能力。

## 模型載入、JIT 與顯示記憶體

開啟 JIT Loading 後，Cherry Studio 首次呼叫某個模型時，LM Studio 可以自動將它載入記憶體或顯示記憶體。首次回覆會明顯慢於後續請求。

LM Studio 0.4+ 還提供：

- **Idle TTL**：模型閒置多久後自動卸載；
- **Auto-Evict**：載入新模型前，自動卸載先前由 JIT 載入的模型；
- **Only Keep Last JIT Loaded Model**：只保留最近使用的 JIT 模型。

Cherry Studio 的 LM Studio 服務商頁面也會顯示**保持活躍時間**。實際是否卸載以及何時釋放記憶體，還會受到 LM Studio 的 JIT、TTL、Auto-Evict 和手動載入狀態影響；疑難排解時應以 LM Studio 的已載入模型清單和伺服器設定為準。

如需手動控制，可以使用：

```bash
lms load <model-key> --context-length 8192 --gpu max
lms unload <model-key>
lms unload --all
```

不要同時載入多個接近裝置上限的大型模型。頻繁切換模型時，開啟 Auto-Evict 通常比持續堆疊模型更穩定。

## 上下文長度

模型支援的最大上下文與實際載入的上下文不是同一個概念。LM Studio 載入模型時設定的 Context Length 才會決定目前執行個體的可用範圍。

上下文過長可能導致：

- RAM 或 VRAM 不足；
- 首次載入時間增加；
- 提示處理變慢；
- 請求被截斷或傳回超限；
- 視覺和長文件工作更容易失敗。

當 Cherry Studio 的模型資訊大於 LM Studio 的實際載入值時，應以 LM Studio 執行階段設定為準。先使用較短的上下文驗證穩定性，再視需要增加。

## 知識庫與嵌入模型

LM Studio 提供 OpenAI 相容的 `/v1/embeddings` 介面，可以執行專用嵌入模型。

1. 下載嵌入模型；
2. 在 LM Studio 中載入或允許 JIT 載入；
3. 在 Cherry Studio 同步模型；
4. 確認該模型被識別為嵌入模型；
5. 在知識庫中選擇該模型並偵測維度；
6. 執行健康檢查後再匯入文件。

Cherry Studio 中的 LM Studio 不支援重排序模型。需要 Rerank 時，應選擇其他服務商。

嵌入模型或維度一旦用於現有知識庫，就不應隨意更換；否則通常需要重新建立向量索引。

## PDF 與附件

目前 V2 不會將 PDF 原始檔直接傳送給 LM Studio。Cherry Studio 會先在本機擷取 PDF 文字，再交給模型：

- 文字型 PDF 通常可以處理；
- 掃描檔需要先進行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取的文字會占用上下文；
- PDF 中的圖片需要單獨傳送給視覺模型。

## Code Tools 與 Anthropic 相容介面

Cherry Studio 的 LM Studio 預設同時保留 Anthropic 相容位址，預設仍為 `http://localhost:1234`，供部分 Code Tools 使用。

LM Studio 提供 `/v1/messages`。如果 Code Tool 要求 Anthropic 相容服務：

1. 確認使用較新版本的 LM Studio；
2. 啟動 API Server；
3. 確認目標模型支援所需的工具能力；
4. 開啟驗證時填入同一個 Token；
5. 使用 LM Studio 中實際的模型識別碼；
6. 先以簡單工作驗證，再開放檔案或命令權限。

支援 Messages 介面不代表任何本機模型都能可靠完成程式碼代理工作。模型能力、上下文、工具呼叫品質和裝置效能都會影響結果。

## 連線至區域網路或遠端 LM Studio

如果 Cherry Studio 與 LM Studio 不在同一台裝置：

1. 在 LM Studio 的 Server Settings 開啟 **Serve on Local Network**；
2. 開啟 **Require Authentication** 並建立 Token；
3. 確認系統防火牆允許伺服器連接埠；
4. 在 Cherry Studio 中填入 LM Studio 主機的區域網路位址；
5. 填入 Token；
6. 先存取 `/v1/models`，再執行健康檢查。

CLI 也可以監聽所有網路介面：

```bash
lms server start --bind 0.0.0.0
```

不要將未經驗證的 LM Studio 連接埠直接暴露至公網。透過公網使用時，應使用 VPN，或設定具備完整 HTTPS、驗證和存取控制的反向 Proxy。

在 Docker、虛擬機器、WSL 或遠端桌面情境中，`localhost` 指向 Cherry Studio 所在的系統，不一定是執行 LM Studio 的主機。應改用實際可連線的位址。

## 常見問題

### 無法連線至 `localhost:1234`

LM Studio API Server 未啟動、連接埠已修改或被防火牆阻擋。先確認 Developer 頁面顯示伺服器正在執行。

### 模型清單是空的

檢查 `/v1/models` 是否有傳回內容。關閉 JIT 時，需要先載入模型；開啟 JIT 時，確認模型已下載且伺服器可以看到。

### 可以同步模型，但對話時發生錯誤

模型可能尚未成功載入、資源不足、上下文過大或介面範本不相容。查看 LM Studio 伺服器記錄和載入狀態。

### 首次回覆很慢

JIT 正在載入模型。後續請求通常會更快；也可以預先載入模型，但會持續占用記憶體或顯示記憶體。

### 傳回記憶體或顯示記憶體不足

改用較小的模型或壓縮程度更高的量化版本，縮短上下文；提高 GPU Offload 設定時應考量裝置餘裕，並卸載其他模型。

### 圖片或 MCP 無法使用

一般對話可用不代表模型具備視覺或工具能力。檢查模型版本、範本、Cherry Studio 的能力識別與 LM Studio 記錄。

### API Token 無效

確認 LM Studio 已開啟 Require Authentication、Token 未被刪除、權限正確，且 Cherry Studio 中沒有多餘的空格。

### 遠端連線遭拒

確認已開啟 Serve on Local Network、連接埠可連線、防火牆和反向 Proxy 路徑正確。不要透過關閉所有安全措施來解決公網連線問題。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。LM Studio 的伺服器、相容介面和模型管理請參閱[官方文件](https://lmstudio.ai/docs)；意見回饋管道請參閱[回饋與建議](../../question-contact/suggestions.md)。
