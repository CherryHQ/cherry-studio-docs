
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# ByteDance (Doubao)

* Inicia sesión en [Volcano Engine](https://console.volcengine.com/)
* Acceso directo haciendo clic [aquí](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Obtener clave de API

* Haz clic en [Gestión de claves API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) en la barra lateral inferior
* Crea una clave API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

* Tras crearla, haz clic en el icono de ojo 🔍 junto a la clave API y copia el valor

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

* Introduce la clave API copiada en CherryStudio y activa el interruptor del proveedor.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Activar y agregar modelos

* En la consola de Ark, activa los modelos necesarios en [Gestión de activaciones](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false). Puedes activar modelos de la serie Doubao o DeepSeek según tus necesidades.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

* En el [documento de lista de modelos](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), localiza el ID de modelo correspondiente.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Ejemplo de lista de ID de modelos de Volcano Engine"><figcaption></figcaption></figure>

* En la configuración de [Servicios de modelos](../../cherrystudio/preview/settings/providers.md) de Cherry Studio, busca Volcano Engine
* Haz clic en "Agregar" y pega el ID del modelo en el cuadro de texto

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

* Repite este proceso para agregar modelos adicionales

### Dirección API

Existen dos formatos válidos:

* Formato predeterminado del cliente: `https://ark.cn-beijing.volces.com/api/v3/`
* Formato alternativo: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
Ambos formatos son funcionalmente equivalentes. Se recomienda mantener el valor predeterminado sin modificaciones.

Para diferencias entre terminaciones `/` y `#`, consulta la sección de direcciones API en [Configuración de proveedores](../../cherrystudio/preview/settings/providers.md#api-di-zhi).
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Ejemplo de cURL en documentación oficial</p></figcaption></figure>