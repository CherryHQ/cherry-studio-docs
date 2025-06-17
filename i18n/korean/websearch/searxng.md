---
icon: searchengin
---

{% hint style="warning" %}
이 문서는 AI에 의해 중국어에서 번역되었으며 아직 검토되지 않았습니다。
{% endhint %}

# SearXNG 배포 및 설정

Cherry Studio는 SearXNG를 통해 웹 검색을 지원합니다. SearXNG는 로컬이나 서버에 배포할 수 있는 오픈 소스 프로젝트이므로, API 공급자가 필요한 다른 구성 방식과는 약간 다릅니다.

**SearXNG 프로젝트 링크**: [SearXNG](https://github.com/searxng/searxng)

## SearXNG 장점

* 오픈소스 무료, API 불필요
* 상대적으로 높은 개인정보 보호 수준
* 고도로 커스터마이징 가능

## 로컬 배포

### 1. Docker 직접 배포

SearXNG는 복잡한 환경 설정이 필요하지 않아 docker compose 없이 빈 포트만 제공하면 배포할 수 있으므로, Docker로 직접 이미지를 가져와 배포하는 것이 가장 빠른 방법입니다.

#### 1. [docker](https://www.docker.com/) 설치 및 설정

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

설치 후 이미지 저장 경로 선택:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. SearXNG 이미지 검색 및 가져오기

검색창에 **searxng** 입력:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

이미지 가져오기:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. 이미지 실행

가져오기 성공 후 **images** 페이지 이동:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

가져온 이미지 선택 후 실행:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

설정 열어 구성:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

예시: `8085` 포트 사용

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

실행 성공 후 링크 클릭하면 SearXNG 프론트엔드 인터페이스 열림:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

이 화면이 표시되면 배포 성공:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## 서버 배포

Windows에 Docker 설치가 까다로울 경우, SearXNG를 서버에 배포하여 다른 사용자와 공유할 수 있습니다. 다만 SearXNG 자체는 아직 인증을 지원하지 않아, 기술적 수단으로 스캔된 인스턴스를 악용할 수 있다는 점이 아쉽습니다.

이에 Cherry Studio는 현재 [HTTP 기본 인증(RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication) 설정을 지원합니다. SearXNG를 공용 네트워크 환경에 노출하려면 **반드시** Nginx 등 리버스 프록시 소프트웨어를 통해 HTTP 기본 인증을 구성해야 합니다. 기본 Linux 운영 지식이 있다면 아래 간단한 튜토리얼을 참고하세요.

### SearXNG 배포

로컬 배포와 마찬가지로 Docker를 사용합니다. [공식 튜토리얼](https://docs.docker.com/engine/install)에 따라 서버에 최신 Docker CE를 설치했다면, Debian 시스템 신규 설치 시 다음 명령어를 한 줄씩 실행하세요:

```bash
sudo apt update
sudo apt install git -y

# 공식 저장소 가져오기
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# 대역폭이 작은 서버면 false로 설정
export IMAGE_PROXY=true

# 설정 파일 수정
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

로컬 포트 변경 또는 기존 nginx 재사용이 필요한 경우 `docker-compose.yaml` 파일을 다음과 같이 수정하세요:

```yaml
version: "3.7"

services:
# Caddy 불필요 시 제거. 기본적으로 Caddy 불필요
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
# Caddy 불필요 시 제거. 기본적으로 Caddy 불필요
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
    # 기본 호스트 포트 8080 매핑, 8000 포트 사용 시 "127.0.0.1:8000:8080"으로 변경
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
# Caddy 불필요 시 제거
  caddy-data:
  caddy-config:
# Caddy 불필요 시 제거
  valkey-data2:
```

`docker compose up -d` 실행해 시작합니다. 로그 확인은 `docker compose logs -f searxng` 명령어를 사용하세요.

### Nginx 리버스 프록시 및 HTTP 기본 인증 설정

보타 패널이나 1Panel 같은 서버 패널을 사용한다면 해당 문서를 참고해 사이트 추가 후 nginx 리버스 프록시를 설정하고, nginx 설정 파일을 찾아 다음 예제 참고해 수정하세요:

```conf
server
{
    listen 443 ssl;

    # 호스트명 지정
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL 설정 시 필요
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    # 패널 리버스 프록시 기본 설정
    location / {
        # location 블록에 다음 두 줄 추가
        # 설정 파일이 /etc/nginx/conf.d/ 경로에 저장되었다고 가정
        # 보타 패널이라면 /www 등 다른 경로일 수 있음
        auth_basic "사용자명과 비밀번호를 입력하세요";
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

nginx 설정 파일이 `/etc/nginx/conf.d`에 저장되었다면, 비밀번호 파일도 동일한 경로에 저장하세요.

명령어 실행 (`example_name`, `example_password`를 실제 사용할 정보로 대체):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

nginx 재시작(또는 설정 재로드).

웹페이지 열어 사용자명과 비밀번호 입력 요청이 표시되는지 확인합니다. 앞서 설정한 정보로 SearXNG 검색 페이지에 성공적으로 접속할 수 있어야 합니다.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Cherry Studio 연관 설정

SearXNG 로컬 또는 서버 배포 성공 후 Cherry Studio 설정을 진행합니다.

웹 검색 설정 페이지에서 Searxng 선택:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

로컬 배포 링크 입력 시 검증 실패는 정상(기본 json 반환 타입 미설정):

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

데이터를 가져올 수 없으므로 설정 파일 수정이 필요합니다.

Docker Files 탭에서 태그된 폴더 찾기:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

확장 후 다른 태그 폴더 탐색:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

**settings.yml** 설정 파일 위치:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

파일 편집기 열기:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

78번째 줄에서 html 타입만 확인 가능:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

json 타입 추가 후 저장 및 이미지 재실행:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Cherry Studio 재검증 시 성공:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

주소 입력 예시:
- 로컬: <http://localhost>:포트번호
- Docker: <http://host.docker.internal>:포트번호

앞서 서버 배포 및 리버스 프록시 설정에 성공했다면 json 반환 타입이 이미 활성화되어 있습니다. HTTP 기본 인증 구성 후 검증하면 401 에러 코드 반환됨:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

클라이언트에 HTTP 기본 인증 정보 입력(사용자명과 비밀번호):

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

재검증 시 성공해야 합니다.

### 추가 설정

기본 네트워크 검색 기능은 작동하지만, 검색 엔진 커스터마이징이 필요할 경우 직접 설정해야 합니다.

이 설정은 대형 모델 호출 설정에 영향을 미치지 않음에 유의하세요.

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

대형 모델 호출용 검색 엔진 설정은 설정 파일에서 진행:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

언어 구성 참고:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

내용이 너무 길면 로컬 IDE에 복사해 수정 후 설정 파일에 붙여넣기 바랍니다.

## 검증 실패 일반 원인

### json 반환 형식 미추가

설정 파일에 json 반환 형식 추가:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### 올바른 검색 엔진 미설정

Cherry Studio는 web general 카테고리를 동시에 포함하는 엔진을 기본 선택하며, 구글 등 엔진이 선택될 경우 중국 내 접속 불가로 실패합니다. 다음 설정으로 baidu 엔진을 강제 사용해 해결하세요:

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

### 접속 속도 과도

searxng의 limiter 설정이 API 접속을 차단할 수 있으니 설정에서 false로 변경해보세요:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>