---
description: cherry studio使用「火山引擎」接入deepseekR1联网功能，喂饭教程。
hidden: True
icon: globe-pointer
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Включение возможности интернет-доступа в Volcano Engine

### 1. Вход/Регистрация учетной записи в «Volcano Engine» <a href="#rclz7" id="rclz7"></a>

Перейдите на официальный сайт: [https://www.volcengine.com/](https://www.volcengine.com/)

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption><p>Официальный сайт Volcano Engine</p></figcaption></figure>

### 2. Создание «Моего приложения» с возможностью интернет-доступа <a href="#gvzaa" id="gvzaa"></a>

2.1. Войдите в Volcano Engine и перейдите на страницу «Volcano Ark»: [https://console.volcengine.com/ark](https://console.volcengine.com/ark)

2.2. **Последовательно нажмите:** <mark style="color:red;">**«Мои приложения» → «Создать приложение» → «Без кода» → «Личный чат»**</mark>

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

### 3. Заполнение информации и публикация приложения <a href="#zzdfe" id="zzdfe"></a>

**Название приложения**: Любое подходящее имя (обязательно <mark style="color:red;">*** помеченные поля</mark>, остальное можно не заполнять).

<mark style="color:red;">**Ключевой момент: плагин интернет-доступа должен быть включен (требуется предварительная активация)**</mark>

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1. Активация функции плагина интернет-доступа (обратите внимание на стоимость и бесплатные квоты) <a href="#mwn38" id="mwn38"></a>

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption><p>Нажмите «Купить сейчас» и выполняйте шаги, пока не появится этот экран – означает успешную активацию.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption><p>Проверьте статус – теперь активация завершена</p></figcaption></figure>

Вернитесь в интерфейс «Заполнение информации о приложении» и продолжите.

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

#### 3.2. Расширенные настройки интернет-поиска <a href="#sp6uz" id="sp6uz"></a>

Выберите в соответствии с потребностями:

* Для точного контроля ввода/вывода используйте **«Кастомный вызов»**;
* Для простоты используйте **«Автоматический вызов»** (значение по умолчанию);
* Если важна актуальность информации, выберите **«Принудительное включение»**.

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### 3.3. Публикация приложения <a href="#fe1gf" id="fe1gf"></a>

Нажмите «Опубликовать» в правом верхнем углу – приложение создано.

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

### 4. Получение API Key <a href="#jtqlu" id="jtqlu"></a>

Последовательно нажмите: **«Руководство по вызову API» → «Выбрать и скопировать API Key» → «Просмотреть и выбрать»**.

Скопируйте API Key для использования в Cherry Studio (подробности на скриншотах):

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

Если API Key отсутствует, нажмите **«Создать API Key»** в правом верхнем углу всплывающего окна.

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

### 5. Использование API Key в Cherry Studio для интернет-доступа к deepseek-R1 <a href="#lrefj" id="lrefj"></a>

#### 5.1. В Cherry Studio: «Настройки» → «Любое имя» → «Тип: OpenAI» <a href="#dvrbv" id="dvrbv"></a>

<figure><img src="../.gitbook/assets/image (64).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (65).png" alt="" width="375"><figcaption></figcaption></figure>

#### 5.2. Настройка URL и ключа <a href="#mt8y0" id="mt8y0"></a>

<figure><img src="../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

<mark style="color:purple;">Если не найдете адрес или требуется пекинский узел, найдите точный адрес здесь (не забудьте "/"):</mark>

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### 5.3. Добавление имени модели <a href="#qmh3i" id="qmh3i"></a>

Важно: скопируйте имя модели из мелкого текста (см. скриншоты), иначе возникнет ошибка.

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

### 6. Предварительный просмотр работы <a href="#peb2p" id="peb2p"></a>

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>