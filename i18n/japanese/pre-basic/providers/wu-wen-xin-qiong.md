
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# Infinite Core

以下の経験はありませんか：WeChatに保存した26本の有益記事はその後開かれることがなく、PCに散らばる「学習資料」フォルダ内の10以上のファイル、半年前に読んだ理論を探したいのに数個のキーワードしか覚えていない。そして日々の情報量が脳の処理限界を超えると、貴重な知識の90%が72時間以内に忘却されます。\
今、Infinite Core大規模モデルプラットフォームAPI + Cherry Studioで構築する個人ナレッジベースなら、WeChat記事や断片的な教材を構造化知識に変換し、精密な呼び出しを実現できます。

### 一、個人ナレッジベース構築

#### 1. Infinite Core APIサービス：「思考中枢」として使いやすく安定
ナレッジベースの「思考中枢」として、Infinite Core大規模モデルプラットフォームはDeepSeek R1フルスペック版などのモデルを提供し、安定したAPIサービスを提供。**現在登録後は無条件・無料で利用可能**。主流の埋め込みモデルbge・jinaモデルでのナレッジベース構築をサポートし、**プラットフォームは最新・最強のオープンソースモデルサービスを継続的に更新**。画像・動画・音声などマルチモーダル対応。

<figure><img src="../../.gitbook/assets/1280X1280 (1) (1).PNG" alt=""><figcaption></figcaption></figure>

#### 2. Cherry Studio：ノーコードで構築可能
Cherry Studioは使いやすいAIツール。RAGナレッジベース開発に1～2ヶ月かかるのに対し、本ツールは**ノーコード操作を特長**。Markdown/PDF/Webページなどをワンクリックでインポート可能（40MBファイルは1分で解析）。PCのローカルフォルダ・WeChat保存記事URL・講義ノートも追加可能です。

### 二、3ステップで専属ナレッジマネージャーを構築

#### Step 1：基本準備
1. Cherry Studio公式サイトからOS対応版をダウンロード（https://cherry-ai.com/）
2. アカウント登録：Infinite Core大規模モデルプラットフォームにログイン（https://cloud.infini-ai.com/genstudio/model?cherrystudio）

<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

* APIキー取得：「モデル広場」でdeepseek-r1を選択→作成クリックでAPIKEYを生成→モデル名をコピー

<figure><img src="../../.gitbook/assets/output (1).png" alt=""><figcaption></figcaption></figure>

#### Step 2：CherryStudio設定で「モデルサービス」にInfinite Coreを選択し、APIキーを入力して有効化

<figure><img src="../../.gitbook/assets/1280X1280 (2) (1).png" alt=""><figcaption></figcaption></figure>

上記完了後、使用時に大規模モデルを選択すればCherryStudioからInfinite Core APIを利用可能。\
利便性向上のため「デフォルトモデル」設定を推奨

<figure><img src="../../.gitbook/assets/01445ab7-b863-4155-b517-2b6c3c581f47.png" alt=""><figcaption></figcaption></figure>

#### Step 3：ナレッジベース追加
Infinite Coreプラットフォームの埋め込みモデルからbgeシリーズまたはjinaシリーズの任意バージョンを選択

<figure><img src="../../.gitbook/assets/1 (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../../.gitbook/assets/2 (2).png" alt=""><figcaption></figcaption></figure>

### 三、実ユーザーシナリオ検証
* 学習資料インポート後、「『機械学習』第3章の核心公式導出を整理」と入力

<figure><img src="../../.gitbook/assets/6bbdbd0d-5db4-4440-b840-3bb3f422b831.gif" alt=""><figcaption></figcaption></figure>

**▼生成結果例**

<figure><img src="../../.gitbook/assets/3.gif" alt=""><figcaption></figcaption></figure>