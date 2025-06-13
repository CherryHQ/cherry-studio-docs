
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 無問芯穹（Muun Shin Kyuu）

こんな経験はありませんか：WeChatに保存した26本の実用的な記事を二度と開かず、PCの「学習資料」フォルダに散らばった10以上のファイル、半年前に読んだ理論を探したいが断片的なキーワードしか覚えていない。日々の情報量が脳の処理限界を超えると、貴重な知識の90%が72時間以内に忘れ去られます。\
今、無問芯穹大規模モデルサービスプラットフォームAPI + Cherry Studioで構築する個人知識ベースを使えば、WeChatの埋もれた記事や断片的な教材を構造化された知識に変換し、正確に呼び出せます。

### 一、個人知識ベースの構築

#### 1. 無問芯穹APIサービス：知識ベースの「思考中枢」、安定で使いやすい
知識ベースの「思考中枢」として、無問芯穹大規模モデルサービスプラットフォームはDeepSeek R1フルスペック版などのモデルを提供し、安定したAPIサービスを実現。**現在、登録後は無制限で無料利用可能。**知識ベース構築を支援する主流の埋め込みモデルbge/jinaをサポートし、**プラットフォームは安定した最新・最強のオープンソースモデルサービスを継続的に更新**、画像・動画・音声などマルチモーダル対応。

<figure><img src="../../.gitbook/assets/1280X1280 (1) (1).PNG" alt=""><figcaption></figcaption></figure>

#### 2. Cherry Studio：コード不要で構築する知識ベース
RAG知識ベース開発に比べ（1-2ヶ月のデプロイ期間）、このツールの利点は**コード操作不要**。Markdown/PDF/ウェブページなどをワンクリックでインポート可能、40MBファイルは1分で解析完了。さらにPCローカルフォルダ・WeChatお気に入り記事・授業ノートも追加可能。

### 二、3ステップで実現する専属知識マネージャー

#### Step 1：基本準備
1. Cherry Studio公式サイトからOS対応版ダウンロード（https://cherry-ai.com/）
2. 無問芯穹大規模モデルサービスプラットフォームでアカウント登録 (https://cloud.infini-ai.com/genstudio/model?cherrystudio)

<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

* APIキー取得：「モデル広場」でdeepseek-r1選択 → 作成クリック → APIKEY取得 → モデル名コピー

<figure><img src="../../.gitbook/assets/output (1).png" alt=""><figcaption></figcaption></figure>

#### Step 2：CherryStudio設定で無問芯穹API連携
モデルサービスから「無問芯穹」を選択し、APIキーを入力後、サービスを有効化

<figure><img src="../../.gitbook/assets/1280X1280 (2) (1).png" alt=""><figcaption></figcaption></figure>

上記完了後、対話時に大規模モデルを選択すればCherryStudioで無問芯穹APIを使用可能。\
利便性向上のため「デフォルトモデル」設定も推奨

<figure><img src="../../.gitbook/assets/01445ab7-b863-4155-b517-2b6c3c581f47.png" alt=""><figcaption></figcaption></figure>

#### Step 3：知識ベース追加
無問芯穹プラットフォームの埋め込みモデルからbgeシリーズ/jinaシリーズの任意のバージョンを選択

<figure><img src="../../.gitbook/assets/1 (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../../.gitbook/assets/2 (2).png" alt=""><figcaption></figcaption></figure>

### 三、実ユーザーシナリオ検証
* 学習資料インポート後、「『機械学習』第3章の核心公式導出を整理」と入力

<figure><img src="../../.gitbook/assets/6bbdbd0d-5db4-4440-b840-3bb3f422b831.gif" alt=""><figcaption></figcaption></figure>

**生成結果（参考）**

<figure><img src="../../.gitbook/assets/3.gif" alt=""><figcaption></figcaption></figure>