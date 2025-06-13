
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Настройка и использование MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Откройте настройки Cherry Studio.
2. Найдите опцию `MCP сервер`.
3. Нажмите `Добавить сервер`.
4. Заполните параметры MCP Server ([ссылка для справки](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Может потребоваться указать:
   * Имя: произвольное название, например `fetch-server`
   * Тип: выберите `STDIO`
   * Команда: введите `uvx`
   * Параметры: введите `mcp-server-fetch`
   * (могут быть другие параметры в зависимости от конкретного сервера)
5. Нажмите `Сохранить`.

{% hint style="success" %}
После настройки Cherry Studio автоматически загрузит необходимый MCP Server - `fetch server`. После завершения загрузки можно начинать использование! Примечание: если mcp-server-fetch не настраивается успешно, попробуйте перезагрузить компьютер.
{% endhint %}

### Включение службы MCP в окне чата

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* После успешного добавления MCP сервера в настройках `MCP сервер`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Демонстрация эффекта использования**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Как видно из изображения выше, при использовании функции `fetch` в MCP Cherry Studio лучше понимает намерения пользовательских запросов. Она получает релевантную информацию из сети и предоставляет более точные и полные ответы.