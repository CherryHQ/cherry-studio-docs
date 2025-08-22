# Настройка и использование MCP


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Откройте настройки Cherry Studio.
2. Найдите опцию `MCP сервер`.
3. Нажмите `Добавить сервер`.
4. Заполните параметры MCP Server ([ссылка на документацию](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Могут потребоваться следующие данные:
   * Название: произвольное имя, например `fetch-server`
   * Тип: выберите `STDIO`
   * Команда: введите `uvx`
   * Аргументы: введите `mcp-server-fetch`
   * (возможны другие параметры в зависимости от сервера)
5. Нажмите `Сохранить`.

{% hint style="success" %}
После настройки Cherry Studio автоматически загрузит необходимый MCP Server - `fetch server`. После завершения загрузки можно начинать работу! Примечание: если mcp-server-fetch не работает, попробуйте перезагрузить компьютер.
{% endhint %}

### Активация MCP сервиса в чате

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* В настройках `MCP сервер` должен быть успешно добавлен MCP сервер

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Демонстрация работы**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Как видно на изображении, благодаря интеграции функции `fetch` из MCP, Cherry Studio лучше понимает запросы пользователей, получает релевантную информацию из интернета и предоставляет более точные и полные ответы.