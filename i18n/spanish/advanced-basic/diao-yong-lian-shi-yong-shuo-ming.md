---
icon: route
---
# Instrucciones de uso de la cadena de llamadas


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Funcionalidad

La cadena de llamadas (también conocido como "trace") proporciona capacidades de análisis de conversaciones, ayudando a los usuarios a observar el rendimiento específico del modelo, base de conocimiento, MCP, búsqueda web y otros componentes durante el diálogo. Es una herramienta de observabilidad implementada sobre [OpenTelemetry](https://opentelemetry.io/docs/languages/js/) que visualiza datos mediante recopilación, almacenamiento y procesamiento en el extremo, ofreciendo bases cuantitativas para identificar problemas y optimizar resultados.

Cada conversación corresponde a un registro trace, compuesto por múltiples spans. Cada span corresponde a una lógica de procesamiento de Cherry Studio, como llamadas a sesiones de modelos, MCP, base de conocimiento o búsqueda web. El trace se muestra en estructura de árbol con spans como nodos, incluyendo datos principales como tiempo de ejecución y uso de tokens. En los detalles del span también pueden verse sus entradas y salidas específicas.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Habilitar Trace

Por defecto, tras instalar Cherry Studio, Trace permanece oculto. Debe activarse en "Configuración" > "Configuración general" > "Modo desarrollador", como se muestra:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Los diálogos anteriores no generarán registros Trace. Solo se crearán registros tras nuevas interacciones de preguntas y respuestas. Los registros se almacenan localmente. Para eliminar completamente los Traces, use: "Configuración" > "Configuración de datos" > "Directorio de datos" > "Limpiar caché". Alternativamente, elimine manualmente los archivos en `~/.cherrystudio/trace`:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Escenarios de uso

### Visualización de toda la cadena

Haga clic en el icono de cadena de llamadas durante un diálogo para ver datos completos de la cadena. Ya sea que involucre modelos, búsqueda web, base de conocimiento o MCP, todos los componentes aparecerán en la ventana de trazabilidad.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Inspeccionar modelos en la cadena

Para ver detalles de un modelo en la cadena, haga clic en su nodo para examinar entradas y salidas específicas.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Inspeccionar búsqueda web en la cadena

Al hacer clic en el nodo de búsqueda web, se muestran las consultas realizadas y los resultados obtenidos.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Inspeccionar base de conocimiento en la cadena

El nodo de base de conocimiento revela las preguntas consultadas y las respuestas generadas.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Ver llamadas MCP en la cadena

Haga clic en el nodo MCP para examinar parámetros de entrada y respuestas del servidor tool.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Problemas y sugerencias

Esta funcionalidad es proporcionada por el equipo de Alibaba Cloud [EDAS](https://www.aliyun.com/product/edas). Para problemas o sugerencias, únase al grupo DingTalk (ID: 21958624) para comunicarse directamente con los desarrolladores.