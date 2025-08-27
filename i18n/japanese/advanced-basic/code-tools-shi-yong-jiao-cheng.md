---
description: Tools
icon: code
---
# Code Tools 使用方法


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




Cherry Studio v1.5.7 バージョンでは、操作が簡単で強力な Code Agent 機能を導入しました。これにより、複数のAIプログラミングエージェントを直接起動して管理できます。このチュートリアルでは、設定から起動までの完全なプロセスを案内します。

***

### 操作手順

#### 1. Cherry Studioをアップグレード

最初に、Cherry Studio が **v1.5.7** 以降のバージョンにアップグレードされていることを確認してください。[GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) または公式サイトから最新バージョンをダウンロードできます。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 2. ナビゲーションバーの位置調整

トップタブ機能を便利に使用するため、ナビゲーションバーを上部に調整することをおすすめします。

* 操作パス: `設定` → `表示設定` → `ナビゲーションバー設定`
* 「ナビゲーションバー位置」オプションを **`上部`** に設定

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. 新規タブ作成

インターフェイス上部の「+」アイコンをクリックし、新しい空白タブを作成します。

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. Code Agent機能を開く

新しく作成したタブで、`Code` （または `</>`）アイコンをクリックし、Code Agent設定画面に進みます。

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. CLIツール選択

ニーズと保有するAPI Keyに基づいて、使用するCode Agentツールを選択します。現在以下のツールがサポートされています：

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Agentが呼び出すモデル選択

モデルドロップダウンリストから、選択したCLIツールと互換性のあるモデルを選択します。_（詳細なモデル互換性については、後述の「重要な注意事項」を参照）_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. 作業ディレクトリ指定

「ディレクトリ選択」ボタンをクリックし、Agentの作業ディレクトリを指定します。Agentはこのディレクトリ下の全てのファイルとサブディレクトリにアクセスでき、プロジェクトの文脈理解、ファイル読み取り、コード実行が可能になります。

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. 環境変数設定

* **自動設定**：ステップ6（モデル）とステップ7（作業ディレクトリ）での選択に基づき、対応する環境変数が自動生成されます。
* **カスタム追加**：Agentやプロジェクトに特定の環境変数（例：`PROXY_URL`など）が必要な場合、この領域でカスタム追加できます。

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. 更新オプション

* **内蔵実行ファイル**：Cherry Studioは上記のCode Agent実行ファイルをすべて内蔵しており、ほとんどの場合インターネット接続なしで直接使用できます。
* **自動更新**：Agentを常に最新バージョンに保ちたい場合は、**`更新を確認し最新バージョンをインストール`**オプションをチェックしてください。チェックすると、起動時に毎回インターネットで更新を確認し、Agentツールを更新します。

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Agent起動

すべての設定が完了したら、 **`起動`** ボタンをクリックします。Cherry StudioはシステムのTerminal（端末）ツールを自動的に呼び出し、すべての環境変数を読み込んだ後、選択したCode Agentを実行します。これでポップアップした端末ウィンドウでAI Agentと対話できます。

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### 重要な注意事項

1. **モデル互換性説明**:
   * **Claude Code**: Anthropic APIエンドポイント形式をサポートするモデルを選択する必要があります。現在公式でサポートされているモデル:
     * Claudeシリーズモデル
     * DeepSeek V3.1 (公式APIプラットフォーム)
     * Kimi K2 (公式APIプラットフォーム)
     * 智譜 GLM 4.5 (公式APIプラットフォーム)
     * **注意**：現在多くのサードパーティプロバイダ（One API, New APIなど）は、DeepSeek, Kimi, GLMのAPIインターフェースの多くがOpenAI Chat Completions形式のみをサポートしており、Claude Codeと直接互換性がない可能性があります。プロバイダ側の順次対応が必要です。
   * **Gemini CLI**: GoogleのGeminiシリーズモデルが必要です。
   * **Qwen Code**: OpenAI Chat Completions API形式をサポートするモデルが対応します。最適なコード生成効果を得るために **`Qwen3 Coder`** シリーズモデルの使用を強く推奨します。
   * **OpenAI Codex**: GPTシリーズモデル（`gpt-4o`, `gpt-5` など）をサポートします。
2. **依存関係と環境競合**:
   * Cherry Studioは独立したNode.js実行環境、Code Agent実行ファイル、環境変数設定を内蔵し、すぐに使えるクリーンな環境を提供します。
   * Agent起動時に依存関係の競合や異常なエラーが発生した場合は、競合を排除するため、システム内にインストールされた関連依存関係（グローバルにインストールされたNode.jsや特定のツールチェーンなど）を一時的に**アンインストールまたは無効化**することを検討してください。
3. **APIトークン消費警告**:
   * **Code AgentのAPIトークン消費量は非常に大きい**です。複雑なタスク処理時、Agentが思考・計画・コード生成のために大量のリクエストを生成し、トークンが急速に消費される可能性があります。
   * ご自身のAPIクォータと予算に基づき、**実力に応じて**トークン使用状況を注意深く監視し、予算超過を防いでください。

このチュートリアルがCherry Studioの強力なCode Agent機能の迅速な習得にお役に立てば幸いです！