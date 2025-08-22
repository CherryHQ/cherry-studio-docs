---
description: Tools
icon: code
---
# Code Tools 使用チュートリアル


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




Cherry Studio v1.5.7 では、操作が簡単で強力な Code Agent 機能が導入されました。これにより、複数のAIプログラミングエージェントを直接起動・管理できます。本チュートリアルでは、設定から起動までのフルプロセスをご案内します。

***

### 操作手順

#### 1. Cherry Studio のアップグレード

まず、Cherry Studio が **v1.5.7** 以降のバージョンにアップグレードされていることを確認してください。最新バージョンは [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) または公式サイトからダウンロードできます。

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### 2. ナビゲーションバーの位置調整

トップタブ機能をより使いやすくするため、ナビゲーションバーを上部に移動することをおすすめします。
* 操作パス：`設定` → `表示設定` → `ナビゲーションバー設定`
* 「ナビゲーションバーの位置」オプションを **`上部`** に設定

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### 3. 新しいタブの作成

インターフェース上部の「+」アイコンをクリックし、新しい空白タブを作成します。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 4. Code Agent 機能の起動

新しく作成したタブで、`Code`（または `</>`）アイコンをクリックし、Code Agent 設定画面に移動します。

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. CLI ツールの選択

ご自身のニーズと所有するAPIキーに基づいて、使用するCode Agentツールを選択します。現在以下のツールが利用可能です：
* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Agentが呼び出すモデルの選択

モデルドロップダウンリストで、選択したCLIツールと互換性のあるモデルを選択します。（詳細なモデル互換性については、後述の「重要な注意事項」を参照）

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. 作業ディレクトリの指定

「ディレクトリを選択」ボタンをクリックし、Agentに作業ディレクトリを指定します。このディレクトリ配下のすべてのファイルとサブディレクトリにAgentがアクセス可能になるため、プロジェクトのコンテキスト理解やコード実行が可能になります。

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. 環境変数の設定
* **自動設定**：ステップ6（モデル）とステップ7（作業ディレクトリ）での選択内容に基づき、対応する環境変数が自動生成されます
* **カスタム追加**：Agentやプロジェクトに特定の環境変数（例：`PROXY_URL`など）が必要な場合、このエリアでカスタム追加できます

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. 更新オプション
* **組み込み実行ファイル**：Cherry Studio にはすべてのCode Agentの実行ファイルが統合されており、ほとんどの場合インターネット接続なしで直接使用できます
* **自動更新**：Agentを常に最新バージョンに保ちたい場合は、**`更新を確認して最新版をインストール`** オプションをチェックしてください。チェックすると、起動時に毎回オンラインで更新確認とAgentツールの更新が行われます

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Agentの起動

すべての設定が完了したら、**`起動`** ボタンをクリックします。Cherry Studio はシステムのTerminal（ターミナル）ツールを自動的に呼び出し、すべての環境変数をロードした後、選択したCode Agentを実行します。ポップアップしたターミナルウィンドウでAI Agentとの対話を開始できます。

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### 重要な注意事項

1. **モデル互換性について**：
   * **Claude Code**: Anthropic APIエンドポイント形式をサポートするモデルを選択する必要があります。現在公式サポートモデルは：
     * Claudeシリーズモデル
     * DeepSeek V3.1 (公式APIプラットフォーム)
     * Kimi K2 (公式APIプラットフォーム)
     * 智譜 GLM 4.5 (公式APIプラットフォーム)
     * **注意**：現在多くのサードパーティプロバイダ（One API, New API等）が提供するDeepSeek, Kimi, GLMのAPIインターフェースはOpenAI Chat Completions形式のみサポートしており、Claude Codeと直接互換性がない可能性があります。プロバイダによる順次対応をお待ちください
   * **Gemini CLI**: GoogleのGeminiシリーズモデルを選択する必要があります
   * **Qwen Code**: OpenAI Chat Completions API形式をサポートするモデルに対応。最適なコード生成効果を得るには**`Qwen3 Coder`**シリーズモデルの使用を強く推奨
   * **OpenAI Codex**: GPTシリーズモデル（例：`gpt-4o`, `gpt-5`等）をサポート
2. **依存関係と環境競合**：
   * Cherry Studioは独立したNode.js実行環境、Code Agent実行ファイル及び環境変数設定を内部統合し、すぐに使用できるクリーンな環境を提供します
   * Agent起動時に依存関係の競合や不具合が発生した場合、システムにインストールされている関連依存関係（グローバルインストールされたNode.jsや特定ツールチェーンなど）を一時的に**アンインストールまたは無効化**し、競合の排除をお試しください
3. **APIトークン消費に関する警告**：
   * **Code AgentはAPIトークンを大量に消費します**。複雑なタスク処理時、Agentは思考・計画・コード生成のために大量のリクエストを生成し、トークンが急速に消費される可能性があります
   * ご自身のAPI割り当て量と予算に基づき、**無理のない範囲で使用**し、トークン使用状況を注意深く監視して予算超過を防いでください

本チュートリアルが、Cherry Studioの強力なCode Agent機能の迅速な導入にお役に立てば幸いです！