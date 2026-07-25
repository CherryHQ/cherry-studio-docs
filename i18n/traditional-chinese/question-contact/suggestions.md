---
icon: file-signature
---

# 意見與建議

選擇適合的管道並提供可重現的資訊，可以顯著提升問題被確認與處理的速度。

## 先選擇意見管道

| 需求 | 建議管道 | 適合提交的內容 |
| :--- | :--- | :--- |
| 軟體故障 | [GitHub Bug Report](https://github.com/CherryHQ/cherry-studio/issues/new/choose) | 當機、功能異常、回歸問題、介面錯誤 |
| 功能建議 | [GitHub Feature Request](https://github.com/CherryHQ/cherry-studio/issues/new/choose) | 新功能、互動改善、現有能力增強 |
| 使用討論 | [GitHub Discussions](https://github.com/CherryHQ/cherry-studio/discussions) | 使用方式、經驗分享、方案討論 |
| 安全漏洞 | [GitHub Security Advisory](https://github.com/CherryHQ/cherry-studio/security/advisories/new) | 可能洩漏資料、繞過權限或執行未授權操作的漏洞 |
| 無法使用 GitHub | [support@cherry-ai.com](mailto:support@cherry-ai.com) | 無法登入 GitHub，或不適合公開傳送的一般支援資訊 |

{% hint style="warning" %}
請勿在公開 Issue 或群組聊天中揭露安全漏洞的重現細節。請使用私密的 Security Advisory。
{% endhint %}

## 提交前先做四件事

1. 更新到最新穩定版本，並確認問題仍可重現。
2. 查看[常見問題](questions.md)，排除設定、額度、網路與模型服務商問題。
3. 搜尋現有的 [Open Issues](https://github.com/CherryHQ/cherry-studio/issues)、[Closed Issues](https://github.com/CherryHQ/cherry-studio/issues?q=is%3Aissue%20state%3Aclosed) 與 [Discussions](https://github.com/CherryHQ/cherry-studio/discussions)。
4. 刪除截圖、日誌與設定中的 API Key、Token、Cookie、個人檔案路徑及對話隱私。

已有相同問題時，請優先補充新的重現資訊，不要重複建立 Issue。

## 回報 Bug

### 標題

標題應包含**功能、平台與現象**，讓維護者不開啟本文也能大致判斷問題。

```text
[Bug] macOS：知識庫重新索引後一直顯示處理中
```

不要只寫「無法使用」、「有問題」或「請修正」。

### 必填資訊

一份可處理的 Bug 報告至少應包含：

* Cherry Studio 版本。
* Windows、macOS 或 Linux 及系統版本。
* 涉及的功能、模型服務商與模型名稱；請勿提供 API Key。
* 可穩定重現的操作步驟。
* 實際結果與預期結果。
* 問題從哪個版本或哪項操作後開始出現。
* 已嘗試的疑難排解方法。
* 必要的截圖、螢幕錄影與去識別化日誌。

版本資訊可在**設定 → 關於**中查看。應用程式日誌可從**設定 → 資料設定 → 資料 → 應用程式日誌**開啟。

### 建議範本

```markdown
## 環境

- Cherry Studio：
- 系統：
- 安裝來源：
- 模型服務商 / 模型：

## 重現步驟

1.
2.
3.

## 實際結果


## 預期結果


## 補充資訊

- 是否穩定重現：
- 從哪個版本開始：
- 已嘗試：
- 去識別化日誌 / 截圖：
```

### 最小重現

如果問題與特定助理、知識庫、MCP 或自訂 CSS 有關，請先嘗試縮小變數：

* 建立一個空白助理或話題。
* 暫時關閉無關的 MCP、技能與連網搜尋。
* 使用一小段不敏感的測試內容。
* 記錄「啟用哪項設定後出現問題」。

最小重現比完整環境截圖更容易定位根本原因。

## 提交功能建議

功能建議不只要描述「想要什麼」，還應說明「目前遇到什麼問題」。

建議包含：

1. **使用情境**：誰在什麼工作流程中遇到問題。
2. **目前障礙**：現有功能為何無法滿足需求。
3. **預期結果**：理想操作與輸出是什麼。
4. **替代方案**：目前如何繞過，以及有哪些缺點。
5. **範圍與邊界**：哪些情況必須支援，哪些可以暫不支援。
6. **示意材料**：必要時提供去識別化截圖、流程圖或互動草圖。

一個 Issue 應儘量只討論一項獨立需求。將多個無關需求放在同一條中，會增加確認範圍與排程的難度。

專案方向可以參考 [Cherry Studio Roadmap](https://github.com/orgs/CherryHQ/projects/7)。Roadmap 不代表交付承諾，具體範圍與時間應以專案維護者的最新說明為準。

## 提問與討論

一般使用問題可以前往 [GitHub Discussions](https://github.com/CherryHQ/cherry-studio/discussions)。提問時請同時說明：

* 目標是什麼。
* 目前設定與操作路徑。
* 已經嘗試了什麼。
* 卡在哪一個步驟。
* 希望獲得哪一類協助。

如果問題已包含可穩定重現的軟體缺陷，應改用 Bug Report；需要追蹤實作狀態的新需求，應改用 Feature Request。

## 回報安全問題

發現下列情況時，請使用 [GitHub Security Advisory](https://github.com/CherryHQ/cherry-studio/security/advisories/new) 私密回報：

* API Key、Token 或本機資料可能遭非預期讀取。
* 權限確認可以被繞過。
* 不受信任的內容可能觸發未授權命令或檔案操作。
* 更新套件、相依套件或網路通訊存在可利用的風險。

報告應包含影響範圍、重現步驟、必要的驗證材料與可能的緩解方式。不要提交真實使用者資料或仍在使用的憑證。

非漏洞類的安全諮詢可聯絡 [security@cherry-ai.com](mailto:security@cherry-ai.com)。

## 社群交流

社群群組適合交流經驗與互助，不是正式的問題追蹤系統。需要維護者確認、關聯版本或持續追蹤的問題，仍應提交到 GitHub。

* [Telegram：CherryStudioAI](https://t.me/CherryStudioAI)
* [Discord：Cherry Studio](https://discord.gg/wez8HtpxqQ)
* [QQ 群組：575014769](https://qm.qq.com/q/lo0D4qVZKi)

群組邀請可能因平台規則或人數限制而變動。若連結失效，請以 [Cherry Studio 官方儲存庫](https://github.com/CherryHQ/cherry-studio) README 中的最新入口為準。

## 保護隱私

提交前請檢查：

* API Key、存取權杖、Cookie 與密碼已完全遮蓋。
* 檔案路徑中的姓名、公司名稱與專案名稱已去識別化。
* 對話、知識庫與文件中沒有不必要的個人或業務資料。
* 日誌只保留與問題時間範圍相關的內容。
* 截圖沒有顯示其他應用程式、瀏覽器分頁或通知中的敏感資訊。

如果憑證已經公開，不要只刪除貼文；應立即在對應服務商後台撤銷並重新產生。
