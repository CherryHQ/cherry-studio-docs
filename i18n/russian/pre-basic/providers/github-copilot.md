
{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# GitHub Copilot

Чтобы использовать GitHub Copilot, сначала у вас должна быть учётная запись GitHub и подписка на GitHub Copilot. Доступна и бесплатная версия подписки, но она не поддерживает последнюю модель Claude 3.7. Подробности см. на [официальном сайте GitHub Copilot](https://github.com/features/copilot).

## Получение Device Code

Нажмите «Войти в GitHub», чтобы получить Device Code и скопировать его.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Пример получения Device Code"><figcaption><p>Получение Device Code</p></figcaption></figure>

## Ввод Device Code в браузере и авторизация

После получения Device Code нажмите на ссылку, чтобы открыть браузер, войдите в учётную запись GitHub, введите Device Code и предоставьте разрешение.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Пример авторизации GitHub"><figcaption><p>Авторизация GitHub</p></figcaption></figure>

После успешной авторизации вернитесь в Cherry Studio и нажмите «Подключить GitHub». После подключения отобразятся ваше имя пользователя и аватар GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Пример успешного подключения GitHub"><figcaption><p>Успешное подключение GitHub</p></figcaption></figure>

## Получение списка моделей через «Управление»

Нажмите кнопку «Управление» внизу, чтобы автоматически получить список поддерживаемых моделей.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Пример получения списка моделей"><figcaption><p>Получение списка моделей</p></figcaption></figure>

## Часто задаваемые вопросы

### Не удалось получить Device Code, попробуйте снова

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Пример ошибки получения Device Code"><figcaption><p>Ошибка получения Device Code</p></figcaption></figure>

Сейчас для запросов используется Axios, который не поддерживает SOCKS-прокси. Используйте системный прокси или HTTP-прокси, либо вообще не настраивайте прокси в CherryStudio, а используйте глобальный прокси. Прежде всего убедитесь, что ваше интернет-соединение работает нормально, чтобы избежать ошибок при получении Device Code.