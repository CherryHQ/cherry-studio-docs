
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# GitHub Copilot

Para usar GitHub Copilot, primero necesitas tener una cuenta de GitHub y suscribirte al servicio GitHub Copilot. La versión gratuita también es válida, pero no admite el modelo más reciente Claude 3.7. Consulta los detalles en el [sitio oficial de GitHub Copilot](https://github.com/features/copilot).

## Obtener el Código del Dispositivo

Haz clic en "Iniciar sesión en GitHub" para obtener y copiar el Device Code.

<figure><img src="../../.gitbook/assets/获取DeviceCode.png" alt="Ejemplo de obtención del Device Code"><figcaption><p>Obtener el Device Code</p></figcaption></figure>

## Introducir el Device Code en el navegador y autorizar

Tras obtener el Device Code, haz clic en el enlace para abrir el navegador. Inicia sesión en tu cuenta de GitHub, ingresa el Device Code y otorga la autorización.

<figure><img src="../../.gitbook/assets/GitHub授权.png" alt="Ejemplo de autorización de GitHub"><figcaption><p>Autorizar GitHub</p></figcaption></figure>

Después de la autorización exitosa, vuelve a Cherry Studio y haz clic en "Conectar GitHub". Tras conectar, se mostrará tu nombre de usuario y avatar de GitHub.

<figure><img src="../../.gitbook/assets/GitHub连接成功.png" alt="Ejemplo de conexión exitosa de GitHub"><figcaption><p>Conexión exitosa a GitHub</p></figcaption></figure>

## Obtener la lista de modelos haciendo clic en "Administrar"

Haz clic en el botón "Administrar" para obtener automáticamente la lista de modelos compatibles actualmente mediante conexión a internet.

<figure><img src="../../.gitbook/assets/管理按钮获取模型列表.png" alt="Ejemplo de obtención de lista de modelos"><figcaption><p>Obtener lista de modelos</p></figcaption></figure>

## Preguntas frecuentes

### Error al obtener el Device Code, por favor reintenta

<figure><img src="../../.gitbook/assets/获取DeviceCode失败.png" alt="Ejemplo de error al obtener el Device Code"><figcaption><p>Error al obtener el Device Code</p></figcaption></figure>

Actualmente, las solicitudes se construyen con Axios, que no admite proxies socks. Utiliza proxy del sistema, proxy HTTP, o configura el proxy directamente a nivel global en lugar de en CherryStudio. Primero, asegúrate de que tu conexión de red funcione correctamente para evitar fallos al obtener el Device Code.