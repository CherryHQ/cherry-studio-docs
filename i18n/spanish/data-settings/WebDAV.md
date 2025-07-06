---
icon: cloud-arrow-up
---
# Respaldo WebDAV


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio permite realizar copias de seguridad mediante WebDAV. Puedes elegir un servicio WebDAV adecuado para tus respaldos en la nube.

Con WebDAV, puedes lograr sincronización multipantalla mediante este método: `PC A` $$\xrightarrow{\text{respaldar}}$$ `WebDAV` $$\xrightarrow{\text{restaurar}}$$ `PC B`.

#### Ejemplo con Jianguoyun (Nutstore)

1. Inicia sesión en Jianguoyun, haz clic en tu nombre de usuario en la esquina superior derecha y selecciona "Información de cuenta":

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

2. Selecciona "Opciones de seguridad", haz clic en "Agregar aplicación"

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

3. Ingresa el nombre de la aplicación y genera una contraseña aleatoria;

<figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

4. Copia y guarda la contraseña;

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

5. Obtén la dirección del servidor, cuenta y contraseña;

<figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

6. En Configuración de Cherry Studio → Configuración de datos, completa la información de WebDAV;

<figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

7. Selecciona respaldar o restaurar datos y configura el intervalo de respaldos automáticos.

<figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Los servicios WebDAV con bajo umbral técnico generalmente incluyen almacenamiento en la nube:

- [Jianguoyun](https://www.jianguoyun.com/)
- [123 Pan](https://www.123pan.com/) (requiere membresía)
- [Aliyun Cloud Drive](https://www.alipan.com/) (requiere compra)
- [Box](https://www.box.com/) (espacio gratuito: 10GB, límite por archivo: 250MB)
- [Dropbox](https://www.dropbox.com/) (espacio gratuito: 2GB, ampliable hasta 16GB mediante invitaciones)
- [TeraCloud](https://teracloud.jp/en/) (espacio gratuito: 10GB + 5GB adicional por invitaciones)
- [Yandex Disk](https://disk.yandex.com/) (capacidad gratuita: 10GB)

Alternativas que requieren despliegue propio:

- [Alist](https://alist.nn.ci/zh/)
- [Cloudreve](https://cloudreve.org/)
- [sharelist](https://github.com/reruin/sharelist)
{% endhint %}