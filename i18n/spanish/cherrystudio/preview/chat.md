---
icon: message
---
# Interfaz de Conversación


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Asistentes y Temas

### Asistente

Un `asistente` permite personalizar la configuración del modelo seleccionado, como ajustes predefinidos de indicaciones (prompts) y parámetros, para que el modelo funcione según tus expectativas.

El `asistente predeterminado del sistema` tiene parámetros genéricos preestablecidos (sin indicaciones), puedes usarlo directamente o buscar la configuración que necesitas en la [página de Agentes](agents.md).

### Tema

El `asistente` es el conjunto padre de los `temas`. Bajo un asistente individual puedes crear múltiples temas (es decir, conversaciones), y todos los `temas` comparten la configuración de parámetros y las indicaciones predefinidas (prompt) del `asistente`.

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botones dentro del Cuadro de Diálogo

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nuevo tema` Crea un nuevo tema dentro del asistente actual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Cargar imagen o documento` La carga de imágenes requiere compatibilidad del modelo. Los documentos se analizan automáticamente como texto contextual para el modelo.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Búsqueda web` Requiere configurar información de búsqueda en la configuración. Los resultados se devuelven como contexto al modelo, consulta [Modo en línea](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de conocimiento` Activa la base de conocimiento, consulta [Tutorial de Base de Conocimiento](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP` Activa la función del servidor MCP, consulta [Tutorial de Uso de MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Generar imagen` Solo se muestra cuando el **modelo de diálogo** seleccionado admite generación de imágenes. (Para modelos de generación de imágenes no conversacionales, visita [Dibujo](./drawing.md)).

![](../../.gitbook/assets/对话界面/选择模型.png) `Seleccionar modelo` Cambia al modelo especificado para las próximas conversaciones, manteniendo el contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases rápidas` Debes predefinir frases comunes en la configuración. Se insertan directamente al invocarlas y admiten variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Borrar mensajes` Elimina todo el contenido del tema actual.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir` Amplía el cuadro de diálogo para facilitar la entrada de textos largos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Limpiar contexto` Trunca el contexto accesible para el modelo sin eliminar contenido, haciendo que "olvide" conversaciones previas.

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Estimar número de tokens` Muestra el número estimado de tokens. Los cuatro valores corresponden a: `Tokens de contexto actuales`, `Máximo de contexto` (∞ indica contexto ilimitado), `Caracteres en el campo de entrada` y `Tokens estimados`.

{% hint style="info" %}
Esta función solo sirve para estimar el número de tokens. El número real varía según el modelo. Consulta los datos proporcionados por el proveedor del modelo.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traducir` Traduce el contenido actual del campo de entrada a inglés.

## Configuración de Conversación

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configuración del Modelo

Sincronizada con los parámetros de `Configuración del Modelo` en la configuración del asistente. Consulta [Configuración del Asistente](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
En la configuración de conversación, esta configuración solo afecta al asistente actual, mientras que el resto son globales. Ejemplo: al establecer el estilo de mensaje como burbujas, se aplicará en todos los temas de cualquier asistente.
{% endhint %}

### Configuración de Mensajes

#### <mark style="color:blue;">**`Línea divisoria de mensajes`**</mark>:

Separa el cuerpo del mensaje de la barra de operaciones con una línea divisoria.

{% tabs %}
{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar fuente serif`**</mark>:

Cambia el estilo de fuente. También puedes personalizar la fuente mediante [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Mostrar números de línea en código`**</mark>:

Muestra números de línea en los fragmentos de código generados por el modelo.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Bloques de código plegables`**</mark>:

Al activar, los bloques de código largos se plegarán automáticamente.

#### <mark style="color:blue;">**`Ajuste automático de líneas en código`**</mark>:

Al activar, las líneas largas en los fragmentos de código se ajustarán automáticamente (al superar el ancho de la ventana).

#### <mark style="color:blue;">**`Plegar contenido de razonamiento automáticamente`**</mark>:

Al activar, los modelos con capacidad de razonamiento plegarán el proceso de razonamiento tras completarlo.

#### <mark style="color:blue;">**`Estilo de mensajes`**</mark>:

Cambia entre estilo de burbujas o lista en la interfaz de conversación.

#### <mark style="color:blue;">**`Estilo de código`**</mark>:

Cambia el estilo visual de los fragmentos de código.

#### <mark style="color:blue;">**`Motor de fórmulas matemáticas`**</mark>:

* KaTeX: Más rápido, optimizado para rendimiento.
* MathJax: Más lento pero con funciones completas y soporte amplio de símbolos.

#### <mark style="color:blue;">**`Tamaño de fuente de mensajes`**</mark>:

Ajusta el tamaño de fuente en la interfaz de conversación.

### Configuración de Entrada

#### <mark style="color:blue;">**`Mostrar número estimado de tokens`**</mark>:

Muestra en el campo de entrada los tokens estimados consumidos por el texto (no representa el consumo real de contexto, solo para referencia).

#### <mark style="color:blue;">**`Pegar texto largo como archivo`**</mark>:

Al pegar texto largo desde otras fuentes, se muestra como archivo para reducir interferencias durante entradas posteriores.

#### <mark style="color:blue;">**`Renderizar Markdown en mensajes de entrada`**</mark>:

Al desactivar, solo se renderizan los mensajes de respuesta del modelo, no los mensajes enviados.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traducir con 3 pulsaciones rápidas de espacio`**</mark>:

Tras escribir un mensaje, presiona la barra espaciadora 3 veces rápidamente para traducir el contenido a inglés.

{% hint style="warning" %}
Nota: Esta acción sobrescribe el texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma de destino`**</mark>:

Establece el idioma de destino para el botón de traducción y la función de 3 pulsaciones.

## Configuración del Asistente

En la interfaz de asistentes, selecciona el <mark style="background-color:yellow;">nombre del asistente</mark> → elige la configuración correspondiente en el <mark style="background-color:yellow;">menú contextual</mark>

### Editar Asistente

{% hint style="info" %}
La configuración del asistente afecta a todos los temas bajo este asistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configuración de Indicaciones (Prompt)

#### <mark style="color:blue;">**`Nombre`**</mark>:

Define un nombre de asistente personalizado para identificarlo fácilmente.

#### <mark style="color:blue;">**`Indicación (Prompt)`**</mark>:

Configura el prompt. Consulta la estructura en la página de Agentes para editar contenido.

#### Configuración del Modelo

#### <mark style="color:blue;">**`Modelo predeterminado`**</mark>:

Fija un modelo predeterminado específico para este asistente. Al agregar desde la página de Agentes o copiar el asistente, el modelo inicial será este. Si no se establece, usará el modelo inicial global ([Modelo predeterminado del asistente](settings/default-models.md#mo-ren-zhu-shou-mo-xing)).

{% hint style="info" %}
Existen dos modelos predeterminados: el [modelo de diálogo global predeterminado](settings/default-models.md#mo-ren-zhu-shou-mo-xing) y el modelo predeterminado del asistente. El modelo predeterminado del asistente tiene prioridad. Si no se establece, coincide con el modelo de diálogo global predeterminado.
{% endhint %}

#### <mark style="color:blue;">**`Restablecer modelo automáticamente`**</mark>:

Activado: Al cambiar a otro modelo durante una conversación y crear un nuevo tema, este se reiniciará al modelo predeterminado del asistente. Desactivado: El nuevo tema heredará el modelo usado en el tema anterior.

> Ejemplo: Si el modelo predeterminado del asistente es gpt-3.5-turbo y en el tema 1 cambias a gpt-4o:
>
> * Con reinicio automático: El tema 2 usará gpt-3.5-turbo.
> * Sin reinicio automático: El tema 2 usará gpt-4o.

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark>:

Controla la aleatoriedad y creatividad de la salida del modelo (valor predeterminado: 0.7):

* Valores bajos (0-0.3):
  * Salidas más deterministas y enfocadas
  * Ideal para generación de código o análisis de datos
  * Prioriza palabras con mayor probabilidad
* Valores medios (0.4-0.7):
  * Equilibrio entre creatividad y coherencia
  * Recomendado para diálogos cotidianos (~0.5)
* Valores altos (0.8-1.0):
  * Mayor creatividad y diversidad
  * Útil para escritura creativa o lluvia de ideas
  * Puede reducir la coherencia

#### <mark style="color:blue;">**`Top P (Muestreo nuclear)`**</mark>:

Valor predeterminado: 1. Valores más bajos producen salidas más monótonas pero comprensibles; valores altos amplían el vocabulario y diversifican las respuestas.

* Valores bajos (0.1-0.3):
  * Considera solo palabras de alta probabilidad
  * Salidas conservadoras y controladas
  * Ideal para documentación técnica
* Valores medios (0.4-0.6):
  * Equilibrio entre diversidad y precisión
  * Apto para diálogos y escritura general
* Valores altos (0.7-1.0):
  * Amplio rango de selección léxica
  * Contenido rico y diverso
  * Recomendado para escritura creativa

{% hint style="info" %}
- Estos parámetros pueden usarse independientemente o combinados
- Elige valores según el tipo de tarea
- Experimenta para encontrar combinaciones óptimas
- Los rangos sugeridos son referenciales; consulta la documentación específica del modelo
{% endhint %}

#### <mark style="color:blue;">**`Cantidad de contexto (Ventana de contexto)`**</mark>

Número de mensajes a mantener en contexto. Valores más altos consumen más tokens:

* 5-10: Diálogos comunes
* >10: Tareas complejas que requieren memoria prolongada (ej.: generación de textos largos con coherencia lógica)
* > Nota: Más mensajes = mayor consumo de tokens

#### <mark style="color:blue;">**`Activar límite de longitud de mensaje (MaxToken)`**</mark>

Máximo [Token](https://docs.cherry-ai.com/question-contact/knowledge#shen-me-shi-tokens) por respuesta. En modelos de lenguaje grande, max token define la calidad y longitud de las respuestas.

> Ejemplo: Al probar la conexión de un modelo en CherryStudio, establece MaxToken=1 si solo necesitas verificar la respuesta.

La mayoría de los modelos tienen límite máximo de 32k Tokens (algunos 64k+). Consulta la documentación específica.

{% hint style="success" %}
Recomendaciones:
* Chat común: 500-800
* Textos cortos: 800-2000
* Generación de código: 2000-3600
* Textos largos: 4000+ (requiere soporte del modelo)
{% endhint %}

{% hint style="warning" %}
Las respuestas suelen limitarse a MaxToken, pero pueden truncarse (ej.: código largo) o ser incompletas. Ajusta según necesidades específicas.
{% endhint %}

#### <mark style="color:blue;">**`Salida en flujo (Stream)`**</mark>

Transmite datos continuamente en lugar de enviarlos completos. Permite ver la respuesta mientras se genera (efecto máquina de escribir).

Desactivado: Muestra la respuesta completa tras generarse (como mensajes de WhatsApp).

Activado: Muestra carácter por carácter conforme el modelo lo genera.

{% hint style="info" %}
Desactiva para modelos que no admitan flujo, como **inicialmente** o1-mini.
{% endhint %}

#### <mark style="color:blue;">**`Parámetros personalizados`**</mark>

Añade parámetros adicionales al cuerpo de la solicitud (ej.: `presence_penalty`). Usado raramente.

> Parámetros como top-p, maxtokens y stream son ejemplos de estos.

Formato: Nombre del parámetro—Tipo (texto, número)—Valor. Referencia: [Visitar](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
Los proveedores de modelos suelen tener parámetros exclusivos. Consulta su documentación.
{% endhint %}

{% hint style="info" %}
* Los parámetros personalizados tienen prioridad sobre los integrados. Si hay duplicados, los personalizados los sobrescriben.

> Ejemplo: Si configuras `model` como `gpt-4o` en parámetros personalizados, siempre usará ese modelo.

* Usa <kbd>nombre_del_parámetro:undefined</kbd> para excluir parámetros.
{% endhint %}