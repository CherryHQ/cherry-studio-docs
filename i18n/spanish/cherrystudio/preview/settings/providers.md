---
icon: cloud-check
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuración de proveedores

Esta página solo presenta las funcionalidades de la interfaz. Para los tutoriales de configuración, puedes consultar el tutorial [Configuración de proveedores](../../../pre-basic/providers/) en los fundamentos básicos.

{% hint style="info" %}
* Al usar un proveedor incorporado, solo necesitas completar la clave correspondiente.
* Diferentes proveedores pueden usar términos distintos para las claves: clave secreta, Key, API Key, token, todos se refieren al mismo concepto.
{% endhint %}

### Clave secreta de API

En Cherry Studio, un solo proveedor admite múltiples claves en rotación, utilizando un método de bucle secuencial en la lista.

* Agrega múltiples claves separadas por comas en inglés. Ejemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Debe usar comas **en inglés**.
{% endhint %}

### Dirección de API

Normalmente no es necesario completar la dirección de API al usar proveedores incorporados. Si necesitas modificarla, ingrésala exactamente como se indica en la documentación oficial correspondiente.

> Si el proveedor da una dirección con formato <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, solo ingresa la parte raíz (<mark style="background-color:red;">https://xxx.xxx.com</mark>).
>
> Cherry Studio concatenará automáticamente la ruta restante (<mark style="background-color:green;">/v1/chat/completions</mark>). Si no sigue estas instrucciones, podría no funcionar correctamente.

{% hint style="info" %}
Nota: Las rutas de modelos de lenguaje de la mayoría de proveedores están unificadas, por lo que generalmente no necesita esta configuración. Si la ruta API usa v2, v3/chat/completions u otra versión, ingrese manualmente la versión correspondiente terminando en `/`; cuando la ruta sea diferente a la convencional <mark style="background-color:green;">/v1/chat/completions</mark>, use la dirección completa provista terminando con `#`.

Es decir:
* Direcciones API terminando con `/` concatenarán "chat/completions"
* Direcciones API terminando con `#` no concatenarán nada, usando solo la dirección ingresada.

![](<../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)![](<../../../.gitbook/assets/image (15).png>)
{% endhint %}

### Añadir modelos

Generalmente, al hacer clic en el botón `Gestionar` de la esquina inferior izquierda, se obtienen automáticamente todos los modelos soportados. Haz clic en `+` junto a cada modelo para agregarlo a tu lista.

{% hint style="info" %}
Los modelos de la ventana emergente no se agregan automáticamente. Debes hacer clic en `+` junto a cada modelo para que aparezcan en la lista de selección de modelos.
{% endhint %}

### Verificación de conectividad

Haz clic en el botón de verificación junto al campo de clave API para probar si la configuración es exitosa.

{% hint style="info" %}
La verificación usa por defecto el último modelo de chat en la lista. Si falla, verifique si hay modelos incorrectos o no soportados.
{% endhint %}

{% hint style="danger" %}
Tras configurar exitosamente, asegúrate de activar el interruptor superior derecho. De lo contrario, el proveedor permanecerá deshabilitado y sus modelos no aparecerán.
{% endhint %}