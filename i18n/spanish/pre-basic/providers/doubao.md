
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

```markdown
# ByteDance (Doubao)

*   Iniciar sesión en [Volcano Engine](https://console.volcengine.com/)
*   Hacer clic directamente [aquí para acceso directo](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D)

<figure><img src="../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

### Obtener API Key

*   Hacer clic en [Administración de claves API](https://console.volcengine.com/ark/region:ark+cn-beijing/apiKey) en la barra lateral inferior
*   Crear una clave API

<figure><img src="../../.gitbook/assets/image (6) (2).png" alt=""><figcaption></figcaption></figure>

*   Después de crear con éxito, hacer clic en el icono de ojo 🔍 junto a la clave API creada para revelar y copiar

<figure><img src="../../.gitbook/assets/image (7) (2).png" alt=""><figcaption></figcaption></figure>

*   Pegar la clave API copiada en Cherry Studio y luego activar el interruptor del proveedor.

<figure><img src="../../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

### Activar y agregar modelos

*   Activar los modelos necesarios en [Gestión de activación](https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D\&OpenTokenDrawer=false) (parte inferior de la barra lateral de la consola Ark). Aquí puede activar la serie Doubao y modelos como DeepSeek según sea necesario.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

*   En el [documento de lista de modelos](https://www.volcengine.com/docs/82379/1330310#%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90), localizar el ID del modelo correspondiente al modelo requerido.

<figure><img src="../../.gitbook/assets/火山引擎_模型ID.png" alt="Ejemplo de lista de IDs de modelos de Volcano Engine"><figcaption></figcaption></figure>

*   Abrir la configuración de [Servicios de modelos](../../cherrystudio/preview/settings/providers.md) en Cherry Studio y buscar Volcano Engine
*   Hacer clic en Agregar, luego pegar el ID del modelo obtenido en el cuadro de texto ID del modelo

<figure><img src="../../.gitbook/assets/volc_ark_01.png" alt=""><figcaption></figcaption></figure>

*   Agregar modelos uno por uno siguiendo este flujo

### Dirección API

Existen dos formatos para la dirección API:

*   Primer formato (predeterminado en el cliente): `https://ark.cn-beijing.volces.com/api/v3/`
*   Segundo formato: `https://ark.cn-beijing.volces.com/api/v3/chat/completions#`

{% hint style="info" %}
No hay diferencia entre ambos formatos. Mantenga el valor predeterminado sin modificaciones.

Para diferencias entre terminaciones `/` y `#`, consulte la sección de dirección API en la configuración de proveedores del documento: [Ir a sección](../../cherrystudio/preview/settings/providers.md#api-di-zhi)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt=""><figcaption><p>Ejemplo de cURL en documentación oficial</p></figcaption></figure>
```