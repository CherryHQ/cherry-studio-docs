---
icon: seal-question
---
# Preguntas frecuentes


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Códigos de error comunes

* **4xx (Códigos de estado de error del cliente)**: Generalmente son errores como sintaxis de solicitud incorrecta, falla de autenticación o falla de autorización que impiden completar la solicitud.
* **5xx (Códigos de estado de error del servidor)**: Generalmente son errores del lado del servidor, como caídas del servidor, tiempo de espera agotado para procesar solicitudes, etc.

| Código de error | Posibles causas                                                                                                                                                            | Solución                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **400**         | Formato del cuerpo de la solicitud incorrecto, etc.                                                                                                                        | <p>Revise el contenido del error devuelto por el diálogo o la <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">consola</a> para ver el mensaje de error y actúe según las indicaciones.</p><p><a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa"><mark style="color:purple;">【Situación común 1】</mark>: Si es un modelo Gemini, puede que sea necesario vincular una tarjeta;<br><mark style="color:purple;">【Situación común 2】</mark>: Volumen de datos excede el límite (común en modelos visuales);<br><mark style="color:purple;">【Situación común 3】</mark>: Parámetros no admitidos o incorrectos. Pruebe con un asistente nuevo;<br><mark style="color:purple;">【Situación común 4】</mark>: Contexto excede el límite. Borre el contexto o reduzca elementos.</a></p> |
| **401**         | Autenticación fallida: modelo no compatible o cuenta del servidor suspendida                                                                                               | Verifique el estado de la cuenta con el proveedor correspondiente                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **403**         | Sin permisos para realizar la operación solicitada                                                                                                                         | Actúe según la información del error en el diálogo o la [consola](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **404**         | Recurso solicitado no encontrado                                                                                                                                           | Verifique la ruta de solicitud, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **422**         | Formato de solicitud correcto pero error semántico                                                                                                                         | El servidor puede analizar pero no procesar. Común con errores semánticos JSON (ej: valor nulo; se esperaba texto pero se proporcionó número/booleano).                                                                                                                                                                                                                                                                                                                                                                                 |
| **429**         | Límite de tasa de solicitudes alcanzado                                                                                                                                        | Espere un momento antes de volver a intentar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **500**         | Error interno del servidor, no se puede completar la solicitud                                                                                                             | Contacte al proveedor si persiste                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **501**         | Función solicitada no implementada en el servidor                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **502**         | El servidor (como puerta de enlace o proxy) recibió una respuesta inválida del servidor remoto                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **503**         | Servidor temporalmente indisponible por sobrecarga o mantenimiento. El retraso puede especificarse en el encabezado Retry-After                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **504**         | Tiempo de espera agotado cuando un servidor (como puerta de enlace o proxy) intentó acceder a un servidor remoto                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

***

## Método para ver errores en la consola

* Haga clic en la ventana del cliente Cherry Studio y presione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- La ventana activa debe ser el cliente Cherry Studio para abrir la consola;
- Abra la consola primero, luego inicie pruebas/diálogos para capturar información.
{% endhint %}

* En la consola: haga clic en <mark style="color:blue;">`Network`</mark> → Busque el último <mark style="color:red;">`completions`</mark> _con × rojo (errores en diálogo/traducción)_ o <mark style="color:red;">`generations`</mark> _errores en dibujo)_ → Haga clic en <mark style="color:blue;">`Response`</mark> para ver la respuesta completa.

> Si no identifica el error, envíe captura al [grupo oficial](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método funciona en diálogos, pruebas de modelo, añadir bases de conocimiento, dibujo, etc. Siempre abra la consola antes de realizar solicitudes.

{% hint style="info" %}
Nombres en la columna Name (② arriba) varían:

Diálogo/traducción/pruebas: <mark style="color:red;">`completions`</mark>

Dibujo: <mark style="color:red;">`generations`</mark>

Crear base de conocimiento: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Fórmulas no renderizadas/error de renderizado

* Si muestra código de fórmula: verifique delimitadores

> **Uso de delimitadores**
>
> _Fórmula en línea_
>
> * Un dólar: `$formula$`
> * o `\(` y `\)`: `\(formula\)`
>
> _Bloque de fórmula_
>
> * Dos dólares: `$$formula$$`
> * o `\[formula\]`
> * Ejemplo: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Error/renderizado incorrecto: común con texto chino. Cambie a motor KaTeX.

***

## No se puede crear base de conocimiento/error al obtener dimensiones de incrustación

1. Estado del modelo no disponible

> Verifique compatibilidad con el proveedor o estado del servicio.

2. Se usó modelo no-incrustable

***

## Modelo no reconoce imágenes/no puede subir/seleccionar imágenes

Primero verifique compatibilidad del modelo. Cherry Studio marca modelos de visión con icono 👁️.

Modelos de visión permiten subir imágenes. Si no coincide: en lista de modelos del proveedor, haga clic en ⚙️ y active opción de imagen.

Para información detallada: consulte proveedor. Modelos no-visuales no procesan imágenes aunque se active.