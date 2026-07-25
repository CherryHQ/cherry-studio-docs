---
icon: file-lines
---

# 貢獻文件

Cherry Studio 社群版文件由 Markdown 存放庫維護，並透過 GitBook 呈現。你可以透過 GitHub Pull Request 貢獻，也可以在取得編輯權限後，透過 GitBook Change Request 修改。

* 文件存放庫：[CherryHQ/cherry-studio-docs](https://github.com/CherryHQ/cherry-studio-docs)
* 產品程式碼：[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)
* 公開文件：[docs.cherryai.com.cn](https://docs.cherryai.com.cn/)

大量更新、多語言修改，以及需要核對程式碼事實的頁面，應優先使用 GitHub；少量文案調整或需要視覺化評論時，可以使用 GitBook。

## 開始前先確認範圍

提交前請回答四個問題：

1. 要修改現有頁面，還是需要新增頁面？
2. 內容對應 Cherry Studio 的哪個版本，或 `main` 中的哪項行為？
3. 提交者可以可靠驗證哪些語言？
4. 是否需要產品螢幕擷取畫面，圖片能否補充文字無法說明的資訊？

如果內容涉及目前功能、設定名稱、模型能力或資料路徑，應先在產品 `main` 程式碼和實際介面中核對。不要只複製舊文件、第三方文章或模型產生的結果。

## 文件結構

簡體中文位於存放庫根目錄，其他公開語言位於：

| 語言 | 目錄 | 目錄檔案 |
| :--- | :--- | :--- |
| 簡體中文 | 存放庫根目錄 | `SUMMARY.md` |
| 中文（繁體） | `i18n/traditional-chinese/` | `i18n/traditional-chinese/SUMMARY.md` |
| English | `i18n/english/` | `i18n/english/SUMMARY.md` |
| 日本語 | `i18n/japanese/` | `i18n/japanese/SUMMARY.md` |
| Русский | `i18n/russian/` | `i18n/russian/SUMMARY.md` |

GitBook 預設使用根目錄中的 `README.md` 作為首頁，並以 `SUMMARY.md` 作為側邊欄目錄。每種語言都有獨立目錄和 `SUMMARY.md`，頁面層級與名稱應在對應語言中保持一致。

## 路徑一：透過 GitHub 貢獻

### 1. Fork 與複製

在 GitHub fork 文件存放庫，然後執行：

```bash
git clone https://github.com/YOUR_GITHUB_NAME/cherry-studio-docs.git
cd cherry-studio-docs
git remote add upstream https://github.com/CherryHQ/cherry-studio-docs.git
git fetch upstream
git switch -c docs/short-description upstream/main
```

### 2. 修改現有頁面

保留原本的檔案路徑，直接編輯對應的 Markdown。任意移動或重新命名檔案會變更頁面 URL；如果確實需要調整路徑，應在 PR 中列出舊位址和新位址，交由維護者確認重新導向。

修改多種語言時，請分別編輯各自目錄中的檔案。不要用簡體中文正文覆蓋其他語言，也不要讓英文或日文頁面繼續引用中文介面的螢幕擷取畫面。

### 3. 新增頁面

新增頁面至少應包含：

1. 簡體中文 Markdown 檔案。
2. `SUMMARY.md` 中位於正確章節的入口。
3. 能夠驗證的其他語言頁面和對應的 `SUMMARY.md` 入口。
4. 頁面使用的本機圖片。
5. 從相關上層頁面或相鄰教學進入新頁面的連結。

檔案名稱應使用穩定、易讀的英文或現有目錄風格。不要將日期、版本號或行銷標題寫入路徑，除非頁面本身只適用於該版本。

如果暫時無法可靠翻譯某種語言，請勿提交未經檢查的機器翻譯。請在 PR 描述中列出待補語言，方便維護者安排後續工作。

## 合格的產品文件頁面

文件結構取決於工作，但通常應包含：

* **用途**：讀者完成後可以得到什麼。
* **前提**：所需的版本、模型、帳戶、檔案或權限。
* **步驟**：使用目前的介面名稱，依照實際操作順序撰寫。
* **結果**：說明成功時會看到什麼、產生什麼或儲存在哪裡。
* **邊界**：平台差異、費用、隱私、資料傳送和不可逆操作。
* **疑難排解**：涵蓋最常見且能實際判斷的失敗原因。
* **下一步**：連結至接下來要使用的功能。

說明「為什麼這樣做」時應保持簡短，並服務於決策。不要加入撰寫過程、內部討論、未經驗證的背景或重複的產品宣傳。

### 文案要求

* 標題和按鈕名稱以目前的 UI 為準。
* 每個步驟只描述一個動作，並讓結果緊跟在動作之後。
* 動態價格、模型清單和活動資訊只在必要時出現，並註明以服務商目前頁面為準。
* 不要將相容介面等同於完整功能支援。
* 不要承諾第三方服務永遠免費、永久可用或一定傳回相同結果。
* 高風險操作應說明備份、權限和復原方式。
* API Key、Token、Cookie、個人路徑和真實對話不得出現在正文或程式碼範例中。

## 螢幕擷取畫面規範

螢幕擷取畫面只用於定位入口、解釋複雜狀態或呈現結果。如果文字已經足夠清楚，不需要為了「看起來完整」而增加圖片。

### 尺寸與構圖

Cherry Studio 桌面螢幕擷取畫面統一採用：

* 實體尺寸：`1920 × 1200`
* 長寬比：`16:10`
* DPR：`2`
* 同一頁面中的圖片應保持相同的視窗尺寸、裁切範圍和視覺比例

不要讓同一組圖片一張極寬、另一張接近正方形。盡量保留完整的操作脈絡，同時讓目標控制項清楚可見。

### 多語言

簡體中文、繁體中文、English、日本語和 Русский 頁面應使用對應語言的產品 UI。對話內容、助理名稱、範例檔案名稱和結果文字也應符合頁面語言。

如果某個介面在目標語言中確實尚未翻譯，應在 PR 中說明產品現況，不要使用其他語言的圖片假裝已經本地化。

### 隱私與檔案

* 使用虛構的帳戶、助理、目錄和對話內容。
* 隱藏 API Key、Token、電子郵件、使用者名稱、個人目錄和通知。
* 不要使用包含真實使用者資料的資料庫或知識庫。
* 圖片存入 `.gitbook/assets/`，並使用唯一且有意義的檔案名稱。
* 在 Markdown 中使用相對路徑，並加入描述圖片用途的 alt 文字。
* 不要引用含時效簽章的暫時下載 URL、私人飛書連結或本機絕對路徑。

建議使用 PNG 或 WebP。圖片應保持清晰，但應避免保留無意義的大面積空白和不必要的超大型檔案。

## Markdown 與 GitBook

存放庫使用常見 Markdown，並包含 GitBook 提示塊和圖片塊。修改時應沿用鄰近頁面的寫法。

### 內部連結

使用相對路徑：

```markdown
[智能體](../advanced-basic/agent.md)
```

目錄首頁可以連結至目錄或 `README.md`，但要先確認目標檔案存在。不要複製正式網站的完整 URL 來取代存放庫內的頁面連結，否則分支 Preview 和多語言路徑很容易跳回正式網站。

### 提示塊

只在資訊確實需要強調時使用：

```markdown
{% hint style="warning" %}
執行前請先備份資料。
{% endhint %}
```

同一頁面不要堆疊大量提示塊。一般步驟和補充說明直接使用段落或列表。

### 目錄檔案

`SUMMARY.md` 決定 GitBook 側邊欄層級。新增、移動或重新命名頁面時，應同步檢查對應語言的 `SUMMARY.md`：

```markdown
* [Agent 案例](advanced-basic/agent-an-li/README.md)
  * [黃金市場回顧 Agent](advanced-basic/agent-an-li/gold-price-case.md)
```

同一個 Markdown 檔案不能在同一份 `SUMMARY.md` 中重複引用。

## 本機檢查

提交前至少執行：

```bash
git status --short
git diff --check
git diff -- SUMMARY.md
```

並以人工確認：

* 所有新增的 Markdown 和圖片都已由 Git 追蹤。
* `SUMMARY.md` 中的路徑存在，而且縮排層級正確。
* 頁面中的相對連結和圖片路徑存在。
* 五種語言沒有互相串入正文或圖片。
* 程式碼塊、提示塊和 frontmatter 都已閉合。
* 沒有暫時 URL、真實金鑰、個人目錄和編輯器產生的重複檔案。

可以在 GitHub 中檢查 Markdown 排版，但 GitHub 和 GitBook 的轉譯並不完全相同。複雜提示塊、圖片尺寸、側邊欄層級和頁面跳轉，應在 GitBook Preview 中再次核對。

## 建立 Pull Request

提交並推送分支：

```bash
git add path/to/page.md SUMMARY.md .gitbook/assets/
git commit -m "docs(section): update page title"
git push -u origin docs/short-description
```

PR 描述至少應包含：

* 修改或新增了哪些頁面。
* 對應的產品版本、程式碼位置或官方來源。
* 已完成和待補的語言。
* 新增或替換了哪些圖片。
* 已執行的連結、結構和視覺檢查。
* 頁面路徑或側邊欄是否發生變更。

如果 PR 尚未準備好，可以先建立 Draft。維護者確認正文、事實、圖片和語言後再合併。

## Preview 與正式發布

文件存放庫連線 GitBook 後，GitHub 和 GitBook 可以雙向同步，但**同步存放庫和分支由 GitBook 管理員設定**。提交 PR 不會立即修改正式文件。

符合 GitBook 組態條件時，PR 中會出現含 Preview URL 的狀態檢查。需要注意：

* Preview 通常要求存取者登入 GitBook。
* 基於安全考量，從 fork 建立的 PR 預設可能不會產生 Preview；管理員可以變更此設定。
* 網站尚未發布或使用特定存取限制時，Preview 也可能無法使用。

因此，不要在 PR 描述中承諾任何人都能開啟 GitBook Preview。沒有自動 Preview 時，應由維護者提供審核環境，或在合併前使用內部預覽。

PR 合併至 GitBook 目前連線的分支後，提交內容才會進入 GitBook 同步和發布流程。合併權限與正式發布由維護者控制。

GitBook 官方參考資料：

* [Git Sync](https://gitbook.com/docs/integrations/git-sync)
* [GitHub Pull Request Preview](https://gitbook.com/docs/getting-started/git-sync/github-pull-request-preview)
* [README 與 SUMMARY 組態](https://gitbook.com/docs/getting-started/git-sync/content-configuration)

## 路徑二：透過 GitBook 編輯

需要 GitBook 編輯權限時，可以傳送電子郵件至 `support@cherry-ai.com`，標題填寫「申請 Cherry Studio Docs 編輯身分」，並說明：

* GitBook 帳戶電子郵件。
* 希望維護的章節和語言。
* 相關文件或產品經驗。
* 計畫進行的修改。

取得權限後，請在 GitBook 中建立 Change Request，而不是直接修改已發布內容。完成自我檢查後邀請維護者 Review；Change Request 合併時，GitBook 會依照管理員組態將變更同步至對應的 Git 分支。

大量修改、跨語言重構或大量圖片替換，仍建議使用 GitHub 分支，方便逐一檢閱檔案和執行自動檢查。

## Review 後如何處理

維護者可能會要求修正事實、減少圖片、補充來源或統一語言。更新時：

1. 只修改回饋涉及的範圍。
2. 保持五種語言的結構一致。
3. 圖片變更後，重新檢查語言、尺寸和隱私。
4. 回覆說明修改內容和驗證結果。

文件合併後如果發現問題，請繼續使用新的 PR 修正，不要透過刪除歷史或直接覆寫正式分支來隱藏錯誤。

程式碼貢獻請閱讀[貢獻程式碼](code.md)。不確定問題應寫在哪裡時，可以先查看[回饋與建議](../question-contact/suggestions.md)。
