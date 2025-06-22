---
icon: searchengin
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Despliegue y Configuración de SearXNG

CherryStudio admite búsquedas en la web a través de SearXNG, un proyecto de código abierto que se puede implementar localmente o en un servidor, por lo que su configuración difiere ligeramente de otros métodos que requieren proveedores de API.

**Enlace al proyecto SearXNG:** [SearXNG](https://github.com/searxng/searxng)

## Ventajas de SearXNG

*   Código abierto y gratuito, sin necesidad de API
*   Relativamente alto nivel de privacidad
*   Altamente personalizable

## Despliegue Local

### 1. Despliegue Directo con Docker

Como SearXNG no requiere configuración de entorno compleja y puede implementarse simplemente proporcionando un puerto libre sin necesidad de docker compose, la forma más rápida es usar Docker para obtener la imagen directamente.

#### 1. Descargar e instalar [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Después de instalar, seleccione una ruta de almacenamiento para la imagen:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Buscar y obtener la imagen de SearXNG

Escriba **searxng** en la barra de búsqueda:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Obtener la imagen:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Ejecutar la imagen

Después de obtener la imagen, vaya a la página **images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Seleccione la imagen obtenida y haga clic en ejecutar:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Abra las opciones de configuración:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Ejemplo con el puerto `8085`:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Después de ejecutarse con éxito, haga clic en el enlace para abrir la interfaz frontend de SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Si aparece esta página, significa que el despliegue fue exitoso:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Despliegue en Servidor

Dado que instalar Docker en Windows puede ser complicado, los usuarios pueden implementar SearXNG en un servidor y compartirlo con otros. Sin embargo, actualmente SearXNG no admite autenticación, lo que permite que otros escaneen y abusen de su instancia implementada.

Por ello, Cherry Studio ahora admite la configuración de [Autenticación HTTP Básica (RFC7617)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Authentication). Si implementa SearXNG en un entorno público, **debe** configurar la autenticación HTTP básica usando software de proxy inverso como Nginx. A continuación se muestra un breve tutorial que requiere conocimientos básicos de administración de Linux.

### Implementar SearXNG

De manera similar, use Docker para implementar. Suponiendo que ya ha instalado Docker CE siguiendo la [guía oficial](https://docs.docker.com/engine/install), aquí hay comandos para una instalación nueva en sistemas Debian:

```bash
sudo apt update
sudo apt install git -y

# Obtener el repositorio oficial
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Si su servidor tiene poco ancho de banda, establezca esto en false
export IMAGE_PROXY=true

# Modificar el archivo de configuración
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

Para cambiar el puerto de escucha local o reutilizar Nginx existente, edite `docker-compose.yaml`:

```yaml
version: "3.7"

services:
# Si no necesita Caddy y reutiliza Nginx local, elimine esto. No necesitamos Caddy por defecto.
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
# Si no necesita Caddy y reutiliza Nginx local, elimine lo anterior. No necesitamos Caddy por defecto.
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
    # Por defecto se asigna al puerto 8080 del host. Si quiere escuchar en el puerto 8000, cambie a "127.0.0.1:8000:8080"
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
# Si no necesita Caddy y reutiliza Nginx local, elimine lo siguiente
  caddy-data:
  caddy-config:
# Si no necesita Caddy y reutiliza Nginx local, elimine lo anterior
  valkey-data2:
```

Ejecute `docker compose up -d` para iniciar. Verifique los registros con `docker compose logs -f searxng`.

### Configurar Proxy Inverso Nginx y Autenticación HTTP Básica

Si usa paneles de servidor como BaoTa o 1Panel, consulte su documentación para configurar Nginx. Modifique el archivo de configuración como se muestra:

```conf
server
{
    listen 443 ssl;

    # Su nombre de host
    server_name search.example.com;

    # index index.html;
    # root /data/www/default;

    # Si está configurado SSL:
    ssl_certificate    /path/to/your/cert/fullchain.pem;
    ssl_certificate_key    /path/to/your/cert/privkey.pem;

    # HSTS
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";

    location / {
        # Agregar estas dos líneas (ajuste la ruta según su sistema)
        auth_basic "Introduzca su nombre de usuario y contraseña";
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

Si guarda la configuración en `/etc/nginx/conf.d`, genere el archivo de contraseñas (reemplace `example_name` y `example_password`):

```bash
echo "example_name:$(openssl passwd -5 'example_password')" > /etc/nginx/conf.d/search.htpasswd
```

Reinicie o recargue Nginx. Verifique que se solicite autenticación:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Configuración en Cherry Studio

Una vez implementado SearXNG localmente o en servidor, configure CherryStudio.

Acceda a los ajustes de búsqueda web y seleccione Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

Si la verificación falla al ingresar la URL local:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

Esto ocurre porque no se ha configurado el tipo de retorno JSON. Modifique el archivo de configuración.

En Docker, vaya a la pestaña Files, busque la carpeta con etiqueta:

<figure><img src="../../.gitbook/assets/searxng_config_img_14.png" alt=""><figcaption></figcaption></figure>

Expanda y encuentre otra carpeta etiquetada:

<figure><img src="../../.gitbook/assets/searxng_config_img_15.png" alt=""><figcaption></figcaption></figure>

Busque el archivo de configuración **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Ábralo en el editor:

<figure><img src="../../.gitbook/assets/searxng_config_img_17.png" alt=""><figcaption></figcaption></figure>

En la línea 78, modifique para incluir JSON:

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Guarde y reinicie la imagen después de agregar el tipo JSON:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Verifique nuevamente en Cherry Studio (ahora debería ser exitosa):

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Use `http://localhost:port` localmente o `http://host.docker.internal:port` para Docker.

Para instancias con autenticación HTTP básica, Cherry Studio mostrará error 401 durante la verificación:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

Ingrese las credenciales en el cliente:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

La verificación ahora debería ser exitosa.

### Otras Configuraciones

SearXNG tiene capacidades de búsqueda predeterminadas. Para personalizar motores de búsqueda:

Estos ajustes no afectan las llamadas de modelos grandes:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Para motores usados por modelos grandes, edite el archivo de configuración:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Referencia de configuración de idioma:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

Si el contenido es extenso, edítelo localmente y pegue los cambios.

## Causas Comunes de Falla en Verificación

### Formato de Retorno Sin JSON

Agregue json al formato en el archivo de configuración:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Motor de Búsqueda Mal Configurado

Cherry Studio usa motores con categorías `web` y `general`. Google puede fallar en algunas regiones. Para usar Baidu:

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

### Velocidad de Acceso Demasiado Alta

Desactive el limitador en la configuración:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>