---
icon: route
---
# Instrucciones de uso de la cadena de llamadas


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Funciones

La cadena de llamadas (también conocida como "trace") proporciona a los usuarios capacidades de observación en las conversaciones, ayudándoles a detectar el rendimiento específico de modelos, bases de conocimiento, MCP, búsqueda web y otros componentes durante el proceso de diálogo. Es una herramienta de observabilidad basada en [OpenTelemetry](https://opentelemetry.io/docs/languages/js/) que recopila, almacena y procesa datos del lado del cliente para lograr visualización, proporcionando una base cuantitativa para identificar problemas y optimizar resultados.

Cada conversación corresponde a un registro de trace, donde un trace consta de múltiples spans. Cada span corresponde a una lógica de procesamiento en Cherry Studio, como invocar sesiones de modelos, llamadas a MCP, consultas a bases de conocimiento, búsquedas web, etc. El trace se muestra como una estructura de árbol con spans como nodos, incluyendo datos principales como tiempo de ejecución y uso de tokens. En los detalles del span también se pueden ver sus entradas y salidas específicas.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Habilitar Trace

Por defecto, después de instalar Cherry Studio, la función Trace está oculta. Para activarla, debe habilitar el "Modo de desarrollador" en "Configuración" → "Configuración general", como se muestra a continuación:

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Los diálogos anteriores no generarán registros de Trace. Solo las nuevas preguntas y respuestas producirán registros de Trace. Estos registros se almacenan localmente. Para eliminar completamente los traces, puede:
1. Ir a "Configuración" → "Configuración de datos" → "Directorio de datos" → "Limpiar caché"
2. Eliminar manualmente los archivos en ~/.cherrystudio/trace

Como se muestra a continuación:

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Escenarios de uso

### Visualización de cadena completa

Haga clic en "Cadena de llamadas" dentro del cuadro de diálogo de Cherry Studio para ver todos los datos de la cadena. Ya sea que se hayan invocado modelos, búsquedas web, bases de conocimiento o MCP durante la conversación, todos se mostrarán en la ventana de la cadena de llamadas.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Ver detalles de modelos en la cadena

Para ver detalles específicos de un modelo en la cadena de llamadas, haga clic en el nodo de invocación del modelo para examinar sus entradas y salidas.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Ver detalles de búsqueda web

Para inspeccionar resultados de búsquedas web en la cadena, haga clic en el nodo de búsqueda web. En los detalles podrá ver la consulta realizada y los resultados devueltos.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Ver detalles de bases de conocimiento

Para examinar interacciones con bases de conocimiento, haga clic en el nodo correspondiente. En los detalles aparecerá la pregunta consultada y la respuesta generada.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Ver detalles de MCP

Para revisar invocaciones a MCP en la cadena, haga clic en el nodo de MCP. Los detalles mostrarán los parámetros de entrada pasados a la herramienta del servidor MCP y la respuesta devuelta.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Problemas y sugerencias

Esta funcionalidad es proporcionada por el equipo de [EDAS](https://www.aliyun.com/product/edas) de Alibaba Cloud. Para reportar problemas o sugerencias, únase al grupo de DingTalk (ID de grupo: 21958624) para comunicarse directamente con los desarrolladores.