---
icon: database
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Настройки данных

Этот интерфейс позволяет выполнять облачное и локальное резервное копирование данных клиента, просматривать локальные каталоги данных и очищать кеш.

### Резервное копирование данных

В настоящее время резервное копирование данных поддерживается только через протокол WebDAV. Вы можете выбрать сервис с поддержкой WebDAV для облачного резервного копирования.

Также вы можете синхронизировать данные между несколькими устройствами по схеме:  
`Устройство A` $$\xrightarrow{\text{резервное копирование}}$$ `WebDAV` $$\xrightarrow{\text{восстановление}}$$ `Устройство B`.

#### Пример использования Nutstore (坚果云)

1. Войдите в Nutstore, нажмите на имя пользователя в правом верхнем углу и выберите "Информация об аккаунте":
<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Выберите "Настройки безопасности" → "Добавить приложение":
<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Введите название приложения и сгенерируйте случайный пароль:
<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Скопируйте и сохраните пароль:
<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Получите адрес сервера, логин и пароль:
<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. В Cherry Studio: Настройки → Настройки данных заполните информацию WebDAV:
<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Выберите резервное копирование или восстановление данных, настройте периодичность автоматического копирования:
<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
**Сервисы WebDAV с низким порогом входа (облачные хранилища):**
* [Nutstore (坚果云)](https://www.jianguoyun.com/)
* [123 Cloud Storage (123盘)](https://www.123pan.com/) (требуется подписка)
* [Aliyun Drive (阿里云盘)](https://www.alipan.com/) (платный)
* [Box](https://www.box.com/) (10 ГБ бесплатно, макс. файл 250 МБ)
* [Dropbox](https://www.dropbox.com/) (2 ГБ бесплатно + 16 ГБ за приглашения)
* [TeraCloud](https://teracloud.jp/en/) (10 ГБ + 5 ГБ за приглашения)
* [Yandex Disk](https://disk.yandex.com/) (10 ГБ бесплатно)

**Сервисы с самостоятельным развертыванием:**
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}