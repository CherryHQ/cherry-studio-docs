---
icon: robot
---
# Cherry Agent の使い方ガイド


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




Cherry Studio v1.7.0.alpha バージョンで Agent が導入されました。Cherry Studio 内で Cherry Agent を使用できます。このチュートリアルでは、設定から起動までの手順を案内します。

### 1. Anthropic タイプのプロバイダを作成する

Anthropic エンドポイントをサポートする任意のサービスプロバイダを使用できます。例として CherryIn を使用し、新しい Agent サービスプロバイダを作成し、キーとアドレスを入力し、任意のモデルを追加します。

{% hint style="warning" %}
Agent モードではトークンの消費量が非常に大きいため、トークンの使用量にご注意ください
{% endhint %}

{% hint style="info" %}
Claude Code にサブスクライブしているユーザーも、キーと URL アドレスを入力してモデルを取得できます
{% endhint %}

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.26.35@2x.png" alt=""><figcaption></figcaption></figure>

### 2. API サーバーを有効化する

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 19.56.22@2x.png" alt=""><figcaption></figcaption></figure>

### 3. Agent を作成する

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.24.43@2x.png" alt=""><figcaption></figcaption></figure>

Agent を右クリックすると編集画面に入り、Agent の権限や利用可能なツール、mcp サービスを編集できます。

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.25.10@2x (1).png" alt=""><figcaption></figcaption></figure>

### 結果表示

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.30.26@2x (1).png" alt=""><figcaption></figcaption></figure>