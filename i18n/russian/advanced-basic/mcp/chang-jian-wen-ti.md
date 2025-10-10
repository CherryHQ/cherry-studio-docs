---
icon: hexagon-exclamation
---
# Часто задаваемые вопросы


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




### 1. mcp-server-time

<figure><img src="../../.gitbook/assets/telegram-cloud-photo-size-5-6068931438453048569-y.jpg" alt=""><figcaption><p>Скриншот ошибки</p></figcaption></figure>

**Решение**  

В строке "Параметры" укажите:

```
mcp-server-time
--local-timezone
<ваш часовой пояс, например: Asia/Shanghai>
```