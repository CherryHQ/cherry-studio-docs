---
icon: searchengin
---

{% hint style="warning" %}
Dokumen ini diterjemahkan dari bahasa Mandarin oleh AI dan belum ditinjau.
{% endhint %}

# Penyebaran dan Konfigurasi SearXNG

CherryStudio mendukung pencarian web melalui SearXNG, sebuah proyek open-source yang dapat disebarkan secara lokal atau di server, sehingga konfigurasinya sedikit berbeda dari metode penyedia API lainnya.

**Tautan Proyek SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## Keunggulan SearXNG

* Open-source dan gratis, tidak memerlukan API
* Privasi yang relatif tinggi
* Dapat disesuaikan secara tinggi

## Penyebaran Lokal

### 1. Penyebaran Langsung dengan Docker

Karena SearXNG tidak memerlukan konfigurasi lingkungan yang kompleks dan cukup menyediakan port kosong, cara tercepat adalah dengan menarik image Docker secara langsung untuk penyebaran.

#### 1. Unduh dan instal [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Setelah instalasi, pilih path penyimpanan image:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Cari dan tarik Image SearXNG

Masukkan **searxng** di bilah pencarian:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Tarik image:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Jalankan Image

Setelah berhasil menarik, buka halaman **images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Pilih image yang ditarik dan klik jalankan:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Buka pengaturan untuk konfigurasi:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Contoh dengan port `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Setelah berjalan, klik tautan untuk membuka antarmuka depan SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Halaman ini menandakan penyebaran berhasil:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Penyebaran Server

Mengingat instalasi Docker di Windows cukup rumit, pengguna dapat menyebarkan SearXNG di server, juga untuk berbagi dengan orang lain. Sayangnya, SearXNG belum mendukung otentikasi, sehingga orang lain dapat menyalahgunakan instans yang Anda sebarkan.

Cherry Studio kini mendukung konfigurasi [HTTP Basic Authentication (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Jika Anda menyebarkan SearXNG di internet publik, **harap** konfigurasikan autentikasi HTTP dasar melalui perangkat lunak reverse proxy seperti Nginx. Berikut tutorial singkat untuk pengguna dengan pengetahuan dasar Linux.

### Penyebaran SearXNG

Serupa dengan sebelumnya, gunakan Docker. Asumsikan Docker CE terbaru telah terinstal di server sesuai [panduan resmi](https://docs.docker.com/engine/install), gunakan perintah berikut untuk Debian:

```bash
sudo apt update
sudo apt install git -y

# Tarik repositori resmi
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Jika bandwidth server kecil, setel false
export IMAGE_PROXY=true

# Ubah file konfigurasi
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

Untuk mengubah port lokal atau menggunakan kembali nginx yang ada, edit `docker-compose.yaml` seperti contoh:

```yaml
version: "3.7"

services:
# Hapus bagian ini jika tidak perlu Caddy dan ingin menggunakan Nginx lokal
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
# Hapus bagian di atas jika tidak perlu Caddy
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
    # Port default 8080, ubah ke "127.0.0.1:8000:8080" untuk port 8000
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
# Hapus jika tidak perlu Caddy
  caddy-data:
  caddy-config:
# Hapus di atas jika tidak perlu Caddy
  valkey-data2:
```

Jalankan `docker compose up -d`. Pantau log dengan `docker compose logs -f searxng`.

### Penyebaran Reverse Proxy Nginx dan Autentikasi HTTP Dasar

Jika menggunakan panel server seperti BaoTa atau 1Panel, konfigurasikan reverse proxy nginx. Modifikasi file konfigurasi nginx seperti contoh:

```conf
server
{
    listen 443 ssl;

    # Nama host Anda
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # Jika SSL dikonfigurasi
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS opsional
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Konfigurasi reverse proxy
    location / {
        # Tambahkan dua baris ini
        auth_basic "Masukkan nama pengguna dan kata sandi";
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

Asumsikan file konfigurasi disimpan di `/etc/nginx/conf.d`, buat file kata sandi di direktori yang sama:

```bash
echo "nama_contoh:$(openssl passwd -5 'kata_sandi_contoh')" > /etc/nginx/conf.d/search.htpasswd
```

Muat ulang nginx. Akses situs web untuk memverifikasi permintaan autentikasi.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Konfigurasi Terkait Cherry Studio

Setelah SearXNG tersebar, lakukan konfigurasi di CherryStudio.

Buka halaman pengaturan pencarian web, pilih Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Masukkan tautan penyebaran lokal, verifikasi mungkin gagal:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

Perlu mengubah konfigurasi karena format json belum diaktifkan.

Buka Docker dan cari folder dengan tag:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Telusuri folder lain dengan tag:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Temukan file konfigurasi **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Buka editor file:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Baris 78, hanya ada format html:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Tambahkan format json, simpan, dan jalankan ulang image:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Verifikasi berhasil di Cherry Studio:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Gunakan alamat lokal: <http://localhost>:port\
Atau alamat Docker: <http://host.docker.internal>:port

Untuk penyebaran server dengan reverse proxy, konfigurasikan autentikasi di Cherry Studio jika verifikasi gagal:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

Masukkan nama pengguna dan kata sandi:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

Verifikasi akan berhasil.

### Konfigurasi Lain

SearXNG telah memiliki kemampuan pencarian bawaan. Untuk menyesuaikan mesin pencari, konfigurasikan:

Pengaturan ini tidak memengaruhi konfigurasi pemanggilan model AI:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Untuk mesin pencari yang dipanggil AI, atur di file konfigurasi:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Referensi konfigurasi bahasa:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

Untuk konten panjang, salin ke IDE lokal, edit, lalu tempelkan kembali.

## Penyebab Umum Kegagalan Verifikasi

### Format Balasan Tanpa JSON

Tambahkan format json di konfigurasi:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Konfigurasi Mesin Pencari Salah

Cherry Studio memilih mesin dengan kategori "web general". Konfigurasikan SearXNG untuk memaksa mesin Baidu jika Google tidak dapat diakses:

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

### Akses Terlalu Cepat

Nonaktifkan limiter di SearXNG:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>