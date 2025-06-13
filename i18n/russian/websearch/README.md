---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Интернет-режим

{% hint style="info" %}
Примеры сценариев, требующих подключения к интернету:

* Актуальная информация: например, сегодняшняя/текущая/только что обновлённая цена на золотые фьючерсы.
* Данные в реальном времени: например, погода, обменные курсы и другие динамические показатели.
* Новые знания: например, новые явления, концепции, технологии и т.д.
{% endhint %}

### I. Как включить интернет

В окне запроса Cherry Studio нажмите значок 【Земля】, чтобы включить интернет.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Нажмите значок Земли - Включить интернет</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Указывает - функция интернета включена</p></figcaption></figure>

### II. Особое внимание: Есть два режима работы интернета

#### Режим 1: Большие модели поставщиков со встроенной функцией интернета

В этом случае после включения интернета можно сразу использовать сервис, всё очень просто.

{% hint style="warning" %}
Вы можете быстро определить, поддерживает ли модель интернет, проверив наличие значка глобуса рядом с её названием в верхней части интерфейса запросов.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

На странице управления моделями этот метод также поможет быстро определить, какие модели поддерживают интернет.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Поставщики моделей с поддержкой интернета, которые в настоящее время поддерживаются Cherry Studio:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (все модели поддерживают интернет)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian и другие</mark>

{% hint style="danger" %}
Особое внимание:

Существует особый случай, когда даже если на модели нет значка глобуса, она всё равно может выходить в интернет, как объясняется в этом руководстве:
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Режим 2: Использование сервиса Tavily для моделей без встроенной функции интернета

При использовании больших моделей без функции интернета (без значка глобуса рядом с именем), когда требуется обработка актуальной информации, используется сервис поиска Tavily.

**При первом использовании Tavily** появится всплывающее окно с инструкциями по настройке - следуйте указаниям, это очень просто!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Всплывающее окно, нажмите: Настройки</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Нажмите "Получить ключ"</p></figcaption></figure>

После нажатия "Получить ключ" вы автоматически перейдёте на **официальный сайт Tavily**. Зарегистрируйтесь, войдите в систему, создайте API-ключ и скопируйте его в Cherry Studio.

{% hint style="danger" %}
Если возникнут сложности с регистрацией, обратитесь к руководству по регистрации Tavily в этой же директории документации.
{% endhint %}

**Документ по регистрации в Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Следующий интерфейс означает успешную регистрацию.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Скопируйте ключ</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Вставьте ключ - всё готово!</p></figcaption></figure>

Проверим результат. Как видно, поиск в интернете работает корректно, а количество результатов соответствует установленному по умолчанию значению: 5.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Внимание: у Tavily есть бесплатный лимит в месяц, превышение потребует оплаты~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> PS: Если обнаружите ошибки, будем рады вашим сообщениям в любое время.