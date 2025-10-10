---
icon: cloud-arrow-up
---
# WebDAV バックアップ


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




Cherry StudioのデータバックアップはWebDAV方式をサポートしています。適切なWebDAVサービスを選択してクラウドバックアップを行うことができます。

WebDAVを利用すると、`Aコンコンピュータ` $$\xrightarrow{\text{バックアップ}}$$ `WebDAV` $$\xrightarrow{\text{復元}}$$ `Bコンピュータ` の形式で複数端末間のデータ同期を実現できます。

#### 坚果云を例とする

1.  坚果云にログインし、右上のユーザー名をクリックして「アカウント情報」を選択：

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2.  「セキュリティオプション」を選択し、「アプリの追加」をクリック

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3.  アプリ名を入力し、ランダムパスワードを生成；

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4.  パスワードをコピーして保存；

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5.  サーサーバーアドレス、アカウント、パスワードを取得；

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6.  Cherry Studio設定→データ設定でWebDAV情報を入力；

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7.  バックアップまたはデータ復元を選択し、自動バックアップの時間間隔を設定可能。

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAVサービスの導入ハードルが比較的低いクラウドストレージ：

- [坚果云](https://www.jianguoyun.com/)
- [123 パン](https://www.123pan.com/)（会員制）
- [アリクラウドドライブ](https://www.alipan.com/)（有料購入必要）
- [Box](https://www.box.com/) (無料容量10GB，単一ファイル制限250MB)
- [Dropbox](https://www.dropbox.com/) (無料2GB，招待で最大16GB拡張可能)
- [TeraCloud](https://teracloud.jp/en/) (無料10GB，招待で5GB追加獲得可能)
- [Yandex Disk](https://disk.yandex.com/) (無料ユーザー10GB容量)

自己デプロイが必要なソリューション：

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [sharelist](https://github.com/reruin/sharelist)
  {% endhint %}