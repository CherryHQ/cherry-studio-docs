---
icon: searchengin
---

{% hint style="warning" %}
Questo documento è stato tradotto dal cinese tramite IA e non è ancora stato revisionato.
{% endhint %}

# Deployment e Configurazione di SearXNG

CherryStudio supporta la ricerca web tramite SearXNG, un progetto open source che può essere distribuito localmente o su server, quindi la configurazione è leggermente diversa rispetto ad altri approcci che richiedono fornitori API.

**Link al progetto SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## Vantaggi di SearXNG

*   Open source e gratuito, nessuna API richiesta
*   Maggiore tutela della privacy
*   Elevata personalizzazione

## Distribuzione Locale

### I. Distribuzione Diretta con Docker

Dato che SearXNG non richiede configurazioni ambientali complesse ed è possibile distribuirlo senza Docker Compose fornendo semplicemente una porta libera, il metodo più rapido è utilizzare Docker per scaricare direttamente l'immagine.

#### 1. Scarica e installa [Docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Dopo l'installazione, scegli un percorso per archiviare le immagini:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Cerca e scarica l'immagine di SearXNG

Digita **searxng** nella barra di ricerca:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Scarica l'immagine:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Esegui l'immagine

Dopo lo scaricamento, vai alla pagina **images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Seleziona l'immagine scaricata e fai clic su "Run":

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Apri le impostazioni per configurarlo:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Esempio con porta `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Dopo l'avvio corretto, fai clic sul link per accedere all'interfaccia frontend di SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Questa pagina indica che la distribuzione ha avuto successo:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Distribuzione su Server

Considerando che l'installazione di Docker su Windows può essere complessa, gli utenti possono distribuire SearXNG su un server, condividendolo anche con altri. Tuttavia, SearXNG non supporta attualmente l'autenticazione, consentendo ad altri di rilevare e abusare della tua istanza tramite tecniche di scansione.

Pertanto, Cherry Studio supporta ora la configurazione dell'[Autenticazione HTTP di Base (RFC7617)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). Se si espone SearXNG in rete pubblica, configurare **obbligatoriamente** l'autenticazione di base tramite software proxy inverso come Nginx. Di seguito una breve guida che richiede conoscenze Linux di base.

### Distribuire SearXNG

Utilizzare Docker per la distribuzione. Supponendo che Docker CE sia già installato sul server seguendo le [istruzioni ufficiali](https://docs.docker.com/engine/install), ecco comandi completi per un'installazione su sistema Debian:

```bash
sudo apt update
sudo apt install git -y

# Clona repository ufficiale
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Se la banda del server è limitata, impostare su false
export IMAGE_PROXY=true

# Modifica file configurazione
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

Per modificare la porta locale o riutilizzare un Nginx esistente, modificare `docker-compose.yaml`:

```yaml
version: "3.7"

services:
# Rimuovere se non serve Caddy e si riutilizza Nginx esistente
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
# Rimuovere se non serve Caddy e si riutilizza Nginx esistente
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
    # Default porta host 8080. Per ascoltare su 8000 modificare in "127.0.0.1:8000:8080"
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
# Rimuovere se non serve Caddy
  caddy-data:
  caddy-config:
# Rimuovere se non serve Caddy
  valkey-data2:
```

Eseguire `docker compose up -d` per avviare. Verificare i log con `docker compose logs -f searxng`.

### Configurare Proxy Inverso Nginx e Autenticazione di Base

Se si utilizza un pannello server come Baota o 1Panel, consultare la documentazione per aggiungere un sito e configurare il proxy inverso Nginx. Modificare il file di configurazione come nell'esempio:

```conf
server
{
    listen 443 ssl;

    # Nome host
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # Configurazione SSL
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS (opzionale)
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Blocco location predefinito per proxy inverso
    location / {
        # Aggiungere le seguenti righe
        auth_basic "Inserisci nome utente e password";
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

Supponendo che il file di configurazione Nginx sia in `/etc/nginx/conf.d`, creare il file delle password:

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Riavviare Nginx (o ricaricare la configurazione). Accedere alla pagina web e inserire le credenziali per verificare la configurazione.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Configurazione di Cherry Studio

Dopo aver distribuito correttamente SearXNG localmente o su server, procedere con la configurazione in Cherry Studio.

Accedere alla pagina delle impostazioni di ricerca web, selezionare Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Inserendo il link locale, la verifica potrebbe fallire:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

La distribuzione predefinita non supporta il formato JSON, modificare il file di configurazione.

In Docker, nella scheda Files, trovare la cartella con tag:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Continuare fino a un'altra cartella con tag:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Trovare il file di configurazione **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Aprire l'editor del file:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Alla riga 78, è presente solo il tipo html:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Aggiungere il tipo JSON, salvare e rieseguire l'immagine:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Ritornare in Cherry Studio e verificare nuovamente:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

L'indirizzo può essere locale: <http://localhost> :porta\
Oppure indirizzo Docker: <http://host.docker.internal> :porta

Per la distribuzione su server con autenticazione configurata, inserire l'indirizzo. La verifica restituirà errore 401:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

Configurare l'autenticazione di base nel client inserendo nome utente e password:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

La verifica dovrebbe ora riuscire.

### Altre Configurazioni

SearXNG ha ora capacità di ricerca predefinite. Per personalizzare i motori di ricerca, configurare manualmente.

Le preferenze nella pagina non influenzano le chiamate dei modelli di grandi dimensioni:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Per configurare i motori di ricerca per i modelli di grandi dimensioni, modificare il file di configurazione:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Guida di configurazione lingua:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

Per modifiche lunghe, copiare il contenuto in un IDE locale e reincollare dopo le modifiche.

## Cause Comuni di Verifica Fallita

### Formato di Restituzione JSON Mancante

Aggiungere JSON al formato di restituzione nel file di configurazione:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Motori di Ricerca Configurati Incorrettamente

Cherry Studio seleziona predefinitamente motori con categorie `web` e `general`. Poiché Google è bloccato in Cina, aggiungere la configurazione per forzare l'uso di Baidu:

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

### Frequenza di Accesso Troppo Elevata

La configurazione `limiter` di SearXNG blocca le chiamate API. Impostare su `false`:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>