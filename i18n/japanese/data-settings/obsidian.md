---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# Obsidian 設定チュートリアル

Cherry StudioはObsidianとの連携をサポートしており、完全な会話または単一の会話をObsidianライブラリにエクスポートできます。

{% hint style="warning" %}
このプロセスでは追加のObsidianプラグインをインストールする必要はありません。ただし、Cherry StudioからObsidianへのインポートはObsidian Web Clipperと同様の原理を使用しているため、[会話が長すぎるとインポートに失敗する](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0)可能性を避けるために、Obsidianを最新バージョンにアップグレードすることをお勧めします（現在のObsidianバージョンは少なくとも**1.7.2**より大きい必要があります）。
{% endhint %}

## 最新チュートリアル

{% hint style="info" %}
旧バージョンのObsidianへのエクスポートと比較して、新バージョンのObsidianへのエクスポート機能ではライブラリパスを自動的に選択できるようになり、ライブラリ名やフォルダ名を手動で入力する必要がなくなりました。
{% endhint %}

### ステップ1: Cherry Studioの設定

Cherry Studioの_設定_ → _データ設定_ → _Obsidian設定_メニューを開きます。ドロップダウンボックスには、ローカルで開いたことがあるObsidianライブラリ名が自動的に表示されます。目標とするObsidianライブラリを選択してください：

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### ステップ2: 会話のエクスポート

#### 完全な会話をエクスポート

Cherry Studioの会話インターフェースに戻り、会話を右クリックして_エクスポート_を選択し、_Obsidianにエクスポート_をクリックします：

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

ポップアップウィンドウが表示され、Obsidianにエクスポートするこの会話ノートの **Properties（属性）**、Obsidian内の**フォルダ位置**、およびエクスポート時の**処理方法**を調整できます：

* **Vault（保管庫）**: ドロップダウンメニューをクリックして他のObsidianライブラリを選択できます
* **Path（パス）**: ドロップダウンメニューをクリックしてエクスポートされた会話ノートを保存するフォルダを選択できます
* Obsidianノートのプロパティ（Properties）として：
  * タグ（tags）
  * 作成時間（created）
  * 出典（source）
* Obsidianへのエクスポートにおける**処理方法**には、以下の3つのオプションがあります：
  * **新規作成（存在する場合は上書き）**: **Path**で指定した`フォルダ`に新しい会話ノートを作成し、同じ名前のノートが存在する場合は古いノートを上書きします
  * **先頭に追加**: 同じ名前のノートが既に存在する場合、選択した会話内容をエクスポートしてそのノートの先頭に追加します
  * **末尾に追加**: 同じ名前のノートが既に存在する場合、選択した会話内容をエクスポートしてそのノートの末尾に追加します

{% hint style="info" %}
プロパティ（属性）が付帯するのは最初の方法のみで、後の2つの方法ではプロパティ（属性）が付帯しません。
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>ノートプロパティの設定</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>パスの選択</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>処理方法の選択</p></figcaption></figure>

すべてのオプションを選択したら、「確定」をクリックすると、完全な会話が対応するObsidianライブラリの対応フォルダにエクスポートされます。

#### 単一会話をエクスポート

単一会話をエクスポートするには、会話の下にある_三本線メニュー_をクリックし、_エクスポート_を選択して、_Obsidianにエクスポート_をクリックします：

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>単一会話をエクスポート</p></figcaption></figure>

その後、完全な会話をエクスポートする場合と同じウィンドウがポップアップし、**ノートプロパティ**と**ノートの処理方法**を設定するよう求められます。同じく[上記のチュートリアル](obsidian.md#dao-chu-wan-zheng-dui-hua)に従って完了してください。

### エクスポート成功

🎉 これで、Cherry StudioとObsidianの連携設定がすべて完了し、エクスポート手順を最初から最後まで実行しました。お楽しみください！

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Obsidianにエクスポート</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>エクスポート結果を表示</p></figcaption></figure>



***

## 旧チュートリアル（Cherry Studio<v1.1.13 用）

### ステップ1: Obsidianの準備

Obsidianライブラリを開き、エクスポートされた会話を保存するための`フォルダ`を作成します（図ではCherry Studioフォルダを例としています）：

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

左下角に枠で囲まれたテキストに注意してください。これがあなたの`保管庫`名です。

### ステップ2: Cherry Studioの設定

Cherry Studioの_設定_ → _データ設定_ → _Obsidian設定_メニューで、[ステップ1](obsidian.md#di-yi-bu)で取得した`保管庫`名と`フォルダ`名を入力します：

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

`グローバルタグ`はオプションで、すべての会話をエクスポートした後、Obsidian内でのタグを設定できます。必要に応じて記入してください。

### ステップ3: 会話のエクスポート

#### 完全な会話をエクスポート

Cherry Studioの会話インターフェースに戻り、会話を右クリックして_エクスポート_を選択し、_Obsidianにエクスポート_をクリックします。

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>完全な会話をエクスポート</p></figcaption></figure>

ポップアップウィンドウが表示され、Obsidianにエクスポートするこの会話ノートの **Properties（属性）**とエクスポート時の**処理方法**を調整できます。Obsidianへのエクスポートにおける**処理方法**には、以下の3つのオプションがあります：

* **新規作成（存在する場合は上書き）**: [ステップ2](obsidian.md#di-er-bu)で指定した`フォルダ`に新しい会話ノートを作成し、同じ名前のノートが存在する場合は古いノートを上書きします
* **先頭に追加**: 同じ名前のノートが既に存在する場合、選択した会話内容をエクスポートしてそのノートの先頭に追加します
* **末尾に追加**: 同じ名前のノートが既に存在する場合、選択した会話内容をエクスポートしてそのノートの末尾に追加します

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>ノートプロパティの設定</p></figcaption></figure>

{% hint style="info" %}
プロパティ（属性）が付帯するのは最初の方法のみで、後の2つの方法ではプロパティ（属性）が付帯しません。
{% endhint %}

#### 単一会話をエクスポート

単一会話をエクスポートするには、会話の下にある_三本線メニュー_をクリックし、_エクスポート_を選択して、_Obsidianにエクスポート_をクリックします。

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>単一会話をエクスポート</p></figcaption></figure>

その後、完全な会話をエクスポートする場合と同じウィンドウがポップアップし、**ノートプロパティ**と**ノートの処理方法**を設定するよう求められます。同じく[上記のチュートリアル](obsidian.md#dao-chu-wan-zheng-dui-hua)に従って完了してください。

### エクスポート成功

🎉 これで、Cherry StudioとObsidianの連携設定がすべて完了し、エクスポート手順を最初から最後まで実行しました。お楽しみください！

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Obsidianにエクスポート</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>エクスポート結果を表示</p></figcaption></figure>