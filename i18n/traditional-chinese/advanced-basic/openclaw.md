---
icon: spider
---

# OpenClaw

Cherry Studio 可以安裝並管理 OpenClaw、在本機啟動 OpenClaw Gateway，並將 Cherry Studio 中現有的模型服務同步至 OpenClaw。啟動成功後，Cherry Studio 會自動開啟內嵌的 OpenClaw 控制面板；你可以繼續在其中設定 WhatsApp、Telegram、Slack、Discord 等管道。

OpenClaw 是獨立執行的個人 AI 助手，不等同於 Cherry Studio 的[智能體](agent.md)。如果只需要在 Cherry Studio 中完成對話或工具任務，直接使用智能體即可；需要使用 OpenClaw 的控制面板、管道和執行方式時，再啟用本頁功能。

{% hint style="warning" %}
OpenClaw 擁有較高的系統權限，智能體任務也可能消耗較多 Token。請只在可信任的裝置和工作區中執行，並檢查它取得的檔案、指令和第三方管道權限。
{% endhint %}

## 開啟 OpenClaw

1. 點選頂部分頁列右側的 **+**，開啟**啟動台**。
2. 點選 **OpenClaw**。
3. Cherry Studio 會先檢查由自己管理的 OpenClaw 是否已安裝。

Cherry Studio 只使用位於自身管理目錄中的 OpenClaw 二進位檔。即使系統 `PATH` 中已存在透過其他方式安裝的 OpenClaw，頁面仍會提示安裝或遷移至受管理版本，以免誤用舊版本。

## 安裝受管理版本

第一次進入時，點選 **安裝 OpenClaw**。Cherry Studio 會依目前的作業系統和處理器下載對應的獨立二進位套件，並顯示安裝日誌。受管理版本不要求你事先安裝 Node.js 或 Git。

支援的組合包括 macOS、Windows 和 Linux 的 x64 或 ARM64。下載時會自動選擇可用來源；中國大陸網路環境會優先嘗試鏡像來源。

安裝完成後，頁面會顯示 OpenClaw 的安裝路徑。在 macOS 和 Linux 上，Cherry Studio 還會嘗試在 `/usr/local/bin/openclaw` 建立連結；在 Windows 上，則會嘗試將受管理目錄加入目前使用者的 `PATH`。這些步驟是為了方便從終端機呼叫，不會影響 Cherry Studio 透過受管理路徑啟動 OpenClaw。

## 選擇模型並啟動

啟動前，請先在 Cherry Studio 的模型服務設定中啟用至少一個可用的服務商，並確保對應模型可以正常呼叫。接著：

1. 在 OpenClaw 頁面選擇一個模型。
2. 點選 **啟動**。
3. Cherry Studio 會將所選服務商和模型設定同步至 OpenClaw。
4. Cherry Studio 會在本機啟動 Gateway，並等待健康檢查通過。
5. 啟動成功後，OpenClaw 控制面板會自動在 Cherry Studio 中開啟。

模型清單只會顯示已啟用且可用的服務商。Ollama、LM Studio 等本機服務可以不填寫 API Key；其他服務商通常需要先完成 API Key 和模型設定。

預設 Gateway 位址為 `127.0.0.1:18790`。執行期間，OpenClaw 頁面會顯示狀態和連接埠。關閉控制面板不會停止 Gateway；需要再次進入時，點選 **開啟控制面板**。

{% hint style="info" %}
每次點選 **啟動** 時，Cherry Studio 都會先同步目前選擇的模型。因此，更換模型後請先停止 Gateway，再選擇新模型並重新啟動。
{% endhint %}

## 同步了哪些設定

Cherry Studio 會合併寫入 `~/.openclaw/openclaw.json`，主要包括：

* 目前服務商的 API 位址、認證資訊和模型清單；
* 目前選擇的預設模型；
* 本機 Gateway 模式、連接埠和自動產生的認證令牌。

現有 OpenClaw 設定不會被整體取代；Cherry Studio 會保留同一模型下已存在的擴充設定，再更新自己管理的服務商和預設模型。如果偵測到舊的 `openclaw.cherry.json`，會將其遷移為 `openclaw.json`，並在需要時備份原始檔案。

{% hint style="warning" %}
OpenClaw 設定檔包含模型服務認證資訊和 Gateway 令牌。請勿分享此檔案、安裝日誌中的敏感內容，或包含令牌的控制面板位址。
{% endhint %}

## 停止、更新與解除安裝

### 停止 Gateway

返回 OpenClaw 頁面，點選 **停止**。正常結束 Cherry Studio 時，應用程式也會嘗試停止由它管理的 Gateway。

### 更新 OpenClaw

進入已安裝頁面時，Cherry Studio 會檢查受管理版本。發現新版本後，安裝路徑旁會顯示版本號；點選版本號並確認即可更新。更新前，執行中的 Gateway 會先停止；更新完成後，需要再次點選 **啟動**。

### 解除安裝 OpenClaw

在 Gateway 停止時，點選安裝路徑區域右側的 **解除安裝**，確認後等待日誌執行完成。Cherry Studio 會移除受管理的二進位檔及其指令連結或 `PATH` 項目。

解除安裝不會刪除 `~/.openclaw/openclaw.json`。如果不再需要其中的服務商認證資訊，請在確認沒有其他 OpenClaw 安裝使用此檔案後自行處理。

## 常見問題

### 安裝下載失敗

確認裝置可以存取下載來源，並在安裝日誌中查看具體錯誤。網路恢復後，可以直接再次點選安裝。如果目前平台或處理器沒有對應的二進位套件，安裝也會失敗。

### 已在終端機安裝，頁面仍提示未安裝

這是預期行為。Cherry Studio 不會執行系統 `PATH` 中的外部 OpenClaw；請在頁面中安裝 Cherry Studio 受管理版本。

### 沒有可選模型

前往模型服務設定，啟用服務商並完成 API Key、API 位址和模型設定。先在一般對話中確認模型可以正常回覆，再返回 OpenClaw 頁面。

### Gateway 無法啟動

預設連接埠 `18790` 可能已被其他程式占用。請先停止現有的 OpenClaw 程序或占用該連接埠的應用程式，再重新啟動。頁面會等待最多約 30 秒進行健康檢查；如果仍然失敗，可以複製錯誤資訊以供排查。

### 終端機找不到 `openclaw`

Cherry Studio 中的控制面板不依賴終端機指令。如果需要從終端機呼叫，請檢查受管理安裝路徑是否已加入 `PATH`；在 macOS 或 Linux 上，建立 `/usr/local/bin/openclaw` 連結可能因權限不足而失敗。

如需了解更多 OpenClaw 管道和控制面板用法，請查看 [OpenClaw 官方文件](https://docs.openclaw.ai/)。
