---
hidden: true
icon: phone-arrow-up-right
---

# Funciones de voz

{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

```markdown
# Funciones de voz

```

Cherry Studio Guía de uso de funciones de voz

I. Descripción general de funciones de voz

Cherry Studio proporciona tres módulos principales de funciones de voz: TTS (texto a voz), ASR (reconocimiento de voz) y llamadas de voz. Estas funcionalidades permiten interactuar de forma natural con la IA mediante voz, mejorando la experiencia de usuario.

* TTS (texto a voz): Convierte las respuestas de texto de la IA en salida de voz
* ASR (reconocimiento de voz): Transcribe tu voz en texto de entrada
* Llamadas de voz: Combina TTS y ASR para ofrecer una experiencia de diálogo vocal similar a ChatGPT

II. Función TTS (texto a voz)

1. Tipos de servicios admitidos

Cherry Studio admite cuatro tipos de servicios TTS:

* OpenAI: Utiliza la API TTS de OpenAI, requiere clave API
* TTS de navegador: Usa la síntesis de voz incorporada del navegador, gratuita sin configuración
* Siliconflow: Utiliza el servicio TTS de Siliconflow, requiere clave API
* TTS online gratuito: Usa servicios TTS gratuitos en línea, sin clave API

2. Métodos de configuración
3. Ingrese a la página de ajustes, seleccione la pestaña "Funciones de voz"
4. En la subpestaña "TTS":
   * Active la función TTS (habilitar interruptor)
   * Seleccione el tipo de servicio TTS
   * Configure parámetros según el servicio elegido:
     * OpenAI: Ingrese clave API, dirección API, seleccione voz y modelo
     * TTS de navegador: Seleccione voz
     * Siliconflow: Ingrese clave API, dirección API, seleccione voz, modelo, formato de respuesta y velocidad
     * TTS online gratuito: Seleccione voz y formato de salida
5. Configure filtros TTS (opcional):
   * Filtrar procesos de pensamiento
   * Filtrar etiquetas Markdown
   * Filtrar bloques de código
6. Establezca si mostrar barra de progreso de TTS
7. Haga clic en "Probar TTS" para verificar la configuración
8. Métodos de uso

* Con TTS activado, las respuestas de la IA se convertirán automáticamente en voz
* En la interfaz de chat, cada respuesta de IA mostrará un botón de reproducción TTS
* Haga clic en el botón para reproducir/pausar el audio
* Si está habilitada, se mostrará una barra de progreso bajo el texto
* Textos largos se sintetizan y reproducen en segmentos continuos

III. Función ASR (reconocimiento de voz)

1. Tipos de servicios admitidos

Cherry Studio admite tres tipos de servicios ASR:

* OpenAI: Utiliza el modelo Whisper de OpenAI, requiere clave API
* Navegador: Usa el reconocimiento de voz integrado del navegador, gratuito sin configuración
* Servidor local: Se conecta a un servidor WebSocket local para reconocimiento de voz

2. Métodos de configuración
3. Ingrese a la página de ajustes, seleccione la pestaña "Funciones de voz"
4. En la subpestaña "ASR":
   * Active la función ASR (habilitar interruptor)
   * Seleccione el tipo de servicio ASR
   * Configure parámetros según el servicio elegido:
     * OpenAI: Ingrese clave API, dirección API, seleccione modelo
     * Navegador: Sin configuración adicional
     * Servidor local: Puede configurar inicio automático del servidor ASR al iniciar la app
   * Seleccione idioma de reconocimiento (predeterminado: chino)
5. Haga clic en "Probar ASR" para verificar la configuración
6. Métodos de uso

* Con ASR activado, aparecerá un botón de micrófono junto al campo de entrada
* Haga clic en el botón para iniciar grabación
* Al hablar, su voz se transcribirá en texto automáticamente
* Haga clic nuevamente para detener la grabación
* Soporta reconocimiento continuo en modo acumulativo

IV. Función de llamadas de voz

1. Características principales

* Combina TTS y ASR para diálogos tipo ChatGPT
* Interfaz en ventana flotante arrastrable
* Soporta modo "mantener pulsado para hablar"
* Atajos personalizables
* Ventana plegable
* Selección de modelos especializados para voz
* Indicadores personalizados

2. Métodos de configuración
3. Ingrese a la página de ajustes, seleccione la pestaña "Funciones de voz"
4. En la subpestaña "Funciones de llamada":
   * Active la función de llamadas (habilitar interruptor)
   * Haga clic en "Seleccionar modelo" para elegir modelo de IA para llamadas
   * Personalice indicadores en el campo de texto (opcional)
   * Haga clic en "Guardar" para guardar cambios o "Restablecer" para valores predeterminados
5. Métodos de uso
6. En la interfaz de chat, haga clic en el ícono de teléfono junto al campo de entrada
7. Se abrirá una ventana de llamada reproduciendo un saludo
8. Mantenga pulsado "Mantener para hablar" para grabar (o use atajos)
9. Suelte para enviar el audio a la IA
10. La IA generará una respuesta y la leerá mediante TTS
11. Controles en la ventana:
    * Mute/Unmute: Controla salida de TTS
    * Pausar/Reanudar: Controla el flujo de conversación
    * Configuración: Personaliza atajos
    * Plegar: Minimiza la ventana
12. Haga clic en Cerrar para finalizar la llamada
13. Configuración de atajos
14. En la ventana de llamada, haga clic en Configuración
15. En el panel, haga clic en Atajos
16. Pulse la tecla deseada (Ej: Espacio, Shift)
17. Haga clic en "Guardar"
18. Al usar: mantenga presionada la tecla para grabar, suelte para enviar

V. Problemas comunes y soluciones

1. Problemas con TTS

* Problema: Sin sonido en TTS\
  Solución: Verifique activación TTS, configuración de servicio y parámetros obligatorios
* Problema: Calidad de audio deficiente\
  Solución: Pruebe diferentes servicios o voces
* Problema: Mensajes de error durante reproducción\
  Solución: Verifique clave API y conexión a internet

2. Problemas con ASR

* Problema: ASR no detecta voz\
  Solución: Verifique activación ASR y parámetros de servicio
* Problema: Baja precisión en reconocimiento\
  Solución: Pruebe servicios alternativos o ajuste micrófono
* Problema: Conexión fallida con servidor\
  Solución: Verifique estado del servidor local o reinicie la app

3. Problemas con llamadas de voz

* Problema: Ventana no se abre\
  Solución: Verifique funciones TTS/ASR activas y configuradas
* Problema: Sin respuesta al mantener pulsado\
  Solución: Verifique permisos de micrófono o reinicie llamada
* Problema: Sin salida de voz en respuestas\
  Solución: Verifique TTS activado y no silenciado

VI. Configuraciones avanzadas

1. TTS avanzado

* Filtros: Excluye procesos de pensamiento, Markdown o bloques de código
* Barra de progreso: Activa/desactiva visualización
* Voces y modelos personalizados

2. ASR avanzado

* Inicio automático de servidor: Activa al iniciar app
* Selección de idioma: Admite múltiples idiomas

3. Llamadas avanzadas

* Indicadores personalizados: Guían respuestas de IA en modo voz
* Modelo dedicado: Selección independiente del modelo de chat
* Atajos personalizados: Configuración personalizada de teclas

VII. Recomendaciones

1. Para TTS:
   * Calidad premium: OpenAI o Siliconflow
   * Sin configuración: TTS de navegador o servicios gratuitos
2. Para ASR:
   * Máxima precisión: OpenAI
   * Sin configuración: Reconocimiento del navegador
3. Optimización de llamadas:
   * Use auriculares para evitar eco
   * Ambientes silenciosos mejoran precisión
   * Indicadores personalizados mejoran respuestas orales
4. Ajuste según necesidades:
   * Solo salida de voz: Active solo TTS
   * Solo entrada de voz: Active solo ASR
   * Diálogo completo: Active funciones de llamada

¡Este manual le ayudará a aprovechar las funciones de voz de Cherry Studio para una experiencia de IA más natural y fluida!

```
```
