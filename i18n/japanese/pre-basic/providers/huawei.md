
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

```markdown
---
icon: cherries
---

# ファーウェイクラウド

一、[ファーウェイクラウド](https://auth.huaweicloud.com/authui/login)でアカウントを作成してログインする

二、[このリンク](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage)をクリックし、ModelArtsコントロールパネルに進む

三、認可

<details>

<summary>認可手順（既に認可済みの場合はスキップ）</summary>

1. (二)のリンクページに進んだ後、案内に従って認可ページへ進む（IAMサブユーザー → 委託新規作成 → 一般ユーザー）

![](<../../.gitbook/assets/image (49).png>)

2. 作成をクリック後、(二)のリンクページに戻る
3. アクセス権限が不十分な旨が表示されるため、メッセージ内の「ここをクリック」を押す
4. 既存の認可を追加して確定する

![](<../../.gitbook/assets/image (50).png>)

注意：この方法は初心者向けで、内容を深く理解する必要がなく、案内に従ってクリックするだけで完了します。一度で認可を成功させられる場合はご自身の方法で行ってください。

</details>

四、サイドバーの認証管理をクリックし、API Key（シークレットキー）を作成してコピーする

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

続いてCherryStudioで新しいプロバイダーを作成

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

作成完了後、シークレットキーを入力する

五、サイドバーのモデルデプロイメントをクリックし、全てを取得する

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

六、呼び出しをクリック

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

①のアドレスをコピーし、CherryStudioのプロバイダーアドレス欄に貼り付け、末尾に「#」を追加

末尾に「#」を追加

末尾に「#」を追加

末尾に「#」を追加

末尾に「#」を追加

「#」を追加する理由は[こちらを参照](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> もちろん、そちらを見なくても直接チュートリアル通り操作可能です；
>
> v1/chat/completionsを削除する方法で入力しても構いません。入力方法が分かればご自身の方法で実施してください。分からない場合は必ずチュートリアル通り操作してください。

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

次に②のモデル名をコピーし、CherryStudioで「+追加」ボタンをクリックして新規モデルを作成

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

モデル名を入力（余計な変更・引用符追加せず、サンプル通りそのまま入力）

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

「モデルを追加」ボタンをクリックして完了

{% hint style="info" %}
ファーウェイクラウドでは各モデルのアドレスが異なるため、各モデルごとに新しいプロバイダーを作成する必要があります。上記手順を繰り返し実施してください。
{% endhint %}
```