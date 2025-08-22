---
icon: message
---
# Interfaz de Conversación


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Asistentes y Temas

### Asistentes

Un `asistente` es una configuración personalizada del modelo seleccionado, como presets de prompt y parámetros. Estos ajustes ayudan a que el modelo funcione según tus expectativas de trabajo.

El `asistente predeterminado del sistema` tiene parámetros genéricos (sin prompt). Puedes usarlo directamente o buscar presets en la [página de agentes](agents.md).

### Temas

El `asistente` es el contenedor padre de los `temas`. Un mismo asistente puede crear múltiples temas (conversaciones), compartiendo configuraciones como parámetros y prompts.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botones del Panel de Diálogo

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nuevo tema`: Crea una nueva conversación dentro del asistente actual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Subir imagen/documento`: Las imágenes requieren soporte del modelo. Los documentos se analizan como texto contextual.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Búsqueda web`: Requiere configuración previa. Los resultados se usan como contexto (ver [Modo online](../../websearch/)).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de conocimiento`: Activa la integración con KB (ver [Guía KB](../../knowledge-base/knowledge-base.md)).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP`: Activa funciones de servidor MCP (ver [Guía MCP](../../advanced-basic/mcp/)).

![](../../.gitbook/assets/对话界面/生成图片.png) `Generar imagen`: Oculto por defecto. Requiere activación manual para modelos compatibles (ej: Gemini).

{% hint style="info" %}
Actualmente se requiere activación manual. Este botón se eliminará en futuras optimizaciones.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Seleccionar modelo`: Cambia el modelo para conversaciones futuras manteniendo contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases rápidas`: Usa frases preconfiguradas con soporte para variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Limpiar mensajes`: Elimina todo el contenido del tema actual.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir`: Amplía el área de entrada para textos largos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpiar contexto`: Trunca el contexto visible al modelo sin borrar contenido.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimación de Tokens`: Muestra: `Contexto actual` / `Máximo contexto` (∞ = ilimitado) / `Caracteres de entrada` / `Tokens estimados`.

{% hint style="info" %}
Estimación referencial. El conteo real varía por modelo. Consulta a tu proveedor.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traducir`: Traduce el contenido del cuadro de entrada a inglés.

## Configuración de Conversación

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configuración de Modelos

Sincronizado con `Configuración de modelos` del asistente (ver [Editar asistente](chat.md#bian-ji-zhu-shou)).

{% hint style="info" %}
Solo esta configuración aplica al asistente actual. Otras son globales (ej: estilo de burbujas aplica a todos los asistentes).
{% endhint %}

### Configuración de Mensajes

#### <mark style="color:blue;">**`Línea divisoria de mensajes`**</mark>:

Separa contenido de mensajes y barra de acciones.

{% tabs %}
{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar fuente serif`**</mark>:

Cambia estilo tipográfico. Personalizable vía [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Mostrar números de línea en código`**</mark>:

Muestra números de línea en bloques de código.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Bloques de código plegables`**</mark>:

Plegado automático para bloques de código largos.

#### <mark style="color:blue;">**`Ajuste de línea en código`**</mark>:

Ajuste automático de líneas largas que excedan el ancho.

#### <mark style="color:blue;">**`Plegar automáticamente procesos de pensamiento`**</mark>:

Plegado automático tras completar procesos de razonamiento.

#### <mark style="color:blue;">**`Estilo de mensajes`**</mark>:

Alterna entre estilo burbuja o lista.

#### <mark style="color:blue;">**`Estilo de código`**</mark>:

Personaliza visualización de fragmentos de código.

#### <mark style="color:blue;">**`Motor de fórmulas matemáticas`**</mark>:

* **KaTeX**: Renderizado más rápido (optimizado para rendimiento).
* **MathJax**: Más completo (soporte avanzado), pero más lento.

#### <mark style="color:blue;">**`Tamaño de fuente de mensajes`**</mark>:

Ajusta tamaño de texto en interfaz de conversación.

### Configuración de Entrada

#### <mark style="color:blue;">**`Mostrar tokens estimados`**</mark>:

Muestra estimación de tokens para texto de entrada (referencial).

#### <mark style="color:blue;">**`Pegar texto largo como archivo`**</mark>:

Convierte textos largos pegados en "archivos" para reducir interferencia visual.

#### <mark style="color:blue;">**`Renderizar Markdown en mensajes enviados`**</mark>:

Controla renderizado Markdown en mensajes de usuario.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traducir con triple espacio`**</mark>:

Traduce contenido al pulsar espacio tres veces consecutivas.

{% hint style="warning" %}
¡Atención! Sobrescribe el texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma objetivo`**</mark>:

Define idioma para traducción por botón/triple espacio.

## Configuración de Asistentes

Selecciona nombre del asistente → Menú contextual → Configuración

### Editar Asistente

{% hint style="info" %}
Los cambios aplican a todos los temas bajo este asistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configuración de Prompt

#### <mark style="color:blue;">**`Nombre`**</mark>:

Nombre personalizable para identificación.

#### <mark style="color:blue;">**`Prompt`**</mark>:

Personalización avanzada. Consulta ejemplos en página de agentes.

#### Configuración de Modelos

#### <mark style="color:blue;">**`Modelo predeterminado`**</mark>:

Modelo inicial para nuevos temas. Si está vacío, usa el [modelo global predeterminado](settings/default-models.md#mo-ren-zhu-shou-mo-xing).

{% hint style="info" %}
Prioridad: **Modelo del asistente** > **Modelo global predeterminado**.
{% endhint %}

#### <mark style="color:blue;">**`Reinicio automático de modelo`**</mark>:

Si está activado: Al crear nuevo tema tras cambiar de modelo, se usa el modelo predeterminado del asistente.  
Si está desactivado: Los nuevos temas heredan el último modelo usado.

> **Ejemplo**: Asistente predeterminado: `gpt-3.5-turbo`.  
> - En Tema 1 cambias a `gpt-4o`.  
> - **Con reinicio automático**: Tema 2 usa `gpt-3.5-turbo`.  
> - **Sin reinicio automático**: Tema 2 usa `gpt-4o`.

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark>:

Controla aleatoriedad en respuestas (valor predeterminado: 0.7):

* **Baja (0-0.3)**:  
  - Salidas predecibles y precisas  
  - Ideal para código o datos  
* **Media (0.4-0.7)**:  
  - Equilibrio creatividad/coherencia  
  - Recomendado para chats (≈0.5)  
* **Alta (0.8-1.0)**:  
  - Máxima creatividad  
  - Para ideas/redacción creativa  

#### <mark style="color:blue;">**`Top P (Muestreo nuclear)`**</mark>:

Predeterminado: 1. Valores bajos → vocabulario limitado/coherente. Valores altos → diversidad léxica.

* **Bajo (0.1-0.3)**:  
  - Selecciona palabras de alta probabilidad  
  - Para documentación técnica  
* **Medio (0.4-0.6)**:  
  - Balance general  
* **Alto (0.7-1.0)**:  
  - Diversidad expresiva  

#### <mark style="color:blue;">**`Ventana de Contexto`**</mark>

Cantidad de mensajes retenidos:

* **5-10**: Conversaciones estándar  
* **>10**: Tareas complejas con memoria extendida  
* ¡Atención! Más mensajes = más tokens  

#### <mark style="color:blue;">**`Limitar longitud de mensaje (MaxToken)`**</mark>

Límite de tokens por respuesta. Varía por modelo (consultar documentación).

> **Uso típico**: Pruebas de conexión (`MaxToken=1`).

**Recomendaciones**:
{% hint style="success" %}
* Chat: 500-800  
* Texto corto: 800-2000  
* Generación de código: 2000-3600  
* Texto largo: 4000+ (requiere soporte del modelo)  
{% endhint %}

{% hint style="warning" %}
Respuestas pueden truncarse si exceden MaxToken. Ajustar según necesidades.
{% endhint %}

#### <mark style="color:blue;">**`Salida en flujo (Stream)`**</mark>

Transmite respuestas progresivamente ("efecto máquina de escribir").  
- **Activado**: Entrega incremental por tokens.  
- **Desactivado**: Entrega completa al finalizar.  

{% hint style="info" %}
Desactivar para modelos incompatibles (ej: o1-mini inicial).
{% endhint %}

#### <mark style="color:blue;">**`Parámetros personalizados`**</mark>

Añade parámetros avanzados al cuerpo de la solicitud (ej: `presence_penalty`).  
Formato: `nombre - tipo - valor` (ver [documentación](https://openai.apifox.cn/doc-3222739)).

{% hint style="info" %}
1. Parámetros personalizados anulan parámetros nativos si coinciden.  
> Ejemplo: Definir `model:gpt-4o` fuerza este modelo siempre.  

2. Usar `<kbd>nombre:undefined</kbd>` elimina parámetros.  
{% endhint %}