---
icon: list
---

# Краткий справочник по всем провайдерам моделей

На этой странице перечислены встроенные шаблоны провайдеров моделей, доступные в текущей версии Cherry Studio V2. Таблица позволяет проверить название провайдера, предварительно настроенные API и ссылку для получения учётных данных. Список обновляется вместе с приложением. Если данные на странице отличаются от клиента, ориентируйтесь на фактическое содержимое раздела `Настройки → Провайдеры моделей → Все поставщики`.

{% hint style="info" %}
Под «API» здесь понимается способ подключения, предварительно настроенный Cherry Studio для соответствующего шаблона. Это не означает, что каждая модель в нём поддерживает одинаковые возможности. Поддержку зрения, рассуждений и вызова инструментов проверяйте по описанию модели у провайдера и с помощью практического теста.
{% endhint %}

## Как пользоваться таблицей

1. Найдите ниже провайдера, у которого уже есть ваша учётная запись или которого вы планируете подключить.
2. Откройте **Ссылку для получения учётных данных** и создайте API Key или учётные данные облачной платформы согласно требованиям провайдера.
3. Вернитесь в раздел Cherry Studio `Настройки → Провайдеры моделей`, переключите фильтр слева на **Все поставщики** и выберите провайдера с тем же названием.
4. Выполните аутентификацию, получите список моделей, включите нужные модели и проверьте подключение по инструкции [Провайдеры моделей](README.md).

Если провайдера нет в списке, но он предоставляет совместимый API, используйте [Пользовательского провайдера](zi-ding-yi-fu-wu-shang.md).

## Обозначения API

| Сокращение на этой странице | Соответствующий API |
|---|---|
| OpenAI Chat | OpenAI Chat Completions |
| OpenAI Responses | OpenAI Responses |
| Anthropic | Anthropic Messages |
| Gemini | Google Generate Content |
| Ollama | Ollama Chat |
| Специализированное подключение | Cherry Studio использует аутентификацию и маршрутизацию, предназначенные для этой облачной платформы или службы |

Фильтр **Agent** в списке слева показывает провайдеров с совместимой конечной точкой Anthropic. Это фильтр по способу подключения, который не гарантирует, что все модели поддерживают вызов инструментов.

## Шаблоны с несколькими API

В этих шаблонах предварительно настроены два API. Для разных моделей одного провайдера можно выбрать подходящий способ подключения.

| Provider | Предварительно настроенные API | Ссылка для получения учётных данных | Руководство |
|---|---|---|---|
| CherryIN | Anthropic, OpenAI Chat | [Получить данные](https://open.cherryin.ai/console/token) | [Настройка](cherryin-1.md) |
| Silicon | Anthropic, OpenAI Chat | [Получить данные](https://cloud.siliconflow.cn/) | [Настройка](siliconcloud.md) |
| AiHubMix | Anthropic, OpenAI Chat | [Получить данные](https://aihubmix.com) | — |
| ZhiPu | Anthropic, OpenAI Chat | [Получить данные](https://open.bigmodel.cn/usercenter/apikeys) | — |
| deepseek | Anthropic, OpenAI Chat | [Получить данные](https://platform.deepseek.com/api_keys) | [Настройка](deepseek.md) |
| DMXAPI | Anthropic, OpenAI Chat | [Получить данные](https://www.dmxapi.cn/) | — |
| TokenFlux | Anthropic, OpenAI Chat | [Получить данные](https://api.tokenflux.ai/dashboard/api-keys) | — |
| 302.AI | Anthropic, OpenAI Chat | [Получить данные](https://dash.302.ai/apis/list) | — |
| Qiniu | Anthropic, OpenAI Chat | [Получить данные](https://portal.qiniu.com/ai-inference/api-key) | — |
| OpenRouter | Anthropic, OpenAI Chat | [Получить данные](https://openrouter.ai/settings/keys) | [Настройка](openrouter.md) |
| Ollama | Anthropic, Ollama | [Официальный сайт](https://ollama.com/) | [Настройка](ollama.md) |
| New API | Anthropic, OpenAI Chat | [Документация](https://docs.newapi.pro/) | [Настройка](newapi.md) |
| LM Studio | Anthropic, OpenAI Chat | [Официальный сайт](https://lmstudio.ai/) | [Настройка](lm-studio.md) |
| Moonshot AI | Anthropic, OpenAI Chat | [Получить данные](https://platform.moonshot.cn/console/api-keys) | [Настройка](moonshot.md) |
| Bailian | Anthropic, OpenAI Chat | [Получить данные](https://bailian.console.aliyun.com/?tab=model#/api-key) | [Настройка](a-li-yun-bai-lian.md) |
| MiniMax | Anthropic, OpenAI Chat | [Получить данные](https://platform.minimaxi.com/user-center/basic-information/interface-key) | [Настройка](minimax.md) |
| ModelScope | Anthropic, OpenAI Chat | [Получить данные](https://modelscope.cn/my/myaccesstoken) | [Настройка](modelscope.md) |
| LongCat | Anthropic, OpenAI Chat | [Получить данные](https://longcat.chat/platform/api_keys) | — |
| Xiaomi MiMo | Anthropic, OpenAI Chat | [Получить данные](https://platform.xiaomimimo.com/#/console/usage) | — |
| zai | Anthropic, OpenAI Chat | [Получить данные](https://z.ai/manage-apikey/apikey-list) | — |
| minimax-global | Anthropic, OpenAI Chat | [Получить данные](https://platform.minimax.io/user-center/basic-information/interface-key) | — |

## Шаблоны с одним API

| Provider | Предварительно настроенный API | Ссылка для получения учётных данных | Руководство |
|---|---|---|---|
| OpenVINO Model Server | OpenAI Chat | [Официальный сайт](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html) | — |
| ocoolAI | OpenAI Chat | [Получить данные](https://one.ocoolai.com/token) | — |
| AlayaNew | OpenAI Chat | [Официальный сайт](https://www.alayanew.com/) | — |
| AIOnly | OpenAI Chat | [Получить данные](https://maas.aiionly.com/keyApi) | — |
| BurnCloud | OpenAI Chat | [Получить данные](https://ai.burncloud.com/token) | — |
| Cephalon | OpenAI Chat | [Получить данные](https://cephalon.cloud/api) | — |
| LANYUN | OpenAI Chat | [Получить данные](https://maas.lanyun.net/#/system/apiKey) | — |
| PH8 | OpenAI Chat | [Получить данные](https://ph8.co/apiKey) | — |
| SophNet | OpenAI Chat | [Получить данные](https://sophnet.com/#/project/key) | — |
| PPIO | OpenAI Chat | [Получить данные](https://ppio.com/settings/key-management) | [Настройка](ppio.md) |
| Anthropic | Anthropic | [Получить данные](https://console.anthropic.com/settings/keys) | [Настройка](anthropic.md) |
| OpenAI | OpenAI Responses | [Получить данные](https://platform.openai.com/api-keys) | [Настройка](openai.md) |
| Gemini | Gemini | [Получить данные](https://aistudio.google.com/app/apikey) | [Настройка](google-gemini.md) |
| Github Models | OpenAI Chat | [Получить данные](https://github.com/settings/tokens) | — |
| Github Copilot | OpenAI Chat | [Официальный сайт](https://github.com/features/copilot) | [Настройка](github-copilot.md) |
| Yi | OpenAI Chat | [Получить данные](https://platform.lingyiwanwu.com/apikeys) | — |
| BAICHUAN AI | OpenAI Chat | [Получить данные](https://platform.baichuan-ai.com/console/apikey) | — |
| StepFun | OpenAI Chat | [Получить данные](https://platform.stepfun.com/interface-key) | — |
| doubao | OpenAI Chat | [Консоль](https://www.volcengine.com/experience/ark) | [Настройка](doubao.md) |
| Infini | OpenAI Chat | [Получить данные](https://cloud.infini-ai.com/iam/secret/key) | — |
| Groq | OpenAI Chat | [Получить данные](https://console.groq.com/keys) | [Настройка](groq.md) |
| Together | OpenAI Chat | [Получить данные](https://api.together.ai/settings/api-keys) | — |
| Fireworks | OpenAI Chat | [Получить данные](https://fireworks.ai/account/api-keys) | — |
| nvidia | OpenAI Chat | [Консоль](https://build.nvidia.com/explore/discover) | — |
| Grok | OpenAI Chat | [Официальный сайт](https://x.ai/) | [Настройка](grok.md) |
| Hyperbolic | OpenAI Chat | [Получить данные](https://app.hyperbolic.xyz/settings) | — |
| Mistral | OpenAI Chat | [Получить данные](https://console.mistral.ai/api-keys/) | — |
| Jina | OpenAI Chat | [Официальный сайт](https://jina.ai) | — |
| Perplexity | OpenAI Chat | [Получить данные](https://www.perplexity.ai/settings/api) | — |
| Xirang | OpenAI Chat | [Консоль](https://huiju.ctyun.cn/service/serviceGroup) | — |
| hunyuan | OpenAI Chat | [Получить данные](https://console.cloud.tencent.com/hunyuan/api-key) | — |
| Tencent Cloud TI | OpenAI Chat | [Получить данные](https://console.cloud.tencent.com/lkeap/api) | — |
| Baidu Cloud | OpenAI Chat | [Получить данные](https://console.bce.baidu.com/iam/#/iam/apikey/list) | — |
| VoyageAI | OpenAI Chat | [Получить данные](https://dashboard.voyageai.com/organization/api-keys) | — |
| Poe | OpenAI Chat | [Получить данные](https://poe.com/api/keys) | — |
| Hugging Face | OpenAI Responses | [Получить данные](https://huggingface.co/settings/tokens) | — |
| Vercel AI Gateway | OpenAI Chat | [Официальный сайт](https://vercel.com/) | — |
| Cerebras AI | OpenAI Chat | [Консоль](https://cloud.cerebras.ai) | — |

## Шаблоны специализированного подключения

Эти варианты не сводятся к обычному сочетанию API Key и Base URL. Подготовьте данные соответствующей облачной платформы для полей на странице.

| Provider | Способ аутентификации или подключения | Ссылка для получения учётных данных | Руководство |
|---|---|---|---|
| Azure OpenAI | Учётные данные Azure, API Version и сведения о развёртывании | [Azure Portal](https://portal.azure.com/) | [Настройка](azure-openai.md) |
| VertexAI | Проект, регион и учётные данные Google Cloud | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) | [Настройка](vertex-ai.md) |
| GPUStack | Адрес службы GPUStack и учётные данные | [Официальный сайт](https://gpustack.ai/) | — |
| AWS Bedrock | Регион AWS и IAM или Bedrock API Key | [Документация IAM](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html) | — |

{% hint style="warning" %}
Провайдеры могут изменять адреса регистрации, права на модели, региональные ограничения и правила оплаты. Перед созданием учётных данных ознакомьтесь с актуальной информацией платформы. Cherry Studio только обеспечивает подключение и не предоставляет учётные записи или квоты от имени провайдера.
{% endhint %}

## Нужной службы нет в списке

- Собственный New API: используйте шаблон [New API](newapi.md).
- Собственный One API или другой совместимый шлюз: см. [OneAPI](oneapi.md) или [Пользовательского провайдера](zi-ding-yi-fu-wu-shang.md).
- Есть только совместимый адрес OpenAI, Anthropic, Gemini или OpenAI Responses: создайте [Пользовательского провайдера](zi-ding-yi-fu-wu-shang.md) и укажите соответствующую конечную точку.

Если шаблон с нужным названием есть, но адрес вашего развёртывания отличается от значения по умолчанию, скопируйте этого провайдера, а затем измените адрес и настройки аутентификации в копии.

При возникновении проблемы сначала проверьте переключатель провайдера, переключатель модели, API Key, Base URL и тип API по разделу [Провайдеры моделей](README.md#частые-вопросы).
