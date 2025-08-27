---
icon: route
---
# Instrucciones de Uso de Trazas (Trace)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Funciones

La traza (también llamada "trace") proporciona capacidades de observación para las conversaciones, ayudando a los usuarios a comprender el rendimiento específico de modelos, bases de conocimiento, MCP, búsquedas web, etc., durante los diálogos. Es una herramienta de observabilidad implementada basada en [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), que visualiza datos mediante recopilación, almacenamiento y procesamiento en el extremo, proporcionando bases cuantificables para identificar problemas y optimizar resultados.

Cada conversación corresponde a un registro de traza. Una traza consta de múltiples spans, donde cada span corresponde a una lógica de procesamiento de Cherry Studio, como invocar un modelo, llamar a MCP, consultar bases de conocimiento o realizar búsquedas web. La traza se muestra en estructura de árbol, donde los spans son nodos. Los datos principales incluyen tiempo de ejecución y consumo de tokens, y en los detalles del span se pueden revisar entradas y salidas específicas.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Habilitar Trazas

Por defecto, después de instalar Cherry Studio, las Trazas están ocultas. Debes habilitarlas en "Configuración" > "Configuración General" > "Modo Desarrollador", como se muestra:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Los registros anteriores no generarán Trazas; solo se crearán registros para nuevas interacciones de preguntas y respuestas. Los registros se almacenan localmente. Para eliminar completamente las Trazas, ve a "Configuración" > "Configuración de Datos" > "Directorio de Datos" > "Borrar Caché", o elimina manualmente los archivos en \~/.cherrystudio/trace:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Casos de Uso

### Visualización de Cadena Completa

Haz clic en "Trazas" en el cuadro de diálogo de Cherry Studio para ver datos de la cadena completa. Ya sea que durante la conversación se invoquen modelos, búsquedas web, bases de conocimiento o MCP, todos aparecerán en esta ventana.

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Detalles de Modelos

Para ver detalles de un modelo específico en la traza, haz clic en el nodo de invocación del modelo para revisar sus entradas y salidas.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Detalles de Búsquedas Web

Para examinar búsquedas web en la traza, haz clic en el nodo correspondiente. En los detalles, podrás ver la consulta realizada y los resultados obtenidos.

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Detalles de Bases de Conocimiento

Al hacer clic en el nodo de base de conocimiento, se muestran las entradas y salidas específicas, incluyendo la consulta realizada y las respuestas recuperadas.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Detalles de Invocaciones MCP

Para analizar invocaciones MCP en la cadena, selecciona el nodo MCP. Los detalles mostrarán los parámetros de entrada del servidor y las respuestas del tool.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Problemas y Sugerencias

Esta funcionalidad es proporcionada por el equipo [EDAS](https://www.aliyun.com/product/edas) de Alibaba Cloud. Para problemas o sugerencias, únete al grupo DingTalk (ID: 21958624) para comunicación directa con desarrolladores.

\