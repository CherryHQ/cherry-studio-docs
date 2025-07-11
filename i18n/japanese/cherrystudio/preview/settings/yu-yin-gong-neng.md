---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}

# 音声機能

```
Cherry Studio 音声機能の使い方

## 一、音声機能の概要

Cherry Studio は三大音声機能モジュールを提供しています：TTS（テキスト音声変換）、ASR（音声認識）、音声通話。これらの機能により、音声を通じてAIと自然に対話でき、使用体験が向上します。

- **TTS（テキスト音声変換）**: AIの返答テキストを音声に変換
- **ASR（音声認識）**: ユーザーの音声をテキストに変換
- **音声通話**: TTSとASRを組み合わせ、ChatGPTのような音声対話体験を実現

## 二、TTS（テキスト音声変換）機能

### 1. 対応サービス

Cherry Studio は4種類のTTSサービスに対応：

- **OpenAI**: OpenAIのTTS APIを使用（APIキー必須）
- **ブラウザTTS**: ブラウザ組み込み音声合成（無料・設定不要）
- **硅基流动 (Siliconflow)**: SiliconflowのTTSサービス（APIキー必須）
- **無料オンラインTTS**: 無料TTSサービス（APIキー不要）

### 2. 設定方法

1) 設定ページで「音声機能」タブを選択
2) 「TTS」サブタブで：
   - TTS機能を有効化（スイッチON）
   - TTSサービスを選択
   - 選択したサービスに応じた設定：
     - OpenAI: APIキー、APIアドレス、音声タイプ、モデル
     - ブラウザTTS: 音声タイプ
     - Siliconflow: APIキー、APIアドレス、音声タイプ、モデル、応答形式、話速
     - 無料オンラインTTS: 音声タイプ、出力形式
3) TTSフィルター設定（任意）：
   - 思考プロセスの除外
   - Markdown記号の除外
   - コードブロックの除外
4) TTS進行バーの表示設定
5) 「TTSテスト」ボタンで設定を確認

### 3. 使用方法

- TTS有効時、AI返答は自動音声化
- チャット画面で各AI返答下に再生ボタン表示
- ボタンクリックで再生/一時停止
- TTS進行バー有効時はテキスト下に表示
- 長文は自動分割・連続再生

## 三、ASR（音声認識）機能

### 1. 対応サービス

3種類のASRサービスに対応：

- **OpenAI**: OpenAIのWhisperモデル（APIキー必須）
- **ブラウザ**: ブラウザ組み込み音声認識（無料・設定不要）
- **ローカルサーバー**: ローカルWebSocketサーバー接続

### 2. 設定方法

1) 設定ページで「音声機能」タブ選択
2) 「ASR」サブタブで：
   - ASR機能有効化（スイッチON）
   - ASRサービス選択
   - サービスに応じた設定：
     - OpenAI: APIキー、APIアドレス、モデル
     - ブラウザ: 追加設定不要
     - ローカルサーバー: 起動時自動起動設定
   - 音声認識言語選択（デフォルト: 中国語）
3) 「ASRテスト」ボタンで設定確認

### 3. 使用方法

- ASR有効時、入力欄横に音声認識ボタン表示
- ボタンクリックで録音開始
- 音声がテキスト変換され入力欄に表示
- 再度クリックで録音終了
- 複数発話の連続認識（累積モード）

## 四、音声通話機能

### 1. 特徴

- TTSとASR連動のChatGPT風対話体験
- ドラッグ可能フローティングウィンドウ
- 長押し発話モード対応
- カスタムショートカット対応
- ウィンドウ折りたたみ機能
- 専用通話モデル選択可能
- カスタムプロンプト対応

### 2. 設定方法

1) 設定ページで「音声機能」タブ選択
2) 「通話機能」サブタブで：
   - 音声通話機能を有効化
   - 「モデル選択」で通話専用AIモデル指定
   - プロンプトテキスト欄でカスタム設定（任意）
   - 「保存」で設定保存／「リセット」でデフォルト復元

### 3. 使用方法

1) チャット画面入力欄右の通話ボタン（電話アイコン）クリック
2) 通話ウィンドウ起動・歓迎音声再生
3) 「長押し発話」ボタン長押しで録音開始（ショートカット可）
4) ボタン離すと録音終了・AI処理開始
5) AI返答をTTSで再生
6) ウィンドウ操作ボタン：
   - ミュート/解除: TTS制御
   - 一時停止/再開: 対話制御
   - 設定: ショートカット設定
   - 折りたたみ: 最小化表示
7) 閉じるボタンで通話終了

### 4. ショートカット設定

1) 通話ウィンドウで設定ボタンクリック
2) 設定パネルで「ショートカット」選択
3) 設定したいキー押下（例: スペース, Shift）
4) 「保存」ボタンで設定確定
5) 使用時: ショートカット長押しで録音開始→離すと送信

## 五、よくある問題と解決法

### 1. TTS関連問題

- **問題**: 音声再生不可
  **解決法**: TTS有効化確認・サービス設定見直し

- **問題**: 再生品質低下
  **解決法**: サービス/音声タイプ変更

- **問題**: エラー表示
  **解決法**: APIキー・ネットワーク接続確認

### 2. ASR関連問題

- **問題**: 音声認識不可
  **解決法**: ASR有効化確認・設定見直し

- **問題**: 認識精度低下
  **解決法**: サービス変更・マイク位置調整

- **問題**: サーバー接続失敗
  **解決法**: ローカルサーバー稼働確認・アプリ再起動

### 3. 音声通話関連問題

- **問題**: 通話ウィンドウ起動不可
  **解決法**: 通話機能有効化・TTS/ASR設定確認

- **問題**: 長押し発話反応なし
  **解決法**: マイク権限確認・通話再起動

- **問題**: AI返答音声なし
  **解決法**: TTS有効化・ミュート状態確認

## 六、高度設定とカスタムオプション

### 1. TTS高度設定

- フィルター設定: 思考/Markdown/コード除去で再生を最適化
- 進行バー表示設定
- カスタム音声/モデル追加

### 2. ASR高度設定

- 自動起動設定: アプリ起動時サーバー自動起動設定
- 言語選択: 音声認識言語変更

### 3. 音声通話高度設定

- カスタムプロンプト: 通話時AI挙動の指示設定
- 専用モデル選択: 通常チャットと別モデル設定
- ショートカットカスタム: 録音操作キー変更

## 七、使用のヒント

1. **TTSサービス選択**:
   - 高音質優先: OpenAI/Siliconflow
   - API設定回避: ブラウザTTS/無料オンラインTTS

2. **ASRサービス選択**:
   - 高精度優先: OpenAI
   - API設定回避: ブラウザ機能

3. **通話体験最適化**:
   - イヤホン使用でエコー防止
   - 静かな環境で認識精度向上
   - カスタムプロンプトで音声再生向け調整

4. **用途別設定の使い分け**:
   - テキストメイン利用: TTSのみ有効
   - 音声入力メイン: ASRのみ有効
   - 完全音声対話: 通話機能有効

本ガイドがCherry Studioの音声機能活用に役立ち、自然で快適なAI対話体験をお楽しみいただければ幸いです！
```