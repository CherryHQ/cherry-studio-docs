---
icon: database
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# データ設定

このインターフェースでは、クライアントデータのクラウドおよびローカルバックアップ、ローカルデータディレクトリのクエリ、キャッシュのクリアなどを行うことができます。

### データバックアップ

現在、データバックアップはWebDAV方式のみをサポートしています。クラウドバックアップには、WebDAVをサポートするサービスを選択できます。

また、`A PC` $$\xrightarrow{\text{バックアップ}}$$ `WebDAV` $$\xrightarrow{\text{復元}}$$ `B PC`の方法で、複数端末のデータ同期を実現できます。

#### Jianguoyunの例

1. Jianguoyunにログインし、右上のユーザー名をクリックし、「アカウント情報」を選択：

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. 「セキュリティオプション」を選択し、「アプリケーションを追加」をクリック：

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. アプリケーション名を入力し、ランダムなパスワードを生成：

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. パスワードをコピーして記録：

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. サーバーアドレス、アカウント、パスワードを取得：

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studioの設定——データ設定で、WebDAV情報を入力：

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. データのバックアップまたは復元を選択し、自動バックアップの時間間隔を設定できます：

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAVサービスのハードルが比較的低いものは、一般的にネットストレージサービスです：

* [Jianguoyun](https://www.jianguoyun.com/)
* [123pan](https://www.123pan.com/)（会員が必要）
* [Alipan](https://www.alipan.com/)（購入が必要）
* [Box](https://www.box.com/) (無料スペース容量は10GB、単一ファイルサイズ制限は250MB)
* [Dropbox](https://www.dropbox.com/) (Dropbox無料版は2GB、友人招待で最大16GBまで拡張可能)
* [TeraCloud](https://teracloud.jp/en/) (無料スペースは10GB、招待で5GB追加獲得可能)
* [Yandex Disk](https://disk.yandex.com/) (無料ユーザーは10GB容量を提供)

次に、自分でデプロイする必要があるサービス：

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}