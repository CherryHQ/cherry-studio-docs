---
icon: server
---

# Ollama

Ollama 可以在 macOS、Windows 和 Linux 上執行本機模型，也可以透過 Ollama Cloud 呼叫雲端模型。Cherry Studio V2 使用 Ollama 原生 Chat API，並從 `/api/tags` 同步目前執行個體可見的模型。

在本機執行時，模型推理和對話請求預設在你的裝置上完成；如果選擇 Cloud 模型、Ollama 雲端 API 或網路搜尋能力，請求仍會離開本機。

{% hint style="info" %}
在 Cherry Studio 中點選**新增**或同步模型，只會讀取 Ollama 現有的模型列表，不會下載模型權重。請先在 Ollama 中拉取模型，再回到 Cherry Studio 同步。
{% endhint %}

## 選擇使用方式

| 方式 | Base URL | API Key |
| --- | --- | --- |
| 同一台電腦上的 Ollama | `http://localhost:11434` | 留空 |
| 區域網路或遠端自建 Ollama | 伺服器實際位址 | 取決於反向代理 |
| 直接連線 Ollama Cloud | `https://ollama.com` | Ollama API Key |
| 本機 Ollama 代理 Cloud 模型 | `http://localhost:11434` | 本機登入後通常留空 |

本機 API 預設不需要身分驗證。Cherry Studio 在 API Key 非空時會傳送 `Authorization: Bearer ...`，可用於 Ollama Cloud 或設定了 Bearer 驗證的反向代理。

## 安裝 Ollama

前往 [Ollama 官網](https://ollama.com/)下載對應的系統版本並完成安裝。

Linux 也可以使用官方安裝指令碼：

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

安裝後確認服務正在執行：

```bash
ollama list
```

如果指令可以傳回模型列表，表示 Ollama CLI 與本機服務基本可用。

## 拉取模型

從 [Ollama 模型庫](https://ollama.com/library)選擇模型和標籤，然後執行：

```bash
ollama pull <model>:<tag>
```

例如：

```bash
ollama pull gemma3
```

常用管理指令：

```bash
ollama list
ollama ps
ollama stop <model>
ollama rm <model>:<tag>
```

- `ollama list`：查看已經拉取的模型；
- `ollama ps`：查看目前已載入的模型及 CPU/GPU 使用情況；
- `ollama stop`：從記憶體或顯示記憶體卸載模型；
- `ollama rm`：刪除本機模型檔案。

模型標籤會影響參數規模、量化方式、上下文和磁碟使用量。不要只看模型系列名稱，應根據記憶體、顯示記憶體和任務選擇特定標籤。

## 在 Cherry Studio 中設定

1. 開啟 `設定 → 模型服務`；
2. 將左側篩選切換為**全部服務商**；
3. 選擇 **Ollama**；
4. 在本機使用時保留 Base URL `http://localhost:11434`；
5. 本機服務的 API Key 留空；
6. 開啟頁面頂端的服務商開關；
7. 點選**新增**讀取 Ollama 模型列表；
8. 檢查同步預覽並套用變更；
9. 只啟用準備使用的模型。

Cherry Studio 會將 `http://localhost:11434`、包含 `/v1` 的位址或包含 `/api` 的位址標準化為 Ollama 原生 `/api` 路徑。為減少混淆，建議填寫不含特定介面的主機位址。

如果剛拉取的模型沒有出現，請先確認 `ollama list` 能看到完全相同的標籤，再重新點選**新增**。

## API Key 與 Cloud 模型

### 透過本機 Ollama 使用 Cloud 模型

先在 Ollama 中登入：

```bash
ollama signin
```

然後依官方說明拉取或執行包含 `:cloud` 的模型。Cherry Studio 仍連線 `http://localhost:11434`，由本機 Ollama 負責雲端驗證。

### 直接連線 Ollama Cloud

1. 在 Ollama 帳戶中建立 API Key；
2. 將 Base URL 改為 `https://ollama.com`；
3. 在 API Key 中填入該金鑰；
4. 同步雲端可用模型；
5. 執行連線和模型健康檢查。

{% hint style="warning" %}
API Key 不應寫入聊天訊息、文件、程式碼儲存庫或問題截圖。Cloud Key 洩漏後應立即在 Ollama 帳戶中撤銷並重新建立。
{% endhint %}

本機模型不會自動變成雲端模型。請確認模型標籤和目前連線的 Ollama 主機，以免誤判資料實際處理的位置。

## 選擇對話、視覺與工具模型

Ollama 模型能力由模型本身和標籤決定，Cherry Studio 會根據模型 ID 識別常見能力。

### 一般對話

任何支援 Ollama Chat API 的生成模型都可以用於基本對話。首次請求需要載入權重，回應可能明顯慢於後續請求。

### 視覺理解

選擇 Ollama 模型庫中明確標記支援 Vision 的模型。同步後檢查 Cherry Studio 是否顯示圖片能力，再上傳一張小型圖片測試。

- 模型名稱相似不代表都支援圖片；
- 不同標籤可能具有不同能力；
- 圖片會增加上下文和記憶體使用量；
- 模型 ID 未被自動識別時，不要只修改顯示名稱來偽裝能力。

### 工具呼叫與 MCP

模型必須原生支援 Tool Calling，Cherry Studio 才能穩定使用 MCP。

1. 選擇模型庫中明確支援工具呼叫的模型；
2. 先完成一般對話；
3. 只啟用一個簡單的 MCP 工具；
4. 明確要求模型呼叫工具；
5. 確認模型實際發起呼叫；
6. 再增加更多工具。

部分小型模型會輸出「打算呼叫工具」的文字，卻不會產生結構化呼叫。遇到這種情況應更換工具能力更強的模型，而不是重複增加提示詞。

## 設定思考模式

Ollama Chat API 使用 `think` 參數控制思考：

- 對支援 GPT-OSS 分級推理的模型，Cherry Studio 可以傳送低、中、高；
- 其他支援思考的模型通常只接受開啟或關閉；
- 選擇**關閉**時傳送 `think: false`；
- 使用預設或開啟時，實際行為仍取決於模型。

如果模型不支援 `think` 卻傳回參數錯誤，請關閉思考或改用正確的模型標籤。不要將一個模型的思考選項直接套用到所有本機模型。

## 上下文與硬體使用量

Ollama 的實際上下文由模型、伺服器設定和可用記憶體決定。更長的上下文會顯著增加 RAM 或 VRAM 使用量。

可以在啟動 Ollama 時設定預設上下文：

```bash
OLLAMA_CONTEXT_LENGTH=8192 ollama serve
```

查看模型是否在 GPU 上執行：

```bash
ollama ps
```

`PROCESSOR` 欄會顯示 CPU、GPU 或混合載入比例。

當 Cherry Studio 中填寫的模型上下文大於 Ollama 實際設定時，伺服器仍可能截斷輸入或傳回超限。應以 Ollama 執行階段設定和記錄為準。

## 模型載入與並行

Ollama 預設會在閒置後卸載模型以釋放資源。需要調整時，可以使用 Ollama 的 `OLLAMA_KEEP_ALIVE`、`OLLAMA_MAX_LOADED_MODELS`、`OLLAMA_NUM_PARALLEL` 和 `OLLAMA_MAX_QUEUE`。

- 讓模型保持常駐可以減少第一則回覆的等待時間，但會持續占用記憶體或顯示記憶體；
- 並行數越高，每個模型需要的上下文記憶體越多；
- 多個大型模型同時載入可能觸發排隊或卸載；
- 佇列已滿時，伺服器可能傳回 503。

不要只提高並行參數。請先使用 `ollama ps` 和系統監控確認硬體餘量。

## 知識庫與嵌入模型

Ollama 可以提供本機嵌入模型，用於知識庫和[全域記憶](../../advanced-basic/memory.md)。

1. 從模型庫拉取專用的嵌入模型；
2. 回到 Cherry Studio 同步模型；
3. 確認模型被識別為嵌入模型；
4. 在知識庫中選擇該模型；
5. 偵測維度並執行健康檢查；
6. 再匯入文件。

Ollama 在 Cherry Studio 中不支援重排序模型。需要 Rerank 時請選擇其他服務商。

嵌入模型一旦用於現有知識庫，就不應任意更換模型或維度；否則通常需要重新建構向量索引。

## PDF 與附件

目前的 V2 不會將 PDF 直接傳送給 Ollama。Cherry Studio 會先在本機擷取 PDF 文字，再交給模型：

- 文字型 PDF 通常可以處理；
- 掃描文件需要先執行 OCR；
- 表格、複雜排版和圖片資訊可能遺失；
- 擷取文字會占用模型上下文；
- PDF 中的圖片需要另外傳送給視覺模型。

## 連線遠端 Ollama

Ollama 預設只監聽 `127.0.0.1:11434`。若要讓其他裝置上的 Cherry Studio 連線，需要在 Ollama 主機設定監聽位址，例如：

```bash
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

不同系統設定環境變數和重新啟動服務的方式不同，請參閱 [Ollama FAQ](https://docs.ollama.com/faq)。

{% hint style="danger" %}
不要將未經驗證的 Ollama 連接埠直接暴露至公開網路。區域網路也應搭配防火牆；公開網路存取應使用 VPN 或具備 HTTPS 與驗證的反向代理。
{% endhint %}

連線 Docker、虛擬機器或 WSL 中的 Ollama 時，`localhost` 指向 Cherry Studio 所在的系統，不一定是容器或虛擬機器。請改用主機可連線的位址，並檢查連接埠對應。

## 檢查連線

1. 在 Ollama 主機執行 `ollama list`；
2. 確認目標模型已拉取；
3. 在 Cherry Studio 執行服務商連線檢查；
4. 點選**新增**同步模型；
5. 執行模型健康檢查；
6. 回到對話介面傳送簡單訊息；
7. 再測試思考、圖片、MCP 或知識庫。

本機指令也失敗時，請先修復 Ollama；只有 Cherry Studio 失敗時，重點檢查 Base URL、網路與模型標籤。

## 常見問題

### 無法連線 `localhost:11434`

Ollama 未啟動、連接埠已修改或遭防火牆封鎖。請先執行 `ollama list`，並檢查 Ollama 記錄。

### 模型列表為空

目前的 Ollama 主機沒有已拉取的模型，或 Cherry Studio 連線到錯誤的主機。`ollama list` 與 Cherry Studio 必須指向同一個執行個體。

### 找不到剛下載的模型

重新點選**新增**同步列表，並使用 `ollama list` 顯示的完整名稱和標籤。Cherry Studio 同步不會替你執行下載。

### 第一則回覆很慢

Ollama 正在將模型載入記憶體或顯示記憶體。使用 `ollama ps` 檢查載入位置；後續請求通常更快。

### 傳回記憶體不足、當機或持續排隊

請選擇參數規模較小或量化程度更高的模型，縮短上下文、降低並行，並停止其他已載入的模型。

### 傳回 503

伺服器負載過高或佇列已滿。請降低並行、等待目前請求完成，或調整 Ollama 佇列設定。

### 圖片或 MCP 無法使用

確認特定模型標籤支援相應能力，並檢查 Cherry Studio 是否正確識別。一般對話可用不代表模型支援視覺或工具。

### 遠端連線遭拒

確認 Ollama 已監聽非本機位址、連接埠已開放、反向代理路徑正確。不要透過關閉所有安全措施來解決公開網路連線問題。

更多一般設定請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。Ollama API 請參閱[官方文件](https://docs.ollama.com/api/introduction)；意見反應管道請參閱[意見反應與建議](../../question-contact/suggestions.md)。
