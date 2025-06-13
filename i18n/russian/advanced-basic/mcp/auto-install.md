
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Автоматическая установка MCP

> Для автоматической установки MCP требуется обновить Cherry Studio до версии v1.1.18 или выше.

## Краткое описание функции

В дополнение к ручной установке, Cherry Studio включает встроенный инструмент `@mcpmarket/mcp-auto-install` - более удобный способ установки MCP-серверов. Вам достаточно ввести соответствующую команду в диалоге с поддерживающей MCP-услуги крупной языковой моделью.

{% hint style="warning" %}
**Напоминание о тестовой фазе:**

* `@mcpmarket/mcp-auto-install` в настоящее время находится на этапе тестирования
* Результат зависит от "интеллекта" языковой модели: некоторые функции добавляются автоматически, другие **требуют ручной корректировки параметров в настройках MCP**
* В текущей реализации поиск источников осуществляется через @modelcontextprotocol, но можно настроить собственные источники (описано ниже)
{% endhint %}

## Инструкция по использованию

Например, вы можете ввести:

```
帮我安装一个 filesystem mcp server
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Ввод команды для установки MCP-сервера</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Интерфейс настройки MCP-сервера</p></figcaption></figure>

Система автоматически распознает ваш запрос и выполнит установку через `@mcpmarket/mcp-auto-install`. Инструмент поддерживает различные типы MCP-серверов, включая:

* filesystem (файловая система)
* fetch (сетевые запросы)
* sqlite (база данных)
* и другие...

> Переменная MCP_PACKAGE_SCOPES позволяет настраивать источники поиска MCP-услуг. Значение по умолчанию: `@modelcontextprotocol`.

## Описание библиотеки `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Конфигурация по умолчанию:**

```json
// `axun-uUpaWEdMEMU8C61K` — это идентификатор сервиса, можно задать произвольно
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
    "MCP_REGISTRY_PATH": "Подробности см. на https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` — пакет с открытым исходным кодом на npm. Документацию и подробную информацию можно найти в [официальном репозитории npm](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` представляет официальную коллекцию MCP-услуг Cherry Studio.
{% endhint %}