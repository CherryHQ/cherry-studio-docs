---
icon: database
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# データ設定

このインターフェースでは、クライアントデータのクラウドおよびローカルバックアップ、ローカルデータディレクトリのクエリ、キャッシュクリアなどの操作が可能です。



### データバックアップ

現在、データバックアップはWebDAV方式のみをサポートしています。WebDAVに対応したサービスを選択してクラウドバックアップを行えます。

また、`A PC` $$\xrightarrow{\text{バックアップ}}$$ `WebDAV` $$\xrightarrow{\text{復元}}$$ `B PC` の方式でマルチデバイスデータ同期を実現可能です。

#### 坚果云の例

1. 坚果云にログインし、右上のユーザー名をクリックして「アカウント情報」を選択：

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. 「セキュリティオプション」を選択し、「アプリの追加」をクリック：

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. アプリ名を入力し、ランダムパスワードを生成：

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. パスワードをコピーして保存：

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. サーバーアドレス、アカウント、パスワードを取得：

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studioの設定→データ設定でWebDAV情報を入力：

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. データのバックアップまたは復元を選択し、自動バックアップの周期を設定可能：

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAVサービスのハードルが比較的低いオンラインストレージサービス：

* [坚果云](https://www.jianguoyun.com/)
* [123盘](https://www.123pan.com/)（会員制）
* [阿里云盘](https://www.alipan.com/)（購入必要）
* [Box](https://www.box.com/) (無料容量10GB，単一ファイル制限250MB)
* [Dropbox](https://www.dropbox.com/) （無料2GB，招待で最大16GBまで拡張可能）
* [TeraCloud](https://teracloud.jp/en/) （無料10GB，招待で+5GB拡張可能）
* [Yandex Disk](https://disk.yandex.com/) (無料ユーザー向け10GB容量)

自己デプロイが必要なサービス：

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}