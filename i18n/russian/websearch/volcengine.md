---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Подключение к интернету через Volcano Engine

### 1. Вход/Регистрация в аккаунте Volcano Engine <a href="#rclz7" id="rclz7"></a>

Посетите официальный сайт: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Официальный сайт Volcano Engine</p></figcaption></figure>

### 2. Создание "Моего приложения" с доступом в интернет <a href="#gvzaa" id="gvzaa"></a>

2.1. Авторизуйтесь в Volcano Engine и перейдите в раздел "Ark" ("Ковчег"): [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Выполните:**<mark style="color:red;">**«Мои приложения» → «Создать приложение» → «Без кода» → «Чат 1 на 1»**</mark> &#x20;

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Заполните информацию и опубликуйте приложение <a href="#zzdfe" id="zzdfe"></a>

**Название приложения**: Произвольное имя согласно требованиям (поле с<mark style="color:red;">**\* обязательно**</mark>, остальное можно оставить пустым)

<mark style="color:red;">**Ключевое: Включите плагин доступа в интернет (требуется предварительная активация)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Активация плагина доступа в интернет (учтите стоимость и бесплатные лимиты) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Нажмите "Купить сейчас" и следуйте инструкциям. Успешная активация подтверждается следующим интерфейсом.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Обратите внимание на статус - активация завершена</p></figcaption></figure>

Вернитесь к интерфейсу заполнения информации о приложении.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Настройка "Расширенной конфигурации" для интернет-поиска <a href="#sp6uz" id="sp6uz"></a>

Рекомендации:
* Для точного контроля ввода/вывода используйте **"Пользовательский вызов"**;
* Для упрощения оставьте **"Автоматический вызов"** (по умолчанию);
* При требовании к актуальности данных - **"Принудительное включение"**.

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Публикация приложения <a href="#fe1gf" id="fe1gf"></a>

Нажмите "Опубликовать" в правом верхнем углу.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Получение API ключа <a href="#jtqlu" id="jtqlu"></a>

Выполните: **«Руководство по API» → «Выберите API Key и скопируйте» → «Просмотреть и выбрать»**

Скопируйте API key для использования в Cherry Studio.

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Примечание: Если ключ отсутствует, создайте его через **«Создать API Key»** в правом верхнем углу.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Использование API Key в Cherry Studio для подключения deepseek-R1 к интернету <a href="#lrefj" id="lrefj"></a>

#### 5.1. В Cherry Studio: «Настройки» → «Произвольное имя» → «Тип: openAI» <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Настройка URL и ключа <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Примечание: Адрес конечной точки можно найти здесь (обязательно добавьте "/" в конце):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Добавление имени модели <a href="#qmh3i" id="qmh3i"></a>

Скопируйте название модели из мелкого шрифта, иначе возникнет ошибка.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Предпросмотр работы <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>