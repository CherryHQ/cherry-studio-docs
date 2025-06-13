---
icon: searchengin
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Despliegue y Configuración de SearXNG

CherryStudio admite búsquedas web mediante SearXNG. SearXNG es un proyecto de código abierto que puede desplegarse localmente o en servidores, por lo que su configuración difiere ligeramente de otros proveedores que requieren API.

**Enlace al proyecto SearXNG**: [SearXNG](https://github.com/searxng/searxng)

## Ventajas de SearXNG

* De código abierto y gratuito, sin necesidad de API
* Mayor privacidad relativa
* Altamente personalizable

## Despliegue Local

### 1. Despliegue Directo con Docker

Como SearXNG no requiere configuraciones complejas de entorno y puede desplegarse simplemente proporcionando un puerto libre sin necesidad de docker compose, la forma más rápida es usar Docker para obtener la imagen directamente.

#### 1. Descargar e instalar [docker](https://www.docker.com/)

<figure><img src="../../.gitbook/assets/searxng_config_img_01.png" alt=""><figcaption></figcaption></figure>

Tras la instalación, selecciona una ruta de almacenamiento para imágenes:

<figure><img src="../../.gitbook/assets/searxng_config_img_02.png" alt=""><figcaption></figcaption></figure>

#### 2. Buscar y obtener la imagen de SearXNG

En la barra de búsqueda escribe **searxng**:

<figure><img src="../../.gitbook/assets/searxng_config_img_03.png" alt=""><figcaption></figcaption></figure>

Obtener la imagen:

<figure><img src="../../.gitbook/assets/searxng_config_img_04.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_05.png" alt=""><figcaption></figcaption></figure>

#### 3. Ejecutar la imagen

Tras obtenerla, ve a la página **images**:

<figure><img src="../../.gitbook/assets/searxng_config_img_06.png" alt=""><figcaption></figcaption></figure>

Selecciona la imagen obtenida y haz clic en ejecutar:

<figure><img src="../../.gitbook/assets/searxng_config_img_07.png" alt=""><figcaption></figcaption></figure>

Abre la configuración para realizar ajustes:

<figure><img src="../../.gitbook/assets/searxng_config_img_08.png" alt=""><figcaption></figcaption></figure>

Usando el puerto `8085` como ejemplo:

<figure><img src="../../.gitbook/assets/searxng_config_img_09.png" alt=""><figcaption></figcaption></figure>

Tras ejecutarse correctamente, haz clic en el enlace para abrir la interfaz de SearXNG:

<figure><img src="../../.gitbook/assets/searxng_config_img_10.png" alt=""><figcaption></figcaption></figure>

Esta página indica un despliegue exitoso:

<figure><img src="../../.gitbook/assets/searxng_config_img_11.png" alt=""><figcaption></figcaption></figure>

## Despliegue en Servidor

Dado que instalar Docker en Windows puede ser complicado, los usuarios pueden implementar SearXNG en un servidor y compartirlo con otros. Lamentablemente, SearXNG aún no admite autenticación, lo que permite que otros escaneen y abusen de tu instancia implementada.

Cherry Studio admite [Autenticación Básica HTTP (RFC7617)](https://developer.mozilla.org/es/docs/Web/HTTP/Authentication). Si expones tu SearXNG en Internet, **debes** configurar la autenticación básica mediante software como Nginx. A continuación, un breve tutorial que requiere conocimientos básicos de Linux.

### Implementar SearXNG

Similar al despliegue local con Docker. Asumiendo que ya tienes Docker CE instalado según el [tutorial oficial](https://docs.docker.com/engine/install), estos comandos funcionan para Debian:

```bash
sudo apt update
sudo apt install git -y

# Obtener repositorio oficial
cd /opt
git clone https://github.com/searxng/searxng-docker.git
cd /opt/searxng-docker

# Para servidores con poco ancho de banda, establecer como false
export IMAGE_PROXY=true

# Modificar configuración
cat <<EOF > /opt/searxng-docker/searxng/settings.yml
# ver https://docs.searxng.org/admin/settings/settings.html#settings-use-default-settings
use_default_settings: true
server:
  # base_url definido en SEARXNG_BASE_URL, ver .env y docker-compose.yml
  secret_key: $(openssl rand -hex 32)
  limiter: false  # deshabilitar para instancias privadas
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

Para cambiar puertos o reutilizar Nginx existente, edita `docker-compose.yaml`:

```yaml
# (Contenido del archivo conservado sin cambios)
```

Ejecuta `docker compose up -d` para iniciar. Ver logs con `docker compose logs -f searxng`.

### Configurar Proxy Inverso Nginx y Autenticación HTTP

Si usas paneles como BT.cn o 1Panel, consulta su documentación para configurar proxy inverso y modificar la configuración Nginx según este ejemplo:

```conf
server
{
    listen 443 ssl;

    # Tu nombre de host
    server_name search.ejemplo.com;

    # (Configuración SSL conservada)

    location / {
        # Añadir estas dos líneas
        auth_basic "Ingrese usuario y contraseña";
        auth_basic_user_file /etc/nginx/conf.d/search.htpasswd;

        # (Resto de configuración proxy conservada)
    }
}
```

Crea el archivo de contraseñas (reemplaza `usuario` y `contraseña`):

```bash
echo "usuario:$(openssl passwd -5 'contraseña')" > /etc/nginx/conf.d/search.htpasswd
```

Reinicia Nginx y verifica que funcione:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-example.png" alt=""><figcaption></figcaption></figure>

## Configuración en Cherry Studio

Tras implementar SearXNG, configura CherryStudio:

Ve a ajustes de búsqueda web > Selecciona Searxng:

<figure><img src="../../.gitbook/assets/searxng_config_img_12.png" alt=""><figcaption></figcaption></figure>

La validación fallará inicialmente:

<figure><img src="../../.gitbook/assets/searxng_config_img_13.png" alt=""><figcaption></figcaption></figure>

Esto se debe a que el formato JSON no está habilitado. Modifica la configuración:

En Docker > Files > Busca el archivo **settings.yml**:

<figure><img src="../../.gitbook/assets/searxng_config_img_16.png" alt=""><figcaption></figcaption></figure>

Edita el archivo, línea ~78, añade "json":

<figure><img src="../../.gitbook/assets/searxng_config_img_18.png" alt=""><figcaption></figcaption></figure>

Guarda y reinicia la imagen:

<figure><img src="../../.gitbook/assets/searxng_config_img_19.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_20.png" alt=""><figcaption></figcaption></figure>

Ahora la validación será exitosa:

<figure><img src="../../.gitbook/assets/searxng_config_img_21.png" alt=""><figcaption></figcaption></figure>

Usa `http://localhost:puerto` localmente o `http://host.docker.internal:puerto` para Docker.

Si implementaste en servidor con autenticación, la validación fallará (código 401):

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting-failed.png" alt=""><figcaption></figcaption></figure>

Configura los credenciales en Cherry Studio:

<figure><img src="../../.gitbook/assets/searxng-basic-auth-client-setting.png" alt=""><figcaption></figcaption></figure>

Y la validación será exitosa.

### Otras Configuraciones

Para personalizar motores de búsqueda, modifica el archivo de configuración:

<figure><img src="../../.gitbook/assets/searxng_config_img_22.png" alt=""><figcaption></figcaption></figure>

Configura los motores para modelos grandes:

<figure><img src="../../.gitbook/assets/searxng_config_img_23.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/searxng_config_img_24.png" alt=""><figcaption></figcaption></figure>

Referencia de configuración:

<figure><img src="../../.gitbook/assets/searxng_config_img_25.png" alt=""><figcaption></figcaption></figure>

## Fallos Comunes de Validación

### Formato JSON no habilitado

Añade "json" en settings.yml:

<figure><img src="../../.gitbook/assets/searxng_json_format.png" alt=""><figcaption></figcaption></figure>

### Motores mal configurados

CherryStudio selecciona motores con categorías web/general. Para evitar fallos con Google en ciertas regiones, fuerza el uso de Baidu:

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

### Límite de tasa

Desactiva limiter en ajustes:

<figure><img src="../../.gitbook/assets/searxng_limiter.png" alt=""><figcaption></figcaption></figure>