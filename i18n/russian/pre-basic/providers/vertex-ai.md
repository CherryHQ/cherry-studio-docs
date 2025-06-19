---
description: 暂时不支持Claude模型
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Vertex AI

## Обзор инструкции

### 1. Получение APIKey

* Перед получением api key для Gemini необходим проект Google Cloud (если у вас уже есть проект, этот шаг можно пропустить)
* Перейдите в [Google Cloud](https://console.cloud.google.com/projectcreate), создайте проект, введите название проекта и нажмите "Создать проект"

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

* Перейдите в [консоль Vertex AI](https://console.cloud.google.com/vertex-ai)
* В созданном проекте активируйте [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Настройка прав доступа API

* Откройте раздел [управления учётными записями сервисов](https://console.cloud.google.com/iam-admin/serviceaccounts) и создайте учётную запись сервиса

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* В разделе управления учётными записями найдите созданную учётную запись, нажмите `Ключи` и создайте новый ключ в формате JSON

<figure><img src="../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* После успешного создания ключ автоматически сохранится на вашем компьютере в виде JSON-файла — **обязательно сохраните его**

## 3. Настройка Vertex AI в Cherry Studio

* Выберите провайдера Vertex AI
* Заполните соответствующие поля данными из JSON-файла

<figure><img src="../../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

Нажмите "Добавить [модель](https://console.cloud.google.com/vertex-ai/model-garden)", и можно начинать работу!