
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Huawei Cloud

1. Crea una cuenta e inicia sesión en [Huawei Cloud](https://auth.huaweicloud.com/authui/login)

2. Haz clic en [este enlace](https://console.huaweicloud.com/modelarts/?region=cn-southwest-2#/model-studio/homepage) para entrar a la consola de ModelArts

3. Autorización

<details>

<summary>Pasos de autorización (omite si ya estás autorizado)</summary>

1. Después de ingresar al enlace del punto 2, accede a la página de autorización siguiendo las indicaciones (haz clic en IAM User → Añadir delegación → Usuario normal)

![](<../../.gitbook/assets/image (49).png>)

2. Después de crear, vuelve al enlace del punto 2
3. Aparecerá un mensaje de permisos insuficientes, haz clic en "Haz clic aquí" dentro del mensaje
4. Añade la autorización existente y confirma

![](<../../.gitbook/assets/image (50).png>)

&#x20;Nota: Este método es adecuado para principiantes. Solo sigue las indicaciones para hacer clic. Si puedes autorizar directamente de otra forma, hazlo a tu manera.

</details>

4. Haz clic en Administración de autenticación en la barra lateral, crea una API Key (clave secreta) y cópiala

<figure><img src="../../.gitbook/assets/微信截图_20250214034650.png" alt=""><figcaption></figcaption></figure>

Luego crea un nuevo proveedor en CherryStudio

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt="" width="300"><figcaption></figcaption></figure>

Después de crear, ingresa la clave secreta

5. Haz clic en Despliegue de modelos en la barra lateral y reclama todos

<figure><img src="../../.gitbook/assets/微信截图_20250214034751.png" alt=""><figcaption></figcaption></figure>

6. Haz clic en Llamar

<figure><img src="../../.gitbook/assets/image (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

Copia la dirección en ① y pégala en la dirección del proveedor de CherryStudio. **Añade "#" al final**  
**Añade "#" al final**  
**Añade "#" al final**  
**Añade "#" al final**  
**Añade "#" al final**

¿Por qué añadir "#"? [Consulta aquí](https://docs.cherry-ai.com/cherrystudio/preview/settings/providers#api-di-zhi)

> También puedes omitir esa parte y seguir el tutorial directamente;  
> o usar el método de eliminar v1/chat/completions. Si sabes cómo hacerlo, usa tu método; si no, sigue estrictamente el tutorial.

<figure><img src="../../.gitbook/assets/image (2) (3).png" alt=""><figcaption></figcaption></figure>

Luego copia el nombre del modelo en ②. En CherryStudio, haz clic en "+ Añadir" para crear un nuevo modelo

<figure><img src="../../.gitbook/assets/image (4) (3).png" alt=""><figcaption></figcaption></figure>

Ingresa el nombre del modelo exactamente como aparece, sin añadir comillas ni modificaciones, copiando fielmente el ejemplo.

<figure><img src="../../.gitbook/assets/image (3) (3).png" alt=""><figcaption></figcaption></figure>

Haz clic en Añadir modelo para completar la creación.

{% hint style="info" %}
En Huawei Cloud, como la dirección de cada modelo es diferente, cada modelo requiere un nuevo proveedor. Repite los pasos anteriores para cada uno.
{% endhint %}