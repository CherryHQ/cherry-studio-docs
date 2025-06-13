
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Автоматическая установка MCP

> Для автоматической установки MCP требуется обновить Cherry Studio до версии v1.1.18 или выше.

## Описание функции

Помимо ручной установки, Cherry Studio включает встроенный инструмент `@mcpmarket/mcp-auto-install` — более удобный способ установки сервера MCP. Просто введите соответствующую команду в диалоге с крупной языковой моделью, поддерживающей MCP сервисы.

{% hint style="warning" %}
**Напоминание о тестовом режиме:**

* `@mcpmarket/mcp-auto-install` пока находится в бета-тестировании
* Эффективность зависит от "интеллекта" модели: некоторые автоматически добавляют настройки, но в некоторых случаях **требуется ручное изменение параметров в настройках MCP**
* В настоящее время поиск источников производится в @modelcontextprotocol, но можно настроить самостоятельно (см. ниже)
{% endhint %}

## Инструкция по использованию

Например, вы можете ввести:

```
помоги установить filesystem mcp сервер
```

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot1.png" alt=""><figcaption><p>Ввод команды для установки MCP сервера</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-auto-install_shot2.png" alt=""><figcaption><p>Интерфейс настройки MCP сервера</p></figcaption></figure>

Система автоматически распознает ваш запрос и завершит установку через `@mcpmarket/mcp-auto-install`. Инструмент поддерживает различные типы MCP серверов, включая:

* filesystem (файловая система)
* fetch (сетевые запросы)
* sqlite (база данных)
* и другие...

> Переменная MCP_PACKAGE_SCOPES позволяет настраивать источники поиска MCP сервисов. Значение по умолчанию: `@modelcontextprotocol`.

## О библиотеке `@mcpmarket/mcp-auto-install`

{% hint style="info" %}
**Базовая конфигурация:**
```json
// `axun-uUpaWEdMEMU8C61K` — идентификатор сервиса, можно указать любой
"axun-uUpaWEdMEMU8C61K": {
  "name": "mcp-auto-install",
  "description": "Автоматическая установка MCP сервисов (бета-версия)",
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
    "MCP_REGISTRY_PATH": "Подробнее на https://www.npmjs.com/package/@mcpmarket/mcp-auto-install"
  },
  "disabledTools": []
}
```

`@mcpmarket/mcp-auto-install` — npm пакет с открытым исходным кодом. Подробная информация и документация доступны в [официальном npm репозитории](https://www.npmjs.com/package/@mcpmarket/mcp-auto-install). `@mcpmarket` — официальная коллекция MCP сервисов Cherry Studio.
{% endhint %}