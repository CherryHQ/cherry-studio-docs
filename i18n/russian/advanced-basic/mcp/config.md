# Настройка и использование MCP


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Откройте настройки Cherry Studio.
2. Найдите опцию `MCP сервер`.
3. Нажмите `Добавить сервер`.
4. Заполните параметры MCP-сервера ([ссылка для справки](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Возможные параметры:
   * Имя: произвольное название, например `fetch-server`
   * Тип: выберите `STDIO`
   * Команда: укажите `uvx`
   * Параметры: укажите `mcp-server-fetch`
   *(могут быть другие параметры в зависимости от сервера)*
5. Нажмите `Сохранить`.

{% hint style="success" %}
После настройки Cherry Studio автоматически загрузит требуемый MCP-сервер - `fetch server`. После завершения загрузки можно начинать работу! Примечание: если mcp-server-fetch не конфигурируется, попробуйте перезагрузить компьютер.
{% endhint %}

### Активация MCP-сервиса в чате

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* В настройках `MCP сервера` MCP-сервер успешно добавлен

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Демонстрация работы**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Как видно из примера, функция `fetch` в составе MCP позволяет Cherry Studio точнее распознавать цели пользовательских запросов, получать релевантную информацию из интернета и давать более точные, комплексные ответы.