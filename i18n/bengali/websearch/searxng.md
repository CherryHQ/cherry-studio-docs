---
icon: searchengin
---

{% hint style="warning" %}
এই নথিটি এআই দ্বারা চীনা থেকে অনুবাদ করা হয়েছে এবং এখনও পর্যালোচনা করা হয়নি।
{% endhint %}

# SearXNG স্থাপন ও কনফিগারেশন

CherryStudio SearXNG এর মাধ্যমে ওয়েব অনুসন্ধান সমর্থন করে। SearXNG হল একটি ওপেন সোর্স প্রকল্প যা লোকালি বা সার্ভারে স্থাপন করা যায়। তাই অন্যান্য API প্রদানকারীদের কনফিগারেশনের চেয়ে এর পদ্ধতি কিছুটা ভিন্ন।

**SearXNG প্রকল্প লিঙ্ক**: [SearXNG](https://github.com/searxng/searxng)

## SearXNG এর সুবিধা

* ওপেন সোর্স ও বিনামূল্যে, API প্রয়োজন নেই
* তুলনামূলকভাবে উচ্চ গোপনীয়তা
* উচ্চ মাত্রায় কাস্টমাইজযোগ্য

## লোকাল স্থাপন

### ১. Docker দিয়ে সরাসরি স্থাপন

SearXNG এর জন্য জটিল পরিবেশ কনফিগারেশনের প্রয়োজন নেই, তাই docker compose ছাড়াই শুধু একটি ফাঁকা পোর্ট দিয়ে স্থাপন করা যায়। সবচেয়ে দ্রুততম উপায় হল Docker ইমেজ টেনে এনে সরাসরি স্থাপন করা।

#### ১. [docker](https://www.docker.com/) ডাউনলোড, ইনস্টল ও কনফিগার করুন

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

ইনস্টলেশনের পর একটি ইমেজ স্টোরেজ পাথ নির্বাচন করুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### ২. SearXNG ইমেজ খুঁজে টেনে আনুন

সার্চ বারে **searxng** লিখুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

ইমেজ টেনে আনুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### ৩. ইমেজ রান করুন

টেনে আনা সফল হলে **images** পেজে যান:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

টেনে আনা ইমেজ নির্বাচন করে রান করুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

সেটিংস খুলে কনফিগার করুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

`8085` পোর্ট উদাহরণ:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

রান সফল হলে লিঙ্কে ক্লিক করে SearXNG ফ্রন্টএন্ড ইন্টারফেস খুলুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

এই পেজ দেখলে স্থাপন সফল:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## সার্ভারে স্থাপন

Windows এ Docker ইনস্টল করা তুলনামূলক কষ্টসাধ্য, তাই ব্যবহারকারীরা SearXNG কে সার্ভারে স্থাপন করতে পারেন এবং অন্যদের সাথে শেয়ার করতে পারেন। তবে দুর্ভাগ্যবশত, SearXNG নিজেই অথেনটিকেশন সমর্থন করে না, ফলে অন্যদের দ্বারা স্ক্যান করে আপনার ইনস্ট্যান্স অপব্যবহার হতে পারে।

এজন্য, Cherry Studio বর্তমানে [HTTP বেসিক অথেনটিকেশন (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication) কনফিগার সমর্থন করে। যদি ব্যবহারকারীরা তাদের স্থাপিত SearXNG কে পাবলিক নেটওয়ার্কে এক্সপোজ করতে চান, তবে **অবশ্যই** Nginx এর মত রিভার্স প্রক্সি সফটওয়্যার দিয়ে HTTP বেসিক অথেনটিকেশন কনফিগার করুন। নীচে একটি সংক্ষিপ্ত টিউটোরিয়াল দেওয়া হল, যার জন্য মৌলিক লিনাক্স অপারেশন দক্ষতা প্রয়োজন।

### SearXNG স্থাপন

একইভাবে, Docker ব্যবহার করে স্থাপন করুন। ধরে নিন আপনি [অফিসিয়াল টিউটোরিয়াল](https://docs.docker.com/engine/install) অনুসারে সার্ভারে সর্বশেষ Docker CE ইনস্টল করেছেন। Debian সিস্টেমে নতুন ইনস্টলেশনের জন্য নীচে সম্পূর্ণ কমান্ড সিরিজ দেওয়া হল:

```bash
sudo apt update
sudo apt install git -y

# অফিসিয়াল রিপোজিটরি টেনে আনুন
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# যদি আপনার সার্ভার ব্যান্ডউইথ কম হয়, false সেট করতে পারেন
export IMAGE_PROXY=true

# কনফিগারেশন ফাইল পরিবর্তন করুন
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# দেখুন https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url SEARXNG_BASE_URL এনভায়রনমেন্ট ভ্যারিয়েবলে ডিফাইন্ড, .env ও docker-compose.yml দেখুন
  secret_key: $(openssl rand -hex 32)
  limiter: false  # প্রাইভেট ইনস্ট্যান্সের জন্য ডিজেবল করা যেতে পারে
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

আপনি যদি লোকাল লিসেন পোর্ট পরিবর্তন করতে বা বিদ্যমান nginx ব্যবহার করতে চান, `docker-compose.yaml` ফাইল এডিট করুন, নীচের উদাহরণ মেনে চালান:

```yaml
version: "3.7"

services:
# যদি Caddy এর প্রয়োজন না থাকে এবং লোকালে বিদ্যমান Nginx থাকে, তবে নীচের অংশ মুছে দিন। আমরা ডিফল্টভাবে Caddy ছাড়াই চালাই।
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
# যদি Caddy এর প্রয়োজন না থাকে এবং লোকালে বিদ্যমান Nginx থাকে, তবে উপরের অংশ মুছে দিন। আমরা ডিফল্টভাবে Caddy ছাড়াই চালাই।
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
    # ডিফল্টভাবে হোস্টের 8080 পোর্টে ম্যাপ করা, 8000 পোর্টে শুনতে চাইলে "127.0.0.1:8000:8080" করুন
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
# যদি Caddy এর প্রয়োজন না থাকে এবং লোকালে বিদ্যমান Nginx থাকে, তবে নীচের অংশ মুছে দিন
  caddy-data:
  caddy-config:
# যদি Caddy এর প্রয়োজন না থাকে এবং লোকালে বিদ্যমান Nginx থাকে, তবে উপরের অংশ মুছে দিন
  valkey-data2:
```

`docker compose up -d` চালু করুন। `docker compose logs -f searxng` দিয়ে লগ দেখতে পারেন।

### Nginx রিভার্স প্রক্সি ও HTTP বেসিক অথেনটিকেশন স্থাপন

আপনি যদি Baota Panel বা 1Panel এর মত সার্ভার প্যানেল ব্যবহার করেন, তাদের ডকুমেন্টেশন দেখে ওয়েবসাইট অ্যাড করুন এবং nginx রিভার্স প্রক্সি কনফিগার করুন। তারপর nginx কনফিগারেশন ফাইল এডিট করতে নীচের উদাহরণ মেনে চালান:

```conf
server
{
    listen 443 ssl;

    # এটা আপনার হোস্টনেম
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL কনফিগার থাকলে এই লাইন দুটি থাকা উচিত
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # ডিফল্ট রিভার্স প্রক্সি কনফিগারেশনের জন্য location ব্লক এভাবে
    location / {
        # শুধু location ব্লকে নিচের দুটি লাইন যোগ করুন, বাকিগুলো অপরিবর্তিত রাখুন
        # এখানে উদাহরণ ধরে নেওয়া হয়েছে আপনার কনফিগ ফাইল /etc/nginx/conf.d/ তে সেভ আছে
        # Baota প্যানেলে সাধারণত /www এর মত পাথে সেভ হয়, সতর্ক থাকুন
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

ধরে নিলাম Nginx কনফিগারেশন ফাইল `/etc/nginx/conf.d` তে সংরক্ষিত, পাসওয়ার্ড ফাইলও একই ডিরেক্টরিতে সংরক্ষণ করব।

নীচের কমান্ড চালান (`example_name`, `example_password` কে আপনার পছন্দের ইউজারনেম ও পাসওয়ার্ড দিয়ে প্রতিস্থাপন করুন):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Nginx রিস্টার্ট করুন (কনফিগ রিলোড করা যায়)।

এখন ওয়েবপেজ খুললে ইউজারনেম ও পাসওয়ার্ড লিখতে বলা হবে। পূর্ব নির্ধারিত ইউজারনেম ও পাসওয়ার্ড দিয়ে SearXNG অনুসন্ধান পেজ সফলভাবে খুলতে পারলে কনফিগারেশন সঠিক।

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio সম্পর্কিত কনফিগারেশন

SearXNG লোকাল বা সার্ভারে সফলভাবে স্থাপন হলে, CherryStudio তে সম্পর্কিত কনফিগারেশন করুন।

ওয়েব সার্চ সেটিংস পেজে গিয়ে Searxng নির্বাচন করুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

লোকাল স্থাপিত লিঙ্ক ইনপুট করলে ভেরিফিকেশন ব্যর্থ হতে পারে, এতে চিন্তা করবেন না:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

কারণ সোজাসুজি স্থাপন করলে json রিটার্ন টাইপ ডিফল্ট কনফিগার করা থাকে না, ডাটা আনতে ব্যর্থ হয়। কনফিগারেশন ফাইল মোডিফাই করতে হবে।

Docker এ ফিরে, Files ট্যাবে ইমেজের ট্যাগ করা ফোল্ডার খুঁজুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

এক্সপ্যান্ড করে নিচে স্ক্রল করুন, আরেকটি ট্যাগ করা ফোল্ডার পাবেন:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

আরও এক্সপ্যান্ড করে, **settings.yml** কনফিগারেশন ফাইল খুঁজুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

ফাইল এডিটর খুলতে ক্লিক করুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

৭৮ নম্বর লাইনে গিয়ে দেখুন টাইপ শুধু html আছে:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

json টাইপ অ্যাড করে সেভ করুন, ইমেজ পুনরায় রান করুন:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Cherry Studio তে ফিরে গিয়ে ভেরিফাই করুন, ভেরিফিকেশন সফল হবে:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

অ্যাড্রেস হিসেবে লোকাল দিতে পারেন: <http://localhost> : পোর্ট নম্বর\
বা Docker অ্যাড্রেস দিন: <http://host.docker.internal> : পোর্ট নম্বর

আগের উদাহরণ অনুসারে সার্ভারে স্থাপন ও রিভার্স প্রক্সি সঠিকভাবে কনফিগার করা থাকলে, এবং json রিটার্ন টাইপ চালু করা থাকলে। অ্যাড্রেস ইনপুট করে ভেরিফাই করার সময় HTTP বেসিক অথেনটিকেশন কনফিগার করা থাকায় ভেরিফিকেশন 401 এরর কোড ফেরত দেবে:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

ক্লায়েন্টে HTTP বেসিক অথেনটিকেশন কনফিগার করে, পূর্ব নির্ধারিত ইউজারনেম ও পাসওয়ার্ড ইনপুট করুন:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

ভেরিফাই করুন, সফল হওয়া উচিত।

### অন্যান্য কনফিগারেশন

এখন SearXNG ডিফল্টভাবে নেটওয়ার্ক সার্চ ক্ষমতা পাবে, খুঁজুন ইঞ্জিন কাস্টমাইজ করতে চ