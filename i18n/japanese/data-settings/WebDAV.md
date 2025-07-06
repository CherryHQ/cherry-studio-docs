---
icon: cloud-arrow-up
---
# WebDAV バックアップ


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




Cherry Studioのデータバックアップは、WebDAV方式によるバックアップをサポートしています。適切なWebDAVサービスを選択してクラウドバックアップを行えます。

WebDAVを使用すると、`Aコンピュータ` $$\xrightarrow{\text{バックアップ}}$$ `WebDAV` $$\xrightarrow{\text{復元}}$$ `Bコンピュータ` の方法で、複数のデバイス間のデータ同期を実現できます。

#### Nutstoreを例として

1. Nutstoreにログインし、右上のユーザー名をクリックして「アカウント情報」を選択:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. 「セキュリティオプション」を選択し、「アプリを追加」をクリック

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. アプリ名を入力し、ランダムパスワードを生成:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. パスワードをコピーして保存:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. サーバーアドレス、アカウント、パスワードを取得:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. Cherry Studio設定→データ設定でWebDAV情報を入力:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. データのバックアップまたは復元を選択し、自動バックアップの時間間隔を設定できます

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
導入が比較的容易なWebDAVサービスは主にクラウドストレージです：

- [Nutstore](https://www.jianguoyun.com/)
- [123 Pan](https://www.123pan.com/)（会員制）
- [Alibaba Cloud Drive](https://www.alipan.com/)（購入が必要）
- [Box](https://www.box.com/) (無料容量10GB、単一ファイル制限250MB)
- [Dropbox](https://www.dropbox.com/) (基本無料2GB、招待で最大16GBまで拡張可能)
- [TeraCloud](https://teracloud.jp/en/) (無料容量10GB、招待で5GB追加可能)
- [Yandex Disk](https://disk.yandex.com/) (無料ユーザー向け容量10GB)

次に、自己ホスティングが必要なサービス：

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [sharelist](https://github.com/reruin/sharelist)
{% endhint %}