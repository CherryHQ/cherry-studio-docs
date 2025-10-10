---
description: Tools
icon: code
---
# Code Tools 使い方ガイド


{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}




Cherry Studio v1.5.7 では、操作が簡単で強力な Code Agent 機能が導入され、複数の AI プログラミングエージェントを直接起動および管理できます。本チュートリアルでは、設定と起動の完全なプロセスをガイドします。

***

### 操作手順

#### 1. Cherry Studio のアップグレード

まず、Cherry Studio が **v1.5.7** 以降にアップグレードされていることを確認してください。最新バージョンは [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) または公式サイトからダウンロードできます。

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 2. ナビゲーションバーの位置調整

上部タブ機能を便利に使用するため、ナビゲーションバーを上部に調整することを推奨します。
* 操作手順: `設定` → `表示設定` → `ナビゲーションバー設定`
* 「ナビゲーションバー位置」オプションを **`上部`** に設定

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. 新規タブの作成

インターーフェース上部の「+」アイコンをクリックし、新しい空白タブを作成します。

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. Code Agent 機能の有効化

新規タブで `Code`（または `</>`）アイコンをクリックし、Code Agent 設定画面に移動します。

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. CLI ツールの選択

要件と所有する API Key に基づき、使用する Code Agent ツールを選択します。現在サポートされているツール:
* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Agent が呼び出すモデルの選択

モデルドロップダウンから、選択した CLI ツールと互換性のあるモデルを選択します。_（詳細な互換性情報は下部「重要注意事項」参照）_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. 作業ディレクトリの指定

「ディレクトリを選択」ボタンをクリックし、Agent の作業ディレクトリを指定します。Agent はこのディレクトリ内の全ファイル・サブディレクトリにアクセスし、プロジェクトのコンコンテキスト理解・ファイル読み取り・コード実行が可能になります。

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. 環境変数の設定
* **自動設定**: 手順6（モデル）と7（作業ディレクトリ）の選択に基づき、対応する環境変数が自動生成されます
* **カスタム追加**: Agent やプロジェクトに特定の環境変数（例: `PROXY_URL`）が必要な場合、この領域で追加設定できます

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. 更新オプション
* **内蔵実行ファイル**: Cherry Studio は全 Code Agent の実行ファイルを統合しており、多くの場合オフラインで即時使用可能です
* **自動更新**: Agent を常に最新版に保つ場合、**`更新をチェックして最新版をインストール`** オプションをチェックします。有効時は起動毎にオンライン更新チェックが行われます

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Agent の起動

設定完了後、**`起動`** ボタンをクリックします。Cherry Studio はシステムのターミナルを自動起動し、全環境変数をロード後、選択した Code Agent を実行します。ポップアップしたターミナルウィンドウで AI Agent との対話を開始できます。

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### 重要注意事項

1. **モデル互換性について**:
   * **Claude Code**: Anthropic API エンドポイント形式をサポートするモデルが必要です。現在公式サポートモデル:
     * Claude シリーズモデル
     * DeepSeek V3.1 (公式APIプラットフォーム)
     * Kimi K2 (公式APIプラットフォーム)
     * 智譜 GLM 4.5 (公式APIプラットフォーム)
     * **注意**: One API/New API 等のサードパーティプロバイダーは DeepSeek/Kimi/GLM 向けに OpenAI Chat Completions 形式のみサポートする場合が多く、Claude Code との直接互換性がない可能性があります
   * **Gemini CLI**: Google の Gemini シリーズモデルのみ対応
   * **Qwen Code**: OpenAI Chat Completions API 形式をサポートするモデルと互換性があり、最適なコード生成には **`Qwen3 Coder`** シリーズを強く推奨
   * **OpenAI Codex**: GPT シリーズモデル（`gpt-4o`, `gpt-5` 等）をサポート
2. **依存関係と環境競合**:
   * Cherry Studio は独立した Node.js 環境・Code Agent 実行ファイル・環境変数設定を統合し、すぐに使えるクリーン環境を提供
   * Agent 起動時に依存関係の競合や異常エラーが発生する場合、システムにインストール済みの関連依存（Node.js 等）を一時**削除または無効化**して競合を排除
3. **API トークン消費警告**:
   * **Code Agent は非常に大量の API トークンを消費します**。複雑なタスク処理時、Agent の思考・計画・コード生成により大量リクエストが発生し、トークンが急激に減少
   * API 割当量と予算に応じて**無理のない範囲で使用**し、トークン使用状況を厳密に監視し予算超過を防止

本チュートリアルが Cherry Studio の強力な Code Agent 機能を素早く習得する助けとなることを願っています！