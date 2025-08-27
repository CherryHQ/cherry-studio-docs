---
icon: message
---
# Interfaz de Conversación


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Asistentes y Temas de Conversación

### Asistente

Un `asistente` es una configuración personalizada del modelo seleccionado, que incluye ajustes como preajustes de indicaciones (prompts) y parámetros. Estas configuraciones permiten adaptar el modelo para que funcione según tus expectativas.

El `asistente predeterminado del sistema` tiene parámetros genéricos (sin prompt) que puedes usar directamente, o puedes buscar configuraciones predefinidas en la página de [agentes](agents.md).

### Tema

El `asistente` es el conjunto principal que contiene múltiples `temas` (conversaciones). Todos los `temas` comparten la misma configuración del modelo y prompt del asistente principal.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botones en el cuadro de diálogo

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nuevo tema` Crea un nuevo tema de conversación dentro del asistente actual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Subir imagen/documento` Sube imágenes (requiere soporte del modelo) o documentos que se analizarán automáticamente como contexto.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Buscar en la web` Configura las búsquedas web en ajustes. Los resultados se usan como contexto. Ver más en [modo online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de Conocimiento` Activa la base de conocimiento. Tutorial en [base de conocimiento](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP` Activa la función MCP. Tutorial en [Uso de MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Generar imagen` Oculto por defecto. Para modelos compatibles como Gemini, es necesario activar esta función manualmente.

{% hint style="info" %}
Debido a limitaciones técnicas, debes activar manualmente este botón para generar imágenes. Se eliminará tras futuras mejoras.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Seleccionar modelo` Cambia el modelo manteniendo el contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases rápidas` Usa frases predefinidas en ajustes, admite variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Borrar mensajes` Elimina todo el contenido del tema actual.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir` Amplía el cuadro de diálogo para textos largos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpiar contexto` Trunca el contexto visible para el modelo (el modelo "olvida" mensajes anteriores).

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Tokens estimados` Muestra: `contexto actual` / `máximo contexto` (∞ = ilimitado), `palabras actuales`, `tokens estimados`.

{% hint style="info" %}
Solo es una estimación. Los tokens reales varían según el modelo. Consulta los datos del proveedor.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traducir` Traduce al inglés el contenido del cuadro de entrada.

## Configuración de conversación

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configuración del modelo

Sincronizado con la configuración del asistente. Ver [Editar asistente](chat.md#editar-asistente).

{% hint style="info" %}
Solo los ajustes de modelo afectan al asistente actual. Otras configuraciones son globales.
{% endhint %}

### Configuración de mensajes

#### <mark style="color:blue;">**`Línea divisoria de mensajes`**</mark>:

Separa el contenido de los mensajes de la barra de acciones.

{% tabs %}
{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar fuente serif`**</mark>：

Cambia el estilo de fuente. También puedes cambiarla mediante [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Mostrar números de línea en código`**</mark>：

Muestra números de línea en bloques de código generados por el modelo.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Bloques de código plegables`**</mark>：

Plegar automáticamente bloques de código largos.

#### <mark style="color:blue;">**`Ajuste de línea en bloques de código`**</mark>：

Ajusta líneas largas que excedan el ancho de la ventana.

#### <mark style="color:blue;">**`Plegar automáticamente contenido reflexivo`**</mark>：

Plegar automáticamente el proceso de razonamiento de los modelos que lo soportan.

#### <mark style="color:blue;">**`Estilo de mensajes`**</mark>：

Cambia entre estilo burbuja o lista.

#### <mark style="color:blue;">**`Estilo de código`**</mark>：

Cambia la apariencia de los fragmentos de código.

#### <mark style="color:blue;">**`Motor de fórmulas matemáticas`**</mark>：

* KaTeX: Renderiza más rápido (optimizado).
* MathJax: Más compatible pero lento.

#### <mark style="color:blue;">**`Tamaño de fuente en mensajes`**</mark>：

Ajusta el tamaño de fuente en la interfaz.

### Configuración de entrada

#### <mark style="color:blue;">**`Mostrar tokens estimados`**</mark>：

Muestra tokens estimados para el texto de entrada (referencia únicamente).

#### <mark style="color:blue;">**`Pegar textos largos como archivos`**</mark>：

Convierte textos largos pegados en formato de archivo para reducir interferencias.

#### <mark style="color:blue;">**`Renderizar Markdown en mensajes de entrada`**</mark>：

Solo renderiza Markdown en respuestas del modelo si está desactivado.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traducir con triple espacio rápido`**</mark>：

Presionar espacio tres veces traduce el mensaje a inglés.

{% hint style="warning" %}
Sobrescribe el texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma de destino`**</mark>：

Configura el idioma de traducción para el botón y la tecla triple espacio.

## Configuración del asistente

Selecciona el <mark style="background-color:yellow;">nombre del asistente</mark> → <mark style="background-color:yellow;">menú contextual</mark> → ajustes correspondientes.

### Editar asistente

{% hint style="info" %}
Afecta a todos temas bajo este asistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configuración de prompt

#### <mark style="color:blue;">**`Nombre`**</mark>：

Nombre personalizable para identificar el asistente.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Ver ejemplos en la página de agentes.

#### Configuración del modelo

#### <mark style="color:blue;">**`Modelo predeterminado`**</mark>：

Define un modelo fijo para este asistente. Si no se establece, se usará el modelo predeterminado global.

{% hint style="info" %}
Prioridad: modelo del asistente > modelo predeterminado global.
{% endhint %}

#### <mark style="color:blue;">**`Restablecer modelo automáticamente`**</mark>：

Si está activado: al crear un nuevo tema, se usará el modelo predeterminado del asistente, ignorando el último modelo usado.

> Ejemplo: modelo predeterminado = gpt-3.5-turbo. Si cambiamos a gpt-4o en tema1:  
> Con restablecimiento activado: nuevo tema = gpt-3.5-turbo  
> Desactivado: nuevo tema = gpt-4o  

#### <mark style="color:blue;">**`Temperatura`**</mark> ：

Controla la creatividad de las respuestas (valor predeterminado: 0.7):
* Baja (0-0.3): respuestas precisas y coherentes
* Media (0.4-0.7): equilibrio creatividad-coherencia (ideal para chatbots)
* Alta (0.8-1.0): máxima creatividad pero menos coherencia

#### <mark style="color:blue;">**`Top P (núcleo de muestreo)`**</mark>：

Valor predeterminado: 1. Valores bajos = respuestas más conservadoras, altos = más diversidad.

#### <mark style="color:blue;">**`Ventana de contexto`**</mark>

Número de mensajes retenidos en el contexto:
* 5-10: conversaciones simples
* >10: tareas complejas (aumenta consumo de tokens)

#### <mark style="color:blue;">**`Activar límite de longitud (MaxToken)`**</mark>

Límite de tokens por respuesta. La mayoría de modelos soportan hasta 32k tokens.

{% hint style="success" %}
Recomendaciones:
* Chat: 500-800
* Texto corto: 800-2000
* Código: 2000-3600
* Texto largo: 4000+ (requiere soporte del modelo)
{% endhint %}

{% hint style="warning" %}
Respuestas pueden truncarse si exceden MaxToken. Ajusta según necesidades.
{% endhint %}

#### <mark style="color:blue;">**`Salida en flujo (Stream)`**</mark>

Si está activado: muestra la respuesta progresivamente como un flujo de texto en tiempo real.  
Desactivado: envía la respuesta completa de una vez.

{% hint style="info" %}
Desactiva para modelos no compatibles como o1-mini.
{% endhint %}

#### <mark style="color:blue;">**`Parámetros personalizados`**</mark>

Agrega parámetros adicionales (presence_penalty, etc.) al cuerpo de la solicitud. Documentación: [link de referencia](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Prioridad: parámetros personalizados > parámetros integrados.
Usa `<nombre_parametro>:undefined` para excluir parámetros.
{% endhint %}