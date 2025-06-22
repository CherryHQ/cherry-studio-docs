
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Автоматическая установка MCP

> Для автоматической установки MCP требуется обновление Cherry Studio до версии v1.1.18 или выше.

## Обзор возможностей

Помимо ручной установки, Cherry Studio включает инструмент `@mcpmarket/mcp-auto-install` — более простой способ установки сервера MCP. Для использования достаточно ввести соответствующую команду в диалоге с LLM-моделью, поддерживающей сервисы MCP.

{% hint style="warning" %}
**Важно на этапе тестирования:**

* `@mcpmarket/mcp-auto-install` находится в бета-версии
* Результат зависит от «интеллекта» LLM-модели: параметры могут добавляться автоматически, но **в некоторых случаях потребуется ручная настройка параметров MCP**
* Поиск источников выполняется в `@modelcontextprotocol`, но можно настроить кастомные параметры (см. ниже)
{% endhint %}

## Инструкция по использованию

Например, введите команду:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Ввод команды для установки сервера MCP</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Интерфейс конфигурации сервера MCP</p></figcaption></figure>

Система автоматически определит требования и выполнит установку через `@mcpmarket/mcp-auto-install`. Инструмент поддерживает различные типы серверов MCP, включая:

* filesystem (файловая система)
* fetch (HTTP-запросы)
* sqlite (база данных)
* и другие...

> Переменная MCP_PACKAGE_SCOPES позволяет кастомизировать источники поиска сервисов MCP. Значение по умолчанию: `@modelcontextprotocol`.

## Описание библиотеки `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Конфигурация по умолчанию:**

```json
// `axun-uUpaWEdMEMU8C61K` - пользовательский ID сервиса
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Automatically install MCP services (Beta version)",
  "isActive": false,
  "registryUrl": "https://registry.npmmirror.com",
  "command": "npx",
  "args": [
    "-y",
    "@mcpmarket/mcp-auto-install",
    "connect",
    "--json"
  ],
  "env": {
    "MCP_REGISTRY_PATH": "详情见https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` — npm-пакет с открытым исходным кодом. Подробную документацию можно найти в [официальном репозитории npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` — официальная коллекция сервисов MCP от Cherry Studio.
{% endhint %}