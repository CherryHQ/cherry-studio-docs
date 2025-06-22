---
icon: searchengin
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# SearXNG Deployment and Configuration

Cherry Studio supports web search via SearXNG, an open-source project deployable both locally and on servers. Its configuration differs slightly from other setups requiring API providers.

**SearXNG Project Link**: [SearXNG](https://github.com/searxng/searxng)

## Advantages of SearXNG
* Open-source and free, no API required
* Relatively high privacy
* Highly customizable

## Local Deployment

### 1. Direct Deployment with Docker
SearXNG doesn't require complex environment configuration and can deploy using Docker with just a single available port.

#### 1. Download, install, and configure [docker](https://www.docker.com/)
<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

After installation, select an image storage path:
<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Search and pull the SearXNG image
Enter **searxng** in the search bar:
<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Pull the image:
<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>
<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Run the image
After successful pull, go to **Images**:
<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Select the pulled image and click run:
<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Open settings for configuration:
<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Take port `8085` as example:
<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

After successful run, open SearXNG frontend via link:
<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

This page indicates successful deployment:
<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Server Deployment
Since Docker installation on Windows can be cumbersome, users can deploy SearXNG on servers for sharing. Unfortunately, SearXNG currently lacks built-in authentication, making deployed instances vulnerable to scanning and abuse.

To address this, Cherry Studio supports [HTTP Basic Authentication (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). If exposing SearXNG publicly, **you must configure HTTP Basic Authentication** via reverse proxies like Nginx. This tutorial assumes basic Linux operations knowledge.

### Deploy SearXNG
Similarly deploy via Docker. Assuming Docker CE is installed per [official guide](https://docs.docker.com/engine/install), run these commands on fresh Debian systems:

```bash
sudo apt update
sudo apt install git -y

# Pull official repo
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Set to false for limited server bandwidth
export IMAGE_PROXY=true

# Modify config
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

Edit `docker-compose.yaml` to change ports or reuse existing Nginx:

```yaml
version: "3.7"

services:
# Remove below if reusing existing Nginx instead of Caddy
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
# Remove above if reusing existing Nginx instead of Caddy
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
    # Default host port:8080, change to "127.0.0.1:8000:8080" for port 8000
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
# Remove below if reusing existing Nginx
  caddy-data:
  caddy-config:
# Remove above if reusing existing Nginx
  valkey-data2:
```

Start with `docker compose up -d`. View logs using `docker compose logs -f searxng`.

### Deploy Nginx Reverse Proxy and HTTP Basic Authentication
For server panels like Baota or 1Panel:
1. Add site and configure Nginx reverse proxy per their docs
2. Locate Nginx config, modify per below example:

```conf
server
{
    listen 443 ssl;

    # Your hostname
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL config
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Reverse proxy config
    location / {
        # Add these two lines in location block
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

Save password file in `/etc/nginx/conf.d`:

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Restart or reload Nginx. Access should prompt for credentials:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio Configuration
After successful SearXNG deployment:

1. Go to web search settings > Select Searxng
<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

2. Initial verification may fail due to missing JSON format:
<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

3. In Docker > Files tab, locate tagged folder > settings.yml
<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>
<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>
<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

4. Edit file, add "json" to formats (line 78)
<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>
<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

5. Rerun image
<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

6. Successful verification in Cherry Studio
<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Use:
- Local: http://localhost:port
- Docker: http://host.docker.internal:port

For server deployments with HTTP Basic Authentication:
1. Initial verification returns 401
<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

2. Configure credentials in client:
<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

### Additional Configuration
To customize search engines:
- Default preferences don't affect model invocations
<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

- Configure model-invoked engines in settings.yml:
<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>
<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Syntax reference:
<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

For lengthy edits, modify in local IDE then paste back.

## Common Verification Failures

### Missing JSON Format
Add "json" to return formats:
<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Incorrect Search Engine Configuration
Cherry Studio defaults to engines with "web" and "general" categories (e.g., Google). In mainland China, force Baidu:

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

### Excessive Access Rate
Disable limiter in settings:
<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>