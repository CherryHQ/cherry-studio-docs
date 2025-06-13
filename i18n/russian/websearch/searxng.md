---
icon: searchengin
---

{% hint style="warning" %}
Этот документ переведен с китайского языка с помощью ИИ и еще не был проверен.
{% endhint %}

# Развертывание и настройка SearXNG

CherryStudio поддерживает веб-поиск через SearXNG — проект с открытым исходным кодом, который можно развернуть локально или на сервере. Этот подход отличается от конфигураций, требующих внешних API-провайдеров.

**Ссылка на проект SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## Преимущества SearXNG

* Открытый исходный код, бесплатный, не требует API
* Повышенная конфиденциальность
* Высокая степень кастомизации

## Локальное развертывание

### 1. Прямое развертывание через Docker

Поскольку SearXNG не требует сложной настройки среды (достаточно свободного порта), самый быстрый способ — развертывание через Docker-образ.

#### 1. Установите и настройте [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

После установки выберите путь хранения образов:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Поиск и загрузка образа SearXNG

Введите **searxng** в поисковой строке:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Загрузите образ:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Запуск образа

После загрузки перейдите в раздел **Images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Выберите образ и запустите:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Откройте настройки:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Например, для порта `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

После успешного запуска откройте интерфейс SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Эта страница подтверждает успешное развертывание:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Развертывание на сервере

Поскольку установка Docker в Windows может быть сложной, SearXNG можно развернуть на сервере для общего доступа. Однако SearXNG **не поддерживает аутентификацию**, что позволяет злоумышленникам находить и злоупотреблять вашим экземпляром.

Cherry Studio поддерживает [HTTP Basic Authentication (RFC7617)](https://developer.mozilla.org/ru/docs/Web/HTTP/Authentication). При публичном развертывании **обязательно** настройте аутентификацию через Nginx. Ниже приведены основные шаги (требуются базовые знания Linux).

### Развертывание SearXNG

Аналогично развертыванию через Docker. Предположим, Docker CE уже установлен ([официальное руководство](https://docs.docker.com/engine/install)). Команды для Debian:

```bash
sudo apt update
sudo apt install git -y

# Загрузка репозитория
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Для медленных серверов можно установить false
export IMAGE_PROXY=true

# Настройка конфигурации
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# см. https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url определяется в SEARXNG_BASE_URL, см. .env и docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # можно отключить для приватного экземпляра
  image_proxy: $IMAGE_PROXY
ui:
  static_use_hash: true
redis:
  url: redis://redis:6379/0
search:
  formats:
    - html
    - json
EOF
```

Для изменения порта или использования существующего Nginx отредактируйте `docker-compose.yaml`:

```yaml
version: "3.7"

services:
# Удалите этот блок, если используете локальный Nginx
  caddy:
    container_name: caddy
    image: docker.io/library/caddy:2-alpine
    network_mode: host
    restart: unless-stopped
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy-data:/data:rw
      - caddy-config:/config:rw
    environment:
      - SEARXNG_HOSTNAME=${SEARXNG_HOSTNAME:-http://localhost}
      - SEARXNG_TLS=${LETSENCRYPT_EMAIL:-internal}
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"
# Удалите этот блок, если используете локальный Nginx
  redis:
    container_name: redis
    image: docker.io/valkey/valkey:8-alpine
    command: valkey-server --save 30 1 --loglevel warning
    restart: unless-stopped
    networks:
      - searxng
    volumes:
      - valkey-data2:/data
    cap_drop:
      - ALL
    cap_add:
      - SETGID
      - SETUID
      - DAC_OVERRIDE
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"

  searxng:
    container_name: searxng
    image: docker.io/searxng/searxng:latest
    restart: unless-stopped
    networks:
      - searxng
    # Порт по умолчанию: 8080, пример для порта 8000: "127.0.0.1:8000:8080"
    ports:
      - "127.0.0.1:8080:8080"
    volumes:
      - ./searxng:/etc/searxng:rw
    environment:
      - SEARXNG_BASE_URL=https://${SEARXNG_HOSTNAME:-localhost}/
      - UWSGI_WORKERS=${SEARXNG_UWSGI_WORKERS:-4}
      - UWSGI_THREADS=${SEARXNG_UWSGI_THREADS:-4}
    cap_drop:
      - ALL
    cap_add:
      - CHOWN
      - SETGID
      - SETUID
    logging:
      driver: "json-file"
      options:
        max-size: "1m"
        max-file: "1"

networks:
  searxng:

volumes:
# Удалите при использовании локального Nginx
  caddy-data:
  caddy-config:
# Удалите при использовании локального Nginx
  valkey-data2:
```

Запустите через `docker compose up -d`. Логи: `docker compose logs -f searxng`.

### Настройка Nginx и HTTP-аутентификации

Для панелей управления (например, BT или 1Panel) настройте реверсивный прокси и добавьте в конфиг Nginx:

```conf
server
{
    listen 443 ssl;

    # Ваш домен
    server_name search.example.com;

    # SSL-сертификаты
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    location / {
        # Добавьте эти строки
        auth_basic "Введите имя пользователя и пароль";
        auth_basic_user_file /etc/nginx/conf.d/search.htpasswd;

        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_protocol_addr;
        proxy_pass http://127.0.0.1:8000;
        client_max_body_size 0;
    }

    # access_log  ...;
    # error_log  ...;
}
```

Создайте файл паролей (замените `example_name` и `example_password`):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Перезапустите Nginx. Проверьте доступ через браузер:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Настройка в Cherry Studio

После развертывания SearXNG настройте Cherry Studio.

Перейдите в настройки веб-поиска → Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

При локальном развертывании проверка может завершиться ошибкой:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

Это происходит из-за отсутствия поддержки JSON. Измените конфигурацию в Docker.

В Docker Desktop найдите конфигурационный файл:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Раскройте папки:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Найдите **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Откройте редактор:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

В строке 78 добавьте `json`:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Сохраните и перезапустите контейнер:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Теперь проверка завершится успешно:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Адрес можно указать локальный (`http://localhost:порт`) или Docker (`http://host.docker.internal:порт`).

Для серверного развертывания с аутентификацией введите учетные данные:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

### Дополнительные настройки

SearXNG использует настройки по умолчанию. Для изменения поисковых систем:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Измените конфигурацию для интеграции с языковыми моделями:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Пример настройки языка:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

## Частые проблемы

### Отсутствие формата JSON

Добавьте `json` в форматы ответа:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Ошибка поисковой системы

Cherry Studio использует двигатели с категориями `web general`. Google недоступен в некоторых регионах. Добавьте приоритет для Baidu:

```yaml
use_default_settings:
  engines:
    keep_only:
      - baidu
engines:
  - name: baidu
    engine: baidu 
    categories: 
      - web
      - general
    disabled: false
```

### Высокая скорость запросов

Отключите ограничитель в настройках:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>