---
icon: cloud-arrow-up
---
# Резервное копирование через WebDAV


{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}




Cherry Studio поддерживает резервное копирование данных через WebDAV. Вы можете выбрать подходящий сервис WebDAV для облачного резервного копирования.

С помощью WebDAV можно синхронизировать данные между несколькими устройствами по схеме: `Компьютер A` $$\xrightarrow{\text{резервное копирование}}$$ `WebDAV` $$\xrightarrow{\text{восстановление}}$$ `Компьютер B`.

#### Пример использования Nutstore

1. Войдите в Nutstore, нажмите на имя пользователя в правом верхнем углу и выберите «Информация об аккаунте»:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Выберите «Настройки безопасности» и нажмите «Добавить приложение»

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Введите название приложения, сгенерируется случайный пароль;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Скопируйте и сохраните пароль;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Получите адрес сервера, учетную запись и пароль;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. В настройках Cherry Studio → настройках данных заполните информацию WebDAV;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Выберите резервное копирование или восстановление данных, а также можно настроить периодичность автоматического резервного копирования.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Сервисы WebDAV с низким порогом входа — это, как правило, облачные хранилища:

- [Nutstore](https://www.jianguoyun.com/)
- [123 Pan](https://www.123pan.com/) (требуется подписка)
- [Aliyun Disk](https://www.alipan.com/) (требуется покупка)
- [Box](https://www.box.com/) (бесплатно предоставляется 10 ГБ, ограничение на размер одного файла — 250 МБ.)
- [Dropbox](https://www.dropbox.com/) (Dropbox предоставляет 2 ГБ бесплатно, можно приглашать друзей для увеличения до 16 ГБ.)
- [TeraCloud](https://teracloud.jp/en/) (бесплатно предоставляется 10 ГБ, также можно получить дополнительно 5 ГБ за приглашения.)
- [Yandex Disk](https://disk.yandex.com/) (бесплатным пользователям предоставляется 10 ГБ.)

Кроме того, есть сервисы, которые требуют самостоятельного развертывания:

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [sharelist](https://github.com/reruin/sharelist)
{% endhint %}