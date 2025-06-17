---
icon: searchengin
---

{% hint style="warning" %}
Tài liệu này được dịch từ tiếng Trung bằng AI và chưa được xem xét.
{% endhint %}

# Triển khai và Cấu hình SearXNG

CherryStudio hỗ trợ tìm kiếm web thông qua SearXNG, một dự án mã nguồn mở có thể triển khai cục bộ hoặc trên máy chủ, do đó hơi khác so với các phương thức cấu hình cần nhà cung cấp API.

**Liên kết dự án SearXNG:** [SearXNG](https://github.com/searxng/searxng)

## Ưu điểm của SearXNG

* Mã nguồn mở miễn phí, không cần API
* Tính riêng tư tương đối cao
* Có thể tùy chỉnh cao

## Triển khai cục bộ

### 1. Triển khai trực tiếp bằng Docker

Do SearXNG không yêu cầu cấu hình môi trường phức tạp và không cần docker compose, chỉ cần cung cấp một cổng trống là có thể triển khai, nên cách nhanh nhất là sử dụng Docker để kéo image trực tiếp.

#### 1. Tải xuống, cài đặt và cấu hình [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Sau khi cài đặt, chọn đường dẫn lưu image:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Tìm kiếm và kéo image SearXNG

Nhập **searxng** vào thanh tìm kiếm:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Kéo image:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Chạy image

Sau khi kéo thành công, vào trang **images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Chọn image đã kéo và nhấp vào "Run":

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Mở cài đặt để cấu hình:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Ví dụ với cổng `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Sau khi chạy thành công, nhấp vào liên kết để mở giao diện frontend SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Trang này xuất hiện có nghĩa là triển khai thành công:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Triển khai trên máy chủ

Do việc cài đặt Docker trên Windows tương đối phức tạp, người dùng có thể triển khai SearXNG trên máy chủ và chia sẻ cho người khác. Tuy nhiên, đáng tiếc là SearXNG hiện chưa hỗ trợ xác thực, dẫn đến người khác có thể quét lạm dụng phiên bản bạn triển khai.

Do đó, Cherry Studio hiện đã hỗ trợ cấu hình [Xác thực HTTP Cơ bản (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Nếu người dùng muốn đặt SearXNG đã triển khai trong môi trường mạng công cộng, **bắt buộc** phải cấu hình Xác thực HTTP Cơ bản thông qua phần mềm reverse proxy như Nginx. Dưới đây là hướng dẫn ngắn gọn, yêu cầu bạn có kiến thức cơ bản về vận hành Linux.

### Triển khai SearXNG

Tương tự, vẫn sử dụng Docker để triển khai. Giả sử bạn đã cài đặt Docker CE phiên bản mới nhất trên máy chủ theo [hướng dẫn chính thức](https://docs.docker.com/engine/install), sau đây là các lệnh hoàn chỉnh cho hệ thống Debian mới cài:

```bash
sudo apt update
sudo apt install git -y

# Kéo kho chính thức
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Nếu máy chủ có băng thông nhỏ, đặt thành false
export IMAGE_PROXY=true

# Sửa file cấu hình
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# Xem tại https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url được xác định trong biến môi trường SEARXNG_BASE_URL, xem .env và docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # Có thể tắt cho phiên bản cá nhân
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

Nếu cần sửa cổng nghe cục bộ hoặc tái sử dụng nginx có sẵn, chỉnh sửa file `docker-compose.yaml`:

```yaml
version: "3.7"

services:
# Nếu không cần Caddy mà tái sử dụng Nginx sẵn có, xóa phần sau. Mặc định chúng ta không cần Caddy.
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
# Nếu không cần Caddy mà tái sử dụng Nginx sẵn có, xóa phần trên. Mặc định chúng ta không cần Caddy.
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
    # Mặc định ánh xạ sang cổng 8080 của máy chủ, nếu muốn nghe 8000 thì đổi thành "127.0.0.1:8000:8080"
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
# Nếu không cần Caddy mà tái sử dụng Nginx sẵn có, xóa phần sau
  caddy-data:
  caddy-config:
# Nếu không cần Caddy mà tái sử dụng Nginx sẵn có, xóa phần trên
  valkey-data2:
```

Thực thi `docker compose up -d` để khởi động. Xem nhật ký bằng `docker compose logs -f searxng`.

### Triển khai reverse proxy Nginx và Xác thực HTTP Cơ bản

Nếu sử dụng bảng điều khiển máy chủ như Bảo Tháp hoặc 1Panel, tham khảo tài liệu để thêm website và cấu hình reverse proxy nginx. Sau đó tìm nơi sửa cấu hình nginx, tham khảo ví dụ:

```conf
server
{
    listen 443 ssl;

    # Tên máy chủ của bạn
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # Nếu đã cấu hình SSL, nên có hai dòng sau
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # Mặc định cấu hình reverse proxy qua bảng điều khiển
    location / {
        # Chỉ cần thêm hai dòng sau trong khối location
        # Ví dụ giả định file cấu hình lưu trong /etc/nginx/conf.d/
        auth_basic "Vui lòng nhập tên người dùng và mật khẩu";
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

Giả sử file cấu hình Nginx lưu trong `/etc/nginx/conf.d`, lưu file mật khẩu cùng thư mục.

Thực thi lệnh (thay `example_name`, `example_password` bằng thông tin của bạn):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Khởi động lại Nginx (hoặc tải lại cấu hình).

Mở trang web, sẽ thấy nhắc nhập thông tin. Nhập tên người dùng và mật khẩu đã đặt để kiểm tra.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cấu hình liên quan trong Cherry Studio

Sau khi triển khai SearXNG cục bộ hoặc trên máy chủ thành công, tiếp theo là cấu hình trong CherryStudio.

Vào trang cài đặt tìm kiếm web, chọn Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Nhập liên kết triển khai cục bộ thấy xác minh thất bại, không cần lo:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

Vì triển khai mặc định chưa cấu hình kiểu trả về json, cần sửa file cấu hình.

Quay lại Docker, vào thẻ Files tìm thư mục có nhãn:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Mở rộng và tiếp tục, sẽ thấy thư mục có nhãn khác:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Mở rộng, tìm file cấu hình **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Nhấp để mở trình soạn thảo:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Tìm dòng 78, thấy chỉ có một kiểu html:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Thêm kiểu json và lưu, chạy lại image:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Quay lại Cherry Studio xác minh, thành công:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Địa chỉ có thể nhập cục bộ: <http://localhost> : số cổng\
Hoặc địa chỉ docker: <http://host.docker.internal> : số cổng

Nếu đã triển khai trên máy chủ và cấu hình reverse proxy, đã bật kiểu trả về json. Nhập địa chỉ để xác minh, do đã cấu hình Xác thực HTTP Cơ bản, nên trả về mã lỗi 401:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

Cấu hình Xác thực HTTP Cơ bản trong client, nhập tên người dùng và mật khẩu đã đặt:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

Xác minh nên thành công.

### Cấu hình khác

Lúc này SearXNG đã có khả năng tìm kiếm mạng mặc định, nếu cần tùy chỉnh công cụ tìm kiếm hãy tự cấu hình

Lưu ý tùy chọn ở đây không ảnh hưởng đến cấu hình khi mô hình lớn gọi:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Nếu cần cấu hình công cụ tìm kiếm để mô hình lớn gọi, đặt trong file cấu hình:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Tham khảo ngôn ngữ cấu hình:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

Nếu nội dung quá dài khó sửa, sao chép vào IDE cục bộ, sửa rồi dán vào file cấu hình.

## Nguyên nhân phổ biến xác minh thất bại

### Chưa thêm định dạng json

Trong file cấu hình, thêm json vào định dạng trả về:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Chưa cấu hình đúng công cụ tìm kiếm