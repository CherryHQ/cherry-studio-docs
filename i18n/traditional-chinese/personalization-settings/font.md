---
icon: book-font
---

# 字型建議

Cherry Studio V2 可以直接讀取系統中已安裝的字型，並分別設定**全域字型**和**程式碼字型**。通常不需要再使用自訂 CSS 修改字型。

## 在 Cherry Studio 中選擇字型

1. 請先將字型安裝到作業系統。
2. 完全退出並重新開啟 Cherry Studio。
3. 前往**設定 > 一般設定 > 顯示與語言**。
4. 在**字型設定**中分別選擇：
   - **全域字型**：用於介面、訊息正文和大部分文字；
   - **程式碼字型**：用於程式碼區塊和程式碼編輯器。
5. 檢查常用語言、數字、標點符號和程式碼是否正常顯示。

兩個字型選項右側都有重設按鈕，可以隨時恢復預設值。

{% hint style="info" %}
字型清單來自作業系統。剛安裝的字型沒有出現時，請先完全退出 Cherry Studio；如果仍未出現，再重新啟動作業系統以更新字型快取。
{% endhint %}

## 如何選擇

### 全域字型

請優先考慮：

- 是否涵蓋你常用的語言；
- 簡體、繁體和日文字形是否符合閱讀習慣；
- 小字型大小下是否清晰；
- 一般、粗體和斜體樣式是否齊全；
- 中英文混合排列時，高度和字重是否協調。

### 程式碼字型

請優先檢查：

- `0` 與 `O`、`1` 與 `l` / `I` 是否容易區分；
- 括號、引號、斜線和運算子是否清楚；
- 是否需要顯示中文、日文或俄文註解；
- 是否喜歡程式設計連字。

當程式碼字型不包含某個字元時，系統會嘗試退回其他字型，因此同一段程式碼中可能會出現字元寬度或風格不一致。

## 正文字型建議

| 字型 | 適用語言 | 特點 | 官方來源 |
| --- | --- | --- | --- |
| Noto Sans | 英文、俄文及其他多種文字 | 涵蓋範圍廣，適合多語言介面 | [Noto 官方文件](https://notofonts.github.io/noto-docs/website/use/) |
| Noto Sans SC | 簡體中文 | 適用於簡體中文字形 | [Noto CJK 說明](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Noto Sans TC | 繁體中文 | 適用於台灣繁體中文字形 | [Noto CJK 說明](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Noto Sans JP | 日文 | 適用於日文字形 | [Noto CJK 說明](https://notofonts.github.io/noto-docs/website/use/#which-noto-fonts-should-i-use-for-chinese-japanese-or-korean) |
| Source Han Sans | 簡體中文、繁體中文、日文、韓文 | Adobe 的 Pan-CJK 開放原始碼字型，提供地區變體 | [Source Han Sans](https://github.com/adobe-fonts/source-han-sans) |

如果經常在同一個介面中混合英文、俄文與 CJK 文字，請優先嘗試 Noto 系列；它會為不同文字提供風格相近的字型家族。

{% hint style="warning" %}
同一個漢字在簡體中文、繁體中文和日文中可能會使用不同字形。請選擇與主要閱讀語言對應的 `SC`、`TC` 或 `JP` 版本。
{% endhint %}

## 程式碼字型建議

| 字型 | 適用情境 | CJK 支援 | 官方來源 |
| --- | --- | --- | --- |
| JetBrains Mono | 英文、俄文程式碼與終端機內容 | 不以 CJK 為主要目標，CJK 註解通常會使用退回字型 | [JetBrains Mono](https://www.jetbrains.com/lp/mono/) |
| Sarasa Mono | 包含中文或日文註解的程式碼 | 提供 `SC`、`TC`、`J` 等地區變體 | [Sarasa Gothic](https://github.com/be5invis/Sarasa-Gothic) |
| Monaspace | 偏好多種風格、字元變體和程式設計連字 | 不以 CJK 為主要目標 | [Monaspace](https://github.com/githubnext/monaspace) |

### 快速選擇

- 主要使用英文或俄文：請先嘗試 **JetBrains Mono**；
- 程式碼中經常包含簡體中文：請先嘗試 **Sarasa Mono SC**；
- 程式碼中經常包含繁體中文：請先嘗試 **Sarasa Mono TC**；
- 程式碼中經常包含日文：請先嘗試 **Sarasa Mono J**；
- 想要嘗試不同的程式碼風格或連字：選擇 **Monaspace** 的其中一個家族。

Monaspace 包含多個風格相容的家族。Cherry Studio 只負責選擇字型家族，不提供字型特性開關；某些連字或字元變體能否顯示，還取決於字型版本和轉譯環境。

## 依文件語言選擇

| 主要介面語言 | 全域字型建議 | 程式碼字型建議 |
| --- | --- | --- |
| 簡體中文 | Noto Sans SC / Source Han Sans CN | Sarasa Mono SC |
| 中文（繁體） | Noto Sans TC / Source Han Sans TW | Sarasa Mono TC |
| English | Noto Sans | JetBrains Mono / Monaspace |
| 日本語 | Noto Sans JP / Source Han Sans JP | Sarasa Mono J |
| Русский | Noto Sans | JetBrains Mono / Monaspace |

這只是起點，不要求整個團隊使用相同的字型。最終應以實際顯示效果和所在組織的字型規範為準。

## 安裝建議

- 只從字型專案官網或官方發行頁面下載；
- 桌面應用程式通常會安裝 `OTF`、`TTF`、`TTC` 或可變字型檔案，請勿優先選擇網頁專用的 `WOFF` / `WOFF2`；
- 大型 CJK 字型套件包含多個地區和字重，依實際需要安裝即可；
- 更新字型前，請先解除安裝舊版本，避免作業系統快取中出現多個同名字型；
- 團隊統一製作截圖或示範時，應統一字型家族和版本。

本文建議的專案都會在官方頁面提供開放原始碼授權資訊。如果要將字型重新封裝到產品、範本或商業交付成果中，仍應以字型檔案附帶的授權條款為準。

## 常見問題

### 字型安裝後沒有出現在清單中

完全退出 Cherry Studio 後重新開啟。macOS 可以在「字體簿」中確認字型是否已啟用；Windows 可以在系統字型設定中確認；Linux 可以更新字型快取後重新啟動應用程式。

### 選擇後，部分字元仍然使用另一種字型

所選字型可能不包含這些字元，系統正在使用退回字型。請改用涵蓋目標語言的字型，或選擇對應的 CJK 地區變體。

### 中文、繁體或日文字形看起來不正確

請檢查是否選擇了錯誤的 `SC`、`TC` 或 `JP` 版本。名稱相近不代表字形標準相同。

### 程式碼欄沒有對齊

請確認選擇的是等寬字型，並檢查程式碼中是否包含該字型不支援的 CJK 或特殊字元。退回字型可能會破壞等寬效果。

### 字型太大或太小

字型家族和字型大小是兩件事。全域介面過大或過小時，可以在同一個頁面調整介面縮放；只有訊息文字不合適時，應調整訊息字型大小。

***

### 取得協助與提交意見回饋

如果在設定或使用過程中遇到問題，請透過[意見回饋與建議](../question-contact/suggestions.md)中列出的官方管道聯絡我們。
