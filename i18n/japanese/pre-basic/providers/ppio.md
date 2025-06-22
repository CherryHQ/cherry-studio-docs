
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# PPIO パイオー・クラウド

## Cherry Studio × PPIO LLM API 接続ガイド

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)チュートリアル概要 <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio はマルチモデル対応のデスクトップクライアントで、Windows、Linux、MacOS 各プラットフォーム向けに提供されています。主要LLMモデルを統合し、多彩なシナリオをサポートするAIアシスタントです。インテリジェントなチャット管理、オープンソースカスタマイズ、マルチテーマUIで生産性を向上させます。

Cherry Studio は現在 **PPIO 高性能APIチャネル**と正式連携——エンタープライズ級のコンピューティングリソースにより **DeepSeek-R1/V3の高速応答**と**99.9%のサービス可用性**を実現し、スムーズなユーザー体験を提供します。

以下のチュートリアルではAPIキーの設定を含む完全な統合手順を解説します。「Cherry Studioインテリジェント制御＋PPIO高性能API」の進化版を3分で構築可能です。

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. Cherry Studioで「PPIO」をプロバイダーとして追加 <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

公式サイトからCherry Studioをダウンロード：[https://cherry-ai.com/download](https://cherry-ai.com/download)（アクセスできない場合はQuarkクラウドリンクを利用：[https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share)）

（1）左下の設定アイコンをクリックし、プロバイダー名を`PPIO`と入力 →「確定」

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

（2）[パイオー算力雲 APIキー管理](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio)にアクセス →【ユーザーアイコン】→【APIキー管理】でコンソール画面へ

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

【＋作成】をクリックし、APIキー名を入力します。**生成されたキーはその場でのみ表示されるため、必ずコピーして保存してください**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

（3）Cherry Studioでキーを登録：設定画面で【PPIO パイオー・クラウド】を選択し、生成したAPIキーを入力 →【チェック】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

（4）モデル選択：例として「deepseek/deepseek-r1/community」を選択（他モデルへ切り替える場合は直接変更可能）

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1/V3 community版は全パラメーター対応の無料体験版です（性能・安定性は有料版と同じ）。継続利用の場合は**課金後に非community版へ切り替え**が必要です。

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. モデル利用設定 <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

（1）【チェック】で接続成功を確認後、正常使用可能に

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

（2）最後に【@】をクリック → PPIOプロバイダー配下のDeepSeek R1モデルを選択 → チャット開始！

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【参考素材：[陳恩](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. PPIO × Cherry Studio 動画チュートリアル <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

ビジュアル学習をご希望の場合はBilibili動画をご利用ください。「PPIO API＋Cherry Studio」の設定手法を手順解説：→ [《【DeepSeekがクルクル回ってイライラする？】PPIO＋DeepSeek フルスペック版 = 渋滞解消，爆速起動》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【動画素材提供：sola】