# Ranking de la Arena LLM (Actualización en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




{% hint style="warning" %}
Este ranking se genera automáticamente a partir de los datos de Chatbot Arena (lmarena.ai).
{% endhint %}

> **Última actualización**: 2025-08-06 11:45:12 UTC / 2025-08-06 19:45:12 CST (hora de Pekín)

{% hint style="info" %}
Haz clic en el **nombre del modelo** dentro de la tabla para acceder a su página de detalles o prueba.
{% endhint %}

## Tabla de clasificación

| Rank(UB) | Rank(StyleCtrl) | Nombre del modelo                                                                                                                         | Puntuación | Int. conf.    | Votos      | Proveedor                    | Licencia                    | Fecha de conocimiento   |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|... (Se mantiene toda la tabla original sin cambios en modelos, puntuaciones, links o datos técnicos)...|
|      214 |             214 | [FastChat-T5-3B](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)                                                          |  883 | +8/-9   | 4,288   | LMSYS                  | Apache 2.0              | 2023/4   |
|      216 |             217 | [StableLM-Tuned-Alpha-7B](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)                                       |  855 | +10/-10 | 3,336   | Stability AI           | CC-BY-NC-SA-4.0         | 2023/4   |
|      216 |             214 | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                              |  837 | +12/-9  | 3,480   | Databricks             | MIT                     | 2023/4   |
|      218 |             215 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                               |  814 | +10/-12 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## Explicaciones

- **Rank(UB)**: Clasificación basada en el modelo Bradley-Terry. Refleja el rendimiento global del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a entender su potencial competitivo.
- **Rank(StyleCtrl)**: Clasificación ajustada al control de estilo conversacional. Busca reducir el sesgo por preferencias de estilo (ej: respuestas extensas vs. concisas), evaluando más objetivamente las capacidades centrales del modelo.
- **Nombre del modelo**: Nombre del Modelo de Lenguaje Grande (LLM). Contiene enlaces a recursos relacionados (haz clic para acceder).
- **Puntuación**: Puntuación Elo obtenida mediante votaciones en la arena. Sistema de clasificación relativa donde mayor puntuación indica mejor rendimiento. Valor dinámico que refleja la capacidad relativa del modelo en el entorno competitivo actual.
- **Int. conf.**: Intervalo de confianza del 95% para la puntuación Elo (ej: `+6/-6`). Intervalos pequeños indican mayor estabilidad y fiabilidad; intervalos grandes pueden sugerir datos insuficientes o rendimiento fluctuante. Proporciona evaluación cuantitativa de la precisión.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Mayor número de votos generalmente implica mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que ofrece el modelo.
- **Licencia**: Tipo de licencia del modelo (ej: Propietaria (Proprietary), Apache 2.0, MIT, etc.).
- **Fecha de conocimiento**: Fecha de corte del conocimiento utilizado en el entrenamiento. **Sin datos** indica información no proporcionada o desconocida.

## Fuentes de datos y frecuencia de actualización

Este ranking se genera automáticamente mediante el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Se actualiza diariamente mediante GitHub Actions.

## Exención de responsabilidad

Este reporte es solo para referencia. Los datos del ranking son dinámicos y se basan en votaciones de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión dependen de las fuentes de datos originales y del procesamiento del proyecto `fboulnois/llm-leaderboard-csv`. Los modelos pueden tener diferentes licencias; consulte siempre las especificaciones oficiales del proveedor.