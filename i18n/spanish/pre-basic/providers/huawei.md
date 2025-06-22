
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Huawei Cloud

1. Crea una cuenta e inicia sesión en [Huawei Cloud](https://auth.huaweicloud.com/authui/login)
2. Haz clic en [este enlace](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) para acceder a la consola de ModelArts
3. Autorización

<details>

<summary>Pasos de autorización (omitir si ya está autorizado)</summary>

1. Después de ingresar al enlace del paso (2), sigue las indicaciones para llegar a la página de autorización (haz clic en IAM subusuario → añadir delegación → usuario común)

![](<../../.gitbook/assets/image (49).png>)

2. Después de crear, regresa al enlace del paso (2)
3. Aparecerá un mensaje de permisos insuficientes. Haz clic en "haz clic aquí" dentro del mensaje
4. Agrega autorizaciones existentes y confirma

![](<../../.gitbook/assets/image (50).png>)

&#x20;Nota: Este método es adecuado para principiantes. No requiere revisar demasiado contenido, solo sigue las indicaciones. Si puedes autorizar correctamente de otra manera, usa tu propio método.

</details>

4. En la barra lateral, haz clic en Administración de autenticación, crea una API Key (clave secreta) y cópiala

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Luego crea un nuevo proveedor de servicios en CherryStudio

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Después de crearlo, ingresa la clave secreta

5. En la barra lateral, haz clic en Implementación de modelos y reclama todos los recursos

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6. Haz clic en Llamadas (Invoke)

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Copia la dirección en ①, pégala en la dirección del proveedor de servicios de CherryStudio **y agrega "#" al final**

y agrega "#" al final

y agrega "#" al final

> ¿Por qué agregar "#"? [Consulta aquí](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)
>
> También puedes omitir la explicación y seguir directamente el tutorial;
>
> Alternativamente, puedes completarlo eliminando v1/chat/completions. Si sabes cómo hacerlo, usa tu método preferido. Si no estás seguro, sigue estrictamente este tutorial.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Luego copia el nombre del modelo en ② y en CherryStudio haz clic en "+ Añadir" para crear un nuevo modelo

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Ingresa el nombre del modelo exactamente como aparece, sin modificaciones ni comillas. Copia fielmente el ejemplo.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Haz clic en "Añadir modelo" para completar la configuración.

{% hint style="info" %}
En Huawei Cloud, cada modelo tiene una dirección diferente, por lo que debes crear un proveedor de servicios separado para cada modelo. Repite los pasos anteriores para cada uno.
{% endhint %}