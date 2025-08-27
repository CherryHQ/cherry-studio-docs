---
description: 暂时不支持Claude模型
---
# Vertex AI


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




## Обзор учебного руководства

### 1. Получение API-ключа

* Перед получением API-ключа для Gemini вам необходим проект в Google Cloud (если у вас уже есть проект, этот шаг можно пропустить)
* Создайте проект на [Google Cloud](https://console.cloud.google.com/projectcreate), введите название проекта и нажмите "Создать проект"

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* Перейдите в [консоль Vertex AI](https://console.cloud.google.com/vertex-ai)
* В созданном проекте активируйте [Vertex AI API](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?inv=1\&invt=Ab0iBA)

<figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

## 2. Настройка прав доступа к API

* Откройте раздел управления доступом для [сервисных аккаунтов](https://console.cloud.google.com/iam-admin/serviceaccounts) и создайте сервисный аккаунт

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

* На странице управления сервисными аккаунтами найдите созданный аккаунт