---
icon: database
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuración de datos

Esta interfaz permite realizar operaciones como respaldo en la nube y local de datos del cliente, consulta del directorio de datos local y limpieza de la caché.

### Respaldo de datos

Actualmente, el respaldo de datos solo admite el método WebDAV. Puedes elegir servicios compatibles con WebDAV para realizar copias de seguridad en la nube.

También puedes sincronizar datos entre múltiples dispositivos mediante el método:  
`Computadora A` $$\xrightarrow{\text{respaldo}}$$ `WebDAV` $$\xrightarrow{\text{restauración}}$$ `Computadora B`

#### Tomando Nutstore como ejemplo

1. Inicia sesión en Nutstore, haz clic en el nombre de usuario en la esquina superior derecha y selecciona "Información de cuenta":
<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecciona "Opciones de seguridad" y haz clic en "Agregar aplicación":
<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Ingresa el nombre de la aplicación y genera una contraseña aleatoria:
<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copia y guarda la contraseña:
<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtén la dirección del servidor, cuenta y contraseña:
<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. En Cherry Studio > Configuración > Configuración de datos, completa la información de WebDAV:
<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Selecciona respaldar o restaurar datos, y configura la frecuencia de copias de seguridad automáticas:
<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Servicios WebDAV con requisitos bajos disponibles en discos en la nube:
* [Nutstore](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (requiere membresía)
* [Alibaba Cloud Drive](https://www.alipan.com/) (requiere compra)
* [Box](https://www.box.com/) (10GB gratuito, límite de 250MB por archivo)
* [Dropbox](https://www.dropbox.com/) (2GB gratuito, ampliable mediante invitaciones)
* [TeraCloud](https://teracloud.jp/en/) (10GB gratis + 5GB adicional por invitación)
* [Yandex Disk](https://disk.yandex.com/) (10GB gratuito)

Servicios que requieren despliegue propio:
* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [Sharelist](https://github.com/reruin/sharelist)
{% endhint %}