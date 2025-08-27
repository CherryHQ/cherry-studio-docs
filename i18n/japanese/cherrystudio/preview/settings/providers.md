---
icon: cloud-check
---

{% hint style="warning" %}
このドキュメントはAIによって中国語から翻訳されており、まだレビューされていません。
{% endhint %}


<think>
We are translating Chinese to Japanese while strictly preserving Markdown structure and technical terms.
 Rules:
 1. Translate only textual content for display, keeping all Markdown syntax intact.
 2. Preserve code blocks, links, image paths, and special tags (like {% hint %}) exactly as is, but translate the text inside them.
 3. Do not translate URLs, file paths, version numbers, or code (except comments within code blocks, but here we have code examples without comments to translate, so we leave the code as is).
 4. For the hint blocks, translate the content but keep the tags and style attributes.
 5. Note: In this document, there are code blocks and example keys (like "sk-xxxx1") that should not be translated.
 6. Also, note the image paths and the example URL format must remain unchanged.

 Let's break down the translation step by step.

 Step 1: Translate the heading "# 模型服务设置" -> "# モデルサービスの設定"

 Step 2: Translate the first paragraph:
 "当前页面仅做界面功能的介绍，配置教程可以参考基础教程中的 [服务商配置](../../../pre-basic/providers/) 教程。"
 -> "このページはインターフェース機能の紹介のみを行います。設定のチュートリアルについては、基本チュートリアルの[サービスプロバイダー設定](../../../pre-basic/providers/)を参照してください。"

 Step 3: Translate the info hint block (style="info"):
 Content:
   - "在使用内置服务商时只需要填写对应的秘钥即可。"
        -> "ビルトインサービスプロバイダーを使用する場合は、対応するシークレットキーを入力するだけで済みます。"
   - "不同服务商对秘钥的叫法可能有所不同，秘钥、Key、API Key、令牌等都指的是同一个东西。"
        -> "サービスプロバイダーによってシークレットキーの呼び方が異なる場合があり、シークレットキー、Key、API Key、トークンなどはすべて同じものを指します。"

 Step 4: Translate the subheading "### API 秘钥" -> "### API シークレットキー"

 Step 5: Translate the paragraph about multi-key usage:
 "在 Cherry Studio 当中，单个服务商支持多 Key 轮询使用，轮询方式为从前到后列表循环的方式。"
 -> "Cherry Studioでは、単一のサービスプロバイダーで複数のキーをローテーション方式で使用することがサポートされています。ローテーション方式は、リストを先頭から末尾まで循環する方法です。"

 Step 6: Translate the bullet point:
 "* 多 Key 用英文逗号隔开添加。如以下示例方式："
 -> "* 複数のキーは英語のカンマで区切って追加します。以下の例のように："

 Step 7: The code block must be preserved exactly, including the strong tag. We don't translate the code:
 <pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4</strong></code></pre>

 Step 8: Translate the warning hint block (style="warning"):
 "必须使用 **英文** 逗号。"
 -> "必ず **英語** のカンマを使用してください。"

 Step 9: Translate the next subheading "### API 地址" -> "### API アドレス"

 Step 10: Translate the paragraph about API address:
 "在使用内置服务商时一般不需要填写 API 地址，如果需要修改请严格按照对应的官方文档给的地址填写。"
 -> "ビルトインサービスプロバイダーを使用する場合、通常はAPIアドレスを入力する必要はありません。変更する必要がある場合は、対応する公式ドキュメントで提供されているアドレスを厳密に守って入力してください。"

 Step 11: Translate the blockquote (note the mark tags for coloring, which we preserve, but translate the text inside):
 "如果服务商给的地址为 <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> 这种格式，只需要填写根地址部分（<mark style="background-color:red;">https://xxx.xxx.com</mark>）即可。

 Cherry Studio 会自动拼接剩余的路径（<mark style="background-color:green;">/v1/chat/completions</mark>），未按要求填写可能会导致无法正常使用。"

 Translation:
 > サービスプロバイダーが提供するアドレスが <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark> という形式の場合、ルートアドレス部分（<mark style="background-color:red;">https://xxx.xxx.com</mark>）のみを入力してください。
 >
 > Cherry Studio は自動的に残りのパス（<mark style="background-color:green;">/v1/chat/completions</mark>）を連結します。要求に従って入力しないと、正常に使用できない可能性があります。

 Step 12: Translate the next info hint block (style="info"):
 Content:
   - The entire paragraph: "说明：大多数服务商的大语言模型路由是统一的，一般情况下不需要进行如下操作。如果服务商的API路径是v2、v3/chat/completions或者其他版本时,可在地址栏手动输入对应版本以'`/`'结尾；当服务商请求路由不是常规的<mark style="background-color:green;">/v1/chat/completions</mark>时使用服务商提供的完整的地址，并以 `#`结尾。"
        -> "説明: ほとんどのサービスプロバイダーの大規模言語モデルのルーティングは統一されており、通常は以下の操作は必要ありません。サービスプロバイダーのAPIパスがv2、v3/chat/completions、またはその他のバージョンの場合、アドレスバーに該当するバージョンを手動で入力し、末尾を「`/」で終わるようにします。サービスプロバイダーのリクエストルートが通常の<mark style="background-color:green;">/v1/chat/completions</mark>でない場合は、サービスプロバイダーが提供する完全なアドレスを使用し、末尾を「`#」で終わらせます。"
   - The bullet points (which are two points in one line? Actually, the original has two separate points, but in the hint block it's written as a paragraph with a list. We'll break it into two points for clarity, but note the original structure is two lines starting with "*" and "-". However, in the original, it's written as:
        "即：
         * API地址使用 `/` 结尾时只拼接\"<mark style="background-color:green;">chat/completions</mark>\"
         * API地址使用 `#` 结尾时不执行拼接操作，只使用填入的地址。"

        We'll translate as:
        "すなわち：
         * APIアドレスが「`/`」で終わる場合、\"<mark style="background-color:green;">chat/completions</mark>\"のみを連結します。
         * APIアドレスが「`#`」で終わる場合、連結操作は行われず、入力されたアドレスのみを使用します。"

   - Then there are two images. The image paths must remain unchanged.

 Step 13: Translate the next subheading "### 添加模型" -> "### モデルの追加"

 Step 14: Translate the paragraph about adding models:
 "一般情况下点击服务商配置页面最左下角的 `管理` 按钮会自动获取该服务商所有支持调用的模型，从获取列表中点击 `+` 号添加到模型列表即可。"
 -> "通常、サービスプロバイダー設定ページの左下にある `管理` ボタンをクリックすると、そのサービスプロバイダーがサポートするすべての呼び出し可能なモデルが自動的に取得されます。取得したリストから `+` をクリックしてモデルリストに追加します。"

 Step 15: Translate the info hint block (style="info"):
 "点击管理按钮时弹窗列表里的模型不会全部添加，需要点击模型右侧的 `+` ，添加到服务商配置页面的模型列表才可以在模型选择列表当中出现。"
 -> "管理ボタンをクリックしたときに表示されるポップアップリストのモデルはすべて追加されません。モデル右側の `+` をクリックして、サービスプロバイダー設定ページのモデルリストに追加する必要があります。そうすることで、モデル選択リストに表示されます。"

 Step 16: Translate the next subheading "### 连通性检查" -> "### 接続性チェック"

 Step 17: Translate the paragraph about connectivity check:
 "点击API 秘钥输入框后的检查按钮即可测试是否成功配置。"
 -> "APIシークレットキー入力ボックスの後にあるチェックボタンをクリックすると、設定が成功したかどうかをテストできます。"

 Step 18: Translate the next info hint block (style="info"):
 "模型检查时默认使用模型列表已添加模型的最后一个对话模型，如果检查时有失败的情况请检查模型列表是否有错误的或不被支持的模型。"
 -> "モデルチェックでは、デフォルトでモデルリストに追加された最後の対話モデルが使用されます。チェック中に失敗