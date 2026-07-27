---
description: 在 Windows 上選擇、安裝和更新 Cherry Studio
icon: windows
---

# Windows

本頁說明如何在 Windows 上選擇安裝套件、完成安裝，以及處理首次啟動時常見的安全性提示或執行階段程式庫問題。如果還沒有安裝套件，請先前往[客戶端下載](../../cherrystudio/download.md)。

{% hint style="warning" %}
Cherry Studio 不支援 Windows 7。請只從 Cherry Studio 官網或 `CherryHQ/cherry-studio` 官方 GitHub Releases 下載安裝套件。
{% endhint %}

## 選擇安裝套件

Windows Release 提供 x64、ARM64 兩種架構，以及 Setup、Portable 兩種套件類型。

| 安裝套件 | 適用情境 |
| --- | --- |
| `x64-setup.exe` | 使用 Intel 或 AMD 處理器的一般 Windows 電腦；適合大多數使用者 |
| `arm64-setup.exe` | 使用 ARM 處理器的 Windows 電腦，例如部分 Snapdragon 裝置 |
| `x64-portable.exe` | x64 電腦；不需要安裝，並希望將程式和資料放在指定目錄 |
| `arm64-portable.exe` | ARM64 電腦；不需要安裝，並希望將程式和資料放在指定目錄 |

如果不確定系統架構，請開啟 **設定 → 系統 → 系統資訊**，查看「系統類型」：

* 顯示「x64 型處理器」時，請選擇 x64。
* 顯示「ARM 型處理器」時，請選擇 ARM64。

Setup 安裝版適合日常使用；Portable 免安裝版更適合臨時測試、隨身碟攜帶或需要獨立資料目錄的情境。

## 驗證下載檔案

官方 GitHub Release 會提供安裝套件的 SHA256。下載完成後，可以在 PowerShell 中執行：

```powershell
Get-FileHash ".\Cherry-Studio-*-setup.exe" -Algorithm SHA256
```

如果使用免安裝版，請將檔名改為對應的 `*-portable.exe`。輸出值應與 Release 頁面列出的 SHA256 完全一致。

如果瀏覽器或 Windows 提示檔案來源不明，請先核對下載網域、檔名和 SHA256；無法確認來源時，請勿繼續執行。

## 安裝 Setup 版

1. 完全結束正在執行的 Cherry Studio。
2. 按兩下 `*-setup.exe`。
3. 依照安裝精靈選擇安裝目錄。
4. 確認選項並完成安裝。
5. 從桌面捷徑或「開始」功能表啟動 Cherry Studio。

升級現有安裝時，直接使用相同系統架構的新版本 Setup 安裝套件即可。升級前，建議先在 **設定 → 資料設定** 建立備份。

## 使用 Portable 版

1. 建立一個可寫入的目錄，例如 `D:\Apps\CherryStudio`。
2. 將 `*-portable.exe` 放入該目錄。
3. 按兩下執行檔啟動。
4. 程式執行期間，請勿移動執行檔或其資料目錄。

如果沒有另外設定資料位置，免安裝版會在執行檔所在目錄下使用 `data` 目錄儲存應用程式資料。備份或移轉免安裝版時，應同時保留執行檔和此目錄。

{% hint style="info" %}
請勿將免安裝版放在需要系統管理員權限才能寫入的目錄。如果希望長期使用、自動建立捷徑並透過安裝精靈升級，建議改用 Setup 安裝版。
{% endhint %}

## 首次啟動

首次啟動後，建議先完成以下檢查：

1. 開啟 **設定 → 模型服務**，新增服務商並啟用至少一個模型。
2. 返回對話頁面，傳送一則測試訊息。
3. 開啟 **設定 → 資料設定**，確認備份方式和資料位置。

如果 Windows Defender SmartScreen 顯示保護提示，請先確認檔案來自官方管道並通過 SHA256 驗證，再依照系統提示查看詳細資訊。請勿為來源不明的安裝套件停用系統安全性功能。

## Visual C++ 執行階段程式庫

Cherry Studio 的部分原生元件依賴 Microsoft Visual C++ Redistributable。如果安裝或啟動時，系統提示缺少執行階段程式庫：

1. 優先允許 Cherry Studio 安裝程式完成相依元件安裝。
2. 如果自動安裝失敗，請前往 [Microsoft Visual C++ Redistributable 官方頁面](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist)。
3. 下載與系統架構相符的 x64 或 ARM64 版本，安裝後重新啟動 Cherry Studio。

請勿從第三方軟體下載站取得執行階段程式庫。

## 更新與切換版本

更新前：

1. 在 **設定 → 資料設定** 建立備份。
2. 完全結束 Cherry Studio。
3. 下載與目前電腦架構相符的新安裝套件。

Setup 使用者可以直接執行新版本安裝套件。Portable 使用者應保留原有的 `data` 目錄，並以新版本執行檔取代舊檔案。

從新版本降級至舊版本時，可能會遇到資料庫或設定不相容。除非已完成備份並清楚了解影響，否則不建議降級。預發行版或每日預覽版本也不應作為重要資料的唯一執行環境。

## 常見問題

### 按兩下後沒有啟動

請依序檢查：

1. 安裝套件架構是否與系統一致。
2. 檔案是否完整，以及 SHA256 是否相符。
3. Visual C++ Redistributable 是否已正確安裝。
4. 安全性軟體是否隔離了程式檔案。
5. 是否已有 Cherry Studio 程序正在執行。

如果仍無法啟動，請記錄 Windows 版本、系統架構、Cherry Studio 版本和錯誤提示，再透過[意見回饋與建議](../../question-contact/suggestions.md)提交。

### Portable 版啟動後像是全新安裝

請檢查執行檔旁的 `data` 目錄是否仍存在、目前目錄是否可寫入，以及是否曾移動執行檔。還原前請先複製現有目錄，避免覆寫仍可使用的資料。

### 安裝後如何開始使用

繼續閱讀：

* [設定模型服務](../../pre-basic/providers/)
* [對話介面](../../cherrystudio/preview/chat.md)
* [資料設定](../../data-settings/)
