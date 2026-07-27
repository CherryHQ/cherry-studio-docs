---
icon: cherries
---

# CherryIN

CherryIN 是 Cherry Studio 內建的模型服務商範本，可以透過一個帳戶連接多種模型。V2 為它預設了 OpenAI Chat Completions 和 Anthropic Messages 端點，並提供帳戶登入、餘額顯示、儲值入口和線路切換。

{% hint style="info" %}
CherryIN 與 [CherryAI 免費試用](cherryin/)不同。CherryIN 使用你自己的帳戶、憑證和餘額；CherryAI 是應用程式內的試用來源，不會出現在一般的模型服務清單中。
{% endhint %}

## 選擇登入方式

開啟 `設定 → 模型服務 → CherryIN`。你可以使用以下任一方式。

### 方式一：登入 CherryIN 帳戶

1. 點選**OAuth 登入**；
2. 在瀏覽器中完成登入和授權；
3. 返回 Cherry Studio；
4. 確認頁面顯示帳戶資訊和餘額；
5. 檢查 CherryIN 頂端的開關是否已開啟。

授權成功後，Cherry Studio 會取得帳戶可用的 API Key，並將透過 OAuth 取得的 Key 新增到 CherryIN 設定中。需要儲值時，可以使用帳戶卡片中的**儲值**按鈕開啟 CherryIN 控制台。

### 方式二：手動填寫 API Key

1. 開啟 [CherryIN Key 管理](https://open.cherryin.ai/console/token)；
2. 建立或複製一個可用的 Key；
3. 返回 Cherry Studio 的 CherryIN 頁面；
4. 在 API Key 區域新增該 Key；
5. 開啟服務商開關。

{% hint style="danger" %}
不要將 API Key 貼到聊天訊息、文件或問題截圖中。需要排查時，只保留經過遮蔽的前後少量字元。
{% endhint %}

## 選擇連線線路

CherryIN 在 V2 中提供三組網域：

| 頁面選項 | 網域 | 建議 |
|---|---|---|
| 加速線路 | `open.cherryin.cc` | 在中國大陸網路環境中優先嘗試 |
| 國際線路 | `open.cherryin.net` | 在海外或國際網路環境中優先嘗試 |
| 備用線路 | `open.cherryin.ai` | 主要線路暫時無法存取時嘗試 |

如果頁面顯示線路下拉式選單，切換線路會同時替換該服務商各端點的網域，並保留原有路徑。沒有下拉式選單時，可以在介面位址區域檢查目前的 Base URL。

{% hint style="warning" %}
線路名稱只代表預設入口，不保證在所有網路中速度相同。選擇後請執行連線檢查，並以實際結果為準。
{% endhint %}

## 同步並啟用模型

1. 在**模型清單**區域點選**新增**；
2. 查看同步預覽中的新增、更新和移除項目；
3. 套用變更；
4. 搜尋準備使用的模型；
5. 開啟目標模型的開關；
6. 執行模型健康檢查。

CherryIN 的模型清單、價格和可用額度會調整，因此本文不會固定列出具體模型。請查看 [CherryIN 模型與價格](https://open.cherryin.ai/pricing)，並以用戶端同步結果為準。

## 介面與模型

CherryIN 範本預設 OpenAI 與 Anthropic 相容端點。Cherry Studio 會結合模型資訊和端點類型傳送請求。

- 一般對話模型通常使用 OpenAI 相容介面；
- Claude 等模型可以使用 Anthropic 相容介面；
- 部分 Gemini 或圖片模型會使用專用路由；
- 同名模型由不同端點提供時，能力和參數可能不同。

不要只根據模型名稱判斷 Agent、視覺、推理或工具呼叫能力。請查看模型標籤並完成實際測試。

## 驗證設定

建議依序完成：

1. 在身分驗證區域執行連線檢查；
2. 在模型清單中執行健康檢查；
3. 返回對話介面選擇目標模型；
4. 傳送一則簡單的文字訊息；
5. 如果需要圖片或工具呼叫，再分別進行最小測試。

只有服務商開關和模型開關都已啟用時，模型才會出現在模型選擇器中。

## 帳戶與登出

透過帳戶登入後，Cherry Studio 可以顯示 CherryIN 帳戶資訊和餘額。點選**登出**會清除儲存在本機的 CherryIN OAuth 登入狀態，並移除透過 OAuth 新增的 Key。

手動新增的 Key 與 OAuth Key 來自不同來源。如果仍需使用手動 Key，請在登出後確認它仍處於啟用狀態。

## 常見問題

### 登入後沒有返回 Cherry Studio

請讓 Cherry Studio 保持執行，並在瀏覽器中重新完成授權。如果系統阻止應用程式連結回呼，請允許瀏覽器開啟 Cherry Studio。

### 登入成功，但模型清單為空

請先點選**新增**。如果仍為空，請檢查帳戶是否有可用的 Key、目前線路是否可以存取，以及 CherryIN 控制台是否已對帳戶開放模型。

### 傳回 401 或 403

Key 可能已失效、遭停用或沒有模型權限。請重新登入，或在 Key 管理頁面建立新 Key 後取代。

### 請求逾時或無法連線

切換加速、國際或備用線路，然後重新執行連線檢查。你也應該檢查系統代理伺服器、防火牆和本機網路。

### Claude 或 Agent 請求失敗

確認所選模型帶有工具呼叫能力，並檢查請求是否使用 Anthropic 相容端點。服務商支援 Anthropic 端點，不代表其中每個模型都支援 Agent。

更多一般設定與多 Key 說明，請參閱[模型服務](README.md)和[模型服務設定](../../cherrystudio/preview/settings/providers.md)。如果仍無法使用，請提交 Cherry Studio 版本、作業系統、模型 ID 和去識別化後的錯誤資訊；意見回饋管道請參閱[意見回饋與建議](../../question-contact/suggestions.md)。
