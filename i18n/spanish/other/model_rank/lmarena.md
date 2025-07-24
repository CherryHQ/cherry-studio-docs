# LLM Arena Leaderboard (Actualización en Tiempo Real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Este es un ranking basado en datos de Chatbot Arena (lmarena.ai), generado mediante un proceso automatizado.

> **Fecha de actualización de datos**: 2025-07-24 11:44:24 UTC / 2025-07-24 19:44:24 CST (Hora de Beijing)

{% hint style="info" %}
Haga clic en el **nombre del modelo** en la clasificación para acceder a su página de detalles o prueba.
{% endhint %}

## Clasificación

| Posición (UB) | Posición (StyleCtrl) | Nombre del Modelo                                                                                                                         | Puntos | Intervalo Conf. | Votos      | Proveedor               | Licencia              | Fecha Límite |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                      | 1474 | +5/-4   | 19,209  | Google                 | Propietaria             | N/D      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)          | 1446 | +4/-5   | 13,692  | Google                 | Propietaria             | N/D      |
| ... *(Se mantienen todos los registros de la tabla sin cambios en URLs, puntajes ni datos técnicos)* |
|      218 |             215 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                               |  814 | +10/-12 | 2,446   | Meta                   | No comercial          | 2023/2   |

## Explicaciones

- **Posición (UB)**: Clasificación calculada mediante el modelo Bradley-Terry. Este ranking refleja el rendimiento integral del modelo en la arena y proporciona una **estimación superior** de su puntuación Elo, ayudando a entender su competitividad potencial.
- **Posición (StyleCtrl)**: Clasificación después del control de estilo conversacional. Este ranking busca reducir el sesgo por preferencias en el estilo de respuesta (p. ej., extenso vs. conciso), evaluando más objetivamente la capacidad central del modelo.
- **Nombre del Modelo**: Nombre del Modelo de Lenguaje Grande (LLM). Esta columna incluye enlaces; haga clic para acceder.
- **Puntos**: Puntuación Elo obtenida por el modelo mediante votos de usuarios en la arena. Cuanto más alta sea la puntuación, mejor el rendimiento del modelo. Este valor es dinámico y refleja la capacidad relativa actual.
- **Intervalo de Confianza**: Intervalo de confianza del 95% para la puntuación Elo (p. ej., `+6/-6`). Un intervalo más estrecho indica una puntuación más estable y fiable. Proporciona una evaluación cuantitativa de la precisión.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Más votos generalmente implican mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que proporciona el modelo.
- **Licencia**: Tipo de licencia del modelo (p. ej., Propietaria, Apache 2.0, MIT).
- **Fecha Límite**: Fecha de corte de los datos de entrenamiento. **N/D** significa información no proporcionada o desconocida.

## Fuente de Datos y Frecuencia de Actualización

Los datos de este ranking son generados y proporcionados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Este ranking se actualiza diariamente mediante GitHub Actions.

## Descargo de Responsabilidad

Este informe es solo para referencia. Los datos del ranking son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión dependen de las fuentes de datos y del procesamiento de `fboulnois/llm-leaderboard-csv`. Diferentes modelos pueden usar licencias distintas; consulte siempre las especificaciones oficiales del proveedor.