---
icon: database
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Настройки данных

Этот интерфейс позволяет выполнять облачное и локальное резервное копирование данных клиента, просматривать локальные каталоги данных, очищать кеш и другие операции.

### Резервное копирование данных

В настоящее время резервное копирование данных поддерживается только через WebDAV. Вы можете выбрать сервис с поддержкой WebDAV для облачного резервного копирования.

Вы также можете синхронизировать данные между устройствами через `Компьютер A` $$\xrightarrow{\text{резервное копирование}}$$ `WebDAV` $$\xrightarrow{\text{восстановление}}$$ `Компьютер B`.

#### Пример с Nutstore

1. Войдите в Nutstore, щелкните имя пользователя в правом верхнем углу и выберите «Информация об аккаунте»:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Выберите «Настройки безопасности», нажмите «Добавить приложение»:

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Введите название приложения и сгенерируйте случайный пароль:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Скопируйте и сохраните пароль:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Получите адрес сервера, учетные данные и пароль:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. В Cherry Studio: Настройки → Настройки данных заполните данные WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Выберите резервное копирование или восстановление данных, настройте периодичность автоматического резервного копирования:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Сервисы WebDAV с низким порогом входа - это обычно облачные хранилища:

* [Nutstore](https://www.jianguoyun.com/)
* [123 Pan](https://www.123pan.com/) (требуется подписка)
* [Aliyun Drive](https://www.alipan.com/) (требуется покупка)
* [Box](https://www.box.com/) (бесплатно 10 ГБ, ограничение на файл - 250 МБ)
* [Dropbox](https://www.dropbox.com/) (бесплатно 2 ГБ, +16 ГБ за приглашения)
* [TeraCloud](https://teracloud.jp/en/) (бесплатно 10 ГБ, +5 ГБ за приглашения)
* [Yandex Disk](https://disk.yandex.com/) (бесплатно 10 ГБ для пользователей)

Сервисы для самостоятельного развертывания:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}