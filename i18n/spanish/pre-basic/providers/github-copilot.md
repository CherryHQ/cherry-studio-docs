
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# GitHub Copilot

Para usar GitHub Copilot, primero necesitas tener una cuenta de GitHub y suscribirte al servicio GitHub Copilot. La versión gratuita también funciona, pero no admite el modelo Claude 3.7 más reciente. Para más detalles, consulta el [sitio oficial de GitHub Copilot](https://github.com/features/copilot).

## Obtener Device Code

Haz clic en "Iniciar sesión en GitHub" para obtener el Device Code y cópialo.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Ejemplo de obtención de Device Code"><figcaption><p>Obtener Device Code</p></figcaption></figure>

## Ingresar Device Code en el navegador y autorizar

Después de obtener el Device Code correctamente, haz clic en el enlace para abrir el navegador. Inicia sesión en tu cuenta de GitHub dentro del navegador, ingresa el Device Code y autoriza el acceso.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Autorización de GitHub"><figcaption><p>Autorización de GitHub</p></figcaption></figure>

Tras autorizar con éxito, vuelve a Cherry Studio y haz clic en "Conectar con GitHub". Al completarse, se mostrarán tu nombre de usuario y avatar de GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Ejemplo de conexión exitosa con GitHub"><figcaption><p>Conexión exitosa con GitHub</p></figcaption></figure>

## Haz clic en "Administrar" para obtener la lista de modelos

Haz clic en el botón "Administrar" inferior para obtener automáticamente la lista de modelos compatibles actualmente.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Ejemplo de obtención de lista de modelos"><figcaption><p>Obtener lista de modelos</p></figcaption></figure>

## Preguntas frecuentes

### Error al obtener Device Code, reintentar

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Ejemplo de error al obtener Device Code"><figcaption><p>Error al obtener Device Code</p></figcaption></figure>

Actualmente las solicitudes se implementan con Axios, que no es compatible con proxy socks. Utiliza proxy de sistema, HTTP proxy, o no configures proxy en CherryStudio (usa proxy global). Primero verifica que tu conexión de red funcione correctamente para evitar este error.