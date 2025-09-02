# LLM Arena Leaderboard (Actualización en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Este es un ranking basado en datos de Chatbot Arena (lmarena.ai), generado mediante un proceso automatizado.

> **Fecha de actualización de los datos**: 2025-09-02 11:41:04 UTC / 2025-09-02 19:41:04 CST (Hora de Pekín)

{% hint style="info" %}
Haz clic en el **nombre del modelo** en la clasificación para ir a su página de detalles o prueba.
{% endhint %}

## Clasificación

| Ranking(UB) | Ranking(StyleCtrl) | Modelo                                                                                                                             | Puntuación | Intervalo confianza | Votos       | Proveedor                     | Licencia                   | Fecha conocimiento |
|:------------|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:-----------|:--------------------|:------------|:------------------------------|:---------------------------|:-------------------|
| 1           | 1                  | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470       | +5/-5               | 26,019      | Google                        | Propietaria             | nan                |
| ...         | ...                | ...                                                                                                                                 | ...        | ...                 | ...         | ...                           | ...                        | ...                |
| 266         | 264                | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   | 840        | +16/-16             | 2,446       | Meta                          | Sin fines comerciales      | 2023/2             |

## Explicación

- **Ranking(UB)**: Clasificación calculada basada en el modelo Bradley-Terry. Refleja el rendimiento integral del modelo en la arena, proporcionando una estimación del **límite superior** de su puntuación Elo para entender su competitividad potencial.
- **Ranking(StyleCtrl)**: Clasificación después de aplicar control de estilo conversacional. Busca reducir el sesgo por preferencias de estilo de respuesta (ej. verbosidad, concisión) para evaluar mejor las capacidades fundamentales.
- **Modelo**: Nombre del modelo de lenguaje grande (LLM). Incluye enlaces a recursos relacionados; haz clic para acceder.
- **Puntuación**: Evaluación Elo obtenida mediante votación de usuarios en la arena. Un valor más alto indica mejor rendimiento. Cambia dinámicamente según el entorno competitivo actual.
- **Intervalo confianza**: Intervalo de confianza del 95% de la puntuación Elo (ej: `+6/-6`). Intervalos más pequeños indican mayor estabilidad; valores grandes sugieren datos insuficientes o rendimiento variable.
- **Votos**: Número total de votos recibidos por el modelo. Más votos suelen indicar mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que ofrece el modelo.
- **Licencia**: Tipo de licencia del modelo (Propietaria, Apache 2.0, MIT, etc.).
- **Fecha conocimiento**: Fecha de corte del conocimiento en datos de entrenamiento. **Datos no disponibles** indica información desconocida o no proporcionada.

## Fuente y frecuencia de actualización

Los datos de este ranking son generados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa información de [lmarena.ai](https://lmarena.ai/). Este ranking se actualiza diariamente mediante GitHub Actions.

## Exención de responsabilidad

Este informe es solo para referencia. Las clasificaciones son dinámicas y se basan en votos de preferencia de usuarios en Chatbot Arena durante períodos específicos. La completitud y precisión dependen de las fuentes originales y del procesamiento en `fboulnois/llm-leaderboard-csv`. Diferentes modelos pueden tener licencias distintas; consulte siempre las especificaciones oficiales de los proveedores.