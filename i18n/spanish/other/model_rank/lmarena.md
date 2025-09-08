# LLM Arena Leaderboard (Updated in Real Time)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




This leaderboard is based on Chatbot Arena (lmarena.ai) data and generated through an automated process.

> **Last Updated**: 2025-09-08 11:40:35 UTC / 2025-09-08 19:40:35 CST (Beijing Time)

{% hint style="info" %}
Click the **model name** in the leaderboard to jump to its details or trial page.
{% endhint %}

## Leaderboard

| Rank(UB) | Rank(StyleCtrl) | Model name                                                                                                                             | Score | Confidence Interval | Votes     | Provider                   | License                       | Knowledge Cutoff |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Same values as original – maintain numerical data URLs license names unchanged |

## Explicación

- **Rank(UB)**: Ranking basado en el modelo Bradley-Terry. Esta clasificación refleja el rendimiento integral del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su competitividad potencial.
- **Rank(StyleCtrl)**: Clasificación después de aplicar el control de estilo conversacional. Su objetivo es reducir el sesgo de preferencia causado por el estilo de respuesta del modelo (p.ej. verbosidad o concisión), evaluando de forma más pura su capacidad central.
- **Model name**: Nombre del Gran Modelo de Lenguaje (LLM). Esta columna contiene enlaces a información relacionada.
- **Score**: Puntuación Elo obtenida por el modelo mediante votación de usuarios en la arena. El sistema Elo clasifica relativamente; una puntuación más alta indica mejor rendimiento. Es dinámica y refleja la capacidad relativa del modelo en el entorno competitivo actual.
- **Confidence Interval**: Intervalo de confianza del 95% para la puntuación Elo (ej. `+6/-6`). Un intervalo menor indica mayor estabilidad y fiabilidad; uno mayor sugiere datos insuficientes o rendimiento volátil. Cuantifica la precisión de la puntuación.
- **Votes**: Número total de votos recibidos por el modelo. Más votos usualmente implican mayor fiabilidad estadística.
- **Provider**: Organización o compañía que provee el modelo.
- **License**: Tipo de licencia del modelo, p.ej. Propietaria (Proprietary), Apache 2.0, MIT, etc.
- **Knowledge Cutoff**: Fecha de actualización de datos de entrenamiento del modelo. **暂无数据** indica información no disponible.

## Fuentes y Frecuencia de Actualización

Los datos de este ranking son generados automáticamente por [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), proyecto que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). La lista se actualiza diariamente mediante GitHub Actions.

## Exención de Responsabilidad

Este reporte es solo para referencia. Los datos del ranking son dinámicos y se basan en votaciones de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión dependen de fuentes de datos superiores y del procesamiento de `fboulnois/llm-leaderboard-csv`. Los modelos pueden tener acuerdos de licencia diferentes; consulte siempre las especificaciones oficiales de los proveedores.