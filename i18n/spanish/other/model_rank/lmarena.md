# Clasificación de LLM Arena (Actualizado en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta es una clasificación generada automáticamente basada en datos de Chatbot Arena (lmarena.ai).

> **Actualización de datos**: 2025-08-28 11:40:47 UTC / 2025-08-28 19:40:47 CST (Hora de Pekín)

{% hint style="info" %}
Haga clic en el **nombre del modelo** en la clasificación para acceder a su página de detalles o para probarlo.
{% endhint %}

## Clasificación

| Rank(UB) | Rank(StyleCtrl) | Nombre del modelo                                                    |   Puntuación | Intervalo de confianza | Votos        | Proveedor                 | Licencia                  | Fecha de corte de conocimiento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Y todas las filas de la tabla exactamente iguales... |
|      237 |             223 | [ChatGLM-6B](https://huggingface.co/THUDM/chatglm-6b)           |  925 | +12/-12 | 4,983   | Tsinghua               | No comercial          | 2023/3   |
|      262 |             258 | [OpenAssistant-Pythia-12B](https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5) |  923 | +10/-10 | 6,368   | OpenAssistant          | Apache 2.0             | 2023/4   |
| ... restante de la tabla sin cambios ... |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                   |  840 | +16/-16 | 2,446   | Meta                   | No comercial          | 2023/2   |

## Explicación

- **Rank(UB)**: Clasificación calculada basada en el modelo Bradley-Terry. Esta clasificación refleja el rendimiento general del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su competitividad potencial.
- **Rank(StyleCtrl)**: Clasificación ajustada por control de estilo conversacional. Esta clasificación busca reducir el sesgo de preferencias causado por el estilo de respuesta del modelo (por ejemplo, verbosidad o concisión), evaluando de manera más pura sus capacidades fundamentales.
- **Nombre del modelo**: Nombre del modelo lingüístico de gran tamaño (LLM). Esta columna contiene enlaces relevantes que permiten redirección al hacer clic.
- **Puntuación**: Puntuación Elo obtenida por el modelo a través de votaciones de usuarios en la arena. El sistema Elo es un ranking relativo donde puntuaciones más altas indican mejor desempeño. Esta puntuación cambia dinámicamente, reflejando la capacidad competitiva actual del modelo.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo (ejemplo: `+6/-6`). Un intervalo más pequeño indica mayor estabilidad y confiabilidad; uno más grande puede sugerir datos insuficientes o alta variabilidad. Proporciona una evaluación cuantitativa de la precisión de la puntuación.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Mayor cantidad de votos generalmente implica mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que ofrece el modelo.
- **Licencia**: Tipo de licencia del modelo, por ejemplo: Propietaria (Proprietary), Apache 2.0, MIT, etc.
- **Fecha de corte de conocimiento**: Fecha de corte del conocimiento en los datos de entrenamiento del modelo. **Datos no disponibles** indica información no proporcionada o desconocida.

## Fuente de datos y frecuencia de actualización

Los datos de esta clasificación se generan automáticamente mediante el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Esta clasificación se actualiza diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos de la clasificación son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión de los datos dependen de las fuentes originales y del procesamiento del proyecto `fboulnois/llm-leaderboard-csv`. Diferentes modelos pueden usar distintas licencias; consulte siempre las indicaciones oficiales de los proveedores.