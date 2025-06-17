
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Установка среды MCP

**MCP (Model Context Protocol)** — это открытый протокол, предназначенный для предоставления контекстной информации крупным языковым моделям (LLM) стандартизированным способом. Подробнее о MCP см. в разделе [#что-такое-mcp](../../question-contact/knowledge.md#shen-me-shi-mcpmodel-context-protocol "mention")

## Использование MCP в Cherry Studio

Ниже на примере функции `fetch` показано, как использовать MCP в Cherry Studio. Подробности можно найти в [документации](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch).

### **Подготовка: установка uv и bun**

{% hint style="warning" %}
Cherry Studio в настоящее время использует только встроенные [uv](https://github.com/astral-sh/uv) и [bun](https://github.com/oven-sh/bun) и **не переиспользует** uv/bun, установленные в системе.
{% endhint %}

В разделе `Настройки → Сервер MCP` нажмите кнопку `Установить`, чтобы автоматически загрузить и установить компоненты. Поскольку загрузка выполняется напрямую с GitHub, процесс может быть медленным и часто завершается сбоем. Успешность установки определяется наличием файлов в папке, упомянутой ниже.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**Каталог установки исполняемых файлов:**  

Windows: `C:\Users\Имя_пользователя\.cherrystudio\bin`  

macOS/Linux: `~/.cherrystudio/bin`  

<figure><img src="../../.gitbook/assets/MCP-cherrystudio_bin_文件夹.png" alt=""><figcaption><p>Каталог bin</p></figcaption></figure>

**Если установка не выполняется:**  
1. Создайте символическую ссылку на соответствующие системные команды в этом каталоге (при отсутствии директории создайте её вручную).  
2. Или загрузите исполняемые файлы вручную:  
Bun: [https://github.com/oven-sh/bun/releases](https://github.com/oven-sh/bun/releases)  
UV: [https://github.com/astral-sh/uv/releases](https://github.com/astral-sh/uv/releases)