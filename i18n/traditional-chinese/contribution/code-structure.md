---
hidden: True
icon: code
---

{% hint style="warning" %}
此文件由 AI 從中文翻譯而來，尚未經過審閱。
{% endhint %}

# 程式碼結構

```yaml
...
├─ docs/ #文件目錄
├─ resources/ #資源檔案目錄
├─ scripts/ #腳本檔案目錄
└─ src/ #主要原始碼目錄
    ├─main/ #主進行程式碼
    ├─preload/ #預加載腳本目錄
    └─renderer/ #渲染進行程式碼
        ├─src/ #渲染進程的原始碼
            ├─assets/ #資源檔案
                ├─fonts/ #字體檔案
                ├─images/ #頭像等圖片檔案
                └─styles/ #樣式檔案
            ├─components/ #元件
            ├─config/ #設定檔
            ├─context/ #上下文
            ├─databases/ #資料庫相關檔案
            ├─hooks/ #自定義 Hooks
            ├─i18n/ #國際化檔案
            ├─pages/ #頁面檔案
            ├─providers/ #服務供應商相關設定
            ├─services/ #服務檔案
            ├─store/ #狀態管理檔案
            ├─types/ #TypeScript 型別定義檔案
            ├─utils/ #工具函式
            ...
        ...
    ...
...

```