---
icon: route
---
# Руководство по использованию цепочки вызовов


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




## Функционал

Цепочка вызовов (также называемая "trace") предоставляет пользователям аналитические возможности для диалогов, помогая отслеживать конкретные проявления моделей, базы знаний, MCP, веб-поиска и других компонентов во время диалога. Это инструмент мониторинга, реализованный на базе [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), который визуализирует данные через сбор, хранение и обработку на стороне клиента, предоставляя количественные оценки для локализации проблем и оптимизации результатов.

Каждый диалог соответствует одному trace, который состоит из нескольких span. Каждый span соответствует логике обработки в Cherry Studio, такой как вызов сессии модели, обращение к MCP, запрос к базе знаний или веб-поиску. Trace отображается в виде древовидной структуры, где span являются узлами дерева. Основные данные включают время выполнения и объем использованных токенов, а в деталях span можно также просмотреть конкретные входные/выходные данные.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Активация Trace

По умолчанию после установки Cherry Studio функция Trace скрыта. Для активации необходимо включить "Режим разработчика" в "Настройки" > "Общие настройки", как показано ниже:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Важно: записи Trace не создаются для предыдущих сессий. Записи формируются только для новых вопросов/ответов. Данные хранятся локально. Для полной очистки Trace используйте "Настройки" > "Настройки данных" > "Каталог данных" > "Очистить кэш", либо вручную удалите файлы в директории \~/.cherrystudio/trace:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Сценарии использования

### Просмотр полной цепочки

Нажмите на значок цепочки вызовов в диалоговом окне Cherry Studio для просмотра полных данных цепочки. Независимо от того, вызывались ли модели, веб-поиск, база знаний или MCP, все обращения отображаются в окне цепочки вызовов.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Анализ моделей в цепочке

Для просмотра деталей модели в цепочке вызовов кликните на соответствующий span модели, чтобы изучить её входные/выходные данные.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Просмотр веб-поиска в цепочке

Для детализации веб-поиска кликните на span веб-поиска. В деталях отображаются запрошенный вопрос и полученные результаты.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Анализ базы знаний в цепочке

Для изучения обращений к базе знаний кликните на соответствующий span. В деталях отображаются запрошенный вопрос и полученный ответ.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Мониторинг обращений к MCP

Для просмотра деталей работы с MCP кликните на span MCP. В деталях отображаются входящие параметры вызова этого серверного инструмента и возвращаемые им результаты.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Проблемы и предложения

Текущий функционал предоставлен командой [EDAS](https://www.aliyun.com/product/edas) Alibaba Cloud. При возникновении вопросов или предложений присоединяйтесь к группе DingTalk (ID группы: 21958624) для обсуждения с разработчиками.