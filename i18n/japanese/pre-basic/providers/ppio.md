# PPIO パイオウクラウド


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




## Cherry Studio の PPIO LLM API 接続方法

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%E6%95%99%E7%A8%8B%E6%A6%82%E8%BF%B0)チュートリアル概要 <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio はマルチモデルデスクトップクライアントで、現在 Windows、Linux、MacOS システム向けインストーラーをサポートしています。主要な LLM モデルを統合し、多様なシナリオを支援します。ユーザーはインインテリジェントな会話管理、オープンソースカスタマイズ、マルチテーマインターーフェースを通じて作業効率を向上できます。

Cherry Studio は **PPIO 高性能 API ゲートウェイ** と完全互換となりました——エンタープライズレベルのコンピューーティングリソースにより、**DeepSeek-R1/V3 の高速応答** と **99.9% のサービス可用性** を実現し、スムーズな体験を提供します。

以下のチュートリアルには完全な接続ソリューション（APIキー設定含む）が含まれており、3分で「Cherry Studio インテリジェントスケジューリング + PPIO 高性能API」のアドバンストモードを開始できます。

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-%E8%BF%9B%E5%85%A5-cherrystudio%EF%BC%8C%E6%B7%BB%E5%8A%A0-%E2%80%9Cppio%E2%80%9D-%E4%BD%9C%E4%B8%BA%E6%A8%A1%E5%9E%8B%E6%8F%90%E4%BE%9B%E5%95%86)1. CherryStudio で「PPIO」をモデルプロバイダーとして追加 <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

まず公式サイトから Cherry Studio をダウンロード：[https://cherry-ai.com/download](https://cherry-ai.com/download) （アクセスできない場合は以下の Quark クラウドリンクから必要なバージョンをダウンロード：[https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

（1）左下の設定をクリックし、プロバイダー名を「`PPIO`」に変更し、「確定」をクリック

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

（2）[パイオウコンピューーティングクラウド API キー管理](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio) にアクセスし、【ユーザーアイコン】→【APIキー管理】でコンソールに入る

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

【+ 作成】ボタンをクリックして新しいAPIキーを作成。キー名をカスタマイズし、**生成されたキーは生成時のみ表示されるため、必ずコピーして保存し、今後の使用に影響しないようにしてください**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

（3）CherryStudio でキーを入力：設定を選択し、【PPIO パイオウクラウド】を選び、公式サイトで生成したAPIキーを入力し、【チェック】をクリック

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

（4）モデル選択：例として deepseek/deepseek-r1/community を選択。他のモデルに変更する場合は直接切り替え可能

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 と V3 community 版は体験用で、全パラメータ完全版モデルです。安定性と効果に違いはありませんが、大量に呼び出す場合は **チャージして非community版に切り替える** 必要があります。

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-%E6%A8%A1%E5%9E%8B%E4%BD%BF%E7%94%A8%E9%85%8D%E7%BD%AE)2. モデル使用設定 <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

（1）【チェック】をクリックして接続成功が表示されれば正常に使用可能

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

（2）最後に【@】をクリックし、PPIOプロバイダー下で追加したDeepSeek R1モデルを選択すればチャット開始～

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【一部素材出典：[陈恩](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-ppio%C3%97cherry-studio-%E8%A7%86%E9%A2%91%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)3. PPIO×Cherry Studio 動画チュートリアル <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

より直感的な学習を希望される場合、Bilibiliに動画チュートリアルを用意しました。「PPIO API+Cherry Studio」の設定方法を手順ごとに説明し、スムーズな開発体験を開始できます → [《【DeepSeekの回転待ちにまだイライラ？】パイオウクラウド+DeepSeek完全版=？渋滞解消、即時起動》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【動画出典：sola】