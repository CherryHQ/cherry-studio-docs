
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# GitHub Copilot

Для использования GitHub Copilot необходимо иметь учётную запись GitHub и подписку на сервис GitHub Copilot. Подойдёт и бесплатная версия подписки (free), однако она не поддерживает новейшую модель Claude 3.7. Подробности смотрите на [официальном сайте GitHub Copilot](https://github.com/features/copilot).

## Получение Device Code

Нажмите «Войти в GitHub», чтобы получить Device Code и скопируйте его.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Пример получения Device Code"><figcaption><p>Получение Device Code</p></figcaption></figure>

## Ввод Device Code и авторизация в браузере

После успешного получения Device Code перейдите по ссылке в браузере, войдите в учётную запись GitHub, введите Device Code и подтвердите доступ.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Пример авторизации GitHub"><figcaption><p>Авторизация GitHub</p></figcaption></figure>

После успешной авторизации вернитесь в Cherry Studio, нажмите «Подключить GitHub». При успешном подключении отобразятся имя пользователя и аватар GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Пример успешного подключения GitHub"><figcaption><p>Успешное подключение GitHub</p></figcaption></figure>

## Получение списка моделей через кнопку «Управление»

Нажмите кнопку «Управление» внизу экрана — автоматически загрузится список поддерживаемых моделей.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Пример получения списка моделей"><figcaption><p>Получение списка моделей</p></figcaption></figure>

## Часто задаваемые вопросы

### Не удалось получить Device Code, повторите попытку

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Пример ошибки получения Device Code"><figcaption><p>Ошибка получения Device Code</p></figcaption></figure>

В настоящее время для отправки запросов используется Axios, который не поддерживает socks-прокси. Рекомендуем использовать системный прокси или HTTP-прокси. Либо отключите настройки прокси в Cherry Studio и используйте глобальный прокси. Убедитесь, что ваше сетевое соединение стабильно, чтобы избежать ошибок при получении Device Code.