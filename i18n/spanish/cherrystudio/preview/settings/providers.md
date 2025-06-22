---
icon: cloud-check
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuración de Proveedores

Esta página solo proporciona una introducción a las funciones de la interfaz. Para el tutorial de configuración, consulte el tutorial de [Configuración de Proveedores](../../../pre-basic/providers/) en los Fundamentos Básicos.

{% hint style="info" %}
* Al utilizar proveedores integrados, solo necesita completar la clave correspondiente.
* La denominación de la clave puede variar según el proveedor; clave, Key, API Key, token, etc., se refieren a lo mismo.
{% endhint %}

### Clave de API

En Cherry Studio, un solo proveedor admite el uso de varias claves en modo de rotación, que se realiza en ciclo secuencial de lista.

* Agregue varias claves separadas por comas en inglés, por ejemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Debe utilizar comas **en inglés**.
{% endhint %}

### Dirección de API

Al utilizar proveedores integrados, generalmente no es necesario completar la dirección de API. Si necesita modificarla, complétela estrictamente según la dirección proporcionada en la documentación oficial correspondiente.

> Si el proveedor proporciona una dirección como <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, solo complete la parte raíz (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
> 
> Cherry Studio agregará automáticamente la ruta restante (<mark style="background-color:green;">/v1/chat/completions</mark>). Si no se completa según lo requerido, podría funcionar incorrectamente.

{% hint style="info" %}
Nota: La mayoría de los proveedores tienen rutas unificadas para modelos de lenguaje grande. Generalmente no se requiere la siguiente configuración. Si la ruta de la API es v2, v3/chat/completions u otra versión, ingrese manualmente la versión terminada en `/` en el campo de dirección. Cuando la ruta no sea <mark style="background-color:green;">/v1/chat/completions</mark>, use la dirección completa proporcionada por el proveedor y termine con `#`.

Es decir:
* Direcciones de API que terminan con `/`: solo agregan "chat/completions"
* Direcciones de API que terminan con `#`: no agregan ruta, usan solo la dirección ingresada.

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Añadir Modelos

Generalmente, al hacer clic en el botón `Administrar` en la esquina inferior izquierda de la página de configuración del proveedor, se obtendrán automáticamente todos los modelos compatibles. Luego haga clic en `+` en la lista para agregarlos a los modelos disponibles.

{% hint style="info" %}
Al hacer clic en Administrar, no se agregan todos los modelos del cuadro emergente. Debe hacer clic en `+` junto a cada modelo para que aparezcan en la lista de selección de modelos.
{% endhint %}

### Verificación de Conectividad

Haga clic en el botón de verificación junto al campo Clave de API para probar la configuración.

{% hint style="info" %}
La verificación usa por defecto el último modelo conversacional agregado. Si falla, verifique si hay modelos incorrectos o no compatibles en la lista.
{% endhint %}

{% hint style="danger" %}
Después de configurar correctamente, active el interruptor superior derecho. De lo contrario, el proveedor permanecerá deshabilitado y sus modelos no estarán disponibles.
{% endhint %}