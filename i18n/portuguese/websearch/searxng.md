---
icon: searchengin
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Implantação e Configuração do SearXNG

O CherryStudio suporta pesquisas na internet através do SearXNG, que é um projeto de código aberto implantável localmente ou em servidores, diferindo ligeiramente de outras configurações que exigem provedores de API.

**Link do projeto SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## Vantagens do SearXNG

*   Open-source e gratuito, sem necessidade de API
*   Privacidade relativamente alta
*   Altamente personalizável

## Implantação Local

### 1. Implantação Direta com Docker

Como o SearXNG não requer configurações complexas de ambiente, pode ser implantado diretamente com Docker sem `docker compose`, bastando fornecer uma porta livre.

#### 1. Baixe e configure o [Docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Após instalar, selecione um caminho de armazenamento para imagens:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Pesquise e baixe a imagem do SearXNG

Digite **searxng** na barra de pesquisa:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Baixe a imagem:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Execute a imagem

Após baixar, acesse a página **images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Selecione a imagem baixada e clique em executar:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Abra as configurações para ajustar:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Exemplo usando a porta `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Após iniciar com sucesso, clique no link para acessar a interface do SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Esta página confirma a implantação bem-sucedida:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Implantação em Servidor

Como a instalação do Docker no Windows pode ser complexa, os usuários podem implantar o SearXNG em servidores e compartilhá-lo. Porém, como o SearXNG atualmente não suporta autenticação, instâncias expostas podem ser abusadas.

Para mitigar isso, o Cherry Studio agora suporta [Autenticação HTTP Básica (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Se expor seu SearXNG publicamente, **configure obrigatoriamente** autenticação via Nginx ou outro software de proxy reverso. Veja um tutorial resumido (requer conhecimentos básicos de Linux).

### Implante o SearXNG

Similar à implantação local via Docker. Após instalar a última versão do Docker CE seguindo o [tutorial oficial](https://docs.docker.com/engine/install), execute estes comandos para instalação limpa no Debian:

```bash
sudo apt update
sudo apt install git -y

# Clonar repositório oficial
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Se a largura de banda do servidor for pequena, defina false
export IMAGE_PROXY=true

# Modificar configurações
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# veja https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url está definido na variável SEARXNG_BASE_URL, ver .env e docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # pode ser desativado para instância privada
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

Para modificar a porta ou reutilizar um Nginx existente, edite `docker-compose.yaml`:

```yaml
version: "3.7"

services:
# Remova abaixo se reutilizar Nginx local. Não precisamos do Caddy por padrão.
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
# Remova acima se reutilizar Nginx local. Não precisamos do Caddy por padrão.
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
    # Mapeia padrão para 8080. Para usar 8000: "127.0.0.1:8000:8080"
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
# Remova abaixo se reutilizar Nginx
  caddy-data:
  caddy-config:
# Remova acima se reutilizar Nginx
  valkey-data2:
```

Execute `docker compose up -d`. Monitore logs com `docker compose logs -f searxng`.

### Configure Proxy Reverso e Autenticação HTTP Básica no Nginx

Se usar painéis como Baota ou 1Panel, adicione um site e configure proxy reverso. Depois, localize o arquivo de configuração do Nginx e ajuste conforme o exemplo:

```conf
server
{
    listen 443 ssl;

    # Nome do seu host
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # SSL requer estas linhas
    ssl_certificate    /caminho/para/fullchain.pem;
    ssl_certificate_key    /caminho/para/privkey.pem;

    # HSTS (opcional)
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    location / {
        # Adicione estas duas linhas
        auth_basic "Insira nome de usuário e senha";
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

Suponha que o arquivo esteja em `/etc/nginx/conf.d`. Crie o arquivo de senhas no mesmo diretório:

```bash
echo "nome_exemplo:$(openssl passwd -5 'senha_exemplo')" > /etc/nginx/conf.d/search.htpasswd
```

Reinicie ou recarregue o Nginx. Ao acessar, será solicitada autenticação. Use as credenciais definidas para verificar.

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Configuração no Cherry Studio

Com o SearXNG implantado, configure no CherryStudio.

Acesse a página de pesquisa na internet e selecione Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Ao inserir a URL local, a validação falha inicialmente:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

O formato JSON não está habilitado por padrão. Ajuste o arquivo de configuração.

No Docker, localize a pasta marcada em **Files**:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Expanda e encontre outra pasta marcada:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Abra o arquivo **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Abra o editor de arquivos:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Na linha 78, adicione `json` aos formatos:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Salve e reinicie a imagem:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Valide novamente no Cherry Studio:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Use `http://localhost:porta` para local ou `http://host.docker.internal:porta` para Docker.

Em implantações com autenticação HTTP, a validação retornará erro 401:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

Adicione as credenciais HTTP Basic Auth:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

A validação deve ser bem-sucedida.

### Outras Configurações

Para personalizar mecanismos de pesquisa, ajuste manualmente as configurações:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Mecanismos usados pelo modelo de IA requerem modificações no arquivo de configuração:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Exemplo de referência de linguagem:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

Para modificações extensas, edite localmente e cole no arquivo.

## Causas Comuns de Falha na Validação

### Formato JSON Não Adicionado

Adicione `json` aos formatos retornados:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Mecanismos de Pesquisa Mal Configurados

O Cherry Studio seleciona mecanismos com categorias `web` e `general`. Problemas ocorrem quando mecanismos como Google são bloqueados. Force o uso do Baidu:

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

### Limite de Taxa Excedido

Desative o limiter no settings.yml:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>