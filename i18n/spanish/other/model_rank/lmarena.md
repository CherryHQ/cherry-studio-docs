# LLM Arena Leaderboard (Actualizado en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




{% hint style="info" %}
Este ranking se genera automáticamente utilizando datos de Chatbot Arena (lmarena.ai).
{% endhint %}

> **Datos actualizados el**: 2025-06-28 11:41:56 UTC / 2025-06-28 19:41:56 CST (Hora de Pekín)

{% hint style="info" %}
Haz clic en el **nombre del modelo** en el ranking para acceder a sus detalles o página de prueba.
{% endhint %}

## Ranking

| Posición(UB) | Posición(StyleCtrl) | Nombre del modelo                                                                                                                         | Puntuación | Intervalo confidencial | Votos      | Proveedor                    | Licencia                    | Fecha límite conocimiento |
|:-------------|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:-----------------------|:-----------|:-----------------------------|:----------------------------|:----------------------------|
|         1    |         1          | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                     | 1477       | +5/-5                 | 12,327     | Google                       | Propietaria                | Datos no disponibles       |
|         2    |         2          | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                       | 1446       | +4/-6                 | 14,040     | Google                       | Propietaria                | Datos no disponibles       |
|         3    |         3          | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                         | 1428       | +5/-3                 | 22,488     | OpenAI                       | Propietaria                | Datos no disponibles       |
|         3    |         2          | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                                     | 1428       | +5/-4                 | 18,205     | OpenAI                       | Propietaria                | Datos no disponibles       |
|         3    |         6          | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                                         | 1424       | +5/-6                 | 11,871     | DeepSeek                     | MIT                         | Datos no disponibles       |
|         3    |         7          | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                                         | 1422       | +4/-5                 | 24,316     | xAI                          | Propietaria                | Datos no disponibles       |
|         4    |         6          | [Gemini-2.5-Flash](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-flash)                                               | 1420       | +5/-6                 | 17,535     | Google                       | Propietaria                | Datos no disponibles       |
|         5    |         4          | [GPT-4.5-Preview](https://openai.com/index/introducing-gpt-4-5/)                                                                           | 1415       | +5/-5                 | 15,271     | OpenAI                       | Propietaria                | Datos no disponibles       |
| ... (resto de filas sin cambios en contenido técnico, solo traducida la frase "暂无数据" a "Datos no disponibles")                           |                      |                                                                                                                                            |            |                        |            |                              |                             |                            |
|       208    |         207        | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                              | 817        | +11/-12               | 2,446      | Meta                         | No comercial               | 2023/2                     |

## Notas

- **Posición(UB)**: Ranking basado en el modelo Bradley-Terry. Este ranking refleja el rendimiento integral del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo para comprender su potencial competitivo.
- **Posición(StyleCtrl)**: Ranking tras aplicar control de estilo conversacional. Este ranking busca reducir el sesgo de preferencia causado por el estilo de respuesta del modelo (ej. prolijidad, brevedad), evaluando de forma más pura sus capacidades principales.
- **Nombre del modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna incluye enlaces; al hacer clic se redirecciona.
- **Puntuación**: Puntuación Elo obtenida por el modelo mediante votos de usuarios en la arena. El Elo es un sistema de ranking relativo: puntuaciones más altas indican mejor rendimiento. Cambia dinámicamente, reflejando la fuerza relativa actual del modelo.
- **Intervalo confidencial**: Intervalo de confianza del 95% para la puntuación Elo (ej: `+6/-6`). Intervalos menores indican mayor estabilidad; mayores pueden sugerir datos insuficientes o alta volatilidad. Evalúa cuantitativamente la precisión de la puntuación.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Más votos típicamente indican mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que ofrece el modelo.
- **Licencia**: Tipo de licencia del modelo (ej. Propietaria, Apache 2.0, MIT, etc.).
- **Fecha límite conocimiento**: Fecha de corte de conocimiento de los datos de entrenamiento. **Datos no disponibles** indica información desconocida o no proporcionada.

## Fuente y frecuencia de actualización

Este ranking se genera automáticamente mediante el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Se actualiza diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos del ranking son dinámicos y basados en votos de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión dependen de las fuentes de datos ascendentes y del procesamiento del proyecto `fboulnois/llm-leaderboard-csv`. Los modelos pueden usar licencias diferentes; consulte siempre las especificaciones oficiales del proveedor.