---
icon: message
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Interfaz de conversación

## Asistentes y temas

### Asistente

El `Asistente` personaliza las configuraciones del modelo seleccionado para optimizar su uso, como preconfigurar instrucciones de aviso (prompts) y parámetros. Estos ajustes ayudan a que el modelo se alinee mejor con tus expectativas de trabajo.

El `Asistente predeterminado del sistema` incluye parámetros generales (sin instrucciones de aviso). Puedes usarlo directamente o buscar configuraciones predefinidas en la [página de Agentes](agents.md).

### Temas

El `Asistente` es el conjunto principal de los `Temas`. Un solo asistente puede crear múltiples temas (conversaciones), donde todos los `Temas` comparten la misma configuración de parámetros e instrucciones (prompts) del asistente.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botones en el cuadro de diálogo

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nuevo tema` Crea un nuevo tema dentro del asistente actual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Subir imagen o documento` Requiere soporte del modelo para imágenes. Los documentos se analizarán automáticamente como contexto textual para el modelo.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Búsqueda web` Debes configurar la búsqueda web en los ajustes. Los resultados se proporcionan como contexto al modelo. Más detalles en [Modo online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de conocimientos` Activa la base de conocimientos. Ver [Tutorial de Base de Conocimientos](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP` Activa la función del servidor MCP. Ver [Tutorial MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Generar imagen` No se muestra por defecto. Para modelos compatibles (ej. Gemini), debes activar manualmente el botón para generar imágenes.

{% hint style="info" %}
Por razones técnicas, debes activar manualmente el botón para generar imágenes. Se eliminará después de optimizar esta función.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Seleccionar modelo` Cambia al modelo especificado para continuar la conversación, conservando el contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases rápidas` Primero configura frases comunes en los ajustes. Llámalas aquí para insertar directamente, con soporte para variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Vaciar mensajes` Elimina todo el contenido del tema actual.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir` Amplía el cuadro de diálogo para ingresar textos largos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpiar contexto` Trunca el contexto disponible para el modelo sin eliminar contenido, haciendo que "olvide" conversaciones anteriores.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Número estimado de Tokens` Muestra la estimación de tokens: `Contexto actual`, `Máximo contexto` (∞ indica contexto infinito), `Palabras actuales en el cuadro de entrada`, `Tokens estimados`.

{% hint style="info" %}
Esta función solo estima tokens. El conteo real varía por modelo; consulta los datos del proveedor.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traducir` Traduce el contenido actual del cuadro de entrada a inglés.

## Configuración de conversación

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configuración del modelo

Sincronizado con parámetros de `Configuración del modelo` en el asistente. Ver [Editar asistente](chat.md#editar-asistente).

{% hint style="info" %}
En la configuración de conversación, solo el modelo afecta al asistente actual. Otros ajustes son globales (ej. estilo de mensajes aplica a todos los temas).
{% endhint %}

### Configuración de mensajes

#### <mark style="color:blue;">**`Línea divisoria de mensajes`**</mark>:

Separa el contenido del mensaje del área de acciones con una línea.

{% tabs %}
{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar fuente serif`**</mark>：

Cambia el estilo de fuente. También puedes personalizar fuentes con [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Mostrar números de línea en código`**</mark>：

Muestra números de línea en bloques de código generados por el modelo.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Bloques de código plegables`**</mark>：

Plegar automáticamente bloques de código largos.

#### <mark style="color:blue;">**`Ajuste de línea en bloques de código`**</mark>：

Ajustar automáticamente líneas largas de código que excedan el ancho de ventana.

#### <mark style="color:blue;">**`Plegar proceso de reflexión automáticamente`**</mark>：

Plegar automáticamente procesos de reflexión después de completarse (para modelos compatibles).

#### <mark style="color:blue;">**`Estilo de mensajes`**</mark>：

Alternar entre estilo de burbujas o estilo de lista.

#### <mark style="color:blue;">**`Estilo de código`**</mark>：

Cambiar estilo visual de bloques de código.

#### <mark style="color:blue;">**`Motor de fórmulas matemáticas`**</mark>：

* KaTeX: Renderizado más rápido, optimizado para rendimiento.
* MathJax: Renderizado más lento, pero soporta más símbolos y comandos matemáticos.

#### <mark style="color:blue;">**`Tamaño de fuente de mensajes`**</mark>：

Ajustar tamaño de fuente en la interfaz de conversación.

### Configuración de entrada

#### <mark style="color:blue;">**`Mostrar tokens estimados`**</mark>：

Mostrar tokens estimados para el texto ingresado (referencia, no consumo real).

#### <mark style="color:blue;">**`Pegar texto largo como archivo`**</mark>：

Texto largo pegado en el cuadro de entrada se mostrará como archivo para reducir interferencias.

#### <mark style="color:blue;">**`Renderizar mensajes de entrada con Markdown`**</mark>：

Cuando está desactivado, solo se renderizan respuestas del modelo, no mensajes enviados.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traducir con 3 espacios rápidos`**</mark>：

Traducir el contenido del cuadro de entrada a inglés presionando espacio tres veces.

{% hint style="warning" %}
Nota: Esto sobrescribe el texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma objetivo`**</mark>：

Establecer idioma objetivo para el botón de traducción y los 3 espacios rápidos.

## Configuración de asistente

Selecciona el <mark style="background-color:yellow;">nombre del asistente</mark> → Configuración en <mark style="background-color:yellow;">menú contextual</mark>

### Editar asistente

{% hint style="info" %}
Los ajustes afectan a todos los temas bajo este asistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configuración de prompt

#### <mark style="color:blue;">**`Nombre`**</mark>：

Nombre personalizado para identificar el asistente.

#### <mark style="color:blue;">**`Prompt`**</mark>：

Instrucciones de aviso. Consulta la sintaxis en la página de Agentes.

#### Configuración del modelo

#### <mark style="color:blue;">**`Modelo predeterminado`**</mark>：

Establece un modelo fijo para este asistente. El modelo inicial será este al agregar desde Agentes o copiar asistentes. Si no se configura, se usa el modelo global (ver [Modelo predeterminado de asistente](settings/default-models.md#modelo-predeterminado-de-asistente)).

{% hint style="info" %}
Existen dos modelos predeterminados: global y de asistente. El modelo del asistente tiene prioridad sobre el global.
{% endhint %}

#### <mark style="color:blue;">**`Restablecer modelo automáticamente`**</mark>：

Activado: Al cambiar de modelo en un tema, los nuevos temas usarán el modelo predeterminado del asistente. Desactivado: Los nuevos temas mantendrán el último modelo usado.

> Ejemplo: Modelo predeterminado = gpt-3.5-turbo. En Tema 1 se cambia a gpt-4o.
>
> - Con restablecimiento automático: Tema 2 usa gpt-3.5-turbo.
> - Sin restablecimiento: Tema 2 usa gpt-4o.

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark>：

Controla aleatoriedad y creatividad (predeterminado: 0.7):

* Baja (0-0.3):
  - Salida más determinista
  - Ideal para generación de código, análisis de datos
* Media (0.4-0.7):
  - Equilibrio entre creatividad y coherencia
  - Recomendado para chatbots (~0.5)
* Alta (0.8-1.0):
  - Mayor creatividad y diversidad
  - Ideal para escritura creativa

#### <mark style="color:blue;">**`Top P (Muestreo de núcleo)`**</mark>：

Predeterminado: 1. Valores bajos generan contenido más monótono y predecible. Valores altos aumentan diversidad léxica.

* Pequeño (0.1-0.3):
  - Vocabulario conservador
  - Ideal para documentación técnica
* Medio (0.4-0.6):
  - Balance entre diversidad y precisión
* Grande (0.7-1.0):
  - Contenido rico y diverso
  - Ideal para escritura creativa

{% hint style="info" %}
- Usa parámetros independientemente o combinados
- Experimenta para encontrar valores óptimos
- Los rangos pueden variar según modelos; consulta documentación.
{% endhint %}

#### <mark style="color:blue;">**`Cantidad de contexto (Context Window)`**</mark>

Mensajes retenidos en contexto. Mayor valor = contexto más largo + más tokens:

* 5-10: Conversaciones simples
* \>10: Tareas complejas que requieren memoria larga (ej. escritura estructurada)
* Nota: Más mensajes = más consumo de tokens

#### <mark style="color:blue;">**`Habilitar límite de longitud (MaxToken)`**</mark>

Máximo de [Tokens](https://docs.cherry-ai.com/question-contact/knowledge#qué-son-tokens) por respuesta. Parámetro crítico que afecta longitud y calidad.

> Ejemplo: Al probar conectividad de modelos, basta con MaxToken=1 para confirmar respuesta.

La mayoría de modelos tienen límites de 32k tokens (algunos 64k+). Consulta especificaciones.

Sugerencias:

{% hint style="success" %}
Recomendaciones:

* Chat básico: 500-800
* Textos cortos: 800-2000
* Generación de código: 2000-3600
* Textos largos: 4000+ (requiere soporte del modelo)
{% endhint %}

{% hint style="warning" %}
Las respuestas pueden truncarse si exceden MaxToken (ej. código largo). Ajusta según necesidades.
{% endhint %}

#### <mark style="color:blue;">**`Salida por flujo (Stream)`**</mark>

Transmite datos continuamente en lugar de enviarlos completos. En CherryStudio, simula efecto "máquina de escribir".

Desactivado: Entrega completa después de generar todo (como mensajes de WhatsApp).
Activado: Entrega progresiva carácter por carácter.

{% hint style="info" %}
Desactívalo para modelos no compatibles (ej. o1-mini en versiones iniciales).
{% endhint %}

#### <mark style="color:blue;">**`Parámetros personalizados`**</mark>

Agrega parámetros extra al cuerpo de solicitud (ej. `presence_penalty`). Uso avanzado.

> Parámetros como top-p, maxtokens y stream pertenecen a esta categoría.
> 
> Sintaxis: Nombre—Tipo (texto/número)—Valor. Ver [Documentación](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Los proveedores de modelos tienen parámetros exclusivos; consulta sus documentaciones.
{% endhint %}

{% hint style="info" %}
* Parámetros personalizados anulan configuraciones integradas si hay conflictos.
  
> Ejemplo: Establecer `model: gpt-4o` ignora cualquier selección de modelo en la conversación.

* Usa <kbd>nombre:undefined</kbd> para excluir parámetros.
{% endhint %}