---
icon: searchengin
---

{% hint style="warning" %}
Bu belge Çince'den yapay zeka tarafından çevrilmiştir ve henüz incelenmemiştir.
{% endhint %}

# SearXNG Dağıtımı ve Yapılandırması

CherryStudio, SearXNG üzerinden web araması desteği sunar. SearXNG, yerel olarak veya sunucuda dağıtılabilen açık kaynaklı bir proje olduğundan, diğer API sağlayıcı gerektiren yapılandırmalardan farklıdır.

**SearXNG Proje Bağlantısı:** [SearXNG](https://github.com/searxng/searxng)

## SearXNG'nin Avantajları

*   Açık kaynak ve ücretsiz, API gerektirmez
*   Nispeten yüksek gizlilik
*   Yüksek düzeyde özelleştirilebilir

## Yerel Dağıtım

### 1. Docker ile Doğrudan Dağıtım

SearXNG karmaşık ortam yapılandırması gerektirmediğinden, docker compose kullanmadan yalnızca boş bir port sağlayarak dağıtım yapılabilir. En hızlı yöntem, Docker ile doğrudan imajı çekerek dağıtmaktır.

#### 1. [docker](https://www.docker.com/) indirme ve kurma

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Kurulumdan sonra bir imaj depolama yolu seçin:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. SearXNG imajını arama ve çekme

Arama çubuğuna **searxng** yazın:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

İmajı çekin:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. İmajı çalıştırma

Çekme başarılı olduktan sonra **images** sayfasına gidin:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Çekilen imajı seçip çalıştırın:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Ayarları yapılandırmak için açın:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Örnek olarak `8085` portu:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Başarıyla çalıştırıldıktan sonra bağlantıya tıklayarak SearXNG arayüzünü açın:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Bu sayfa göründüğünde dağıtım başarılı demektir:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Sunucu Dağıtımı

Windows altında Docker kurulumunun nispeten zor olması nedeniyle, kullanıcılar SearXNG'yi sunucuya dağıtabilir ve başkalarıyla paylaşabilir. Ancak ne yazık ki SearXNG şu anda kimlik doğrulamayı desteklemediğinden, teknik yöntemlerle başkaları tarafından taranabilir ve kötüye kullanılabilir.

Bu nedenle, Cherry Studio şu anda [HTTP Temel Kimlik Doğrulama (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication) desteği sunmaktadır. Kendi dağıttığınız SearXNG'yi genel ağa açmayı planlıyorsanız, lütfen Nginx gibi ters proxy yazılımları kullanarak HTTP Temel Kimlik Doğrulama yapılandırdığınızdan **emin olun**. Aşağıda temel Linux yönetimi bilgisine ihtiyaç duyulan kısa bir kılavuz sunulmaktadır.

### SearXNG Dağıtımı

Benzer şekilde, Docker ile dağıtım yapılır. Sunucuda [resmi kılavuz](https://docs.docker.com/engine/install) ile en son Docker CE sürümünün kurulu olduğunu varsayarsak, Debian sisteminde yeni kurulum için aşağıdaki komutlar kullanılabilir:

```bash
sudo apt update
sudo apt install git -y

# Resmi depoyu çek
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Sunucu bant genişliği düşükse false yapılabilir
export IMAGE_PROXY=true

# Yapılandırma dosyasını düzenle
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

Yerel dinleme portunu değiştirmek veya yerel mevcut nginx'i kullanmak için `docker-compose.yaml` dosyasını aşağıdaki gibi düzenleyin:

```yaml
version: "3.7"

services:
# Eğer Caddy gerekmiyor ve yerel Nginx kullanılıyorsa aşağıdaki kaldırılır.
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
# Eğer Caddy gerekmiyor ve yerel Nginx kullanılıyorsa yukarıdaki kaldırılır.
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
    # Varsayılan olarak ana bilgisayar 8080 portu, 8000 kullanmak için "127.0.0.1:8000:8080" yapılır
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
# Eğer Caddy gerekmiyor ve yerel Nginx kullanılıyorsa aşağıdaki kaldırılır
  caddy-data:
  caddy-config:
# Eğer Caddy gerekmiyor ve yerel Nginx kullanılıyorsa yukarıdaki kaldırılır
  valkey-data2:
```

Başlatmak için `docker compose up -d` komutunu çalıştırın. Günlükleri görmek için `docker compose logs -f searxng` kullanın.

### Nginx Ters Proxy ve HTTP Temel Kimlik Doğrulama Dağıtımı

Eğer Baota veya 1Panel gibi sunucu panel programları kullanıyorsanız, belgelerine bakarak web sitesi ekleyip nginx ters proxy yapılandırın. Sonra nginx yapılandırma dosyasını bulun ve aşağıdaki örnekle düzenleyin:

```conf
server
{
    listen 443 ssl;

    # Host adınız
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL yapılandırıldıysa bu iki satır olmalı
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Ters proxy varsayılan yapılandırması
    location / {
        # location bloğuna sadece bu iki satırı ekleyin
        # Örnek yapılandırma dosyası /etc/nginx/conf.d/ altında saklanıyor
        auth_basic "Kullanıcı adı ve şifrenizi girin";
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

Nginx yapılandırma dosyasının `/etc/nginx/conf.d` altında olduğunu varsayarsak, şifre dosyasını aynı dizine kaydedin.

Komutu çalıştırın (`example_name`, `example_password` kısımlarını kendi bilgilerinizle değiştirin):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Nginx'i yeniden başlatın (veya yapılandırmayı yeniden yükleyin).

Web sayfasını açtığınızda kullanıcı adı ve şifre istenmelidir. Önceden ayarladığınız bilgilerle giriş yaparak SearXNG arama sayfasına erişebilirseniz yapılandırma doğrudur.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio İlgili Yapılandırma

SearXNG yerel veya sunucuda başarıyla dağıtıldıktan sonra, CherryStudio için ilgili yapılandırma yapılmalıdır.

Web araması ayarları sayfasına gidin, Searxng seçin:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Yerel dağıtım bağlantısını doğrudan girdiğinizde doğrulama başarısız olabilir, endişelenmeyin:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

Çünkü doğrudan dağıtıldığında varsayılan olarak json dönüş türü yapılandırılmamıştır, veri alınamaz. Yapılandırma dosyasını değiştirmeniz gerekir.

Docker'a dönün, Files sekmesinde etiketli klasörü bulun:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Genişletin ve başka bir etiketli klasör bulana kadar aşağı inin:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Devam edin, **settings.yml** yapılandırma dosyasını bulun:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Dosya düzenleyiciyi açın:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

78. satırı bulun, yalnızca html türü olduğunu göreceksiniz:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Json türünü ekleyip kaydedin, imajı yeniden çalıştırın:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Cherry Studio'ya dönüp tekrar doğrulayın, doğrulama başarılı:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Adres olarak yerel adres yazılabilir: <http://localhost>:port numarası  
Veya docker adresi: <http://host.docker.internal>:port numarası

Önceki örnekle sunucu dağıtımı yapıp ters proxy yapılandırdıysanız ve json dönüş türünü açtıysanız, adres girip doğrulama yaptığınızda HTTP Temel Kimlik Doğrulama nedeniyle 401 hatası almalısınız:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

İstemci tarafında HTTP Temel Kimlik Doğrulama yapılandırın, ayarladığınız kullanıcı adı ve şifreyi girin:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

Doğrulayın, başarılı olmalıdır.

### Diğer Yapılandırmalar

Artık SearXNG varsayılan arama yeteneğine sahiptir. Arama motorlarını özelleştirmek için kendiniz yapılandırmanız gerekir

Buradaki tercihlerin büyük dil modeli çağrıları üzerinde etkisi olmadığını unutmayın

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Büyük dil modeli tarafından kullanılacak arama motorlarını yapılandırmak için yapılandırma dosyasında ayarlam