# Установка среды MCP


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




**MCP (Model Context Protocol)** — это открытый протокол, предназначенный для стандартизированной передачи контекстной информации крупным языковым моделям (LLM). Подробнее о MCP см. в разделе [#что-такое-mcpmodel-context-protocol](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Использование MCP в Cherry Studio

Ниже на примере функции `fetch` показано, как применять MCP в Cherry Studio. Подробную информацию можно найти в [документации](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Подготовка: установка uv и bun**

{% hint style="warning" %}
Cherry Studio в настоящее время использует только встроенные [uv](https://github.com/astral-sh/uv) и [bun](https://github.com/oven-sh/bun) и **не переиспользует** уже установленные в системе uv и bun.
{% endhint %}

В разделе `Настройки → MCP-сервер` нажмите кнопку `Установить`, чтобы автоматически загрузить и установить компоненты. Так как загрузка происходит напрямую с GitHub, скорость может быть низкой, и возможны сбои. Успешность установки проверяйте по наличию файлов в папках, указанных ниже.

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Директория установки исполняемых файлов:**

Windows: `C:\Users\Имя_пользователя\.cherrystudio\bin`

macOS/Linux: `~/.cherrystudio/bin`

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Директория bin</p></figcaption></figure>

**При проблемах с установкой:**

Вы можете создать символические ссылки на системные команды в указанных директориях (если директории отсутствуют — создайте вручную). Также исполняемые файлы можно загрузить вручную:

Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)\
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)