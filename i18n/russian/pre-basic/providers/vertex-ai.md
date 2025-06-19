---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Vertex AI

## Обзор учебного руководства

### 1. Получение API-ключа

* Перед получением API-ключа Gemini вам необходимо иметь проект Google Cloud (если он уже есть, этот шаг можно пропустить)
* Перейдите в [Google Cloud](https://console.cloud.google.com/projectcreate) для создания проекта, введите название проекта и нажмите "Создать проект"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Перейдите в [консоль Vertex AI](https://console.cloud.google.com/vertex-ai)
* В созданном проекте активируйте [Vertex AI API](ttps://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Настройка прав доступа к API

* Откройте интерфейс управления правами [сервисного аккаунта](https://console.cloud.google.com/iam-admin/serviceaccounts) и создайте сервисный аккаунт

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* На странице управления сервисными аккаунтами найдите созданный аккаунт, нажмите `Ключи` и создайте новый ключ в формате JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* После успешного создания файл ключа автоматически сохранится на вашем компьютере в формате JSON - **обязательно сохраните его в надежном месте**

## 3. Настройка Vertex AI в Cherry Studio

* Выберите провайдера Vertex AI
* Заполните соответствующие поля данными из JSON-файла

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Нажмите "Добавить [модель](https://console.cloud.google.com/vertex-ai/model-garden)", и можно начинать работу!