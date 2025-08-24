---
hidden: True
icon: phone-arrow-up-right
---
# Funcionalidad de Voz


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




{% hint style="warning" %}
Esta función está en pausa porque el desarrollador relevante no continuó manteniendo el PR.
{% endhint %}

Guía de uso de la funcionalidad de voz de Cherry Studio

## 1. Resumen de la funcionalidad de voz

Cherry Studio ofrece tres módulos principales de funcionalidad de voz: TTS (Texto a Voz), ASR (Reconocimiento de Voz) y Llamadas de Voz. Estas características le permiten interactuar de forma natural con la IA mediante voz, mejorando su experiencia de usuario.

- **TTS (Texto a Voz)**: Convierte las respuestas de la IA en salida de voz
- **ASR (Reconocimiento de Voz)**: Convierte su voz en texto
- **Llamadas de Voz**: Combina TTS y ASR para una experiencia conversacional similar a ChatGPT

## 2. Función TTS (Texto a Voz)

### 2.1 Servicios compatibles

Cherry Studio soporta cuatro tipos de servicios TTS:

- **OpenAI**: Utiliza la API TTS de OpenAI, requiere clave API
- **Navegador TTS**: Usa la síntesis de voz integrada del navegador, gratuito sin configuración
- **Siliconflow**: Utiliza el servicio TTS de Siliconflow, requiere clave API
- **TTS Online Gratuito**: Servicio TTS online gratuito, sin clave API

### 2.2 Método de configuración

1) Ingrese a Configuración > Pestaña "Funcionalidad de voz"
2) En la subpestaña "TTS":
   - Active TTS (alternar ON)
   - Seleccione tipo de servicio TTS
   - Configure parámetros según el servicio:
     - **OpenAI**: Clave API, dirección API, voz, modelo
     - **Navegador TTS**: Seleccione voz
     - **Siliconflow**: Clave API, dirección API, voz, modelo, formato de respuesta, velocidad
     - **TTS Online Gratuito**: Voz y formato de salida
3) Opciones de filtro TTS (opcional):
   - Filtrar procesos de pensamiento
   - Filtrar marcas Markdown
   - Filtrar bloques de código
4) Configure si mostrar barra de progreso TTS
5) Haga clic en "Probar TTS" para verificar la configuración

### 2.3 Modo de uso

- Las respuestas de IA se convierten automáticamente en voz
- Botones de reproducción aparecen bajo cada respuesta
- Haga clic para reproducir/pausar
- La barra de progreso muestra avance (si está activa)
- Textos largos se sintetizan y reproducen en segmentos

## 3. Función ASR (Reconocimiento de Voz)

### 3.1 Servicios compatibles

- **OpenAI**: Usa modelo Whisper de OpenAI, requiere clave API
- **Navegador**: Función integrada del navegador, gratuito sin configuración
- **Servidor Local**: Conexión a servidor WebSocket local

### 3.2 Método de configuración

1) Configuración > Pestaña "Funcionalidad de voz"
2) Subpestaña "ASR":
   - Active ASR (alternar ON)
   - Seleccione tipo de servicio ASR
   - Configure parámetros según servicio:
     - **OpenAI**: Clave API, dirección API, modelo
     - **Navegador**: Sin configuración adicional
     - **Servidor Local**: Opción para iniciar automáticamente al abrir aplicación
   - Seleccione idioma de reconocimiento (predeterminado: chino)
3) Haga clic en "Probar ASR" para verificar

### 3.3 Modo de uso

- Botón de micrófono aparece junto al campo de entrada
- Haga clic para iniciar grabación
- Al hablar, el texto aparece en campo de entrada
- Vuelva a hacer clic para detener grabación
- Soporta reconocimiento continuo con modo acumulativo

## 4. Función de Llamadas de Voz

### 4.1 Características clave

- Experiencia conversacional tipo ChatGPT con TTS + ASR
- Ventana flotante arrastrable
- Modo "Mantener pulsado para hablar"
- Personalización de atajos de teclado
- Ventana colapsable
- Modelos especializados para llamadas
- Indicaciones personalizadas

### 4.2 Configuración

1) Configuración > Pestaña "Funcionalidad de voz"
2) Subpestaña "Llamadas":
   - Active llamadas de voz (alternar ON)
   - Haga clic en "Seleccionar modelo" para elegir IA conversacional
   - Personalice indicaciones en el cuadro de texto (opcional)
   - Guarde o restaure indicaciones predeterminadas

### 4.3 Modo de uso

1) Haga clic en el ícono de teléfono en el chat
2) Se abre ventana de llamada con saludo de voz
3) Mantenga pulsado "Mantener para hablar" (o use atajo)
4) Suelte para enviar grabación a la IA
5) La IA responde mediante TTS
6) Controles de ventana:
   - Silenciar/Activar sonido
   - Pausar/Reanudar conversación
   - Configurar atajos
   - Colapsar ventana
7) Cierre para finalizar llamada

### 4.4 Configuración de atajos

1) En ventana de llamada > ícono de ajustes
2) Panel de configuraciones > botón "Atajos"
3) Presione tecla deseada (ej: Espacio, Shift)
4) Guarde configuración
5) Use: Mantenga tecla para grabar, suelte para enviar

## 5. Problemas comunes y soluciones

### 5.1 Problemas TTS
- **Sin sonido**: Verifique activación TTS y parámetros
- **Calidad deficiente**: Cambie servicio o voz
- **Errores**: Revise clave API y conexión de red

### 5.2 Problemas ASR
- **Sin reconocimiento**: Active ASR y revise parámetros
- **Baja precisión**: Cambie servicio o ajuste micrófono
- **Error de conexión**: Verifique servidor local o reinicie app

### 5.3 Problemas de llamadas
- **Ventana no abre**: Active función y revise TTS/ASR
- **Sin respuesta al grabar**: Verifique permisos de micrófono
- **Sin voz en respuestas**: Active TTS y verifique silencio

## 6. Configuración avanzada

### 6.1 TTS avanzado
- Filtrado: Procesos de pensamiento, Markdown, código
- Barra de progreso personalizable
- Voces y modelos personalizados

### 6.2 ASR avanzado
- Inicio automático de servidor
- Selección de idioma

### 6.3 Llamadas avanzadas
- Indicaciones personalizadas
- Modelos dedicados
- Personalización de atajos

## 7. Recomendaciones de uso

### 7.1 Selección de TTS
- **Alta calidad**: OpenAI o Siliconflow
- **Sin configuración**: TTS de Navegador o Online Gratuito

### 7.2 Selección de ASR
- **Alta precisión**: OpenAI
- **Sin configuración**: Navegador

### 7.3 Optimización de llamadas
- Use auriculares para evitar eco
- Ambientes silenciosos mejoran reconocimiento
- Indicaciones personalizadas optimizan respuestas

### 7.4 Ajustes según necesidades
- **Principalmente texto**: Active solo TTS
- **Principalmente voz**: Active solo ASR
- **Conversación completa**: Active llamadas de voz

¡Esperamos que esta guía le ayude a aprovechar al máximo las funcionalidades de voz de Cherry Studio para una experiencia de IA más natural e intuitiva!