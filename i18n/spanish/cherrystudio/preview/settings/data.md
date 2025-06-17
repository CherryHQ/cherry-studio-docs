---
icon: database
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuración de Datos

Esta interfaz permite realizar operaciones como copia de seguridad en la nube y local de datos del cliente, consulta del directorio de datos local y limpieza de caché.

### Copia de Seguridad de Datos

Actualmente, la copia de seguridad de datos solo admite el método WebDAV. Puedes elegir servicios compatibles con WebDAV para realizar copias de seguridad en la nube.

También puedes sincronizar datos entre múltiples dispositivos mediante el método `Computadora A` $$\xrightarrow{\text{backup}}$$ `WebDAV` $$\xrightarrow{\text{restaurar}}$$ `Computadora B`.

#### Ejemplo con Nutstore

1. Inicia sesión en Nutstore, haz clic en el nombre de usuario en la esquina superior derecha y selecciona "Información de la cuenta":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecciona "Opciones de seguridad" y haz clic en "Agregar aplicación":

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Ingresa el nombre de la aplicación y genera una contraseña aleatoria:

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copia y guarda la contraseña:

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtén la dirección del servidor, cuenta y contraseña:

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. En Configuración de Cherry Studio → Configuración de datos, completa la información de WebDAV:

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Selecciona hacer copia de seguridad o restaurar datos, y configura el intervalo automático para copias de seguridad:

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Los servicios WebDAV con menor barrera de entrada suelen ser almacenamientos en la nube:
* [Nutstore](https://www.jianguoyun.com/)
* [123 Pan](https://www.123pan.com/) (requiere membresía)
* [Aliyun Drive](https://www.alipan.com/) (requiere compra)
* [Box](https://www.box.com/) (10GB de espacio gratuito, máximo 250MB por archivo)
* [Dropbox](https://www.dropbox.com/) (2GB gratis, ampliable hasta 16GB mediante invitaciones)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratis + 5GB adicionales por invitación)
* [Yandex Disk](https://disk.yandex.com/) (10GB para usuarios gratuitos)

Alternativas que requieren implementación propia:
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}