---
icon: robot
---
# Руководство по использованию Cherry Agent


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




В версии Cherry Studio v1.7.0.alpha был представлен Agent, позволяющий использовать Claude Code в Cherry Studio. В этом руководстве описан полный процесс настройки и запуска.

### 1. Создание поставщика типа Anthropic

Можно использовать любого провайдера, поддерживающего конечные точки Anthropic. Например, с CherryIn создайте нового поставщика Agent, заполните ключ и адрес, добавьте любую модель. (⚠️ Режим Agent потребляет большое количество токенов, будьте внимательны с их использованием)

> Пользователи, подписанные на Claude Code, также могут ввести ключ и URL-адрес для получения модели

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.26.35@2x.png" alt=""><figcaption></figcaption></figure>

### 2. Запуск API-сервера

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 19.56.22@2x.png" alt=""><figcaption></figcaption></figure>

### 3. Создание Agent

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.24.43@2x.png" alt=""><figcaption></figcaption></figure>

Щелкните правой кнопкой мыши по Agent, чтобы перейти в режим редактирования, где можно настроить права доступа и инструменты/mcp службы.

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.25.10@2x (1).png" alt=""><figcaption></figcaption></figure>

### Демонстрация результата

<figure><img src="../.gitbook/assets/CleanShot 2025-10-12 at 20.30.26@2x (1).png" alt=""><figcaption></figcaption></figure>