---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Интернет-режим

{% hint style="info" %}
Примеры ситуаций, требующих подключения к интернету:

* Актуальная информация: например, цены на фьючерсы золота за сегодня/на этой неделе/только что.
* Динамические данные: например, погода, курсы валют и другие меняющиеся показатели.
* Новые знания: например, о новых явлениях, концепциях, технологиях и т.д.
{% endhint %}

### 1. Как включить интернет-режим

В окне запроса Cherry Studio нажмите значок 【🌐】, чтобы активировать подключение.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Нажмите значок планеты – включите интернет</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Индикатор – интернет-режим активирован</p></figcaption></figure>

### 2. Важное примечание: два режима работы

#### Режим 1: Встроенная функция подключения у поставщиков моделей

Если модель изначально поддерживает интернет, после активации можно сразу использовать онлайн-функции.

{% hint style="warning" %}
Проверить поддержку подключения можно по значку 🌐 рядом с названием модели в интерфейсе чата.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Этот метод также работает на странице управления моделями для быстрой идентификации поддержки сети.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Поставщики моделей с поддержкой интернета в Cherry Studio**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (все модели)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian</mark>

{% hint style="danger" %}
Особый случай:
Даже без значка 🌐 некоторые модели могут работать в сети, как описано в руководстве ниже.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Режим 2: Использование сервиса Tavily для моделей без встроенной поддержки

Если модель не имеет значка 🌐, но требует обработки актуальных данных, используется сервис поиска Tavily.

**При первом использовании Tavily** появится окно настройки – следуйте инструкциям.

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Нажмите: «Настроить»</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Нажмите «Получить ключ»</p></figcaption></figure>

После нажатия откроется страница регистрации на **официальном сайте Tavily**. Зарегистрируйтесь, создайте API-ключ и вставьте его в Cherry Studio.

{% hint style="danger" %}
Инструкция по регистрации доступна в документации Tavily в этом каталоге.
{% endhint %}

**Руководство по регистрации Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Интерфейс ниже подтверждает успешную регистрацию.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Скопируйте ключ</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Вставьте ключ – настройка завершена</p></figcaption></figure>

Тест работы: результаты показывают успешный поиск (по умолчанию выбрано 5 источников).

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Внимание: Tavily имеет месячные бесплатные ограничения, превышение требует оплаты~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> P.S.: При обнаружении ошибок обращайтесь в любое время.