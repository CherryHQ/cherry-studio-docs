---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Vertex AI

## Обзор учебного руководства

### 1. Получение API-ключа

*   Перед получением API-ключа для Gemini необходимо иметь проект Google Cloud (если уже имеется, этот шаг можно пропустить)
*   Перейдите в [Google Cloud](https://console.cloud.google.com/projectcreate) для создания проекта: укажите название проекта и нажмите "Создать проект"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

*   Откройте [консоль Vertex AI](https://console.cloud.google.com/vertex-ai)
*   В созданном проекте активируйте [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Настройка прав доступа API

*   Откройте интерфейс управления [сервисными аккаунтами](https://console.cloud.google.com/iam-admin/serviceaccounts) и создайте сервисный аккаунт

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

*   На странице управления сервисными аккаунтами найдите созданный аккаунт, нажмите `Ключи` и создайте новый ключ в формате JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

*   После создания ключ автоматически сохранится на компьютер в виде JSON-файла — **обязательно сохраните его**

## 3. Настройка Vertex AI в Cherry Studio

*   Выберите провайдера Vertex AI
*   Заполните соответствующие поля данными из JSON-файла

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Нажмите "Добавить [модель](https://console.cloud.google.com/vertex-ai/model-garden)", чтобы начать использование!