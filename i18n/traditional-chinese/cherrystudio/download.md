---
icon: download
---

# 用戶端下載

Cherry Studio 提供 Windows、macOS 和 Linux 安裝套件。為避免下載頁面的特定版本號過期，本頁只保留長期有效的官方入口；開啟下載頁面後，請選擇最新穩定版和符合系統架構的檔案。

## 官方下載入口

* [Cherry Studio 官方網站下載頁面](https://cherry-ai.com/download)
* [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases)
* [GitHub 最新穩定版](https://github.com/CherryHQ/cherry-studio/releases/latest)

{% hint style="warning" %}
請只從 Cherry Studio 官方網站、`CherryHQ/cherry-studio` 官方儲存庫或下載頁面明確列出的映像站取得安裝套件。請勿執行來源不明、經過重新封裝或要求關閉安全軟體的安裝程式。
{% endhint %}

## 選擇穩定版或預覽版

| 類型 | 如何辨識 | 適合對象 |
| :--- | :--- | :--- |
| 穩定版 | 在 GitHub Releases 中標記為 **Latest**，版本號通常不含 `alpha`、`beta` 或 `rc` | 日常使用，建議選擇 |
| 預發行版 | 標記為 **Pre-release**，版本號可能包含 `alpha`、`beta` 或 `rc` | 希望提前測試新功能的使用者 |
| 每日預覽建置 | 來自官方 [V2 Daily Preview Build](https://github.com/CherryHQ/cherry-studio/actions/workflows/v2-daily-preview-build.yml) | 開發、測試和問題重現 |

預覽版可能包含尚未完成的資料遷移、介面或相容性變更。安裝前請先完成備份；重要資料環境應優先使用穩定版。

## Windows

### 選擇架構

開啟**設定 → 系統 → 系統資訊**，查看「系統類型」：

* `x64` 或「x64 型處理器」：下載 `x64`。
* `ARM64` 或「ARM 型處理器」：下載 `arm64`。

多數 Intel 和 AMD 電腦使用 `x64`。只有 Windows on ARM 裝置使用 `arm64`。

### 選擇安裝套件

| 檔案類型 | 說明 |
| :--- | :--- |
| `*-x64-setup.exe` / `*-arm64-setup.exe` | 安裝版；支援選擇安裝目錄並建立捷徑 |
| `*-x64-portable.exe` / `*-arm64-portable.exe` | 可攜版；適合不想執行安裝流程的情境 |

{% hint style="warning" %}
Cherry Studio 不支援 Windows 7。請在支援的 Windows 版本上安裝。
{% endhint %}

安裝步驟和系統安全提示請參閱 [Windows 安裝教學](../pre-basic/installation/windows.md)。

## macOS

開啟**蘋果選單 → 關於這台 Mac**，查看「晶片」或「處理器」：

* 顯示 Apple M 系列晶片：下載 `arm64`。
* 顯示 Intel 處理器：下載 `x64`。

| 檔案類型 | 說明 |
| :--- | :--- |
| `*-arm64.dmg` / `*-x64.dmg` | 建議使用的圖形化安裝套件 |
| `*-arm64.zip` / `*-x64.zip` | 壓縮檔版本 |

Apple Silicon 套件適用於 M1、M2、M3、M4 等 Apple 晶片。如果選錯架構，應用程式可能無法開啟，或只能透過相容層執行。

安裝步驟和「無法驗證開發者」等提示請參閱 [macOS 安裝教學](../pre-basic/installation/macos.md)。

## Linux

在終端機中執行：

```bash
uname -m
```

* 輸出 `x86_64`：選擇 `x86_64` 或 `amd64`。
* 輸出 `aarch64` / `arm64`：選擇 `arm64` / `aarch64`。

官方 Release 通常提供：

| 檔案類型 | 適用情境 |
| :--- | :--- |
| `.AppImage` | 跨發行版直接執行 |
| `.deb` | Debian、Ubuntu 及其衍生發行版 |
| `.rpm` | Fedora、RHEL、Rocky Linux 等 RPM 系列發行版 |

不同格式的架構命名可能不同，例如 x64 在 `.deb` 檔名中通常寫成 `amd64`，在 AppImage 中可能寫成 `x86_64`。

## 下載後檢查

1. 確認檔案來自官方網域或 `github.com/CherryHQ/cherry-studio`。
2. 再次核對作業系統、架構和安裝套件格式。
3. 如果 Release 頁面提供 SHA-256 摘要，請在執行前與本機檔案摘要比對。
4. 更新或測試預覽版前，先備份 Cherry Studio 資料。

### 計算 SHA-256

{% tabs %}
{% tab title="Windows PowerShell" %}
```powershell
Get-FileHash .\Cherry-Studio-安裝套件檔名 -Algorithm SHA256
```
{% endtab %}

{% tab title="macOS" %}
```bash
shasum -a 256 ~/Downloads/Cherry-Studio-安裝套件檔名
```
{% endtab %}

{% tab title="Linux" %}
```bash
sha256sum ~/Downloads/Cherry-Studio-安裝套件檔名
```
{% endtab %}
{% endtabs %}

輸出必須與官方 Release 中對應檔案的 SHA-256 完全一致。如果不一致，請勿執行該檔案，並從官方入口重新下載。

## 下一步

* [安裝教學](../pre-basic/installation/)
* [設定模型服務](../pre-basic/providers/)
* [對話介面](preview/chat.md)
