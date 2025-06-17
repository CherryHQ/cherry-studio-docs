---
icon: searchengin
---

{% hint style="warning" %}
This document was translated from Chinese by AI and has not yet been reviewed.
{% endhint %}

# SearXNG Deployment and Configuration

CherryStudio supports web searches through SearXNG. SearXNG is an open-source project that can be deployed locally or on a server, so its configuration is slightly different from other methods that require an API provider.

**SearXNG Project Link**: [SearXNG](https://github.com/searxng/searxng)

## Advantages of SearXNG

*   Open-source and free, no API required
*   Relatively high privacy
*   Highly customizable

## Local Deployment

### 1. Direct Deployment with Docker

Since SearXNG does not require a complex environment setup, you can deploy it without using docker compose. Simply providing an available port is sufficient. Therefore, the quickest method is to directly pull the image and deploy it using Docker.

#### 1. Download, install, and configure [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

After installation, select a path to store images:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Search for and pull the SearXNG image

Enter **searxng** in the search bar:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Pull the image:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Run the image

After the pull is successful, go to the **images** page:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Select the pulled image and click Run:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Open the settings to configure:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Using port `8085` as an example:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

After it starts successfully, click the link to open the SearXNG frontend interface:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

This page indicates a successful deployment:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Server Deployment

Given that installing Docker on Windows can be quite troublesome, users can deploy SearXNG on a server, which also allows sharing it with others. Unfortunately, SearXNG itself does not currently support authentication, meaning others could scan for and abuse your deployed instance through technical means.

To address this, Cherry Studio now supports configuring [HTTP Basic Authentication (RFC7617)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Authentication). If you plan to expose your self-deployed SearXNG to the public internet, you **must** configure HTTP Basic Authentication using a reverse proxy software like Nginx. The following is a brief tutorial that requires basic Linux system administration knowledge.

### Deploying SearXNG

Similarly, we will still use Docker for deployment. Assuming you have already installed the latest version of Docker CE on your server following the [official tutorial](https://docs.docker.com/engine/install), here is a one-stop command for a fresh installation on a Debian system:

```bash
sudo apt update
sudo apt install git -y

# Clone the official repository
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# If your server has low bandwidth, you can set this to false
export IMAGE_PROXY=true

# Modify the configuration file
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

If you need to change the local listening port or reuse an existing local nginx, you can edit the `docker-compose.yaml` file. Refer to the following example:

```yaml
version: "3.7"

services:
# If you don't need Caddy and want to reuse an existing local Nginx, remove the section below. We don't need Caddy by default.
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
# If you don't need Caddy and want to reuse an existing local Nginx, remove the section above. We don't need Caddy by default.
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
    # By default, it maps to port 8080 on the host. If you want to listen on port 8000, change it to "127.0.0.1:8000:8080"
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
# If you don't need Caddy and want to reuse an existing local Nginx, remove the section below
  caddy-data:
  caddy-config:
# If you don't need Caddy and want to reuse an existing local Nginx, remove the section above
  valkey-data2:
```

Run `docker compose up -d` to start. Run `docker compose logs -f searxng` to view the logs.

### Deploying Nginx Reverse Proxy and HTTP Basic Authentication

If you are using a server control panel like Baota Panel or 1Panel, please refer to their documentation to add a website and configure the nginx reverse proxy. Then, find where to modify the nginx configuration file and make changes based on the example below:

```conf
server
{
    listen 443 ssl;

    # This line is your hostname
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # If you have configured SSL, you should have these two lines
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # When configuring a reverse proxy through a panel, the default location block looks like this
    location / {
        # Just add the two lines below to the location block, leaving everything else as is.
        # This example assumes your configuration file is saved in the /etc/nginx/conf.d/ directory.
        # For Baota, it would likely be saved in a directory like /www, so be aware of that.
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

Assuming the Nginx configuration file is saved in `/etc/nginx/conf.d`, we will save the password file in the same directory.

Execute the command (replace `example_name` and `example_password` with the username and password you intend to set):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Restart Nginx (reloading the configuration also works).

Now, try opening the webpage. You should be prompted to enter a username and password. Enter the credentials you set earlier to see if you can successfully access the SearXNG search page, thereby checking if the configuration is correct.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio Related Configuration

After successfully deploying SearXNG locally or on a server, the next step is to configure it in CherryStudio.

Go to the Web Search settings page and select Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

If you enter the link for the local deployment directly and validation fails, don't worry:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

This is because a direct deployment does not have the json return type configured by default, so data cannot be retrieved. You need to modify the configuration file.

Go back to Docker, and in the Files tab, find the tagged folder within the image:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

After expanding it, scroll down further, and you will find another tagged folder:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Expand it again and find the **settings.yml** configuration file:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Click to open the file editor:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Find line 78. You will see that the only type is html

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Add the json type, save, and restart the image

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Return to Cherry Studio to validate again. Validation successful:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

The address can be either local: `http://localhost:<port_number>`
or the Docker address: `http://host.docker.internal:<port_number>`

If you followed the previous example to deploy on a server and correctly configured the reverse proxy, the json return type will already be enabled. After entering the address and validating, since HTTP Basic Authentication has been configured for the reverse proxy, the validation should now return a 401 error code:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

Configure HTTP Basic Authentication in the client, entering the username and password you just set:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

Validate, and it should succeed.

### Other Configurations

At this point, SearXNG has default web search capabilities. If you need to customize the search engines, you need to configure it yourself.

Note that the preferences here do not affect the configuration when called by the large model.

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

To configure the search engines that the large model will use, you need to set them in the configuration file:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Language configuration reference:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

If the content is too long and inconvenient to edit directly, you can copy it to a local IDE, modify it, and then paste it back into the configuration file.

## Common Reasons for Validation Failure

### JSON format not added to return formats

Add json to the return formats in the configuration file:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Search engine not configured correctly

Cherry Studio defaults to selecting engines whose categories include both "web" and "general" for searching. By default, engines like Google are selected, which fails in mainland China due to access restrictions. Adding the following configuration to force searxng to use the Baidu engine can solve the problem:

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

### Access rate is too fast

The limiter setting in searxng is blocking API access. Please try setting it to false in the settings:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>