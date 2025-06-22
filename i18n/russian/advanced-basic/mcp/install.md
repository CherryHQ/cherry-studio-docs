
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Установка окружения MCP

**MCP (Model Context Protocol)** — это открытый протокол, предназначенный для стандартизированной передачи контекстной информации крупным языковым моделям (LLM). Подробнее о MCP см. в разделе [#что-такое-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Использование MCP в Cherry Studio

Ниже на примере функции `fetch` показано, как использовать MCP в Cherry Studio. Подробности можно найти в [документации](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Подготовка: установка uv и bun**

{% hint style="warning" %}
Cherry Studio использует только встроенные [uv](https://github.com/astral-sh/uv) и [bun](https://github.com/oven-sh/bun), **не переиспользуя** системные версии этих инструментов.
{% endhint %}

В разделе `Настройки → MCP-сервер` нажмите кнопку `Установить`, чтобы автоматически загрузить и установить компоненты. Поскольку загрузка идёт напрямую с GitHub, скорость может быть низкой с высокой вероятностью сбоев. Успешность установки определяется наличием файлов в папках, указанных ниже.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Каталоги установки исполняемых файлов:**

Windows: `C:\Users\Имя_пользователя\.cherrystudio\bin`

macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Каталог bin</p></figcaption></figure>

**При проблемах с установкой:**

1. Создайте символические ссылки на системные исполняемые файлы в указанных каталогах. При отсутствии каталогов — создайте их вручную.
2. Либо загрузите файлы вручную:
   - Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)
   - UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)  
   и разместите исполняемые файлы в соответствующем каталоге.