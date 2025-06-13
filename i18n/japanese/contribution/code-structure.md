---
hidden: True
icon: code
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# コード構造

```yaml
...
├─ docs/ #ドキュメントディレクトリ
├─ resources/ #リソースファイルディレクトリ
├─ scripts/ #スクリプトファイルディレクトリ
└─ src/ #主要ソースコードディレクトリ
    ├─main/ #メインプロセスコード
    ├─preload/ #プリロードスクリプトディレクトリ
    └─renderer/ #レンダリングプロセスコード
        ├─src/ #レンダリングプロセスのソースコード
            ├─assets/ #リソースファイル
                ├─fonts/ #フォントファイル
                ├─images/ #アバターなどの画像ファイル
                └─styles/ #スタイルファイル
            ├─components/ #コンポーネント
            ├─config/ #設定ファイル
            ├─context/ #コンテキスト
            ├─databases/ #データベース関連ファイル
            ├─hooks/ #カスタムHooks
            ├─i18n/ #国際化ファイル
            ├─pages/ #ページファイル
            ├─providers/ #プロバイダー関連設定
            ├─services/ #サービスファイル
            ├─store/ #状態管理ファイル
            ├─types/ #TypeScriptタイプ定義ファイル
            ├─utils/ #ユーティリティ関数
            ...
        ...
    ...
...
```