---
icon: searchengin
---

{% hint style="warning" %}
Dit document is door AI vertaald vanuit het Chinees en is nog niet beoordeeld.
{% endhint %}

# SearXNG Implementatie en Configuratie

CherryStudio ondersteunt webzoekopdrachten via SearXNG, een open source project dat zowel lokaal als op een server kan worden geïmplementeerd. Dit verschilt van andere configuratiewijzen die API-providers vereisen.

**SearXNG projectlink**: [SearXNG](https://github.com/searxng/searxng)

## Voordelen van SearXNG

* Open source en gratis, geen API nodig
* Relatief hoge privacybescherming
* Zeer aanpasbaar

## Lokale Implementatie

### Eén: Direct implementeren met Docker

Omdat SearXNG geen complexe omgevingsconfiguratie vereist, kan het zonder docker compose worden geïmplementeerd door simpelweg een vrije poort beschikbaar te stellen. De snelste methode is direct implementeren met Docker.

#### 1. Download, installeer en configureer [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Selecteer na installatie een opslagpad voor afbeeldingen:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Zoek en download SearXNG-afbeelding

Typ **searxng** in de zoekbalk:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Download de afbeelding:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Draai de afbeelding

Ga na het downloaden naar de **images** pagina:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Selecteer de gedownloade afbeelding en klik op run:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Open instellingen voor configuratie:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Voorbeeld met poort `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Na succesvol opstarten opent u de SearXNG-interface via de link:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Deze pagina bevestigt een geslaagde implementatie:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Serverimplementatie

Omdat Docker installeren op Windows complex kan zijn, kunnen gebruikers SearXNG op een server implementeren en delen. SearXNG ondersteunt echter nog geen authenticatie, waardoor anderen uw instantie kunnen misbruiken.

Cherry Studio ondersteunt nu [HTTP Basic Authentication (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Configureer dit via Nginx of andere reverse proxy-software bij publicatie op internet. Hieronder vindt u een beknopte handleiding waarvoor basiskennis van Linux nodig is.

### Implementeer SearXNG

Implementeer met Docker. Na installatie van Docker CE via de [officiële handleiding](https://docs.docker.com/engine/install), gebruik deze commando's voor Debian-systemen:

```bash
sudo apt update
sudo apt install git -y

# Download officiële repository
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Stel in op false bij beperkte bandbreedte
export IMAGE_PROXY=true

# Pas configuratie aan
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

Pas zo nodig `docker-compose.yaml` aan voor poortconfiguratie:

```yaml
version: "3.7"

services:
# Verwijder onderstaande sectie indien Caddy niet nodig is
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
# Verwijder bovenstaande sectie indien Caddy niet nodig is
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
    # Wijzig poortindeling naar "127.0.0.1:8000:8080" voor poort 8000
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
# Verwijder indien Caddy niet nodig
  caddy-data:
  caddy-config:
# Verwijder bovenstaande indien Caddy niet nodig
  valkey-data2:
```

Start met `docker compose up -d`. Logs: `docker compose logs -f searxng`.

### Configureer Nginx Reverse Proxy en HTTP Basic Authentication

Gebruik bij serverpanels (zoals Baota of 1Panel) deze nginx-configuratie:

```conf
server
{
    listen 443 ssl;

    # Uw hostnaam
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL-configuratie
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    location / {
        # Voeg authenticatielijnen toe
        auth_basic "Voer gebruikersnaam en wachtwoord in";
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

Maak een wachtwoordbestand aan:

```bash
echo "gebruikersnaam:$(openssl passwd -5 'wachtwoord')" > /etc/nginx/conf.d/search.htpasswd
```

Herstart Nginx.

Log vervolgens in om configuratie te controleren:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio Configuratie

Na succesvolle SearXNG-implementatie:

Ga naar netwerkzoekinstellingen en selecteer Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Foutmelding bij lokale link? Dit is normaal:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

JSON-respons is standaard uitgeschakeld. Pas configuratie aan via Docker Files-tab:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Blader naar **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Open bestandseditor:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Voeg JSON toe aan regel 78:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Sla op en herstart:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Verificatie nu succesvol:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Gebruik:
- Lokaal: `http://localhost:poort`
- Docker: `http://host.docker.internal:poort`

Bij HTTP-basisauthenticatie verschijnt foutcode 401:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

Voeg credentials toe:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

Verificatie slaagt nu.

### Aanvullende configuratie

Standaard zoekfuncties zijn actief; voor maatwerk configureer zoekmachines.

Hoofdconfiguratie beïnvloedt geen modellaanroepen:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Configureer machines voor modellaanroepen in instellingen:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Taalreferentie:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

Bewerk grote configs extern en plak terug.

## Veelvoorkomende verificatiefouten

### JSON-respons niet ingeschakeld

Voeg toe in instellingen:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Onjuiste zoekmachineconfiguratie

Cherry Studio selecteert standaard machines met categorieën `web` én `general`. Deze oplossing forceert baidu:

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

### Te snel aanvragen

Zet limiter op false:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>