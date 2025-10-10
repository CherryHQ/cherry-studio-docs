---
icon: message
---
# Interfaz de Conversación


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Asistentes y Temas

### Asistente

El `Asistente` consiste en personalizar la configuración del modelo seleccionado para su uso, como establecer indicaciones predefinidas y parámetros preconfigurados. Estas configuraciones permiten adaptar el modelo a tus expectativas laborales.

El `Asistente predeterminado del sistema` ofrece parámetros genéricos preconfigurados (sin indicaciones). Puedes usarlo directamente o buscar configuraciones específicas en la [página de agentes](agents.md).

### Temas

El `Asistente` es el conjunto padre de los `Temas`. Un solo asistente puede contener múltiples temas (conversaciones), donde todos los `Temas` comparten la configuración del modelo del `Asistente`, como parámetros e indicaciones (prompts).

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Botones del cuadro de diálogo

<figure><img src="../../.gitbook/assets/对话界面/对话框.png" alt=""><figcaption></figcaption></figure>

![](../../.gitbook/assets/对话界面/新话题.png) `Nuevo tema`: Crea un nuevo tema dentro del asistente actual.

![](../../.gitbook/assets/对话界面/上传图片或文档.png) `Subir imagen o documento`: Requiere soporte del modelo. Los documentos se analizan automáticamente como contexto para el modelo.

![](../../.gitbook/assets/对话界面/网络搜索.png) `Búsqueda web`: Configura información de búsqueda en ajustes. Los resultados se envían como contexto al modelo. Detalles en [Modo online](../../websearch/).

![](../../.gitbook/assets/对话界面/知识库.png) `Base de conocimiento`: Activa la base de conocimiento. Ver [Tutorial de base de conocimiento](../../knowledge-base/knowledge-base.md).

![](<../../.gitbook/assets/对话界面/MCP 服务器.png>) `Servidor MCP`: Activa la funcionalidad de servidor MCP. Ver [Tutorial de MCP](../../advanced-basic/mcp/).

![](../../.gitbook/assets/对话界面/生成图片.png) `Generar imagen`: No visible por defecto. Para modelos compatibles (ej. Gemini), actívalo manualmente.

{% hint style="info" %}
Por limitaciones técnicas, debes activar manualmente este botón para generar imágenes. Se eliminará tras futuras optimizaciones.
{% endhint %}

![](../../.gitbook/assets/对话界面/选择模型.png) `Seleccionar modelo`: Cambia el modelo para conversaciones futuras conservando el contexto.

![](../../.gitbook/assets/对话界面/快捷短语.png) `Frases rápidas`: Configura frases comunes en ajustes y úsalas aquí. Soporta variables.

![](../../.gitbook/assets/对话界面/清空消息.png) `Borrar mensajes`: Elimina todo el contenido del tema actual.

![](../../.gitbook/assets/对话界面/展开.png) `Expandir`: Amplía el cuadro de diálogo para textos largos.

![](../../.gitbook/assets/对话界面/清除上下文.png) `Borrar contexto`: Limpia el contexto disponible para el modelo sin eliminar contenido ("olvida" conversaciones anteriores).

![](<../../.gitbook/assets/对话界面/预估 Token 数.png>) `Tokens estimados`: Muestra tokens estimados. Datos: `Contexto actual`, `Máximo contexto` (∞ = ilimitado), `Palabras en entrada actual`, `Tokens estimados`.

{% hint style="info" %}
Solo estimación. Los tokens reales varían según el modelo. Consulta datos del proveedor.
{% endhint %}

![](../../.gitbook/assets/对话界面/翻译.png) `Traducir`: Traduce el contenido actual al inglés.

## Configuración de conversación

<figure><img src="../../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Configuración del modelo

Sincronizada con los parámetros de `Configuración del modelo` del asistente. Ver [Editar asistente](chat.md#bian-ji-zhu-shou).

{% hint style="info" %}
En Configuración de conversación, solo esta sección afecta al asistente actual. Otros ajustes son globales (ej. estilo de burbuja aplica a todos los temas).
{% endhint %}

### Configuración de mensajes

#### <mark style="color:blue;">**`Línea divisoria de mensajes`**</mark>:

Separa el contenido del mensaje de la barra de acciones.

{% tabs %}
{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Usar fuente serif`**</mark>：

Cambia el estilo de fuente. También puedes personalizar fuentes mediante [CSS personalizado](../../personalization-settings/).

#### <mark style="color:blue;">**`Mostrar números de línea en código`**</mark>：

Muestra números de línea en bloques de código generados.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Bloques de código plegables`**</mark>：

Plegado automático cuando bloques de código son extensos.

#### <mark style="color:blue;">**`Ajuste de línea en bloques de código`**</mark>：

Ajuste automático para líneas largas que excedan la ventana.

#### <mark style="color:blue;">**`Plegado automático de pensamientos`**</mark>：

Modelos compatibles pliegan automáticamente procesos de pensamiento tras completarlos.

#### <mark style="color:blue;">**`Estilo de mensaje`**</mark>：

Cambia entre estilos de burbuja o lista.

#### <mark style="color:blue;">**`Estilo de código`**</mark>：

Cambia el estilo visual de bloques de código.

#### <mark style="color:blue;">**`Motor de fórmulas matemáticas`**</mark>：

* KaTeX: Renderizado más rápido, optimizado para rendimiento.
* MathJax: Renderizado lento, pero más completo en símbolos y comandos.

#### <mark style="color:blue;">**`Tamaño de fuente de mensajes`**</mark>：

Ajusta el tamaño de fuente en la interfaz.

### Configuración de entrada

#### <mark style="color:blue;">**`Mostrar tokens estimados`**</mark>：

Muestra tokens estimados para texto de entrada (referencial, no consumo real).

#### <mark style="color:blue;">**`Pegar texto largo como archivo`**</mark>：

Textos largos pegados se muestran como archivos para reducir interferencias.

#### <mark style="color:blue;">**`Renderizar Markdown en entrada`**</mark>：

Desactivado: Solo renderiza respuestas del modelo, no mensajes enviados.

{% tabs %}
{% tab title="Desactivado" %}
<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Activado" %}
<figure><img src="../../.gitbook/assets/image (7) (1).png" alt="" width="563"><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

#### <mark style="color:blue;">**`Traducción rápida (3 espacios)`**</mark>：

Tres espacios consecutivos traducen mensaje a inglés (sobrescribe texto original).

{% hint style="warning" %}
Advertencia: Sobrescribe el texto original.
{% endhint %}

#### <mark style="color:blue;">**`Idioma objetivo`**</mark>：

Configura idioma para botón de traducción y método de 3 espacios.

## Configuración del asistente

Selecciona <mark style="background-color:yellow;">nombre del asistente</mark> → Menú contextual → Configuración

### Editar asistente

{% hint style="info" %}
Afecta a todos los temas bajo este asistente.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Configuración de indicaciones

#### <mark style="color:blue;">**`Nombre`**</mark>：

Nombre personalizado para identificación.

#### <mark style="color:blue;">**`Indicación`**</mark>：

Prompt. Consulta formatos en la página de agentes.

#### Configuración del modelo

#### <mark style="color:blue;">**`Modelo predeterminado`**</mark>：

Modelo fijo para este asistente. Si no se establece, usa el [modelo global](settings/default-models.md#mo-ren-zhu-shou-mo-xing).

{% hint style="info" %}
Prioridad: Modelo del asistente > Modelo global de conversación. Sin configuración, modelo del asistente = modelo global.
{% endhint %}

#### <mark style="color:blue;">**`Reinicio automático de modelo`**</mark>：

Activado: Al crear temas nuevos, usan el modelo predeterminado del asistente. Desactivado: Nuevos temas heredan el modelo del tema anterior.

> Ejemplo: Modelo predeterminado = gpt-3.5-turbo. En Tema 1 cambio a gpt-4o:
>
> • Reinicio automático ON: Tema 2 usa gpt-3.5-turbo
>
> • Reinicio automático OFF: Tema 2 usa gpt-4o

#### <mark style="color:blue;">**`Temperatura (Temperature)`**</mark> ：

Controla aleatoriedad (valor predeterminado: 0.7):
* Baja (0-0.3): Precisión (ej. código)
* Media (0.4-0.7): Equilibrio (ej. conversación)
* Alta (0.8-1.0): Creatividad (ej. escritura)

#### <mark style="color:blue;">**`Top P (Muestreo nuclear)`**</mark>：

Predeterminado: 1. Valores bajos = salida conservadora; altos = diversidad:
* Bajo (0.1-0.3): Vocabulario restringido (ej. documentos)
* Medio (0.4-0.6): Equilibrio
* Alto (0.7-1.0): Diversidad creativa

{% hint style="info" %}
- Parámetros usables individualmente o combinados
- Experimenta para ajustarlos a tus necesidades
- Rangos sugeridos: referencia general (consultar documentación específica del modelo)
{% endhint %}

#### <mark style="color:blue;">**`Cantidad de contexto (Context Window)`**</mark>

Número de mensajes retenidos (mayor cantidad = más tokens):
* 5-10: Conversaciones simples
* \>10: Tareas complejas (ej. redacción estructurada)
* Nota: Más mensajes = mayor consumo de tokens

#### <mark style="color:blue;">**`Habilitar límite de longitud (MaxToken)`**</mark>

Tokens máximos por respuesta. Afecta calidad y longitud:
> Ejemplo: Para probar conectividad, establecer MaxToken=1

Límites típicos: 32k tokens (varía por modelo). Recomendaciones:
{% hint style="success" %}
• Chat básico: 500-800  
• Textos cortos: 800-2000  
• Generación de código: 2000-3600  
• Textos largos: ≥4000 (requiere soporte del modelo)
{% endhint %}

{% hint style="warning" %}
Respuestas pueden truncarse si exceden MaxToken. Ajusta según necesidades.
{% endhint %}

#### <mark style="color:blue;">**`Salida en flujo (Stream)`**</mark>

Transmisión continua de datos (efecto máquina de escribir):
• Activado: Salida carácter por carácter  
• Desactivado: Salida completa tras generación

{% hint style="info" %}
Desactiva para modelos incompatibles (ej. o1-mini inicial).
{% endhint %}

#### <mark style="color:blue;">**`Parámetros personalizados`**</mark>

Añade parámetros adicionales al cuerpo de la solicitud (ej. `presence_penalty`). Normalmente avanzado.  
Referencia: [Documentación](https://openai.apifox.cn/doc-3222739)

{% hint style="info" %}
• Prioridad: Parámetros personalizados > Parámetros integrados  
  > Ejemplo: Configurar `model:gpt-4o` ignora selecciones posteriores  
• Usa <kbd>nombre_parametro:undefined</kbd> para excluir parámetros  
• Proveedores pueden tener parámetros exclusivos (consultar documentación)
{% endhint %}