---
icon: searchengin
---

{% hint style="warning" %}
Ten dokument został przetłumaczony z chińskiego przez AI i nie został jeszcze zweryfikowany.
{% endhint %}

```markdown
# Wdrażanie i konfiguracja SearXNG

CherryStudio obsługuje wyszukiwanie w sieci za pośrednictwem SearXNG — projektu open source, który można wdrożyć lokalnie lub na serwerze. Jego konfiguracja różni się nieco od innych rozwiązań wymagających dostawców API.

**Link do projektu SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## Zalety SearXNG

* Open source i bezpłatne, bez potrzeby używania API
* Wysoki poziom prywatności
* Możliwość wysokiego stopnia dostosowania

## Wdrażanie lokalne

### 1. Bezpośrednie wdrażanie za pomocą Dockera

Ponieważ SearXNG nie wymaga skomplikowanej konfiguracji środowiska, można go wdrożyć bez użycia docker compose — wystarczy zapewnić wolny port. Najszybszą metodą jest pobranie obrazu Dockera i bezpośrednie wdrożenie.

#### 1. Pobierz, zainstaluj i skonfiguruj [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Po instalacji wybierz ścieżkę przechowywania obrazów:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Wyszukaj i pobierz obraz SearXNG

Wpisz **searxng** w pasku wyszukiwania:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Pobierz obraz:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Uruchom obraz

Po pomyślnym pobraniu przejdź do zakładki **Images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Wybierz pobrany obraz i kliknij "Run":

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Otwórz ustawienia, aby skonfigurować:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Dla przykładu portu `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Po pomyślnym uruchomieniu kliknij link, aby otworzyć interfejs frontend SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Pojawienie się tej strony oznacza, że wdrożenie zakończyło się sukcesem:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Wdrażanie na serwerze

Ponieważ instalacja Dockera w systemie Windows jest kłopotliwa, użytkownicy mogą wdrożyć SearXNG na serwerze i udostępniać go innym. Niestety, SearXNG nie obsługuje jeszcze uwierzytelniania, co oznacza, że inni mogą nadużywać Twojej instancji.

Cherry Studio obsługuje teraz [HTTP Basic Authentication (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Jeśli udostępniasz instancję SearXNG publicznie, **koniecznie** skonfiguruj uwierzytelnianie podstawowe za pomocą oprogramowania takiego jak Nginx. Poniżej krótki przewodnik wymagający podstawowej wiedzy o administrowaniu Linuxem.

### Wdrażanie SearXNG

Podobnie używamy Dockera. Zakładając, że masz już zainstalowany najnowszy Docker CE według [oficjalnego przewodnika](https://docs.docker.com/engine/install), poniższe polecenia nadają się do nowej instalacji w Debianie:

```bash
sudo apt update
sudo apt install git -y

# Pobierz oficjalne repozytorium
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Jeśli Twój serwer ma małą przepustowość, możesz ustawić na false
export IMAGE_PROXY=true

# Zmodyfikuj plik konfiguracyjny
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# see https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url is defined in the SEARXNG_BASE_URL environment variable, see .env and docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # can be disabled for a private instance
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

Jeśli chcesz zmienić port lokalny lub użyć istniejącego Nginxa, edytuj `docker-compose.yaml`:

```yaml
version: "3.7"

services:
# Jeśli nie potrzebujesz Caddy i chcesz ponownie użyć istniejącego Nginxa, usuń poniższe
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
# Jeśli nie potrzebujesz Caddy i chcesz ponownie użyć istniejącego Nginxa, usuń powyższe
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
    # Domyślnie mapowany na port 8080 hosta. Jeśli chcesz nasłuchiwać na porcie 8000, zmień na "127.0.0.1:8000:8080"
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
# Jeśli nie potrzebujesz Caddy i chcesz ponownie użyć istniejącego Nginxa, usuń poniższe
  caddy-data:
  caddy-config:
# Jeśli nie potrzebujesz Caddy i chcesz ponownie użyć istniejącego Nginxa, usuń powyższe
  valkey-data2:
```

Wykonaj `docker compose up -d`, aby uruchomić. Użyj `docker compose logs -f searxng` do przeglądania logów.

### Konfiguracja odwrotnego proxy Nginx i uwierzytelniania podstawowego

Jeśli używasz panelu (np. Baota lub 1Panel), skonfiguruj odwrotne proxy w Nginx, a następnie zmodyfikuj konfigurację zgodnie z przykładem:

```conf
server
{
    listen 443 ssl;

    # Ta linia to Twoja nazwa hosta
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # Jeśli skonfigurowano SSL, powinny być te dwie linie
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Domyślna konfiguracja odwrotnego proxy
    location / {
        # Dodaj te dwie linie w bloku location
        auth_basic "Please enter your username and password";
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

Utwórz plik haseł (zmień `example_name` i `example_password`):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Uruchom ponownie Nginx. Dostęp do strony powinien teraz wymagać uwierzytelnienia:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Konfiguracja w Cherry Studio

Po pomyślnym wdrożeniu SearXNG, przejdź do ustawień wyszukiwania w CherryStudio i wybierz Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Wprowadź adres lokalnej instancji (początkowo weryfikacja może nie powieść się):

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

Aby rozwiązać problem, dodaj typ zwrotu JSON w pliku `settings.yml` (znajdź go w kontenerze Dockera):

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Dodaj `json` w linii 78:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Zapisz zmiany i uruchom ponownie kontener:

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Weryfikacja powinna teraz zakończyć się sukcesem:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Adresy możliwe do użycia:
- Lokalny: `http://localhost:[port]`
- Adres Dockera: `http://host.docker.internal:[port]`

Dla instancji z uwierzytelnianiem HTTP dodaj dane logowania w Cherry Studio:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

### Inne konfiguracje

Domyślne ustawienia wyszukiwarki w interfejsie nie wpływają na konfigurację używaną przez modele AI. Aby dostosować wyszukiwarki dla modeli, edytuj plik konfiguracyjny:

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Referencje konfiguracji języków:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

## Typowe problemy z weryfikacją

### Brak formatu JSON
Dodaj `json` w sekcji formatów:
<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Niepoprawna konfiguracja wyszukiwarki
Dodaj do konfiguracji, aby wymusić używanie Baidu:
```
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

### Ograniczenie limitera
Wyłącz limiter w ustawieniach:
<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>
```