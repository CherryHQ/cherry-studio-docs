
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# PPIO Pai Ou Cloud

## Cherry Studio интеграция с PPIO LLM API

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#%D0%9E%D0%B1%D0%B7%D0%BE%D1%80-%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)Обзор обучения <a href="#e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0" id="e6-95-99-e7-a8-8b-e6-a6-82-e8-bf-b0"></a>

Cherry Studio — это мультиплатформенный десктопный клиент, поддерживающий установку на Windows, Linux и MacOS. Он объединяет основные LLM-модели и предоставляет сценарную поддержку. Пользователи могут повысить эффективность работы через интеллектуальное управление диалогами, кастомизацию с открытым исходным кодом и мультитематические интерфейсы.

Cherry Studio теперь глубоко интегрирован с **высокопроизводительным API-каналом PPIO** — благодаря гарантиям корпоративного уровня вычислений достигается **высокая скорость отклика DeepSeek-R1/V3** и **доступность сервиса 99.9%**, обеспечивая быстрый и плавный опыт.

В руководстве ниже представлена полная схема подключения (включая настройку ключей). Активируйте продвинутый режим «Умная маршрутизация Cherry Studio + Высокопроизводительный API PPIO» за 3 минуты.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#1-id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba)1. Войдите в CherryStudio, добавьте «PPIO» как провайдера моделей <a href="#id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba" id="id-1-e8-bf-9b-e5-85-a5-cherrystudio-ef-bc-8c-e6-b7-bb-e5-8a-a0-e2-80-9cppio-e2-80-9d-e4-bd-9c-e4-b8-ba"></a>

Сначала скачайте Cherry Studio с официального сайта: [ ](https://cherry-ai.com/download)[https://cherry-ai.com/download](https://cherry-ai.com/download) (Если не открывается, используйте ссылку на Quark Disk: [https://pan.quark.cn/s/c8533a1ec63e#/list/share](https://pan.quark.cn/s/c8533a1ec63e#/list/share))

(1) Нажмите настройки в левом нижнем углу, укажите имя провайдера: `PPIO`, нажмите «ОК»

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-setting.png" alt=""><figcaption></figcaption></figure>

(2) Перейдите в [Управление API-ключами Pai Ou Cloud](https://ppinfra.com/user/register?invited_by=JYT9GD\&utm_source=github_cherry-studio), щёлкните на [аватар пользователя] → [Управление API-ключами]

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-01.png" alt=""><figcaption></figcaption></figure>

Нажмите [+ Создать] для генерации нового ключа API. Укажите имя ключа. **Ключ отображается только при создании — обязательно скопируйте и сохраните его, чтобы не прерывать дальнейшее использование**

<figure><img src="https://static.ppinfra.com/docs/image/llm/ppinfra-create-api-key-02.png" alt=""><figcaption></figcaption></figure>

(3) Вставьте ключ в CherryStudio: выберите [PPIO Pai Ou Cloud], введите API-ключ с сайта, нажмите [Проверить]

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3601.PNG" alt=""><figcaption></figcaption></figure>

(4) Выберите модель: например, deepseek/deepseek-r1/community. Для смены модели просто выберите другую.

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3602.PNG" alt=""><figcaption></figcaption></figure>

DeepSeek R1 и V3 community — пробные версии. Это полнофункциональные модели со всеми параметрами, без разницы в стабильности и эффективности. Для массового использования **пополните счёт и переключитесь на не-community версию**.

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#2-id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae)2. Настройка использования моделей <a href="#id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae" id="id-2-e6-a8-a1-e5-9e-8b-e4-bd-bf-e7-94-a8-e9-85-8d-e7-bd-ae"></a>

(1) После успешной [Проверки] можно использовать сервис

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-3603.png" alt=""><figcaption></figcaption></figure>

(2) Нажмите [@], выберите модель DeepSeek R1 от PPIO и начинайте общение\~

<figure><img src="https://static.ppinfra.com/docs/image/llm/cherry-studio-ppio-config-02.png" alt=""><figcaption></figcaption></figure>

[Источник материалов: [Чэнь Энь](https://www.kdocs.cn/l/ctGiF5K6PQoO)]

### [​](https://ppinfra.com/docs/third-party/cherry-studio-use#3-id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b)3. Видеоруководство по PPIO × Cherry Studio <a href="#id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b" id="id-3-ppio-c3-97cherry-studio-e8-a7-86-e9-a2-91-e4-bd-bf-e7-94-a8-e6-95-99-e7-a8-8b"></a>

Если предпочитаете визуальное обучение — на Bilibili есть видеоурок. Пошагово поможем освоить настройку «PPIO API + Cherry Studio». Перейдите по ссылке → [《Все ещё бесит, когда DeepSeek бесконечно грузится? Pai Ou Cloud + DeepSeek Full Version = 0 задержек, мгновенный старт》](https://www.bilibili.com/video/BV1BZNmeTEwg/?buvid=XX82F37818653072D274A6BB8A4FE7938A30C\&from_spmid=search.search-result.0.0\&is_story_h5=false\&mid=3CpKQv%2Bjnb8k6iTGlUl1eH8FTQ%2FSZMtL1rElX6M3iMo%3D\&plat_id=116\&share_from=ugc\&share_medium=android\&share_plat=android\&share_session_id=b892268f-5751-4f6e-9690-50b37855d346\&share_source=WEIXIN\&share_source=weixin\&share_tag=s_i\&spmid=united.player-video-detail.0.0\&timestamp=1739160448\&unique_k=eKDZuRP\&up_id=3546757841554023\&vd_source=50fea165795ccc47455a165f5bcaeed2)

[Источник видео: sola]