---
icon: cloud-check
---
# Configuración de Servicio de Modelo


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta página solo presenta las funciones de la interfaz. Para guías de configuración completa, consulta el tutorial de [Configuración de Proveedores](../../../pre-basic/providers/) en los Fundamentos Básicos.

{% hint style="info" %}
* Usando proveedores nativos: solo requiere completar las claves correspondientes.
* Puede haber variaciones en el nombre de la clave entre proveedores: clave, key, API key o token, todas se refieren al mismo concepto.
{% endhint %}

### Clave API

En Cherry Studio, un proveedor individual soporta rotación de múltiples claves, siguiendo un ciclo secuencial de la lista.

* Se agregan múltiples claves separadas por comas en inglés. Ejemplo:

<pre><code><strong>sk-xxxx1,sk-xxxx2,sk-xxxx3,sk-xxxx4
</strong></code></pre>

{% hint style="warning" %}
Debes utilizar **comas en inglés** exclusivamente.
{% endhint %}

### Dirección API

Normalmente no es necesario completar la dirección API con proveedores nativos. Si requieres modificarla, ingresa el valor exacto según la documentación oficial.

> Si el proveedor indica una dirección como <mark style="background-color:red;">https://xxx.xxx.com</mark><mark style="background-color:green;">/v1/chat/completions</mark>, solo debes ingresar la raíz (<mark style="background-color:red;">https://xxx.xxx.com</mark>).  
> Cherry Studio concatenará automáticamente la ruta restante (<mark style="background-color:green;">/v1/chat/completions</mark>). Un formato incorrecto podría generar fallos.

{% hint style="info" %}
Nota: Los modelos de lenguaje principales usan rutas estandarizadas. Solo si el proveedor usa versiones no estándar (ej: v2, v3/chat/completions) debes:
* Ingresar `/` al final de la versión para que el sistema concatene "chat/completions"
* Usar `#` al final al ingresar rutas completas no convencionales para desactivar concatenación.

Ejemplos:  
<img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (15).png" alt="" data-size="original">
{% endhint %}

### Añadir modelos

Haz clic en `Gestionar` (esquina inferior izquierda) para obtener automáticamente todos los modelos soportados. Agrega los seleccionados con el botón `+`.

{% hint style="info" %}
Al hacer clic en Gestionar, los modelos no se añaden automáticamente. Debes seleccionar individualmente usando `+` para que aparezcan en la lista configurada.
{% endhint %}

### Verificación de conectividad

Haz clic en el botón de verificación junto a la clave API para probar la configuración.

{% hint style="info" %}
La prueba usa el último modelo conversacional añadido en la lista. Si falla, verifica posibles modelos erróneos o no soportados.
{% endhint %}

{% hint style="danger" %}
💡 ¡Activa el interruptor superior derecho después de configurar! De lo contrario, el proveedor permanecerá deshabilitado y sus modelos serán invisibles.
{% endhint %}