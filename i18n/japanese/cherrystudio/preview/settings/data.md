---
icon: database
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# データ設定

このインターフェースでは、クライアントデータのクラウドおよびローカルバックアップ、ローカルデータディレクトリの照会、キャッシュのクリアなどの操作が可能です。

### データバックアップ

現在のデータバックアップはWebDAV方式のみをサポートしています。WebDAVをサポートするサービスを選択してクラウドバックアップを行えます。

`A端末` $$\xrightarrow{\text{バックアップ}}$$ `WebDAV` $$\xrightarrow{\text{復元}}$$ `B端末` の方法で、複数端末間のデータ同期を実現することも可能です。

#### ナッツクラウドを例に

1. ナッツクラウドにログインし、右上のユーザー名をクリックして「アカウント情報」を選択：

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. 「セキュリティオプション」を選択し、「アプリ追加」をクリック

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. アプリ名を入力し、ランダムパスワードを生成

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. パスワードをコピーして保存

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. サーバーアドレス、アカウント、パスワードを取得

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio 設定 → データ設定で、WebDAV情報を入力

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. データのバックアップまたは復元を選択し、自動バックアップの間隔を設定可能

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAVサービスでは、導入ハードルの低いクラウドストレージが一般的です：

* [坚果云](https://www.jianguoyun.com/)（会員制）
* [123盘](https://www.123pan.com/)（会員制）
* [阿里云盘](https://www.alipan.com/)（購入制）
* [Box](https://www.box.com/) (無料容量10GB、単一ファイル制限250MB)
* [Dropbox](https://www.dropbox.com/) (無料2GB、招待で最大16GBまで拡張可能)
* [TeraCloud](https://teracloud.jp/en/) (無料10GB、招待で+5GB追加)
* [Yandex Disk](https://disk.yandex.com/) (無料ユーザーに10GB提供)

次に、自己導入が必要なサービス：

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}