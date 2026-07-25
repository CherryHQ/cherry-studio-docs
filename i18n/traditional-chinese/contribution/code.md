---
icon: square-code
---

# 貢獻程式碼

Cherry Studio 接受功能、錯誤修正、測試、效能、無障礙和開發工具等程式碼貢獻。目前 V2 的日常開發位於 `main` 分支；開始前請先確認問題、變更範圍和驗證方法。

專案存放庫：[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)

## 開始前

請先閱讀：

* [貢獻者指南](https://github.com/CherryHQ/cherry-studio/blob/main/CONTRIBUTING.md)
* [行為準則](https://github.com/CherryHQ/cherry-studio/blob/main/CODE_OF_CONDUCT.md)
* [開發指南](https://github.com/CherryHQ/cherry-studio/blob/main/docs/guides/development.md)
* [專案開發約定](https://github.com/CherryHQ/cherry-studio/blob/main/CLAUDE.md)
* [開放原始碼授權條款](https://github.com/CherryHQ/cherry-studio/blob/main/LICENSE)

如果準備實作較大型的功能、變更使用者流程或重構公用介面，建議先搜尋 [Issues](https://github.com/CherryHQ/cherry-studio/issues) 和現有 Pull Request。沒有相關討論時，請先提交 Issue 說明問題、目標和方案，以減少重複工作和方向偏差。

第一次參與時，可以從下列標籤開始尋找合適的工作：

* [good first issue](https://github.com/CherryHQ/cherry-studio/labels/good%20first%20issue)
* [help wanted](https://github.com/CherryHQ/cherry-studio/labels/help%20wanted)
* [kind/bug](https://github.com/CherryHQ/cherry-studio/labels/kind%2Fbug)

## 選擇正確的分支

| 變更 | 基礎分支 | PR 目標分支 |
| :--- | :--- | :--- |
| 目前功能、V2 開發、重構、最佳化和錯誤修正 | `main` | `main` |
| 已發布 V1 的最小維護修正 | `v1` | `v1` |

V1 修正不會自動進入 `main`。如果同一個問題也存在於目前的開發分支，需要另外建立一個以 `main` 為目標的向前移植 PR。

不要直接向上游分支提交。請先 fork 存放庫，再從正確的基礎分支建立自己的短期功能分支。

## 準備開發環境

目前 `main` 在 `.node-version` 中固定使用 Node.js `24.11.1`，並在 `package.json` 中固定使用 pnpm `10.27.0`。這些版本會隨存放庫更新；每次開始工作時，都應以本機分支中的檔案為準。

### Windows：先啟用符號連結

存放庫使用符號連結同步部分檔案。Windows 使用者應在複製存放庫前：

1. 在系統設定中啟用**開發人員模式**，或取得建立符號連結的權限。
2. 執行：

```powershell
git config --global core.symlinks true
```

3. 再複製存放庫。如果存放庫是在尚未啟用符號連結時複製，建議啟用後重新複製。

### Fork 與複製

先在 GitHub 中 fork `CherryHQ/cherry-studio`，然後執行：

```bash
git clone https://github.com/YOUR_GITHUB_NAME/cherry-studio.git
cd cherry-studio
git remote add upstream https://github.com/CherryHQ/cherry-studio.git
git fetch upstream
git switch -c fix/short-description upstream/main
```

將 `YOUR_GITHUB_NAME` 和分支名稱替換為自己的值。功能分支可使用 `feat/`，錯誤修正可使用 `fix/`，文件變更可使用 `docs/`。

### 安裝 Node.js 與相依套件

使用支援 `.node-version` 或 `.nvmrc` 的版本管理工具，安裝存放庫要求的 Node.js。例如：

```bash
nvm install
nvm use
corepack enable
corepack pnpm install
```

請透過 Corepack 使用存放庫鎖定的 pnpm，不要使用其他全域 pnpm 改寫 `pnpm-lock.yaml`。除非確實修改了相依套件，否則 PR 不應包含無關的鎖定檔案變更。

### 建立本機環境檔案

```bash
cp .env.example .env
```

`.env` 已由 Git 忽略。只填寫本機開發所需的值，不要將真實的 API Key、Token、Cookie 或其他認證資訊提交至程式碼、測試、日誌和螢幕擷取畫面。

### 啟動應用程式

```bash
corepack pnpm dev
```

首次啟動會先產生 OpenAPI 檔案，再開啟 Electron 開發執行個體。偵錯主程序或轉譯程序時，可以使用：

```bash
corepack pnpm debug
```

如果相依套件安裝或啟動失敗，請先核對 Node.js 和 pnpm 版本、確認鎖定檔案沒有被其他套件管理工具修改，再查看終端機中的第一個錯誤。

## 開始修改

### 先瞭解局部約定

Cherry Studio 是包含 Electron 主程序、預載入層、React 轉譯層和多個共用套件的 monorepo。編輯某個目錄前：

1. 閱讀該目錄和上層目錄中的 `README.md`。
2. 查看附近的同類實作和測試。
3. 搜尋 `@deprecated` 標記，避免繼續擴充正在淘汰的介面。
4. 只修改解決目前問題所需的檔案。

轉譯層不應直接存取 Node.js API；需要跨程序能力時，應沿用 preload 和 IPC 邊界。日誌應使用專案的 `loggerService`，不要新增 `console.log`。

### 讓變更可以測試

修正問題時，應優先新增可重現問題的測試；新增行為時，請為成功、失敗和邊界情況補充測試。專案使用 Vitest，並依區域提供測試指令：

```bash
corepack pnpm test:main
corepack pnpm test:renderer
corepack pnpm test:aicore
corepack pnpm test:shared
```

不必每次都執行所有區域。開發期間先執行最接近變更的測試，提交前再執行完整檢查。

### 使用者可見文字

新增或修改介面文字時，應使用現有的國際化機制，不要在元件中直接撰寫只適用於單一語言的字串。至少執行：

```bash
corepack pnpm i18n:check
corepack pnpm i18n:hardcoded:strict
```

需要同步新鍵值時，請先閱讀存放庫的[國際化指南](https://github.com/CherryHQ/cherry-studio/blob/main/docs/guides/i18n.md)，再使用對應的指令碼。

### 資料庫結構

修改 Drizzle Schema 時，應產生並提交對應的移轉：

```bash
corepack pnpm db:migrations:generate
corepack pnpm db:migrations:check
```

如果 rebase 後移轉編號發生衝突，不要只修改 SQL 檔案名稱或手動編輯 snapshot。請依照存放庫的資料移轉文件重新產生，並確認移轉鏈和 Schema 一致。

## 提交前檢查

先查看實際變更：

```bash
git status --short
git diff --check
git diff
```

確認沒有暫存檔案、認證資訊、個人路徑、無關格式化或意外的鎖定檔案變更。

根據變更執行最相關的測試，然後執行存放庫提供的完整檢查：

```bash
corepack pnpm build:check
```

`build:check` 會執行程式碼規範、類型、OpenAPI、文件連結和測試等檢查。資料庫、嚴格國際化、技能或特定套件的檢查可能由 CI 另外執行；如果變更涉及這些區域，也應事先執行對應的指令。

{% hint style="info" %}
檢查指令碼和 Node.js 版本會隨 `main` 更新。如果本文指令與存放庫衝突，請以目前分支的 `package.json`、`.node-version`、`CONTRIBUTING.md` 和 CI 組態為準。
{% endhint %}

## 建立提交

專案要求小型且聚焦的 Conventional Commit，並要求提交包含 DCO sign-off：

```bash
git add path/to/changed-file
git commit --signoff -m "fix(module-name): describe the change"
```

常用類型包括 `feat`、`fix`、`refactor`、`docs`、`test` 和 `chore`。Scope 應指向特定模組，並使用簡短的 kebab-case 名稱，不要使用 `main` 這類過於籠統的範圍。

`--signoff` 會在提交訊息中加入：

```text
Signed-off-by: Your Name <your.email@example.com>
```

這表示你有權依照專案授權條款提交這項貢獻，不等同於 GPG 或 SSH 加密簽章。

## 與上游同步

建立 PR 前，將分支更新至最新的 `main`：

```bash
git fetch upstream
git rebase upstream/main
```

解決衝突並重新執行相關檢查後，再推送自己的分支：

```bash
git push -u origin fix/short-description
```

如果已推送過，並且因 rebase 需要更新遠端，請確認該分支僅由自己使用，再採用安全的 `--force-with-lease`；不要對共用分支直接強制推送。

## 提交 Pull Request

建立 PR 時：

1. 基礎存放庫選擇 `CherryHQ/cherry-studio`。
2. V2 和目前開發變更的 base 選擇 `main`。
3. 依照 PR 範本填寫變更前後、實作原因、取捨、相關 Issue、Breaking Change 和 Release Note。
4. 使用者可見的變更應附上螢幕擷取畫面或螢幕錄影，並說明測試系統和驗證步驟。
5. 只有在所有必要內容準備完成後，才要求 Review。

方向尚未確定或仍在開發時，可以先建立 **Draft PR**。Draft PR 會略過專案 CI，也不會自動指派 Review；準備完成後再標記為 Ready for review。

新貢獻者的非 Draft PR 可能會先取得 `needs-ok-to-test` 標籤，CI 不會立即執行。維護者在 PR 中加入 `/ok-to-test` 後，才會建立測試工作流程。這是正常的安全流程，不需要反覆關閉或重新開啟 PR。

## 處理 Review

收到意見後：

1. 逐項確認問題和預期行為。
2. 在原始分支提交小型且清楚的後續修改。
3. 重新執行受影響的測試。
4. 回覆說明修改位置和驗證結果。
5. 將已解決的討論交由 Reviewer 確認。

不要為了「讓 CI 變綠」而刪除有效測試、放寬類型或繞過安全檢查。如果失敗與目前 PR 無關，應在 PR 中提供日誌和重現依據，請維護者判斷。

## 常見問題

### 安裝相依套件後，鎖定檔案大量變更

通常是 Node.js 或 pnpm 版本不相符。復原自己無意產生的鎖定檔案變更，依照 `.node-version` 和 `packageManager` 重新準備環境，再執行 `corepack pnpm install`。

### Windows 中技能或同步檔案異常

確認在複製存放庫前已啟用開發人員模式和 `core.symlinks=true`。如果存放庫中的符號連結已被取出為一般檔案，請在啟用後重新複製。

### CI 一直沒有開始

先檢查 PR 是否仍為 Draft。新貢獻者還應查看是否存在 `needs-ok-to-test` 標籤；等待維護者執行 `/ok-to-test`。

### 不確定是否需要新增 Issue

小型、明確的錯誤修正可以直接提交 PR，並在描述中提供重現步驟。較大型功能、介面變更或有多種方案的變更，建議先使用 Issue 取得共識。

文件貢獻請閱讀[貢獻文件](docs.md)。其他問題可以透過[回饋與建議](../question-contact/suggestions.md)聯絡社群。
