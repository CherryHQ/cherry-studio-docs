---
icon: cloud-check
---
# Configuración del servicio de modelos


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta página solo describe las funciones de la interfaz. Para ver los tutoriales de configuración, puede consultar la guía [Configuración de proveedores](../../../pre-basic/providers/) en los tutoriales básicos.

{% hint style="info" %}
* Al usar proveedores integrados, solo necesita completar la clave correspondiente.
* Diferentes proveedores pueden usar términos distintos para la clave: clave secreta, Key, API Key, token, etc., todos se refieren al mismo concepto.
{% endhint %}

### Clave API

En Cherry Studio, un mismo proveedor admite múltiples claves para uso rotativo. La rotación sigue un ciclo secuencial de lista (de adelante hacia atrás).

* Agregue múltiples claves separadas por comas en inglés. Ejemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Debe usar comas en **inglés**.
{% endhint %}

### Dirección API

Generalmente no es necesario completar la dirección API cuando se usan proveedores integrados. Si necesita modificarla, ingrese la dirección exacta proporcionada en la documentación oficial correspondiente.

> Si el proveedor da una dirección como <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, solo debe ingresar la dirección base (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio completará automáticamente la ruta restante (<mark style="background-color:green;">/v1/chat/completions</mark>). Si no se sigue este formato, podría causar errores.

{% hint style="info" %}
Nota: La mayoría de los proveedores usan rutas unificadas para modelos grandes de lenguaje, por lo que generalmente no se requiere configuración adicional. Si el proveedor usa rutas API como v2, v3/chat/completions u otras versiones, ingrese manualmente la versión correspondiente terminando con "`/`". Cuando la ruta del proveedor no sea la convencional <mark style="background-color:green;">/v1/chat/completions</mark>, use la dirección completa proporcionada por el proveedor y termine con `#`.

Es decir:
* Las direcciones API terminadas en `/` solo agregarán "<mark style="background-color:green;">chat/completions</mark>"
* Las direcciones API terminadas en `#` no agregarán rutas, usando solo la dirección ingresada.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Agregar modelos

Normalmente, al hacer clic en el botón `Administrar` en la esquina inferior izquierda de la página de configuración del proveedor, se obtendrán automáticamente todos los modelos compatibles. Desde la lista obtenida, haga clic en `+` para agregarlos a la lista de modelos.

{% hint style="info" %}
Al hacer clic en el botón Administrar, no se agregarán todos los modelos de la ventana emergente. Debe hacer clic en `+` junto al modelo para agregarlo a la lista de modelos en la página de configuración del proveedor, y así aparecerá en la lista de selección de modelos.
{% endhint %}

### Verificación de conexión

Haga clic en el botón de verificación junto al campo de entrada de la Clave API para probar si la configuración es exitosa.

{% hint style="info" %}
La verificación del modelo usa por defecto el último modelo de conversación agregado a la lista. Si hay errores durante la verificación, compruebe si hay modelos incorrectos o no compatibles en la lista.
{% endhint %}

{% hint style="danger" %}
Después de configurar correctamente, asegúrese de activar el interruptor en la esquina superior derecha. De lo contrario, el proveedor permanecerá deshabilitado y sus modelos no aparecerán en la lista de selección.
{% endhint %}