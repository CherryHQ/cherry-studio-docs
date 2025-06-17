---
icon: face-viewfinder
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# ナレッジベース文書の前処理

ナレッジベース文書の前処理を行うには、Cherry Studioをv1.5.0以上にアップグレードする必要があります。

### OCRサービスプロバイダーの設定

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 11.50.10@2x (1).jpg" alt=""><figcaption></figcaption></figure>

「API KEYを取得」をクリックするとブラウザで申請ページが開きます。「すぐに申請」をクリックしフォームに入力後、取得したAPI KEYを入力欄に入力します。

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 11.51.55@2x.jpg" alt=""><figcaption></figcaption></figure>

### ナレッジベース文書前処理の設定

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 20.01.03@2x.jpg" alt=""><figcaption></figcaption></figure>

作成済みのナレッジベースで上記の設定を行うと、文書前処理の設定が完了します。

### 文書のアップロード

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 12.01.59@2x.jpg" alt=""><figcaption></figcaption></figure>

> 右上の検索機能でナレッジベースの結果を確認できます

### 会話での使用方法

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 14.11.00@2x.jpg" alt=""><figcaption></figcaption></figure>

> ナレッジベース利用のヒント: **処理能力の高い**モデルを使用する場合、ナレッジベース検索モードを意図認識に変更すると、質問内容をより正確かつ広範囲に表現できます

### ナレッジベース意図認識の有効化

<figure><img src="../.gitbook/assets/CleanShot 2025-06-03 at 14.12.47@2x.jpg" alt=""><figcaption></figcaption></figure>

```mermaid
flowchart TD
    A[技術文書翻訳ルール]
    A --> B[マークダウン構文を保持]
    A --> C[技術用語を維持]
    A --> D[URL/パスを変更不可]
    B --> E[見出し # 変更せず]
    B --> F[画像パス ../.gitbook/ 保持]
    C --> G[API KEY v1.5.0 原文維持]
    D --> H[https:// を変更禁止]
```