
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# PPIO Пайоу Юнь

## Подключение Cherry Studio к PPIO LLM API

### Обзор руководства <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio — это мультимодельный десктопный клиент, поддерживающий установку на Windows, Linux и MacOS. Он объединяет основные LLM-модели и предоставляет мультисценарную поддержку. Пользователи могут повысить продуктивность за счёт интеллектуального управления диалогами, кастомизации через открытый код и многотемного интерфейса.

Cherry Studio теперь глубоко интегрирован с **высокопроизводительным API-каналом PPIO** — благодаря корпоративным вычислительным мощностям обеспечивается **высокоскоростной отклик DeepSeek-R1/V3** и **доступность сервиса 99,9%**, что гарантирует быстрый и плавный опыт.

Нижеприведённое руководство содержит полную схему подключения (включая настройку ключей), позволяющую за 3 минуты активировать продвинутый режим «Интеллектуальная маршрутизация Cherry Studio + Высокопроизводительный API PPIO».

### 1. Настройка PPIO в Cherry Studio в качестве поставщика моделей <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Сначала скачайте Cherry Studio с официального сайта: [https://cherry-ai.com/download](https://cherry-ai.com/download) (если недоступно, используйте альтернативную ссылку в Kuake: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Нажмите настройки в нижнем левом углу, укажите имя поставщика: `PPIO`, нажмите «Подтвердить»

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Перейдите в [Управление API-ключами PPIO](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), выберите [Аватар пользователя] → [Управление API-ключами]

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Нажмите 【+ Создать】, укажите имя ключа. **Сгенерированный ключ отображается только один раз — обязательно скопируйте и сохраните его во избежание проблем с использованием!**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Вставьте ключ в Cherry Studio: выберите 【PPIO Пайоу Юнь】, введите API-ключ и нажмите 【Проверить】

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Выберите модель (на примере deepseek/deepseek-r1/community). Для смены модели выберите другую из списка.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

Версии DeepSeek R1 и V3 community предназначены для тестирования и используют полную версию модели без ограничений. Для интенсивного использования **пополните баланс и переключитесь на не-community версию**.

### 2. Конфигурация моделей <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) После успешного подключения (статус 【Проверить】) можно начинать работу

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Выберите через 【@】модель DeepSeek R1 от PPIO, чтобы начать диалог

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

【Источник материалов: [Чэнь Энь](https://www.kdocs.cn/l/ctGiF5K6PQoO)】

### 3. Видеоруководство по использованию PPIO×Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Для наглядного обучения мы подготовили видеоинструкцию на Bilibili. Пошаговое руководство поможет быстро освоить настройку связки «API PPIO + Cherry Studio». Начните плавную работу → [《Устали от вечной загрузки DeepSeek? PPIO + полная версия DeepSeek = мгновенный отклик и никаких задержек》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

【Автор видео: sola】