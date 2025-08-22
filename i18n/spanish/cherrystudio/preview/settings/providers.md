---
icon: cloud-check
---
# Configuración del servicio de modelos


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta página solo describe las funciones de la interfaz. Para el tutorial de configuración, consulta la guía [Configuración de proveedores](../../../pre-basic/providers/) en los tutoriales básicos.

{% hint style="info" %}
* Al usar proveedores integrados, solo necesitas ingresar la clave correspondiente.
* Diferentes proveedores pueden usar términos distintos para referirse a la clave: clave, Key, API Key o token, todos significan lo mismo.
{% endhint %}

### Clave API

En Cherry Studio, cada proveedor admite el uso rotativo de múltiples claves mediante un sistema de ciclos secuenciales en la lista.

* Para agregar múltiples claves, sepáralas con comas en inglés. Por ejemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Debe usarse **coma** inglesa.
{% endhint %}

### Dirección API

Generalmente no es necesario completar la dirección API al usar proveedores integrados. Si necesitas modificarla, ingresa la dirección exacta especificada en la documentación oficial correspondiente.

> Si el proveedor proporciona una dirección tipo <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, ingresa solo la dirección raíz (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio completará automáticamente el resto de la ruta (<mark style="background-color:green;">/v1/chat/completions</mark>). Un formato incorrecto podría impedir el funcionamiento normal.

{% hint style="info" %}
Nota: La mayoría de los proveedores tienen rutas unificadas para modelos de lenguaje. Si la ruta API del proveedor es v2, v3/chat/completions u otra versión, ingresa manualmente la versión correspondiente terminada con `/` en la barra de direcciones. Cuando la ruta no sea la convencional <mark style="background-color:green;">/v1/chat/completions</mark> usa la dirección completa proporcionada por el proveedor, terminada con `#`.

Es decir:
* Las direcciones API terminadas en `/` solo agregarán "<mark style="background-color:green;">chat/completions</mark>"
* Las direcciones API terminadas con `#` no realizarán concatenación, usando solo la dirección ingresada.

<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Agregar modelos

Generalmente, al hacer clic en el botón `Administrar` en la esquina inferior izquierda de la página de configuración, se obtendrán automáticamente todos los modelos soportados por el proveedor. Desde la lista obtenida, haz clic en `+` para agregarlos a la lista de modelos.

{% hint style="info" %}
Los modelos en la ventana emergente al hacer clic en el botón de gestión no se agregan automáticamente: debes hacer clic en `+` junto a cada modelo para que aparezca en la lista de selección de modelos.
{% endhint %}

### Verificación de conectividad

Haz clic en el botón de verificación junto al campo de entrada de la clave API para probar la configuración.

{% hint style="info" %}
Por defecto, la verificación utiliza el último modelo de diálogo añadido a la lista. Si falla, verifica que no haya modelos incorrectos o no soportados en la lista.
{% endhint %}

{% hint style="danger" %}
Después de una configuración exitosa, activa el interruptor en la esquina superior derecha. De lo contrario, el proveedor permanecerá inactivo y sus modelos no aparecerán en la lista.
{% endhint %}