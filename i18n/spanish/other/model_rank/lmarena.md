# Tabla de clasificación LLM Arena (actualizada en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta es una tabla de clasificación basada en datos de Chatbot Arena (lmarena.ai), generada mediante un proceso automatizado.

> **Fecha de actualización de datos**: 2025-08-16 11:40:33 UTC / 2025-08-16 19:40:33 CST (hora de Pekín)

{% hint style="info" %}
Haga clic en el **nombre del modelo** en la tabla de clasificación para ir a su página de detalles o prueba.
{% endhint %}

## Tabla de clasificación

| Posición(UB) | Posición(StyleCtrl) | Nombre del modelo                                                                                                               | Puntuación | Intervalo de confianza | Votos     | Proveedor               | Licencia                | Fecha límite de conocimiento |
|:-------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------|:----------|:----------------------|:---------|:-----------------------|:-----------------------|:-----------------------------|
| 1            | 1                  | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470      | +5/-5                 | 26,019   | Google                 | Proprietary            | nan                          |
| 2            | 2                  | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446      | +6/-6                 | 13,715   | Google                 | Proprietary            | nan                          |
| 3            | 2                  | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                             | 1434      | +9/-9                 | 4,112    | Z.ai                   | MIT                    | nan                          |
| 4            | 2                  | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                         | 1434      | +6/-6                 | 13,058   | xAI                    | Proprietary            | nan                          |
| 5            | 3                  | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                | 1429      | +4/-4                 | 30,777   | OpenAI                 | Proprietary            | nan                          |
| ...          | ...                | ...                                                                                                                             | ...       | ...                   | ...      | ...                    | ...                    | ...                          |
| 264          | 263                | [StableLM-Tuned-Alpha-7B](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)                                           | 873       | +12/-12               | 3,336    | Stability AI           | CC-BY-NC-SA-4.0        | 2023/4                       |
| 265          | 263                | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                                   | 857       | +13/-13               | 3,480    | Databricks             | MIT                    | 2023/4                       |
| 266          | 264                | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                    | 840       | +16/-16               | 2,446    | Meta                   | Non-commercial         | 2023/2                       |

## Explicaciones

- **Posición(UB)**: Clasificación calculada basada en el modelo Bradley-Terry. Esta clasificación refleja el rendimiento integral del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender la competitividad potencial del modelo.
- **Posición(StyleCtrl)**: Clasificación después del control del estilo de conversación. Esta clasificación tiene como objetivo reducir el sesgo de preferencia causado por estilos de respuesta del modelo (por ejemplo, extenso o conciso), evaluando más puramente las capacidades básicas del modelo.
- **Nombre del modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna ya contiene enlaces relacionados con el modelo, haga clic para ir.
- **Puntuación**: Puntuación Elo del modelo obtenida a través de votos de usuarios en la arena. El puntaje Elo es un sistema de clasificación relativa donde puntajes más altos indican mejor rendimiento. Esta puntuación es dinámica y refleja la fuerza relativa del modelo en el entorno competitivo actual.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo del modelo (por ejemplo: `+6/-6`). Un intervalo más pequeño indica que la puntuación es más estable y confiable; por el contrario, un intervalo más grande puede significar datos insuficientes o mayor fluctuación. Proporciona una evaluación cuantitativa de la precisión de la puntuación.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Más votos generalmente significan mayor confiabilidad estadística de su puntuación.
- **Proveedor**: Organización o empresa que proporciona este modelo.
- **Licencia**: Tipo de licencia del modelo, como propiedad (Proprietary), Apache 2.0, MIT, etc.
- **Fecha límite de conocimiento**: Fecha límite de conocimiento de los datos de entrenamiento del modelo. **Sin datos** indica que la información relevante no está disponible o es desconocida.

## Fuente de datos y frecuencia de actualización

Los datos de esta tabla de clasificación se generan y proporcionan automáticamente mediante el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Esta clasificación se actualiza automáticamente todos los días mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos de la tabla de clasificación son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante un período específico. La integridad y precisión de los datos dependen de las fuentes originales aguas arriba y del procesamiento del proyecto `fboulnois/llm-leaderboard-csv`. Diferentes modelos pueden tener diferentes licencias, consulte siempre las instrucciones oficiales del proveedor del modelo.