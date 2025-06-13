---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

```markdown
# Funciones de Voz

```
Cherry Studio Manual de Uso de Funciones de Voz

I. Resumen de Funciones de Voz

Cherry Studio proporciona tres módulos principales de funciones de voz: TTS (texto a voz), ASR (reconocimiento de voz) y llamadas de voz. Estas funciones permiten una comunicación natural con la IA mediante voz, mejorando la experiencia de usuario.

- TTS (texto a voz): Convierte las respuestas de texto de la IA en salida de voz
- ASR (reconocimiento de voz): Convierte tu voz en entrada de texto
- Llamadas de voz: Combina TTS y ASR para una experiencia de diálogo similar a ChatGPT

II. Función TTS (Texto a Voz)

1. Tipos de servicio admitidos

Cherry Studio admite cuatro tipos de servicios TTS:

- OpenAI: Utiliza la API TTS de OpenAI, requiere clave de API
- Navegador TTS: Usa la síntesis de voz integrada del navegador, gratuito y sin configuración
- Siliconflow: Utiliza el servicio TTS de Siliconflow, requiere clave de API
- TTS en línea gratuito: Usa servicios TTS gratuitos en línea, no requiere clave de API

2. Método de configuración

1) Ingresa a la página de configuración, selecciona la pestaña "Funciones de Voz"
2) En la subpestaña "TTS":
   - Habilita la función TTS (activa el interruptor)
   - Selecciona el tipo de servicio TTS
   - Configura los parámetros según el servicio seleccionado:
     - OpenAI: Ingresa clave de API, dirección API, selecciona voz y modelo
     - Navegador TTS: Selecciona voz
     - Siliconflow: Ingresa clave de API, dirección API, selecciona voz, modelo, formato de respuesta y velocidad
     - TTS en línea gratuito: Selecciona voz y formato de salida
3) Configura opciones de filtro TTS (opcional):
   - Filtrar procesos de pensamiento
   - Filtrar marcas Markdown
   - Filtrar bloques de código
4) Establece si mostrar la barra de progreso TTS
5) Haz clic en "Probar TTS" para verificar la configuración

3. Método de uso

- Una vez habilitado el TTS, las respuestas de IA se convertirán automáticamente a voz
- En la interfaz de chat, cada respuesta de IA mostrará un botón de reproducción TTS
- Haz clic para reproducir/pausar
- Si está habilitada, se mostrará la barra de progreso debajo del texto
- Los textos largos se sintetizan y reproducen en segmentos continuos

III. Función ASR (Reconocimiento de Voz)

1. Tipos de servicio admitidos

Cherry Studio admite tres tipos de servicios ASR:

- OpenAI: Usa el modelo Whisper de OpenAI, requiere clave de API
- Navegador: Usa reconocimiento de voz integrado del navegador, gratuito sin configuración
- Servidor local: Conecta con servidor WebSocket local para reconocimiento de voz

2. Método de configuración

1) Ingresa a la página de configuración, selecciona "Funciones de Voz"
2) En la subpestaña "ASR":
   - Habilita la función ASR (activa el interruptor)
   - Selecciona tipo de servicio ASR
   - Configura parámetros según el servicio:
     - OpenAI: Clave API, dirección API, modelo
     - Navegador: Sin configuración adicional
     - Servidor local: Opción para iniciar automáticamente al abrir la aplicación
   - Selecciona idioma de reconocimiento (predeterminado: chino)
3) Haz clic en "Probar ASR" para verificar configuración

3. Método de uso

- Al habilitar ASR, aparecerá un botón de micrófono junto al campo de entrada
- Haz clic para comenzar a grabar
- El habla se convierte a texto en el campo de entrada
- Vuelve a hacer clic para detener la grabación
- Admite reconocimiento continuo con modo de acumulación

IV. Función de Llamadas de Voz

1. Características

- Combina TTS y ASR para diálogos de voz estilo ChatGPT
- Interfaz flotante arrastrable
- Modo de pulsación prolongada para hablar
- Personalización de atajos de teclado
- Ventana plegable
- Selección de modelo dedicado
- Indicadores personalizables

2. Configuración

1) Ingresa a Configuración > Funciones de Voz
2) En subpestaña "Función de Llamada":
   - Activa función de llamada de voz
   - Selecciona modelo IA para llamadas
   - Personaliza indicadores (opcional)
   - Guarda o restaura indicadores predeterminados

3. Uso

1) Haz clic en el ícono de teléfono en el chat
2) Se abrirá ventana de llamada con saludo de voz
3) Mantén presionado "Pulsar para hablar" (o usa atajo)
4) Suelta para enviar grabación
5) La IA responde mediante TTS
6) Controles de ventana:
   - Silenciar/reanudar TTS
   - Pausar/continuar diálogo
   - Configurar atajos
   - Plegar ventana
7) Cierra para finalizar llamada

4. Configuración de atajos

1) Haz clic en ⚙️ en ventana de llamada
2) Selecciona "Atajos"
3) Presiona tecla deseada (espacio, Shift, etc.)
4) Guarda configuración
5) Mantén presionada la tecla para grabar, suelta para enviar

V. Problemas Comunes y Soluciones

1. Problemas con TTS

- Sin sonido: Verifica habilitación TTS y parámetros
- Calidad baja: Prueba diferentes servicios/voces
- Errores: Verifica clave API y conexión

2. Problemas con ASR

- Sin reconocimiento: Verifica configuración ASR
- Baja precisión: Cambia servicio o ajusta micrófono
- Error de conexión: Reinicia aplicación/servidor

3. Problemas con llamadas

- Ventana no abre: Verifica habilitación y config. TTS/ASR
- Sin respuesta al pulsar: Verifica permisos de micrófono
- Sin salida de voz: Verifica TTS habilitado y no silenciado

VI. Configuración Avanzada

1. TTS avanzado
- Filtros: Procesos de pensamiento, Markdown, código
- Barra de progreso personalizable
- Voces y modelos personalizados

2. ASR avanzado
- Inicio automático de servidor
- Selección de idioma

3. Llamadas avanzadas
- Indicadores personalizados
- Selección de modelo dedicado
- Atajos personalizados

VII. Recomendaciones de Uso

1. Selección TTS:
   - Alta calidad: OpenAI o Siliconflow
   - Sin configuración: TTS de navegador o gratuito

2. Selección ASR:
   - Alta precisión: OpenAI
   - Sin configuración: Reconocimiento de navegador

3. Optimización de llamadas:
   - Usa auriculares para evitar eco
   - Ambientes silenciosos mejoran precisión
   - Indicadores personalizados para respuestas optimizadas

4. Configuración flexible:
   - Solo TTS para enfoque en texto
   - Solo ASR para entrada por voz
   - Función completa para diálogos completos

¡Esperamos que esta guía te ayude a aprovechar al máximo las funciones de voz de Cherry Studio para una experiencia de IA más natural!
```