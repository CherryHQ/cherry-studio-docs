---
icon: database
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuración de Datos

Esta interfaz permite realizar operaciones como copias de seguridad en la nube y locales de datos del cliente, consulta de directorios de datos locales y limpieza de caché.

### Copia de Seguridad de Datos

Actualmente, la copia de seguridad de datos solo admite el método WebDAV. Puedes elegir servicios compatibles con WebDAV para realizar copias de seguridad en la nube.

También puedes sincronizar datos entre múltiples dispositivos mediante este flujo: `Computadora A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restaurar}}$$ `Computadora B`.

#### Ejemplo con Jianguoyun

1. Inicia sesión en Jianguoyun, haz clic en el nombre de usuario en la esquina superior derecha y selecciona "Información de cuenta":
<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecciona "Opciones de seguridad" y haz clic en "Añadir aplicación":
<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Ingresa el nombre de la aplicación y genera una contraseña aleatoria:
<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copia y guarda la contraseña:
<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtén la dirección del servidor, cuenta y contraseña:
<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. En Cherry Studio Configuración → Configuración de datos, completa la información de WebDAV:
<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Selecciona copia de seguridad o restauración de datos, y configura la periodicidad de copias automáticas:
<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Servicios WebDAV con bajo umbral de acceso (principalmente almacenamientos en nube):
* [Jianguoyun](https://www.jianguoyun.com/)
* [123 Pan](https://www.123pan.com/) (requiere membresía)
* [Alibaba Cloud Drive](https://www.alipan.com/) (de pago)
* [Box](https://www.box.com/) (10GB gratis, límite 250MB por archivo)
* [Dropbox](https://www.dropbox.com/) (2GB gratis, ampliable a 16GB)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratis + 5GB por invitación)
* [Yandex Disk](https://disk.yandex.com/) (10GB gratis)

Otras opciones que requieren despliegue propio:
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}