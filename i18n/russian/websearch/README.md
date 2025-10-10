---
description: 如何在 Cherry Studio 使用联网模式
icon: globe
---
# Режим работы в сети


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




{% hint style="info" %}
Примеры ситуаций, требующих подключения к Интернету:

* Актуальная информация: например, текущие цены на золотые фьючерсы сегодня/на этой неделе/только что.
* Динамические данные: например, погода, курсы валют и другие изменяющиеся показатели.
* Новейшие знания: например, новые явления, концепции, технологии и т.д.
{% endhint %}

### I. Как включить работу в сети

В окне запроса Cherry Studio нажмите значок 【🌐】, чтобы активировать работу в сети.

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption><p>Нажмите значок земного шара — активируйте работу в сети</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption><p>Индикатор активированного режима работы в сети</p></figcaption></figure>

### II. Важное примечание: два режима работы в сети

#### Режим 1: Встроенная функция работы в сети у моделей провайдеров

В этом случае после активации функции вы можете сразу использовать интернет-сервисы — всё очень просто.

{% hint style="warning" %}
Быстро проверить поддержку сети моделью можно по наличию значка мини-карты рядом с названием модели в верхней части интерфейса.
{% endhint %}

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

На странице управления моделями этот метод также помогает быстро определить поддерживаемые функции.

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

> <mark style="color:green;">**Провайдеры моделей с поддержкой сети в Cherry Studio:**</mark>
>
> * <mark style="color:green;">Google Gemini</mark>
> * <mark style="color:green;">OpenRouter (все модели поддерживают)</mark>
> * <mark style="color:green;">Tencent Hunyuan</mark>
> * <mark style="color:green;">Zhipu AI</mark>
> * <mark style="color:green;">Alibaba Cloud Bailian и др.</mark>

{% hint style="danger" %}
Особое внимание:
  
Возможны исключительные случаи, когда модель без значка 🌐 всё же может работать в сети — как описано в руководстве ниже.
{% endhint %}

{% content-ref url="volcengine.md" %}
[volcengine.md](volcengine.md)
{% endcontent-ref %}

***

#### Режим 2: Использование сервиса Tavily для моделей без встроенной поддержки сети

При работе с моделью без функции работы в сети (без значка 🌐), когда требуется обработка актуальных данных, используется поисковый сервис Tavily.

**При первом использовании Tavily** появится окно с инструкцией по настройке — просто следуйте указаниям!

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption><p>Всплывающее окно — нажмите «Настроить»</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption><p>Нажмите «Получить ключ»</p></figcaption></figure>

После нажатия вы перейдете на **официальный сайт Tavily**. Зарегистрируйтесь, создайте API-ключ и скопируйте его в Cherry Studio.

{% hint style="danger" %}
Инструкцию по регистрации см. в документации Tavily в этом же каталоге.
{% endhint %}

**Руководство по регистрации Tavily:**

{% content-ref url="tavily.md" %}
[tavily.md](tavily.md)
{% endcontent-ref %}

Интерфейс ниже подтверждает успешную регистрацию.

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption><p>Скопируйте ключ</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption><p>Вставьте ключ — готово!</p></figcaption></figure>

Проверьте результат. Система выполняет поиск по умолчанию с 5 результатами.

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Внимание: Tavily имеет ежемесячный бесплатный лимит, превышение требует оплаты~~
{% endhint %}

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

> P.S.: При обнаружении ошибок вы можете связаться с нами в любое время.