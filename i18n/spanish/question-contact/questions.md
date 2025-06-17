---
icon: seal-question
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Preguntas Frecuentes

## Códigos de Error Comunes

* **4xx (Códigos de estado de error del cliente)**: Generalmente indican errores de sintaxis en la solicitud, fallos de autenticación o autorización que impiden completar la solicitud.
* **5xx (Códigos de estado de error del servidor)**: Generalmente indican errores del servidor, como caídas del servidor o tiempos de espera agotados al procesar solicitudes.

| Código de error          | Posibles causas                                                   | Solución                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <h4>400</h4> | Formato incorrecto del cuerpo de la solicitud, etc.                                       | <p>Consulte el contenido del error en la respuesta del diálogo o <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">consola</a> para ver el error y actuar según la indicación.</p><p><mark style="color:purple;">【Caso común 1】</mark>: Para modelos Gemini, puede requerir vinculación de tarjeta;<br><mark style="color:purple;">【Caso común 2】</mark>: Sobrepaso del límite de datos, común en modelos visuales cuando la imagen supera el límite de tamaño por solicitud;<br><mark style="color:purple;">【Caso común 3】</mark>: Parámetros no compatibles o incorrectos. Pruebe crear un nuevo asistente limpio;<br><mark style="color:purple;">【Caso común 4】：</mark> Contexto excede límite, borre contexto o inicie nuevo diálogo o reduzca mensajes contextuales.</p> |
| <h4>401</h4> | Fallo de autenticación: modelo no compatible o cuenta de servidor bloqueada, etc.                 | Contactar o verificar estado de cuenta con el proveedor correspondiente                                                                                                                                                                                                                                                                                                                                                                   |
| <h4>403</h4> | Sin permiso para realizar la operación solicitada                                          | Actuar según el error en la respuesta del diálogo o error en la [consola](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                               |
| <h4>404</h4> | Recurso solicitado no encontrado                                                         | Verificar ruta de solicitud, etc.                                                                                                                                                                                                                                                                                                                                                                                                    |
| <h4>422</h4> | Formato correcto pero error semántico                                                     | El servidor puede analizar pero no procesar. Común en errores semánticos JSON (ej: valor nulo; esperaba cadena pero se proporcionó número/booleano).                                                                                                                                                                                                                                                                                     |
| <h4>429</h4> | Límite de tasa de solicitudes alcanzado                                                    | Tasa de solicitudes (TPM o RPM) alcanzó el límite, espere un momento antes de reintentar                                                                                                                                                                                                                                                                                                                                             |
| <h4>500</h4> | Error interno del servidor, no se puede completar la solicitud                                   | Contactar al proveedor si persiste                                                                                                                                                                                                                                                                                                                                                                                                   |
| <h4>501</h4> | Función solicitada no implementada en el servidor                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>502</h4> | Respuesta inválida recibida por servidor proxy/puerta de enlace                               |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>503</h4> | Servidor temporalmente sobrecargado o en mantenimiento (ver cabecera Retry-After para tiempo de espera) |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <h4>504</h4> | Tiempo de espera agotado en servidor proxy/puerta de enlace                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                      |

***

## Método para ver errores en la consola

* Haga clic en la ventana del cliente Cherry Studio y presione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>)

{% hint style="info" %}
- La ventana activa actual debe ser la del cliente Cherry Studio para abrir la consola;
- Primero abra la consola, luego haga clic en "Probar" o inicie diálogos/acciones para capturar información de solicitudes.
{% endhint %}

* En la consola emergente, haga clic en <mark style="color:blue;">`Network`</mark> → Busque la última entrada marcada con <mark style="color:red;">`×`</mark> en <mark style="color:red;">`completions`</mark>_(errores en diálogos, traducciones, comprobación de conectividad)_ o <mark style="color:red;">`generations`</mark>_(errores en dibujo)_ → Haga clic en <mark style="color:blue;">`Response`</mark> para ver la respuesta completa (área ④ en la imagen).

> Si no puede determinar la causa del error, tome una captura de esta pantalla y envíela al [Grupo oficial de discusión](https://t.me/CherryStudioAI) para obtener ayuda.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método funciona para diálogos, pruebas de modelos, creación de bases de conocimiento, dibujo, etc. Siempre abra primero la consola antes de realizar acciones.

{% hint style="info" %}
El nombre en la columna Name (② arriba) varía según el escenario:

Diálogos/traducciones/comprobación de modelos: <mark style="color:red;">`completions`</mark>&#x20;

Dibujo: <mark style="color:red;">`generations`</mark>

Creación de base de conocimiento: <mark style="color:red;">`embeddings`</mark>&#x20;
{% endhint %}

***

## Fórmulas no renderizadas/errores de renderización

* Cuando las fórmulas muestran código en lugar de renderizarse, verifique los delimitadores:

> **Uso de delimitadores**
>
> _Fórmulas en línea_
>
> * Usar signo de dólar simple: `$fórmula$`
> * O usar `\(` y `\)`: `\(fórmula\)`
>
>
>
> _Bloques de fórmulas independientes_
>
> * Usar doble signo de dólar: `$$fórmula$$`
> * O usar `\[fórmula\]`
> * Ejemplo: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Errores de renderización/glifos incorrectos (común con caracteres chinos): Cambie el motor de renderización a KateX.

***

## No se puede crear base de conocimiento/fallo al obtener dimensión de incrustación

1. Estado del modelo no disponible

> Verifique si el proveedor admite este modelo o si el servicio está operativo.

2. Uso de modelos no compatibles con incrustación

***

## Modelo no reconoce imágenes/no puede cargar o seleccionar imágenes

Primero verifique si el modelo admite reconocimiento visual. Los modelos populares en Cherry Studio muestran un icono de 👁️ junto al nombre si admiten imágenes.

Los modelos visuales permiten cargar imágenes. Si un modelo no está clasificado correctamente, localícelo en la lista de modelos del proveedor, haga clic en el botón ⚙️ junto al nombre y active la opción de imágenes.

Consulte la información específica del modelo con el proveedor. Los modelos sin capacidad visual ignorarán la opción de imágenes aunque esté activada.