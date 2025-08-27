---
icon: seal-question
---
# Preguntas frecuentes


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Códigos de error comunes

* **4xx (Códigos de estado de error del cliente)**: Generalmente indican errores de sintaxis en la solicitud, fallas de autenticación o autorización que impiden completar la solicitud.
* **5xx (Códigos de estado de error del servidor)**: Generalmente indican errores del servidor, como caídas del servidor o tiempos de espera excedidos durante el procesamiento de solicitudes.

| Código | Posibles causas                                                                                 | Solución                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **400** | Formato incorrecto del cuerpo de la solicitud, etc.                                             | <p>Verificar el contenido del error devuelto en la conversación o <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">consultar el método de visualización de errores en consola</a> para ver los detalles del error y actuar según las indicaciones.</p><p><a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa"><mark style="color:purple;">[Caso común 1]</mark>: Para modelos Gemini, podría requerirse asociar una tarjeta de crédito;<br><mark style="color:purple;">[Caso común 2]</mark>: Volumen de datos excedido, común en modelos de visión cuando las imágenes superan el límite de tamaño por solicitud;<br><mark style="color:purple;">[Caso común 3]</mark>: Parámetros no soportados o incorrectos. Probar con un asistente limpio;<br><mark style="color:purple;">[Caso común 4]</mark>: Contexto excedido. Limpiar contexto, comenzar nueva conversación o reducir el número de mensajes.</a></p> |
| **401** | Error de autenticación: modelo no soportado o cuenta de servidor bloqueada, etc.                | Verificar el estado de la cuenta con el proveedor correspondiente                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **403** | Sin permisos para la operación solicitada                                                       | Actuar según la información de error devuelta en la conversación o en la [consola](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                                                                                                             |
| **404** | Recurso solicitado no encontrado                                                                 | Verificar la ruta de solicitud, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **422** | Sintaxis correcta pero error semántico                                                           | Errores que el servidor puede analizar pero no procesar. Comunes en errores semánticos JSON (valores nulos, tipo de dato incorrecto, etc.).                                                                                                                                                                                                                                                                                                                                                                                |
| **429** | Límite de tasa de solicitudes alcanzado                                                          | Tasa de solicitudes (TPM o RPM) excedida. Esperar antes de reintentar                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **500** | Error interno del servidor, no se puede completar la solicitud                                   | Contactar al proveedor si persiste                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **501** | Función solicitada no implementada en el servidor                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **502** | Respuesta inválida recibida de un servidor remoto por parte de un proxy o gateway                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **503** | Servidor temporalmente incapaz de procesar solicitudes (sobrecarga/mantenimiento). Ver cabecera Retry-After |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **504** | Tiempo de espera agotado al obtener solicitudes desde servidor remoto (proxy/gateway)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

***

## Método para ver errores en la consola

* Presionar <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (en Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>) después de hacer clic en la ventana de cliente de Cherry Studio

{% hint style="info" %}
- La ventana activa debe ser la del cliente de Cherry Studio para abrir la consola
- Se debe abrir primero la consola antes de realizar pruebas o iniciar conversaciones para capturar la información de solicitudes
{% endhint %}

* En la consola, ir a <mark style="color:blue;">`Network`</mark> → Buscar la última entrada con <mark style="color:red;">`×`</mark> rojo llamada <mark style="color:red;">`completions`</mark>_(para errores en conversaciones, traducción o verificación de modelos)_ o <mark style="color:red;">`generations`</mark>_(errores en generación de imágenes)_ → Hacer clic en <mark style="color:blue;">`Response`</mark> para ver el contenido completo (área ④ en la imagen)

> Si no puede determinar la causa del error, envíe una captura de esta pantalla al [grupo oficial](https://t.me/CherryStudioAI) para obtener ayuda

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método funciona no solo en conversaciones, sino también al probar modelos, agregar bases de conocimiento o generar imágenes. Siempre se debe abrir primero la consola antes de realizar la acción que se desea inspeccionar.·

{% hint style="info" %}
El nombre en la columna Name (área ②) varía según el escenario:

Conversaciones, traducción, verificación de modelos: <mark style="color:red;">`completions`</mark>

Generación de imágenes: <mark style="color:red;">`generations`</mark>

Creación de base de conocimiento: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Fórmulas no renderizadas/errores de renderización

* Si las fórmulas muestran código en lugar de renderizarse, verificar los delimitadores:

> **Uso de delimitadores**
>
> _Fórmulas en línea_
>
> * Usar un dólar simple: `$formula$`
> * O usar `\(` y `\)`, ej: `\(formula\)`
>
> _Bloques de fórmulas independientes_
>
> * Usar doble dólar: `$$formula$$`
> * O usar `\[formula\]`
> * Ejemplo: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Errores de renderización/caracteres corruptos: comunes con contenido en chino. Intentar cambiar el motor de fórmulas a KateX.

***

## No se puede crear la base de conocimiento/error al obtener dimensiones de incrustación

1. Estado del modelo no disponible

> Confirmar si el proveedor soporta el modelo o verificar su estado de servicio.

2. Se usó un modelo no especializado en incrustaciones

***

## Modelo no reconoce imágenes/error al subir o seleccionar imágenes

Primero verificar si el modelo soporta reconocimiento visual. En modelos populares Cherry Studio los clasifica con un icono de ojo junto al nombre.

Los modelos de reconocimiento visual permiten subir archivos de imagen. Si la funcionalidad no está habilitada, buscar el modelo en la lista del proveedor, hacer clic en el botón de configuración y marcar la opción de imagen.

La información detallada del modelo está disponible con cada proveedor. Como con los modelos de incrustación, habilitar imágenes en modelos sin soporte visual no tendrá efecto.