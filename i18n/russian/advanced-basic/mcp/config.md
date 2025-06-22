
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Настройка и использование MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1.  Откройте настройки Cherry Studio.
2.  Найдите опцию `MCP 服务器`.
3.  Нажмите `添加服务器`.
4.  Заполните параметры MCP Server ([ссылка для справки](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Возможные поля для заполнения:
    *   Имя: произвольное имя, например `fetch-server`
    *   Тип: выберите `STDIO`
    *   Команда: введите `uvx`
    *   Параметры: введите `mcp-server-fetch`
    *   (могут быть другие параметры в зависимости от сервера)
5.  Нажмите `保存`.

{% hint style="success" %}
После настройки Cherry Studio автоматически скачает необходимый MCP Server - `fetch server`. После завершения загрузки можно начать использование! Примечание: при неудачной настройке mcp-server-fetch попробуйте перезагрузить компьютер.
{% endhint %}

### Активация службы MCP в чате

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt="Пример кнопки MCP в поле ввода"><figcaption></figcaption></figure>

*   Убедитесь, что сервер MCP успешно добавлен в настройках `MCP 服务器`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt="Пример настройки сервера MCP"><figcaption></figcaption></figure>

### **Демонстрация работы**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Как показано выше, благодаря функции `fetch` MCP, Cherry Studio лучше понимает запросы пользователей, находит релевантную информацию в сети и предоставляет более точные и полные ответы.