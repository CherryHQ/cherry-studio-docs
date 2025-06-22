---
icon: seal-question
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Preguntas frecuentes

## Códigos de error comunes

* **4xx (códigos de estado de error del cliente)**: Generalmente son solicitudes imposibles de completar debido a errores de sintaxis, fallos de autenticación o autorización.
* **5xx (códigos de estado de error del servidor)**: Generalmente son errores del servidor, como caídas del sistema o tiempos de espera excedidos.

| Código de error | Posibles escenarios | Solución |
|----------------|---------------------|----------|
| <h4>400</h4> | Cuerpo de solicitud con formato incorrecto | <p>Consulte el contenido del error devuelto por el diálogo o revise la información en la <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">consola</a>, y actúe según las indicaciones.</p><p><mark style="color:purple;">【Escenario común 1】</mark>: Para modelos Gemini, puede ser necesario vincular una tarjeta de crédito;<br><mark style="color:purple;">【Escenario común 2】</mark>: Volumen de datos excedido, común en modelos de visión cuando las imágenes superan el límite de tráfico por solicitud;<br><mark style="color:purple;">【Escenario común 3】</mark>: Parámetros no compatibles o mal configurados. Intente crear un nuevo asistente limpio para verificar;<br><mark style="color:purple;">【Escenario común 4】</mark>: Contexto excede el límite, borre el contexto, inicie un nuevo diálogo o reduzca el número de mensajes contextuales.</p> |
| <h4>401</h4> | Error de autenticación: modelo no compatible o cuenta suspendida | Contacte al proveedor de servicios o verifique el estado de la cuenta |
| <h4>403</h4> | Sin permisos para realizar la operación | Siga las indicaciones del mensaje de error o consulte errores en la <a href="questions.md#kong-zhi-tai-bao-cuo-cha-kan-fang-fa">consola</a> |
| <h4>404</h4> | Recurso solicitado no encontrado | Verifique la ruta de solicitud |
| <h4>422</h4> | Formato correcto pero error semántico | Errores comunes en valores JSON (ej: valor nulo; se esperaba texto pero se ingresó número/booleano) |
| <h4>429</h4> | Límite de solicitudes alcanzado | Tasa de solicitudes (TPM/RPM) excedida, espere antes de reintentar |
| <h4>500</h4> | Error interno del servidor | Contacte al proveedor si persiste |
| <h4>501</h4> | Función no implementada por el servidor |  |
| <h4>502</h4> | Respuesta inválida desde servidor remoto al actuar como proxy |  |
| <h4>503</h4> | Servicio no disponible temporalmente por sobrecarga o mantenimiento | El tiempo de espera puede especificarse en la cabecera Retry-After |
| <h4>504</h4> | Tiempo de espera excedido al obtener respuesta desde servidor remoto |  |

***

## Método para ver errores en consola

* Presione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> (Mac: <kbd>Command</kbd> + <kbd>Option</kbd> + <kbd>I</kbd>) con Cherry Studio activo

{% hint style="info" %}
- La ventana activa debe ser el cliente de Cherry Studio para abrir la consola;
- Debe abrirse la consola antes de iniciar pruebas/diálogos para capturar la información.
{% endhint %}

* En la consola: Click en <mark style="color:blue;">`Network`</mark> → Seleccione el último <mark style="color:red;">`completions`</mark> (errores en diálogos/traducciones) o <mark style="color:red;">`generations`</mark> (errores en imágenes) marcado con × rojo → Ver contenido completo en <mark style="color:blue;">`Response`</mark>.

> Si no puede determinar la causa, capture esta pantalla y envíela al [grupo oficial](https://t.me/CherryStudioAI).

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Este método funciona también en pruebas de modelos, creación de bases de conocimiento, generación de imágenes, etc. Siempre debe abrirse la consola primero.

{% hint style="info" %}
Nombres comunes en diferentes escenarios:

Diálogos/Traducciones/Pruebas: <mark style="color:red;">`completions`</mark>  
Generación de imágenes: <mark style="color:red;">`generations`</mark>  
Creación de bases de conocimiento: <mark style="color:red;">`embeddings`</mark>  
{% endhint %}

***

## Fórmulas no renderizadas/errores en fórmulas

* Si se muestra código sin renderizar, verifique los delimitadores:

> **Uso de delimitadores**  
> _Fórmulas en línea_  
> - Un signo de dólar: `$formula$`  
> - O `\(formula\)`  
>   
> _Bloques de fórmulas_  
> - Doble signo de dólar: `$$formula$$`  
> - O `\[formula\]`  
> - Ejemplo: `$$\sum_{i=1}^n x_i$$`  
> $$\sum_{i=1}^n x_i$$

* Errores/desorden al contener chino: Cambie el motor de renderizado a KaTeX.

***

## No se puede crear base de conocimiento/error dimensiones embedding

1. Modelo no disponible  
> Verifique compatibilidad y estado con el proveedor.
   
2. Uso de modelo no embedding

***

## Modelo no reconoce imágenes/no permite subir imágenes

Primero verifique si el modelo admite reconocimiento visual: Los modelos compatibles tienen ícono de ojo 🔍 junto al nombre.  

Si la función no está habilitada:
- En la lista de modelos del proveedor, haga clic en ⚙️ junto al modelo  
- Marque la opción "Imagen"  

Los modelos sin capacidad visual no procesarán imágenes aunque esté marcada la opción. Consulte información técnica específica del modelo con su proveedor.