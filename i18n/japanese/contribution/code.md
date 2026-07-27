---
icon: square-code
---

# コードへのコントリビューション

Cherry Studio では、機能、Bug 修正、テスト、性能、アクセシビリティ、開発ツールなどのコードコントリビューションを受け付けています。現在の V2 開発は `main` ブランチで行われています。開始前に、問題、変更範囲、検証方法を確認してください。

プロジェクトリポジトリ：[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)

## 始める前に

最初に次をお読みください。

* [コントリビューターガイド](https://github.com/CherryHQ/cherry-studio/blob/main/CONTRIBUTING.md)
* [行動規範](https://github.com/CherryHQ/cherry-studio/blob/main/CODE_OF_CONDUCT.md)
* [開発ガイド](https://github.com/CherryHQ/cherry-studio/blob/main/docs/guides/development.md)
* [プロジェクト開発規約](https://github.com/CherryHQ/cherry-studio/blob/main/CLAUDE.md)
* [オープンソースライセンス](https://github.com/CherryHQ/cherry-studio/blob/main/LICENSE)

大きな機能の実装、ユーザーフローの変更、公開インターフェースのリファクタリングを予定している場合は、先に [Issues](https://github.com/CherryHQ/cherry-studio/issues) と既存の Pull Request を検索してください。関連する議論がなければ、問題、目標、案を説明する Issue を最初に作成すると、重複作業と方向のずれを減らせます。

初めてのコントリビューションには、次のラベルからタスクを探せます。

* [good first issue](https://github.com/CherryHQ/cherry-studio/labels/good%20first%20issue)
* [help wanted](https://github.com/CherryHQ/cherry-studio/labels/help%20wanted)
* [kind/bug](https://github.com/CherryHQ/cherry-studio/labels/kind%2Fbug)

## 正しいブランチを選ぶ

| 変更 | ベースブランチ | PR の対象ブランチ |
| :--- | :--- | :--- |
| 現在の機能、V2 開発、リファクタリング、最適化、Bug 修正 | `main` | `main` |
| リリース済み V1 の最小限の保守修正 | `v1` | `v1` |

V1 の修正は自動的に `main` へ入りません。同じ問題が現在の開発ブランチにもある場合は、`main` 向けに別の forward-port PR が必要です。

上流ブランチへ直接コミットしないでください。リポジトリを fork し、正しいベースブランチから短期の作業ブランチを作成します。

## 開発環境を準備する

現在の `main` は `.node-version` で Node.js `24.11.1`、`package.json` で pnpm `10.27.0` を固定しています。バージョンはリポジトリの更新により変わるため、作業開始時にはローカルブランチのファイルを基準にしてください。

### Windows：最初にシンボリックリンクを有効にする

リポジトリは一部のファイル同期にシンボリックリンクを使用します。Windows ではクローン前に次を行ってください。

1. システム設定で**開発者モード**を有効にするか、シンボリックリンク作成権限を付与します。
2. 次を実行します。

```powershell
git config --global core.symlinks true
```

3. その後でリポジトリをクローンします。シンボリックリンクを有効にする前にクローンした場合は、有効化後に再クローンすることを推奨します。

### Fork とクローン

GitHub で `CherryHQ/cherry-studio` を fork してから、次を実行します。

```bash
git clone https://github.com/YOUR_GITHUB_NAME/cherry-studio.git
cd cherry-studio
git remote add upstream https://github.com/CherryHQ/cherry-studio.git
git fetch upstream
git switch -c fix/short-description upstream/main
```

`YOUR_GITHUB_NAME` とブランチ名を自分の値に置き換えます。機能ブランチには `feat/`、Bug 修正には `fix/`、ドキュメント変更には `docs/` を使用できます。

### Node.js と依存関係をインストールする

`.node-version` または `.nvmrc` に対応するバージョン管理ツールで、リポジトリ指定の Node.js をインストールします。例：

```bash
nvm install
nvm use
corepack enable
corepack pnpm install
```

Corepack 経由でリポジトリ固定の pnpm を使用してください。別のグローバル pnpm で `pnpm-lock.yaml` を書き換えないでください。依存関係を実際に変更した場合を除き、PR に無関係なロックファイル変更を含めないでください。

### ローカル環境ファイルを作成する

```bash
cp .env.example .env
```

`.env` は Git から除外されています。ローカル開発に必要な値だけを入力し、実際の API Key、Token、Cookie、その他の認証情報をコード、テスト、ログ、スクリーンショットへコミットしないでください。

### アプリを起動する

```bash
corepack pnpm dev
```

初回起動では OpenAPI ファイルを生成してから、Electron の開発インスタンスが開きます。メインプロセスまたはレンダラープロセスをデバッグする場合は、次を使用できます。

```bash
corepack pnpm debug
```

依存関係のインストールまたは起動に失敗した場合は、まず Node.js と pnpm のバージョンを照合し、他のパッケージマネージャーがロックファイルを変更していないことを確認してから、ターミナルの最初のエラーを確認します。

## 変更を始める

### 対象範囲の規約を理解する

Cherry Studio は、Electron のメインプロセス、preload 層、React レンダラー層、複数の共有パッケージを含む monorepo です。ディレクトリを編集する前に：

1. そのディレクトリと親ディレクトリの `README.md` を読みます。
2. 近くにある同種の実装とテストを確認します。
3. `@deprecated` を検索し、廃止予定のインターフェースを拡張しないようにします。
4. 現在の問題を解決するために必要なファイルだけを変更します。

レンダラー層から Node.js API へ直接アクセスしないでください。プロセス間の機能が必要な場合は、既存の preload と IPC の境界に従います。ログにはプロジェクトの `loggerService` を使用し、新しい `console.log` を追加しないでください。

### テスト可能な変更にする

Bug 修正では、先に問題を再現するテストを追加することを推奨します。新しい動作には、成功、失敗、境界条件のテストを追加してください。プロジェクトは Vitest を使用し、領域別のテストコマンドがあります。

```bash
corepack pnpm test:main
corepack pnpm test:renderer
corepack pnpm test:aicore
corepack pnpm test:shared
```

毎回すべてを実行する必要はありません。開発中は変更に最も近いテストを先に実行し、コミット前に完全なチェックを行います。

### ユーザーに表示されるテキスト

画面の文字列を追加・変更するときは、コンポーネントに 1 言語だけの文字列を直接書かず、既存の国際化機構を使用してください。少なくとも次を実行します。

```bash
corepack pnpm i18n:check
corepack pnpm i18n:hardcoded:strict
```

新しいキーを同期する必要がある場合は、リポジトリの[国際化ガイド](https://github.com/CherryHQ/cherry-studio/blob/main/docs/guides/i18n.md)を読んでから、対応するスクリプトを使用します。

### データベース構造

Drizzle Schema を変更した場合は、対応するマイグレーションを生成してコミットします。

```bash
corepack pnpm db:migrations:generate
corepack pnpm db:migrations:check
```

rebase 後にマイグレーション番号が競合した場合、SQL ファイル名だけを変更したり snapshot を手作業で編集したりしないでください。リポジトリのデータマイグレーション文書に従って再生成し、マイグレーションチェーンと Schema が一致することを確認します。

## コミット前のチェック

実際の変更を最初に確認します。

```bash
git status --short
git diff --check
git diff
```

一時ファイル、認証情報、個人パス、無関係なフォーマット、意図しないロックファイル変更がないことを確認します。

変更に最も関係するテストを実行してから、リポジトリの完全なチェックを実行します。

```bash
corepack pnpm build:check
```

`build:check` は、コード規約、型、OpenAPI、ドキュメントリンク、テストなどを確認します。データベース、厳格な国際化、スキル、特定パッケージのチェックは CI で別途実行される場合があります。関連領域を変更した場合は、対応するコマンドも事前に実行してください。

{% hint style="info" %}
チェック用スクリプトと Node.js のバージョンは `main` の更新に伴って変わります。このページのコマンドがリポジトリと異なる場合は、現在のブランチの `package.json`、`.node-version`、`CONTRIBUTING.md`、CI 設定を基準にしてください。
{% endhint %}

## コミットを作成する

プロジェクトは、小さく焦点を絞った Conventional Commit と、DCO sign-off を求めています。

```bash
git add path/to/changed-file
git commit --signoff -m "fix(module-name): describe the change"
```

一般的な種類は `feat`、`fix`、`refactor`、`docs`、`test`、`chore` です。Scope は具体的なモジュールを示す短い kebab-case 名にし、`main` のような広すぎる範囲を使わないでください。

`--signoff` はコミットメッセージに次を追加します。

```text
Signed-off-by: Your Name <your.email@example.com>
```

これは、このコントリビューションをプロジェクトのライセンスで提出する権利があることを表します。GPG または SSH による暗号署名とは異なります。

## 上流と同期する

PR を作成する前に、ブランチを最新の `main` へ更新します。

```bash
git fetch upstream
git rebase upstream/main
```

競合を解決して関連チェックを再実行してから、自分のブランチを push します。

```bash
git push -u origin fix/short-description
```

すでに push 済みで、rebase によりリモート更新が必要な場合は、そのブランチを自分だけが使用していることを確認してから、安全な `--force-with-lease` を使用してください。共有ブランチを直接 force push しないでください。

## Pull Request を作成する

PR 作成時：

1. ベースリポジトリに `CherryHQ/cherry-studio` を選びます。
2. V2 と現在の開発変更では、base に `main` を選びます。
3. PR テンプレートに、変更前後、実装理由、トレードオフ、関連 Issue、Breaking Change、Release Note を記載します。
4. ユーザーに表示される変更にはスクリーンショットまたは画面録画を添付し、テストした OS と検証手順を記載します。
5. 必要な内容がすべて揃ってから Review を依頼します。

方向が未確定、または開発中の場合は、先に **Draft PR** を作成できます。Draft PR ではプロジェクト CI が実行されず、Review も自動的に割り当てられません。準備ができたら Ready for review に変更します。

新しいコントリビューターの非 Draft PR には、最初に `needs-ok-to-test` ラベルが付き、CI がすぐに始まらない場合があります。保守担当者が PR に `/ok-to-test` を追加すると、テストパイプラインが作成されます。これは通常のセキュリティ手順であり、PR を繰り返し閉じたり開き直したりする必要はありません。

## Review に対応する

コメントを受けたら：

1. 問題と期待される動作を 1 件ずつ確認します。
2. 元のブランチへ、小さく明確な追加変更をコミットします。
3. 影響するテストを再実行します。
4. 変更場所と検証結果を返信します。
5. 解決済みの議論は Reviewer に確認してもらいます。

「CI を緑にする」ために有効なテストを削除したり、型を緩めたり、安全確認を回避したりしないでください。失敗が現在の PR と無関係な場合は、ログと再現根拠を PR に記載し、保守担当者に判断を依頼します。

## よくある質問

### 依存関係をインストールしたらロックファイルが大幅に変わった

通常は Node.js または pnpm のバージョン不一致が原因です。意図せず作成したロックファイル変更を戻し、`.node-version` と `packageManager` に従って環境を準備し直してから、`corepack pnpm install` を実行します。

### Windows でスキルまたは同期ファイルに異常がある

クローン前に開発者モードと `core.symlinks=true` を有効にしたことを確認してください。リポジトリのシンボリックリンクが通常ファイルとしてチェックアウトされている場合は、有効化後に再クローンします。

### CI が始まらない

PR が Draft のままかを最初に確認します。新しいコントリビューターは `needs-ok-to-test` ラベルが付いているかも確認し、保守担当者が `/ok-to-test` を実行するまで待ちます。

### 新しい Issue が必要か分からない

小さく明確な Bug 修正は、説明に再現手順を記載して直接 PR を作成できます。大きな機能、インターフェース変更、複数の案がある変更は、先に Issue で合意を得ることを推奨します。

ドキュメントへのコントリビューションは[ドキュメントへのコントリビューション](docs.md)をお読みください。その他の質問は[フィードバックと提案](../question-contact/suggestions.md)からコミュニティへ連絡できます。
