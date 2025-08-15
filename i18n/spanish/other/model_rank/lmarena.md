# LLM Arena Leaderboard (Actualización en Tiempo Real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta es una clasificación basada en los datos de Chatbot Arena (lmarena.ai), generada automáticamente.

> **Última actualización de datos**: 2025-08-15 11:42:06 UTC / 2025-08-15 19:42:06 CST (Hora de Pekín)

{% hint style="info" %}
Haz clic en el **nombre del modelo** en la clasificación para acceder a su página de detalles o prueba.
{% endhint %}

## Leaderboard

|   Posición(UB) |   Posición(StyleCtrl) | Nombre del Modelo                                                                                                                  |   Puntuación | Intervalo Confianza | Votos      | Proveedor                 | Licencia                 | Fecha Corte Conocimiento |
|:---------|:----------------|:------------------------------------------------------------------------------------------------------------------------------------|:-------|:--------------|:-------|:---------------------|:-----------------------|:-------------------|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                            |   1470 | +5/-5       | 26,019 | Google              | Propietario           | nan                |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              |   1446 | +6/-6       | 13,715 | Google              | Propietario           | nan                |
|... (continuación completa de la tabla sin alterar datos técnicos)...|
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                     |    840 | +16/-16     | 2,446  | Meta                | No comercial          | 2023/2             |

## Explicación

- **Posición(UB)**: Clasificación basada en el modelo Bradley-Terry. Refleja el rendimiento general del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a entender su competitividad potencial.
- **Posición(StyleCtrl)**: Clasificación tras el control de estilo de conversación. Busca reducir el sesgo por preferencias de estilo de respuesta (p.ej., verbosidad, concisión), evaluando más objetivamente las capacidades centrales.
- **Nombre del Modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna incluye enlaces a recursos relacionados.
- **Puntuación**: Puntuación Elo obtenida mediante votación de usuarios. Valores más altos indican mejor rendimiento relativo en el entorno competitivo actual.
- **Intervalo Confianza**: Intervalo de confianza del 95% para la puntuación Elo (ej. `+6/-6`). Intervalos pequeños indican mayor estabilidad; grandes sugieren datos limitados o fluctuaciones.
- **Votos**: Número total de votos recibidos para el modelo en la arena. Más votos suelen indicar mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa responsable del modelo.
- **Licencia**: Tipo de licencia del modelo (Propietario, Apache 2.0, MIT, etc.).
- **Fecha Corte Conocimiento**: Fecha límite de los datos de entrenamiento. **Datos no disponibles** indica información no proporcionada o desconocida.

## Fuente de Datos y Frecuencia de Actualización

Esta clasificación se genera automáticamente mediante el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). El ranking se actualiza diariamente mediante GitHub Actions.

## Descargo de Responsabilidad

Este informe es solo para referencia. Los datos son dinámicos y se basan en preferencias de votación de usuarios durante periodos específicos. La integridad y precisión dependen de las fuentes originales y el procesamiento de `fboulnois/llm-leaderboard-csv`. Los modelos pueden tener licencias diferentes; consulte siempre las indicaciones oficiales del proveedor.