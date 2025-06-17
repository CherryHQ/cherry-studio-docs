---
icon: searchengin
---

{% hint style="warning" %}
เอกสารนี้ได้รับการแปลจากภาษาจีนโดย AI และยังไม่ได้รับการตรวจสอบ
{% endhint %}

# การติดตั้งและกำหนดค่า SearXNG

CherryStudio รองรับการค้นหาข้อมูลทางอินเทอร์เน็ตผ่าน SearXNG ซึ่งเป็นโครงการโอเพนซอร์สที่สามารถติดตั้งได้ทั้งบนเครื่องท้องถิ่นและเซิร์ฟเวอร์ ดังนั้นจึงมีวิธีการกำหนดค่าที่แตกต่างจากการตั้งค่าที่ต้องใช้ API ของผู้ให้บริการ

**ลิงก์โครงการ SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## ข้อดีของ SearXNG

*   โอเพนซอร์สและฟรี ไม่จำเป็นต้องใช้ API
*   มีความเป็นส่วนตัวค่อนข้างสูง
*   สามารถปรับแต่งได้อย่างมาก

## การติดตั้งบนเครื่องท้องถิ่น

### 1. ติดตั้งด้วย Docker โดยตรง

เนื่องจาก SearXNG ไม่จำเป็นต้องมีการกำหนดค่าสภาพแวดล้อมที่ซับซ้อน และไม่จำเป็นต้องใช้ docker compose เพียงระบุพอร์ตว่างหนึ่งพอร์ตก็สามารถติดตั้งได้ ดังนั้นวิธีที่เร็วที่สุดคือใช้ Docker ดึงอิมเมจมาโดยตรงเพื่อติดตั้ง

#### 1. ดาวน์โหลด ติดตั้ง และกำหนดค่า [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

เลือกเส้นทางการจัดเก็บอิมเมจหลังการติดตั้ง:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. ค้นหาและดึงอิมเมจ SearXNG

ป้อน **searxng** ในแถบค้นหา:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

ดึงอิมเมจ:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. รันอิมเมจ

เมื่อดึงสำเร็จ ไปที่หน้า **images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

เลือกอิมเมจที่ดึงมาแล้วคลิกรัน:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

เปิดรายการตั้งค่าสำหรับกำหนดค่า:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

ตัวอย่างพอร์ต `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

เมื่อรันสำเร็จแล้ว คลิกที่ลิงก์เพื่อเปิดอินเทอร์เฟซหน้ารวมของ SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

หากเห็นหน้านี้แสดงว่าติดตั้งสำเร็จ:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## การติดตั้งบนเซิร์ฟเวอร์

เนื่องจากบน Windows การติดตั้ง Docker เป็นเรื่องที่ค่อนข้างยุ่งยาก ผู้ใช้สามารถติดตั้ง SearXNG บนเซิร์ฟเวอร์และแบ่งปันให้ผู้อื่นใช้ได้ แต่ที่น่าเสียดายคือ SearXNG เองยังไม่รองรับการตรวจสอบสิทธิ์ ซึ่งทำให้ผู้อื่นสามารถสแกนและใช้ตัวอย่างที่คุณติดตั้งไปในทางที่ผิดได้ทางเทคนิค

ด้วยเหตุนี้ Cherry Studio จึงได้รองรับการกำหนดค่า [HTTP Basic Authentication (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication) แล้ว หากผู้ใช้ต้องการให้ SearXNG ที่ติดตั้งไปทำงานภายใต้สภาพแวดล้อมอินเทอร์เน็ตสาธารณะ โปรด **จำเป็นต้อง** กำหนดค่า HTTP Basic Authentication ผ่านซอฟต์แวร์ reverse proxy เช่น Nginx ด้านล่างนี้เป็นบทเรียนย่อ ซึ่งต้องมีความรู้พื้นฐานเกี่ยวกับการดูแลระบบ Linux

### ติดตั้ง SearXNG

เช่นเดียวกัน ยังคงใช้ Docker ในการติดตั้ง สมมติว่าคุณได้ติดตั้ง Docker CE เวอร์ชันล่าสุดบนเซิร์ฟเวอร์แล้วตาม [บทเรียนอย่างเป็นทางการ](https://docs.docker.com/engine/install) ด้านล่างนี้เป็นคำสั่งทั้งหมดที่ใช้ได้กับการติดตั้งใหม่บนระบบ Debian:

```bash
sudo apt update
sudo apt install git -y

# ดึงคลังอย่างเป็นทางการ
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# หากแบนด์วิธเซิร์ฟเวอร์ของคุณเล็ก สามารถตั้งค่าเป็น false ได้
export IMAGE_PROXY=true

# แก้ไขไฟล์กำหนดค่า
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

หากคุณต้องการแก้ไขพอร์ตที่เซิร์ฟเวอร์รอรับข้อมูล หรือนำ nginx ที่มีอยู่กลับมาใช้ คุณสามารถแก้ไขไฟล์ `docker-compose.yaml` โดยอ้างอิงดังนี้:

```yaml
version: "3.7"

services:
# หากไม่ต้องการ Caddy และนำ Nginx ที่มีอยู่แล้วกลับมาใช้ ให้ลบบล็อกด้านล่างนี้ออก ตามค่าเริ่มต้นไม่ต้องการ Caddy
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
# หากไม่ต้องการ Caddy และนำ Nginx ที่มีอยู่แล้วกลับมาใช้ ให้ลบบล็อกด้านบนนี้ออก ตามค่าเริ่มต้นไม่ต้องการ Caddy
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
    # โดยค่าเริ่มต้นแมปไปที่พอร์ต 8080 บนโฮสต์ หากคุณต้องการรับฟังที่พอร์ต 8000 ให้เปลี่ยนเป็น "127.0.0.1:8000:8080"
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
# หากไม่ต้องการ Caddy และนำ Nginx ที่มีอยู่แล้วกลับมาใช้ ให้ลบบล็อกด้านล่างนี้ออก
  caddy-data:
  caddy-config:
# หากไม่ต้องการ Caddy และนำ Nginx ที่มีอยู่แล้วกลับมาใช้ ให้ลบบล็อกด้านบนนี้ออก
  valkey-data2:
```

รันคำสั่ง `docker compose up -d` เพื่อเริ่ม คุณสามารถดูบันทึกได้ด้วยคำสั่ง `docker compose logs -f searxng`

### ติดตั้ง Nginx reverse proxy และ HTTP Basic Authentication

หากคุณใช้โปรแกรมแผงควบคุมเซิร์ฟเวอร์ เช่น Baota หรือ 1Panel โปรดดูเอกสารประกอบเพื่อเพิ่มเว็บไซต์และกำหนดค่า nginx reverse proxy จากนั้นค้นหาสถานที่แก้ไขไฟล์กำหนดค่า nginx และอ้างอิงจากตัวอย่างด้านล่างนี้เพื่อแก้ไข:

```conf
server
{
    listen 443 ssl;

    # นี่คือชื่อโฮสต์ของคุณ
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # หากตั้งค่า SSL แล้ว ควรมีสองบรรทัดนี้
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # โดยค่าเริ่มต้น เมื่อกำหนดค่ารีเวิร์สพร็อกซีผ่านแผงควบคุม บล็อก location จะมีลักษณะเช่นนี้
    location / {
        # เพียงเพิ่มสองบรรทัดด้านล่างในบล็อก location ส่วนที่เหลือคงไว้ดังเดิม
        # ที่นี่สมมติว่าไฟล์กำหนดค่าของคุณเก็บไว้ในไดเรกทอรี /etc/nginx/conf.d/
        # สำหรับ Baota ควรเก็บไว้ในไดเรกทอรีเช่น /www ฯลฯ ควรระวัง
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

สมมติว่าไฟล์กำหนดค่า Nginx เก็บไว้ใน `/etc/nginx/conf.d` โดยเราจะเก็บไฟล์รหัสผ่านไว้ในไดเรกทอรีเดียวกัน

รันคำสั่ง (แทนที่ `example_name`, `example_password` ด้วยชื่อผู้ใช้และรหัสผ่านที่คุณต้องการกำหนด):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

รีสตาร์ท Nginx (หรือโหลดการกำหนดค่าใหม่)

ตอนนี้คุณสามารถเปิดหน้าเว็บ ซึ่งจะแจ้งให้คุณป้อนชื่อผู้ใช้และรหัสผ่าน โปรดป้อนชื่อผู้ใช้และรหัสผ่านที่ตั้งไว้ข้างต้นเพื่อตรวจสอบว่าสามารถเข้าสู่หน้าแสดงผลการค้นหา SearXNG ได้สำเร็จหรือไม่ เพื่อตรวจสอบว่าการตั้งค่าถูกต้องหรือไม่

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## การกำหนดค่าที่เกี่ยวข้องใน Cherry Studio

เมื่อ SearXNG ติดตั้งสำเร็จบนเครื่องท้องถิ่นหรือเซิร์ฟเวอร์แล้ว ขั้นตอนถัดไปคือการกำหนดค่าที่เกี่ยวข้องใน CherryStudio

ไปที่หน้าการตั้งค่าการค้นหาอินเทอร์เน็ต แล้วเลือก Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

เมื่อป้อนลิงก์ที่ติดตั้งบนเครื่องท้องถิ่นโดยตรง จะพบว่าการตรวจสอบล้มเหลว ณ จุดนี้ไม่ต้องกังวล:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

เนื่องจากหลังติดตั้งโดยตรง ค่าเริ่มต้นไม่ได้กำหนดค่าประเภทการส่งคืน json ดังนั้นจึงไม่สามารถรับข้อมูลได้ จำเป็นต้องแก้ไขไฟล์กำหนดค่า

กลับไปที่ Docker ไปที่แท็บ Files และค้นหาโฟลเดอร์ที่มีแท็กในอิมเมจ:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

ขยายออกแล้วเลื่อนลง จะพบอีกโฟลเดอร์หนึ่งที่มีแท็ก:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

ขยายต่อไป ค้นหาไฟล์กำหนดค่า **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

คลิกเพื่อเปิดโปรแกรมแก้ไขไฟล์:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

ไปที่บรรทัดที่ 78 จะเห็นว่ามีเพียงประเภท html เท่านั้น

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

เพิ่มประเภท json แล้วบันทึก จากนั้นรันอิมเมจใหม่อีกครั้ง

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

กลับไปที่ Cherry Studio อีกครั้งเพื่อตรวจสอบ ซึ่งควรตรวจสอบสำเร็จ:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

สามารถป้อนที่อยู่เครื่องท้องถิ่น: <http://localhost> : หมายเลขพอร์ต\
หรือป้อนที่อยู่ docker: <http://host.docker.internal> : หมายเลขพอร์ต

หากผู้ใช้ปฏิบัติตามตัวอย่างก่อนหน้านี้ในการติดตั้งบนเซิร์ฟเวอร์และกำหนดค่ารีเวิร์สพร็อกซีอย่างถูกต้อง และเปิดใช้งานประเภทการส่งคืน json แล้ว เมื่อป้อนที่อยู่แล้วตรวจสอบ เนื่องจากรีเวิร์สพร็อกซีถูกกำหนดค่าให้ HTTP Basic Authentication การตรวจสอบควรส่งคืนข้อผิดพลาดรหัส 401:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

กำหนดค่า HTTP Basic Authentication ฝั่งไคลเอนต์ ป้อนชื่อผู้ใช้และรหัสผ่านที่ตั้งไว้ก่อนหน้านี้:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

ดำเนินการตรวจสอบ ควรตรวจสอบสำเร็จ

### การกำหนดค่าอื่นๆ

ณ จุดนี้ SearXNG มีความสามารถในการค้นหาอินเทอร์เน็ตตามค่าเริ่มต้นอยู่แล้ว หากต้องการปรับแต่งเครื่องมือค้นหา จำเป็นต้องกำหนดค่าเอง

โปรดทราบว่าการตั้งค่าล่วงหน้า (Preferences) ที่นี่ไม่ส่งผลต่อการกำหนดค่าเมื่อโมเดลขนาดใหญ่เรียกใช้

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

หากต้องการกำหนดค่าเครื่องมือค้นหาที่จะถูกเรียกใช้โดยโมเดลขนาดใหญ่ จำเป็นต้องกำหนดค่าในไฟล์กำหนดค่า:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

เอกสารอ้างอิงการกำหนดค่าภาษา:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

หากเนื้อหายาวเกินไปและแก้ไขโดยตรงไม่สะดวก คุณสามารถคัดลอกไปยัง IDE บนเครื่องท้องถิ่นของคุณ แก้ไข แล้ววางกลับในไฟล์กำหนดค่า

## สาเหตุทั่วไปของการตรวจสอบล้มเหลว

### ไม่ได้เพิ่มรูปแบบ json ในรูปแบบการส่งคืน

เพิ่ม json ในรูปแบบการส่งคืนในไฟล์กำหนดค่า:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### ไม่ได้กำหนดค่าเครื่องมือค้นหาอย่าง