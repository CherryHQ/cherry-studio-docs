---
icon: searchengin
---

{% hint style="warning" %}
यह दस्तावेज़ AI द्वारा चीनी से अनुवादित किया गया है और अभी तक इसकी समीक्षा नहीं की गई है।
{% endhint %}

# SearXNG तैनाती और विन्यास

CherryStudio SearXNG के माध्यम से वेब खोज का समर्थन करता है। SearXNG एक ओपन-सोर्स प्रोजेक्ट है जिसे स्थानीय रूप से या सर्वर पर तैनात किया जा सकता है, इसलिए यह अन्य API प्रदाताओं से थोड़ा अलग है।

**SearXNG प्रोजेक्ट लिंक**: [SearXNG](https://github.com/searxng/searxng)

## SearXNG के फायदे

* ओपन-सोर्स और मुफ़्त, कोई API की ज़रूरत नहीं
* अपेक्षाकृत उच्च गोपनीयता
* उच्च स्तर पर अनुकूलन योग्य

## स्थानीय तैनाती

### १. डायरेक्ट Docker तैनाती

SearXNG को कॉम्प्लेक्स एनवायरनमेंट कॉन्फ़िगरेशन की आवश्यकता नहीं होती और एक खाली पोर्ट के साथ तैनात किया जा सकता है। इसलिए Docker का उपयोग करके सीधे इमेज खींचना सबसे तेज़ तरीका है।

#### १. [docker](https://www.docker.com/) डाउनलोड, इंस्टॉल और कॉन्फ़िगर करें

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

इंस्टॉल करने के बाद एक इमेज स्टोरेज पथ चुनें:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### २. SearXNG इमेज खोजें और खींचें

सर्च बार में **searxng** टाइप करें:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

इमेज खींचें:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### ३. इमेज चलाएँ

खींचने के बाद **images** पेज पर जाएँ:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

खींची गई इमेज को चुनकर रन पर क्लिक करें:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

कॉन्फ़िगर करने के लिए सेटिंग्स खोलें:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

`8085` पोर्ट के उदाहरण में:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

सफलतापूर्वक चलने पर लिंक पर क्लिक करके SearXNG इंटरफ़ेस खोलें:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

यह पेज दिखे तो तैनाती सफल हुई:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## सर्वर तैनाती

Windows पर Docker इंस्टॉल करना जटिल हो सकता है, इसलिए आप SearXNG को किसी सर्वर पर तैनात कर सकते हैं। हालाँकि, SearXNG अभी ऑथेंटिकेशन सपोर्ट नहीं करता, इसलिए दूसरे इसका गलत इस्तेमाल कर सकते हैं।

इस समस्या के समाधान के लिए Cherry Studio [HTTP बेसिक ऑथेंटिकेशन (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication) सपोर्ट करता है। यदि आप SearXNG को पब्लिक नेटवर्क पर एक्सपोज़ कर रहे हैं, तो कृपया Nginx जैसे रिवर्स प्रॉक्सी सॉफ़्टवेयर के माध्यम से HTTP बेसिक ऑथेंटिकेशन कॉन्फ़िगर करें। नीचे एक संक्षिप्त ट्यूटोरियल है (मूल लिनक्स ज्ञान आवश्यक)।

### SearXNG तैनाती

इसी तरह Docker का उपयोग करें। मान लें कि आपने पहले से [ऑफ़िशियल ट्यूटोरियल](https://docs.docker.com/engine/install) के अनुसार Docker CE इंस्टॉल कर लिया है। Debian सिस्टम पर निम्नलिखित कमांड्स चलाएँ:

```bash
sudo apt update
sudo apt install git -y

# ऑफ़िशियल रिपॉजिटरी क्लोन करें
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# यदि सर्वर बैंडविड्थ कम है तो false सेट करें
export IMAGE_PROXY=true

# कॉन्फ़िग फ़ाइल बनाएँ
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

यदि पोर्ट बदलना चाहते हैं, तो `docker-compose.yaml` फ़ाइल एडिट करें:

```yaml
version: "3.7"

services:
# यदि Caddy की जरूरत न हो और पहले से Nginx मौजूद हो तो इस सेक्शन को हटाएँ
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
# यदि Caddy की जरूरत न हो और पहले से Nginx मौजूद हो तो इस सेक्शन को हटाएँ
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
    # डिफ़ॉल्ट पोर्ट 8080, 8000 पर लिसन करने के लिए "127.0.0.1:8000:8080" करें
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
# यदि Caddy की जरूरत न हो और पहले से Nginx मौजूद हो तो इस सेक्शन को हटाएँ
  caddy-data:
  caddy-config:
# यदि Caddy की जरूरत न हो और पहले से Nginx मौजूद हो तो इस सेक्शन को हटाएँ
  valkey-data2:
```

`docker compose up -d` चलाकर स्टार्ट करें। लॉग देखने के लिए `docker compose logs -f searxng` चलाएँ।

### Nginx रिवर्स प्रॉक्सी और HTTP बेसिक ऑथेंटिकेशन तैनाती

यदि आप Baota या 1Panel जैसे पैनल इस्तेमाल करते हैं, तो कृपया उनके डॉक्यूमेंट के अनुसार वेबसाइट जोड़ें और Nginx रिवर्स प्रॉक्सी कॉन्फ़िगर करें। फिर nginx कॉन्फ़िग फ़ाइल एडिट करें:

```conf
server
{
    listen 443 ssl;

    # आपका होस्टनाम
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL कॉन्फ़िगरेशन
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # लोकेशन ब्लॉक में ये दो लाइनें जोड़ें
    location / {
        auth_basic "कृपया अपना उपयोगकर्ता नाम और पासवर्ड दर्ज करें";
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

कॉन्फ़िग फ़ाइल `/etc/nginx/conf.d` में सेव करें। पासवर्ड फ़ाइल बनाने के लिए ये कमांड चलाएँ (`example_name` और `example_password` अपने यूज़रनेम/पासवर्ड से बदलें):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Nginx को रीस्टार्ट करें। अब वेबपेज खोलने पर यूज़रनेम/पासवर्ड मांगेगा। सही कॉन्फ़िगरेशन चेक करने के लिए अपना क्रिडेंशियल्स डालकर SearXNG पेज ओपन करें।

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio सम्बंधित विन्यास

SearXNG तैनात होने के बाद CherryStudio के लिए कॉन्फ़िगर करें।

नेटवर्क सर्च सेटिंग्स पर जाकर Searxng चुनें:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

स्थानीय लिंक डालने पर वेरिफ़िकेशन विफल हो सकता है:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

यह इसलिए क्योंकि डिफ़ॉल्ट रूप से json रिटर्न टाइप कॉन्फ़िगर नहीं होता। कॉन्फ़िग फ़ाइल बदलने की ज़रूरत है।

Docker के Files टैब पर जाकर टैग्ड फ़ोल्डर ढूंढें:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

आगे बढ़ें और अन्य टैग्ड फ़ोल्डर खोलें:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

**settings.yml** कॉन्फ़िग फ़ाइल खोलें:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

फ़ाइल एडिटर खोलें:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

लाइन 78 पर, फॉर्मेट्स में सिर्फ html है:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

json जोड़ें और सेव करके इमेज को रीस्टार्ट करें:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Cherry Studio पर वापस जाकर वेरिफ़ाई करें, सफल होगा:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

पता के रूप में दर्ज करें:
- स्थानीय: <http://localhost:पोर्ट>
- Docker: <http://host.docker.internal:पोर्ट>

यदि आपने पहले HTTP बेसिक ऑथेंटिकेशन कॉन्फ़िग किया है, तो वेरिफ़िकेशन 401 एरर देगा:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

क्लाइंट पर HTTP बेसिक ऑथेंटिकेशन कॉन्फ़िगर करें:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

अब वेरिफ़िकेशन सफल होगा।

### अन्य विन्यास

SearX