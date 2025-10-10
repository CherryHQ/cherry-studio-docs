---
icon: seal-question
---
# Preguntas Frecuentes


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Códigos de Error Comunes

* **4xx (Códigos de estado de error del cliente)**: Generalmente indican errores de sintaxis en la solicitud, fallos de autenticación o autorización que impiden completar la petición.
* **5xx (Códigos de estado de error del servidor)**: Generalmente indican errores del servidor, como caídas del sistema o tiempos de espera agotados.

| Código de Error | Posibles Causas                                                                 | Solución                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **400**         | Formato incorrecto del cuerpo de la solicitud, etc.                             | <p>Verifique el contenido del error en la respuesta del diálogo o consulte <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">la consola</a> para ver los detalles del error y siga las indicaciones.</p><p><a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa"><mark style="color:purple;">[Caso común 1]</mark>: Para modelos Gemini, puede requerir vinculación de tarjeta;<br><mark style="color:purple;">[Caso común 2]</mark>: Volumen de datos excedido, común en modelos visuales cuando las imágenes superan el límite de tamaño por solicitud;<br><mark style="color:purple;">[Caso común 3]</mark>: Parámetros no soportados o incorrectos. Pruebe crear un asistente nuevo para verificar;<br><mark style="color:purple;">[Caso común 4]:</mark> Contexto excedido. Limpie el historial, inicie nuevo diálogo o reduzca la cantidad de mensajes contextuales.</a></p> |
| **401**         | Autenticación fallida: modelo no soportado o cuenta del proveedor suspendida, etc. | Contacte al proveedor o verifique el estado de la cuenta                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **403**         | Sin permisos para la operación solicitada                                       | Siga las indicaciones del error en la respuesta del diálogo o en los [errores de la consola](questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa)                                                                                                                                                                                                                                                                                                                                                              |
| **404**         | Recurso solicitado no encontrado                                                | Verifique la ruta de la solicitud, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **422**         | Sintaxis correcta pero error semántico                                          | El servidor puede analizar pero no procesar la solicitud. Común en errores semánticos JSON (ej: valores nulos; se esperaba texto pero se ingresó número/booleano).                                                                                                                                                                                                                                                                                                                                          |
| **429**         | Límite de tasa de solicitudes alcanzado                                         | Tasa de solicitudes (TPM o RPM) excedida. Espere un momento antes de reintentar                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **500**         | Error interno del servidor, no se pudo completar la solicitud                   | Contacte al proveedor si el error persiste                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **501**         | Función no implementada en el servidor                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **502**         | Respuesta inválida recibida desde servidor remoto al actuar como puerta de enlace |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **503**         | Servidor sobrecargado o en mantenimiento (el retraso puede indicarse en Retry-After) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **504**         | Tiempo de espera agotado al obtener respuesta desde servidor remoto             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

***

## Método para Ver Errores en la Consola

* Presione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>) con la ventana de Cherry Studio activa.

{% hint style="info" %}
- La ventana activa debe ser el cliente de Cherry Studio para abrir la consola;
- Debe abrirse la consola antes de iniciar pruebas o diálogos para capturar la información.
{% endhint %}

* En la consola, haga clic en <mark style="color:blue;">`Network`</mark> → Seleccione la última solicitud marcada con <mark style="color:red;">`×`</mark> llamada <mark style="color:red;">`completions`</mark>_ (errores en diálogos/traducciones) _ o <mark style="color:red;">`generations`</mark>_ (errores en generación de imágenes) _ → Haga clic en <mark style="color:blue;">`Response`</mark> para ver el contenido completo (área ④ en la imagen).

> Si no puede determinar la causa del error, envíe una captura de pantalla de esta interfaz al [grupo oficial](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método funciona para diálogos, pruebas de modelos, creación de bases de conocimiento y generación de imágenes. Siempre abra la consola antes de realizar la solicitud.

{% hint style="info" %}
Los nombres en la columna Name (② arriba) varían según el escenario:

Diálogos/Traducciones/Pruebas: <mark style="color:red;">`completions`</mark>

Generación de imágenes: <mark style="color:red;">`generations`</mark>

Creación de base de conocimiento: <mark style="color:red;">`embeddings`</mark>
{% endhint %}

***

## Fórmulas no Renderizadas/Errores de Renderizado

* Si se muestra código en lugar de fórmulas, verifique los delimitadores:

> **Uso de delimitadores**
>
> _Fórmulas en línea_
>
> * Un símbolo de dólar: `$fórmula$`
> * O `\(` y `\)`: `\(fórmula\)`
>
> _Bloques de fórmulas_
>
> * Doble símbolo de dólar: `$$fórmula$$`
> * O `\[fórmula\]`
> * Ejemplo: `$$\sum_{i=1}^n x_i$$`\
>   $$\sum_{i=1}^n x_i$$

* Errores de renderizado/caracteres incorrectos: comunes con texto en chino. Cambie el motor de renderizado a KateX.

***

## Error al Crear Base de Conocimiento/Fallo al Obtener Dimensión de Embedding

1. Modelo no disponible

> Verifique si el proveedor soporta el modelo o su estado operativo.

2. Uso de modelo no apto para embeddings

***

## Modelo no Reconoce Imágenes/Error al Subir o Seleccionar Imágenes

Primero confirme si el modelo soporta visión. Cherry Studio identifica modelos con visión con un icono de ojo junto al nombre.

Los modelos con visión permiten subir imágenes. Si la funcionalidad no está habilitada, busque el modelo en el proveedor, haga clic en  ⚙ y active la opción de imágenes.

Consulte la información del modelo en el proveedor. Modelos sin capacidad visual no funcionarán aunque se active la opción.