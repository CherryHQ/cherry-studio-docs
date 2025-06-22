---
icon: searchengin
---

{% hint style="warning" %}
Este documento foi traduzido do chinês por IA e ainda não foi revisado.
{% endhint %}

# Implantação e Configuração do SearXNG

CherryStudio oferece suporte à pesquisa na web via SearXNG. Como o SearXNG é um projeto de código aberto que pode ser implantado localmente ou em servidores, sua configuração difere ligeiramente de outros provedores que exigem APIs.

**Link do projeto SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## Vantagens do SearXNG

* Código aberto e gratuito, sem necessidade de API
* Alta privacidade relativa
* Altamente personalizável

## Implantação Local

### 1. Implantação Direta com Docker

Como o SearXNG não requer configurações complexas de ambiente, podemos implantá-lo rapidamente usando Docker com apenas uma porta livre, sem precisar do docker compose.

#### 1. Baixar e configurar [Docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Após instalar, selecione um caminho para armazenamento de imagens:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Pesquisar e baixar a imagem do SearXNG

Na barra de pesquisa, digite **searxng**:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Baixar a imagem:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Executar a imagem

Após o download, acesse a página **Images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Selecione a imagem baixada e clique em "Run":

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Abra as configurações para ajustar:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Exemplo usando a porta `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Após execução bem-sucedida, clique no link para abrir a interface do SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Esta página confirma a implantação bem-sucedida:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Implantação em Servidor

Como a instalação do Docker no Windows pode ser complexa, os usuários podem implantar o SearXNG em servidores e compartilhá-lo. No entanto, o SearXNG atualmente **não suporta autenticação**, permitindo que outros localizem e abusem da instância.

Para solucionar isso, o Cherry Studio agora suporta [Autenticação Básica HTTP (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Se você expor seu SearXNG publicamente, **configure obrigatoriamente** a autenticação via Nginx ou software similar. Abaixo está um tutorial rápido (requer conhecimentos básicos de Linux).

### Implantar o SearXNG

Use Docker conforme anteriormente. Supondo que o Docker CE já está instalado ([tutorial oficial](https://docs.docker.com/engine/install)), execute estes comandos (Debian):

```bash
sudo apt update
sudo apt install git -y

# Clonar repositório oficial
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Para servidores com baixa largura de banda, defina como false
export IMAGE_PROXY=true

# Modificar configurações
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

Para alterar a porta ou reutilizar um Nginx existente, edite `docker-compose.yaml`:

```yaml
version: "3.7"

services:
# Remova esta seção para reutilizar o Nginx existente
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
# Remova esta seção para reutilizar o Nginx existente
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
    # Porta padrão 8080. Para usar 8000: "127.0.0.1:8000:8080"
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
# Remova esta seção para reutilizar o Nginx existente
  caddy-data:
  caddy-config:
# Remova esta seção para reutilizar o Nginx existente
  valkey-data2:
```

Execute `docker compose up -d` para iniciar. Monitore logs com `docker compose logs -f searxng`.

### Configurar Proxy Reverso e Autenticação HTTP Básica no Nginx

Se usar painéis como Baota ou 1Panel, consulte a documentação para configurar o proxy reverso. Adicione ao arquivo Nginx:

```conf
server
{
    listen 443 ssl;

    # Seu nome de host
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # Certificado SSL
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # Adicione estas linhas ao bloco location
    location / {
        auth_basic "Informe seu usuário e senha";
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

Crie o arquivo de senhas (substitua `exemplo_usuario` e `exemplo_senha`):

```bash
echo "exemplo_usuario:$(openssl passwd -5 'exemplo_senha')" > /etc/nginx/conf.d/search.htpasswd
```

Reinicie o Nginx. Acesse a página para verificar a autenticação:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Configuração no Cherry Studio

Após implantar o SearXNG, configure no CherryStudio:

Acesse as configurações de pesquisa na web e selecione Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

A validação inicial falhará (normal, sem JSON configurado):

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

### Corrigir Configuração

No Docker, acesse a guia **Files** e localize `settings.yml`:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Abra o editor de arquivos:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

Na linha 78, adicione `json` aos formatos:

**Antes**  
<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

**Depois**  
<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

Reinicie a imagem:

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Valide novamente no Cherry Studio:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Use:
- Local: `http://localhost:[porta]`
- Docker: `http://host.docker.internal:[porta]`

Para instâncias em servidor com autenticação, adicione credenciais nas configurações:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

### Personalização de Mecanismos de Busca

O SearXNG vem com configurações padrão. Para personalizar mecanismos usados pelos modelos de IA, ajuste o arquivo de configuração:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

Exemplo de configuração:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

## Erros Comuns de Validação

### Formato JSON Não Adicionado

Adicione `json` aos formatos em `settings.yml`:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Mecanismos de Busca Incorretos

Para evitar falhas com Google em regiões bloqueadas, force o uso do Baidu:

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

Desative o `limiter` em `settings.yml`:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>