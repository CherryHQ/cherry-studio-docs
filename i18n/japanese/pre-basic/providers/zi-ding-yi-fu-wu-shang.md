
{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# カスタムプロバイダー

Cherry Studioは主流のAIモデルサービスを統合しているだけでなく、強力なカスタマイズ機能も提供します。**カスタムAIプロバイダー**機能により、必要なAIモデルを簡単に接続できます。

## なぜカスタムAIプロバイダーが必要ですか？

* **柔軟性：** 事前設定のプロバイダーリストに制限されず、ニーズに最適なAIモデルを自由選択
* **多様性：** 様々なプラットフォームのAIモデルを試し、それぞれの強みを発見
* **制御性：** APIキーやアクセスアドレスを直接管理し、セキュリティとプライバシーを確保
* **カスタマイズ：** プライベートデプロイメントモデルを接続し、特定ビジネスシナリオに対応

## カスタムAIプロバイダーの追加方法

以下の簡単な手順でカスタムAIプロバイダーを追加できます：

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **設定を開く：** Cherry Studio左ナビゲーションバーの「設定」（歯車アイコン）をクリック
2. **モデルサービスへ移動：** 設定ページで「モデルサービス」タブを選択
3. **プロバイダーを追加：** 既存プロバイダーリスト下部の「＋追加」ボタンをクリックし、ポップアップを開く
4. **情報を入力：**
   * **プロバイダー名：** 識別しやすい名称を入力（例：MyCustomOpenAI）
   * **プロバイダー種別：** 以下のサポート対象から選択：
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **設定を保存：** 「追加」ボタンをクリックして設定を保存

## カスタムAIプロバイダーの設定

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

追加後、リストから対象プロバイダーを選択し詳細設定：

1. **有効状態：** リスト右端のトグルスイッチでサービスの有効/無効を制御
2. **APIキー：**
   * AIプロバイダーから提供されたAPIキーを入力
   * 右側の「検証」ボタンでキーの有効性を確認
3. **APIアドレス：**
   * AIサービスのベースURLを入力
   * プロバイダー公式ドキュメントで正しいアドレスを確認
4. **モデル管理：**
   * 「＋追加」ボタンで使用するモデルIDを入力（例：`gpt-3.5-turbo`，`gemini-pro`）
   <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>
   * モデル名が不明な場合はプロバイダー公式ドキュメントを参照
   * 「管理」ボタンで追加済みモデルの編集・削除が可能

## 利用開始

上記設定が完了すれば、Cherry StudioのチャットインターフェースでカスタムAIプロバイダーとモデルを選択し、AIとの対話を開始できます！

## vLLMをカスタムAIプロバイダーとして使用

vLLMはOllamaに似た高速LLM推論ライブラリです。Cherry Studioへの統合手順：

1. **vLLMのインストール：** 公式ドキュメント（[https://docs.vllm.ai/en/latest/getting\_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)）に従いインストール

    ```sh
    pip install vllm # pip利用時
    uv pip install vllm # uv利用時
    ```
2. **vLLMサービスの起動：** OpenAI互換インターフェースでサービスを起動：
   * `vllm.entrypoints.openai.api_server`で起動：
   
    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```
   
   * `uvicorn`で起動：
   
    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

   サービスが正常に起動し、デフォルトポート`8000`でリッスンすることを確認。`--port`パラメータでポート指定も可能。

3. **Cherry StudioにvLLMプロバイダーを追加：**
   * 前述の手順で新規カスタムAIプロバイダーを追加
   * **プロバイダー名：** `vLLM`
   * **プロバイダー種別：** `OpenAI`を選択
4. **vLLMプロバイダーの設定：**
   * **APIキー：** vLLMは不要なため空欄または任意入力
   * **APIアドレス：** vLLMサービスアドレス（例：`http://localhost:8000/`）
   * **モデル管理：** vLLMにロードしたモデル名を追加（例：`gpt2`）
5. **会話開始：** Cherry StudioでvLLMプロバイダーと`gpt2`モデルを選択し、vLLM駆動のLLMと対話開始

## ヒントとコツ

* **ドキュメント確認：** APIキー、アクセスアドレス、モデル名等はプロバイダー公式ドキュメントで必ず確認
* **APIキーの検証：** 「検証」ボタンでキーの有効性を確認し、エラーを予防
* **APIアドレスの注意：** プロバイダーやモデルによりアドレスが異なるため正確に入力
* **モデルの選択的追加：** 実際に使用するモデルのみを追加し、不要なモデルの登録は避ける