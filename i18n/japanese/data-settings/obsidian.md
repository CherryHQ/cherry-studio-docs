---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# Obsidian 設定チュートリアル

Cherry Studio は Obsidian との連携をサポートし、完全な対話または個別の対話を Obsidian ライブラリにエクスポートできます。

{% hint style="warning" %}
このプロセスには追加の Obsidian プラグインのインストールは不要です。ただし、Cherry Studio から Obsidian へのインポートは Obsidian Web Clipper と同様の原理を使用しているため、[対話が長すぎる場合のインポート失敗](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0)を避けるために、Obsidian を最新バージョン（現在の Obsidian バージョンは少なくとも **1.7.2** 以上）にアップグレードすることを強く推奨します。
{% endhint %}

## 最新チュートリアル

{% hint style="info" %}
旧バージョンの Obsidian エクスポート機能と比較して、新しいバージョンではライブラリパスを自動選択するため、手動でライブラリ名やフォルダ名を入力する必要がなくなりました。
{% endhint %}

### ステップ 1: Cherry Studio の設定

Cherry Studio の _設定_ → _データ設定_ → _Obsidian 設定_メニューを開きます。ドロップダウンには本機で開いたことのある Obsidian ライブラリ名が自動表示されるので、ターゲットの Obsidian ライブラリを選択します：

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### ステップ 2: 対話のエクスポート

#### 完全な対話のエクスポート

Cherry Studio の対話インターフェースに戻り、対話を右クリックして _エクスポート_ を選択し、_Obsidian にエクスポート_をクリックします：

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

ポップアップウィンドウが表示され、Obsidian にエクスポートする対話ノートの **Properties（プロパティ）**、Obsidian 内の**配置フォルダ位置**、エクスポート方法を設定できます：

* **保管庫**：ドロップダウンメニューから他の Obsidian ライブラリを選択可能
* **パス**：ドロップダウンメニューからエクスポート先フォルダを選択可能
* Obsidian ノートプロパティ（Properties）：
  * タグ（tags）
  * 作成日時（created）
  * 出典（source）
* Obsidian へのエクスポート方法（以下3つから選択）：
  * **新規作成（存在する場合は上書き）**：指定した`フォルダ`に新規ノートを作成し、同名ノートが存在する場合は上書き
  * **先頭に追加**：同名ノートが存在する場合、選択した対話内容をノートの先頭に追加
  * **末尾に追加**：同名ノートが存在する場合、選択した対話内容をノートの末尾に追加

{% hint style="info" %}
Properties（プロパティ）が付与されるのは最初の方法のみで、後の2つの方法には付属しません。
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>ノートプロパティの設定</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>パスの選択</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>処理方法の選択</p></figcaption></figure>

すべてのオプションを選択したら、[OK]をクリックして完全な対話を対応する Obsidian ライブラリのフォルダにエクスポートします。

#### 個別の対話のエクスポート

個別の対話をエクスポートするには、対話の下にある_三本線メニュー_をクリックし、_エクスポート_を選択してから_Obsidian にエクスポート_をクリックします：

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>個別対話のエクスポート</p></figcaption></figure>

その後、完全な対話をエクスポートするときと同じウィンドウが表示され、**ノートプロパティ**と**ノートの処理方法**の設定を求められます。[上記のチュートリアル](obsidian.md#dao-chu-wan-zheng-dui-hua)と同じ手順で完了してください。

### エクスポート成功

🎉 これで Cherry Studio と Obsidian の連携設定がすべて完了し、エクスポートプロセスを完全に実行しました。お楽しみください！

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Obsidian へのエクスポート</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>エクスポート結果の確認</p></figcaption></figure>

***

## 旧チュートリアル（Cherry Studio\<v1.1.13 用）

### ステップ 1: Obsidian の準備

Obsidian ライブラリを開き、エクスポートした対話を保存するための`フォルダ`を作成します（図では Cherry Studio フォルダを例示）：

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

左下の枠で囲まれたテキスト（`保管庫`名）をメモしておいてください。

### ステップ 2: Cherry Studio の設定

Cherry Studio の _設定_ → _データ設定_ → _Obsidian 設定_メニューで、[ステップ 1](obsidian.md#di-yi-bu)で取得した`保管庫`名と`フォルダ`名を入力します：

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

`グローバルタグ`はオプションで、すべての対話をエクスポート後の Obsidian タグを設定できます（必要に応じて入力）。

### ステップ 3: 対話のエクスポート

#### 完全な対話のエクスポート

Cherry Studio の対話インターフェースで対話を右クリックし、_エクスポート_を選択してから_Obsidian にエクスポート_をクリックします。

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>完全な対話のエクスポート</p></figcaption></figure>

ポップアップウィンドウが表示され、Obsidian にエクスポートする対話ノートの **Properties（プロパティ）**とエクスポート方法を設定できます。以下の3つから選択可能です：

* **新規作成（存在する場合は上書き）**：[ステップ 2](obsidian.md#di-er-bu)で指定した`フォルダ`に新規ノートを作成し、同名ノートが存在する場合は上書き
* **先頭に追加**：同名ノートが存在する場合、選択した対話内容をノートの先頭に追加
* **末尾に追加**：同名ノートが存在する場合、選択した対話内容をノートの末尾に追加

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>ノートプロパティの設定</p></figcaption></figure>

{% hint style="info" %}
Properties（プロパティ）が付与されるのは最初の方法のみで、後の2つの方法には付属しません。
{% endhint %}

#### 個別の対話のエクスポート

個別の対話をエクスポートするには、対話の下にある_三本線メニュー_をクリックし、_エクスポート_を選択してから_Obsidian にエクスポート_をクリックします。

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>個別対話のエクスポート</p></figcaption></figure>

その後、完全な対話をエクスポートするときと同じウィンドウが表示され、**ノートプロパティ**と**ノートの処理方法**の設定を求められます。[上記のチュートリアル](obsidian.md#dao-chu-wan-zheng-dui-hua)と同じ手順で完了してください。

### エクスポート成功

🎉 これで Cherry Studio と Obsidian の連携設定がすべて完了し、エクスポートプロセスを完全に実行しました。お楽しみください！

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Obsidian へのエクスポート</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>エクスポート結果の確認</p></figcaption></figure>