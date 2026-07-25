---
icon: desktop-arrow-down
---

# 安裝教學

本頁說明 Cherry Studio 的一般安裝流程，並引導你前往對應系統的詳細教學。如果還沒有安裝套件，請先前往[用戶端下載](../../cherrystudio/download.md)。

## 安裝前

1. 確認安裝套件來自 Cherry Studio 官方網站或 `CherryHQ/cherry-studio` 官方 GitHub Releases。
2. 核對作業系統和 CPU 架構，避免混用 x64、ARM64、amd64 或 aarch64 套件。
3. 關閉正在執行的 Cherry Studio。
4. 如果要升級、降級或測試預覽版，請先在**設定 → 資料設定**中建立備份。

{% hint style="warning" %}
請勿在沒有備份的情況下，從新版本降級至舊版本。新版本可能已經遷移本機資料庫或設定，舊版本不一定能夠讀取遷移後的資料。
{% endhint %}

## Windows

Windows 提供安裝版和可攜版：

* **Setup 安裝版**：依照精靈選擇目錄並完成安裝，適合多數使用者。
* **Portable 可攜版**：直接執行執行檔，適合暫時使用或不想執行安裝流程的情境。

Cherry Studio 不支援 Windows 7。首次執行時如果出現系統保護提示，請先核對安裝套件來源和檔案摘要，再依 [Windows 安裝教學](windows.md)處理。

## macOS

1. 下載符合晶片架構的 `.dmg`：Apple 晶片選擇 `arm64`，Intel 晶片選擇 `x64`。
2. 開啟 DMG，將 Cherry Studio 拖曳至「應用程式」。
3. 從「應用程式」啟動。

macOS 可能會在首次執行時顯示開發者驗證或安全提示。處理方式請參閱 [macOS 安裝教學](macos.md)。

## Linux

Linux Release 通常提供 AppImage、deb 和 rpm 三種格式。選擇其中一種即可，請勿重複安裝多種格式。

### AppImage

```bash
chmod +x ./Cherry-Studio-*.AppImage
./Cherry-Studio-*.AppImage
```

AppImage 不需要系統層級安裝。如果無法啟動，請優先檢查檔案架構是否正確；部分發行版還需要安裝 AppImage 所需的 FUSE 相容元件。

### Debian / Ubuntu

```bash
sudo apt install ./Cherry-Studio-*-amd64.deb
```

ARM64 裝置應使用檔名中包含 `arm64` 的 deb 套件。

### Fedora / RHEL / Rocky Linux

```bash
sudo dnf install ./Cherry-Studio-*.rpm
```

請依裝置選擇 `x86_64` 或 `aarch64` 套件。

## 升級

在相同系統和架構上安裝較新的穩定版時，本機資料通常會保留。為降低風險：

1. 先完成本機或遠端備份。
2. 完全結束 Cherry Studio。
3. 使用符合目前系統和架構的新安裝套件升級。
4. 啟動後，先檢查模型服務、對話、知識庫和 Agent 是否正常。

預發行版或每日預覽建置可能包含尚未穩定的資料遷移。請勿將唯一一份重要資料只保留在預覽版環境中。

## 安裝後

首次啟動後，建議依序完成：

1. 在**設定 → 模型服務**中新增服務提供者和模型。
2. 返回對話頁面傳送一則測試訊息。
3. 確認資料儲存和備份位置。
4. 再依需求啟用知識庫、Agent、MCP 或其他進階功能。

繼續閱讀：

* [設定模型服務](../../pre-basic/providers/)
* [對話介面](../../cherrystudio/preview/chat.md)
* [資料設定](../../data-settings/)
* [常見問題](../../question-contact/questions.md)
