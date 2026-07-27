---
icon: file-code
---

# 自訂 CSS

自訂 CSS 可以覆寫 Cherry Studio 的介面樣式，適合調整內建設定未提供的色彩、間距、圓角和元件外觀。

{% hint style="warning" %}
自訂 CSS 屬於進階功能。應用程式升級後，元件結構、類別名稱和變數可能會變更；一段目前有效的樣式不保證可以在後續版本中繼續生效。
{% endhint %}

## 何時需要使用

撰寫 CSS 前，請先檢查**設定 > 一般設定 > 顯示與語言**。V2 已經內建以下選項：

- 淺色、深色和跟隨系統主題；
- 主題強調色彩；
- 介面縮放；
- 全域字型和程式碼字型；
- 話題位置與顯示方式。

這些內建選項更穩定，也可以直接重設。只有內建設定無法實現目標時，才使用自訂 CSS。

## 開啟 CSS 編輯器

1. 點擊 Cherry Studio 左下角的**設定**。
2. 進入**一般設定**。
3. 在第二層選單中選擇**自訂 CSS**。
4. 在編輯器中輸入或貼上 CSS。

編輯內容會儲存到本機設定，並在內容變更後套用到介面，不需要另外點擊儲存按鈕。

建議先保留目前 CSS 的副本，再逐段修改。每新增一小段，就檢查聊天、設定、彈出視窗和輔助視窗；發生異常時會比較容易找出問題。

## 從最小樣式開始

以下範例只會調整使用者訊息背景和常用圓角：

```css
:root {
  --chat-background-user: rgba(0, 185, 107, 0.08);
  --list-item-border-radius: 12px;
}
```

如果要分別設定淺色和深色主題，可以使用根元素的主題類別：

```css
:root:not(.dark) {
  --chat-background-user: rgba(0, 120, 80, 0.08);
}

:root.dark {
  --chat-background-user: rgba(90, 220, 160, 0.12);
}
```

{% hint style="info" %}
Cherry Studio V2 使用 `.light` / `.dark` 類別表示目前的主題。舊主題中常見的 `body[theme-mode="dark"]` 寫法，不應再作為新樣式的基礎。
{% endhint %}

## 常用語意變數

請優先覆寫語意變數，這種方式比直接定位內部類別名稱更不容易失效。

| 變數 | 作用 |
| --- | --- |
| `--color-primary` | 主要強調色彩 |
| `--color-background` | 主要背景色彩 |
| `--color-background-subtle` | 次要背景色彩 |
| `--color-foreground` | 主要文字色彩 |
| `--color-foreground-secondary` | 次要文字色彩 |
| `--color-border` | 常用邊框色彩 |
| `--color-card` | 卡片背景色彩 |
| `--color-popover` | 彈出層背景色彩 |
| `--chat-background-user` | 使用者訊息背景色彩 |
| `--chat-background-assistant` | 助理訊息背景色彩 |
| `--font-family` | 全域字型堆疊 |
| `--code-font-family` | 程式碼字型堆疊 |

例如，以下樣式會分別設定兩種主題的背景和邊框：

```css
:root:not(.dark) {
  --color-background: #f7f8f6;
  --color-background-subtle: #f0f2ef;
  --color-border: rgba(20, 35, 28, 0.12);
}

:root.dark {
  --color-background: #171a18;
  --color-background-subtle: #1e221f;
  --color-border: rgba(235, 255, 244, 0.12);
}
```

{% hint style="warning" %}
主題色彩和字型已經有內建設定。如果同時在 CSS 中覆寫相同的變數，最終效果會取決於選擇器優先順序和載入順序，可能與設定頁面顯示的值不一致。
{% endhint %}

## 修改特定元件

當變數無法完成目標時，可以使用瀏覽器開發人員工具檢查元素，再撰寫選擇器。

```css
/* 示例：让设置页中的卡片边框更明显 */
[class*="border-border"] {
  border-color: color-mix(in srgb, var(--color-border) 75%, var(--color-foreground) 25%);
}
```

這類選擇器比語意變數更容易受到版本升級影響。請遵循以下原則：

- 盡量限制作用範圍，避免直接覆寫所有 `div`、`button` 或 `input`；
- 少用依賴層級和序號的選擇器，例如 `:nth-child()`；
- 請勿假設自動產生的類別名稱長期不變；
- 避免大範圍使用 `!important`；
- 為每組規則加入簡短註解，說明用途；
- 修改後，同時檢查淺色和深色主題。

以上的元件選擇器只用於說明寫法，不代表穩定的公開介面。

## 尋找目前的變數

Cherry Studio 正在移轉到新的 V2 設計系統，因此變數分為兩類：

- [V2 主題變數](https://github.com/CherryHQ/cherry-studio/blob/main/packages/ui/src/styles/theme.css)；
- [相容於舊介面的變數](https://github.com/CherryHQ/cherry-studio/blob/main/src/renderer/assets/styles/legacy-vars.css)。

相容變數仍在使用，但未來可能會移除。新主題應優先採用 V2 語意變數，並在每次主要版本升級後重新檢查效果。

編輯器頂部的 **cherrycss.com** 連結可以開啟社群主題網站。使用社群主題前，請先閱讀完整的 CSS，並確認來源值得信任。

## 安全建議

CSS 本身不是 JavaScript，但仍可能透過 `url()`、`@import` 或外部字型請求網路資源。使用第三方主題時：

- 檢查是否引用陌生網域；
- 請勿在 CSS 中寫入 Token、Cookie、使用者名稱或本機路徑；
- 優先將需要的圖片和字型儲存到可信任的位置；
- 保留原始主題來源和版本號；
- 請勿執行主題作者另外提供但用途不明的主控台指令碼。

## 恢復預設樣式

一般情況下：

1. 開啟**設定 > 一般設定 > 自訂 CSS**。
2. 複製並備份仍需要保留的內容。
3. 清空編輯器中的所有 CSS。
4. 確認介面恢復；必要時重新啟動應用程式。

如果錯誤的樣式遮住設定按鈕或讓頁面無法操作，請參閱[清除 CSS 設定](clear-css.md)。

## 常見問題

### 輸入 CSS 後沒有變化

請先確認語法完整，沒有遺漏右大括號。然後檢查選擇器是否仍與目前版本的元素相符，以及變數名稱是否存在。

### 淺色主題正常，深色主題異常

請將兩種主題的規則分開，分別使用 `:root:not(.dark)` 和 `:root.dark`，並檢查文字與背景的對比度。

### 修改主題色彩沒有作用

主題色彩會由內建設定寫入執行階段變數。請優先使用**顯示與語言 > 主題色彩**；如果必須透過 CSS 覆寫，需要檢查 `--cs-theme-primary` 與選擇器優先順序，但不建議同時維護兩套值。

### 升級後配置錯亂

請先暫時清空所有自訂 CSS，確認問題是否消失。接著逐段恢復，刪除依賴舊類別名稱、舊 DOM 層級或相容變數的規則。

### 輔助視窗顯示異常

自訂 CSS 也可能套用到快捷助理、劃詞工具等視窗。請避免使用過於寬泛的全域選擇器，並逐一檢查常用視窗。

***

### 取得協助與提交意見回饋

如果在設定或使用過程中遇到問題，請透過[意見回饋與建議](../question-contact/suggestions.md)中列出的官方管道聯絡我們。
