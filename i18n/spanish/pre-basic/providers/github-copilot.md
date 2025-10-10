# GitHub Copilot


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Para usar GitHub Copilot, primero debes tener una cuenta de GitHub y suscribirte al servicio GitHub Copilot. La versión gratuita (free) también es válida, pero no admite el último modelo Claude 3.7. Para más detalles, consulta el [sitio oficial de GitHub Copilot](https://github.com/features/copilot).

## Obtener Device Code

Haz clic en "Iniciar sesión en GitHub" para obtener el Device Code y cópialo.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Ejemplo de obtención de Device Code"><figcaption><p>Obtener Device Code</p></figcaption></figure>

## Ingresar Device Code en el navegador y autorizar

Tras obtener el Device Code correctamente, haz clic en el enlace para abrir el navegador. Inicia sesión en tu cuenta de GitHub, ingresa el Device Code y otorga la autorización.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Ejemplo de autorización de GitHub"><figcaption><p>Autorización de GitHub</p></figcaption></figure>

Al autorizar correctamente, regresa a Cherry Studio y haz clic en "Conectar GitHub". Tras el éxito, se mostrarán tu nombre de usuario y avatar de GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Ejemplo de conexión exitosa de GitHub"><figcaption><p>Conexión exitosa de GitHub</p></figcaption></figure>

## Haz clic en "Administrar" para obtener la lista de modelos

Haz clic en el botón "Administrar" inferior para obtener automáticamente la lista de modelos actualmente compatibles mediante conexión a internet.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Ejemplo de botón Administrar para obtener lista de modelos"><figcaption><p>Obtener lista de modelos</p></figcaption></figure>

## Preguntas frecuentes

### Error al obtener Device Code, reintenta

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Ejemplo de error al obtener Device Code"><figcaption><p>Error al obtener Device Code</p></figcaption></figure>

Actualmente las solicitudes se construyen con Axios, que no admite proxies socks. Utiliza proxy de sistema o HTTP, o no configures proxy en CherryStudio y usa proxy global. Primero verifica que tu conexión de red funcione correctamente para evitar este error.