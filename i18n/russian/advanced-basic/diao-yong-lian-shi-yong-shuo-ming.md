---
icon: route
---
# Инструкция по использованию цепочки вызовов


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




## Функциональные возможности

Цепочка вызовов (также называемая "trace") предоставляет пользователям возможность анализировать диалоги, помогая отслеживать работу модели, базы знаний, MCP, веб-поиска и других компонентов в процессе общения. Это инструмент наблюдения, реализованный на основе [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), который визуализирует данные через сбор, хранение и обработку на стороне клиента, предоставляя количественную основу для диагностики проблем и оптимизации.

Каждый диалог соответствует одному набору данных trace. Один trace состоит из нескольких span-ов, где каждый span соответствует определенной логике обработки в Cherry Studio: вызов сессии модели, обращение к MCP, запрос к базе знаний, веб-поиск и т.д. Trace отображается в виде древовидной структуры, где span-ы являются узлами. Основные данные включают время выполнения и количество использованных токенов, а в деталях span-а можно просмотреть конкретные входные и выходные данные.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Включение Trace

По умолчанию после установки Cherry Studio функция Trace скрыта. Для её активации перейдите в "Настройки" → "Общие настройки" → "Режим разработчика", как показано на изображении:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Trace не записывается для предыдущих сессий — записи создаются только для новых вопросов. Данные хранятся локально. Для полной очистки Trace: 
1. Перейдите в "Настройки" → "Настройки данных" → "Каталог данных" → "Очистить кеш"
2. Или вручную удалите файлы в каталоге `~/.cherrystudio/trace`

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Примеры использования

### Просмотр полной цепочки
Нажмите на значок цепочки вызовов в диалоговом окне Cherry Studio для просмотра полной цепочки данных. В окне отображаются все вызовы: модели, веб-поиска, базы знаний и MCP.

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Анализ моделей в цепочке
Для просмотра деталей вызова модели нажмите на соответствующий узел, чтобы изучить входные и выходные данные.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Мониторинг веб-поиска
Нажмите на узел веб-поиска для просмотра отправленного запроса и полученных результатов.

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Просмотр обращений к базе знаний
Нажмите на узел базы знаний, чтобы увидеть исходный запрос и возвращённый ответ.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Отслеживание вызовов MCP
Для анализа работы MCP нажмите на соответствующий узел и проверьте входные параметры и возвращаемые значения инструмента.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>
<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Проблемы и предложения

Функция разработана командой Alibaba Cloud [EDAS](https://www.aliyun.com/product/edas). Для обратной связи присоединяйтесь к группе DingTalk (ID: 21958624) для обсуждения с разработчиками.

\