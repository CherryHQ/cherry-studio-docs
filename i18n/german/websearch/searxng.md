---
icon: searchengin
---

{% hint style="warning" %}
Dieses Dokument wurde von einer KI aus dem Chinesischen übersetzt und ist noch nicht überprüft worden.
{% endhint %}

# Bereitstellung und Konfiguration von SearXNG

CherryStudio unterstützt Websuche über SearXNG. SearXNG ist ein Open-Source-Projekt, das lokal oder auf einem Server bereitgestellt werden kann und sich daher von anderen Konfigurationen unterscheidet, die API-Anbieter erfordern.

**SearXNG-Projektlink**: [SearXNG](https://github.com/searxng/searxng)

## Vorteile von SearXNG

* Open Source und kostenlos, ohne API erforderlich
* Relativ hohe Privatsphäre
* Hochgradig anpassbar

## Lokale Bereitstellung

### 1. Direkte Bereitstellung mit Docker

Da SearXNG keine komplexe Umgebungskonfiguration benötigt, kann Docker ohne docker compose verwendet werden. Ein freier Port genügt für die Bereitstellung. Die schnellste Methode ist das direkte Abrufen des Docker-Images.

#### 1. Docker [herunterladen](https://www.docker.com/), installieren und konfigurieren

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Nach der Installation einen Image-Speicherpfad auswählen:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. SearXNG-Image suchen und abrufen

In der Suchleiste **searxng** eingeben:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Image abrufen:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Image ausführen

Nach erfolgreichem Abruf zur **Images**-Seite navigieren:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Abgerufenes Image auswählen und starten:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Einstellungen zur Konfiguration öffnen:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Am Beispiel von Port `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Nach erfolgreichem Start den Link öffnen, um die SearXNG-Oberfläche aufzurufen:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Diese Seite zeigt eine erfolgreiche Bereitstellung an:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Serverbereitstellung

Da die Docker-Installation unter Windows aufwändig ist, können Nutzer SearXNG auf einem Server bereitstellen. Jedoch unterstützt SearXNG derzeit keine Authentifizierung, was zu Missbrauch führen kann.

Cherry Studio unterstützt nun [HTTP Basic Authentication (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Bei öffentlicher Bereitstellung **unbedingt** über Nginx konfigurieren. Kurzanleitung für Linux-Server:

### SearXNG bereitstellen

Ähnlich mit Docker. Bei installiertem Docker CE (nach [offizieller Anleitung](https://docs.docker.com/engine/install)):

```bash
sudo apt update
sudo apt install git -y

# Offizielles Repository abrufen
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Bei geringer Bandbreite auf false setzen
export IMAGE_PROXY=true

# Konfigurationsdatei anpassen
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

Für Portänderungen oder bestehenden Nginx `docker-compose.yaml` anpassen:

```yaml
version: "3.7"

services:
# Caddy entfernen, wenn lokaler Nginx verwendet wird
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
# Caddy entfernen, wenn lokaler Nginx verwendet wird
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
    # Standard-Port 8080, für 8000 auf "127.0.0.1:8000:8080" ändern
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
# Entfernen, wenn lokaler Nginx verwendet wird
  caddy-data:
  caddy-config:
# Entfernen, wenn lokaler Nginx verwendet wird
  valkey-data2:
```

Mit `docker compose up -d` starten. Logs mit `docker compose logs -f searxng` anzeigen.

### Nginx Reverse Proxy und HTTP Basic Authentication

Bei Serverpanels (z.B. Baota, 1Panel) Nginx-Konfiguration anpassen:

```conf
server
{
    listen 443 ssl;

    # Ihr Hostname
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # Bei SSL konfiguriert:
    ssl_certificate    /pfad/zum/cert/fullchain.pem;
    ssl_certificate_key    /pfad/zum/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    location / {
        # Diese beiden Zeilen hinzufügen
        auth_basic "Benutzername und Passwort eingeben";
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

Passwortdatei erstellen (Benutzername/Passwort ersetzen):

```bash
echo "benutzername:$(openssl passwd -5 'passwort')" > /etc/nginx/conf.d/search.htpasswd
```

Nginx neustarten. Die Authentifizierung sollte jetzt funktionieren:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio Konfiguration

Nach erfolgreicher SearXNG-Bereitstellung in Cherry Studio konfigurieren.

In den Web-Such-Einstellungen Searxng auswählen:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Bei lokaler Bereitstellung schlägt die Validierung zunächst fehl:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

JSON-Rückgabetyp ist standardmäßig deaktiviert. Konfiguration anpassen.

In Docker zur Registerkarte "Files" navigieren:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Zum beschrifteten Ordner navigieren:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

**settings.yml** finden und öffnen:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Zeile 78: Nur HTML ist aktiviert

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

JSON hinzufügen, speichern und Image neu starten:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Validierung sollte jetzt erfolgreich sein:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Adresse kann sein:
- Lokal: <http://localhost>:Portnummer
- Docker: <http://host.docker.internal>:Portnummer

Bei Serverbereitstellung mit Authentifizierung tritt Fehler 401 auf:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

HTTP Basic Authentication konfigurieren:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

### Weitere Konfigurationen

Suchmaschinen können angepasst werden:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Für KI-Modellintegration Konfigurationsdatei bearbeiten:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Sprachreferenz:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

## Häufige Validierungsfehler

### JSON-Format nicht aktiviert

JSON in der Konfiguration hinzufügen:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Suchmaschinen fehlerhaft konfiguriert

Cherry Studio erfordert Kategorien mit "web" und "general". Beispiel für Baidu:

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

### Zu viele Anfragen

Limiter in den Einstellungen deaktivieren:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>