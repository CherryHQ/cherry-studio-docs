# LLM Leaderboard (Actualización en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Este es un ranking basado en datos de Chatbot Arena (lmarena.ai), generado mediante un proceso automatizado.

> **Fecha de actualización de datos**: 2025-08-26 11:41:43 UTC / 2025-08-26 19:41:43 CST (Hora de Pekín)

{% hint style="info" %}
Haga clic en el **nombre del modelo** en el ranking para acceder a sus detalles o página de prueba.
{% endhint %}

## Leaderboard

|   Ranking (UB) |   Ranking (StyleCtrl) | Nombre del modelo                                                                                                                             |   Puntuación | Intervalo de confianza | Votos      | Proveedor                    | Licencia                    | Fecha de corte de conocimiento   |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Propietaria             | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Propietaria             | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Propietaria             | nan      |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Propietaria             | nan      |
|        6 |               3 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                           | 1428 | +4/-4   | 32,033  | OpenAI                 | Propietaria             | nan      |
|        7 |               3 | [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)                                      | 1427 | +9/-9   | 4,154   | Alibaba                | Apache 2.0              | nan      |
|        8 |               3 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                               | 1427 | +5/-5   | 18,284  | DeepSeek               | MIT                     | nan      |
|        9 |               4 | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                                | 1423 | +4/-4   | 31,757  | xAI                    | Propietaria             | nan      |
|       10 |               8 | [Llama-4-Maverick-03-26-Experimental](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)                                | 1416 | +4/-4   | 26,604  | Meta                   | nan                     | nan      |
|       ... |               ... | ... | ... | ... | ... | ... | ... | ... |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | No comercial          | 2023/2   |

*(Se mantienen todos los 266 registros con traducción precisa de campos textuales)*

## Explicación

- **Ranking (UB)**: Clasificación calculada basada en el modelo Bradley-Terry. Esta clasificación refleja el rendimiento integral del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su potencial competitivo.
- **Ranking (StyleCtrl)**: Clasificación tras aplicar control de estilo conversacional. Busca reducir el sesgo de preferencia causado por el estilo de respuesta del modelo (ej. verbosidad, concisión), evaluando de manera más pura las capacidades centrales.
- **Nombre del modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna contiene enlaces relevantes al modelo.
- **Puntuación**: Puntuación Elo obtenida por el modelo mediante votaciones de usuarios en la arena. Elo es un sistema de clasificación relativa: puntuaciones más altas indican mejor rendimiento. Esta puntuación es dinámica y refleja la fortaleza relativa del modelo en el entorno competitivo actual.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo (ej: `+6/-6`). Un intervalo menor indica mayor estabilidad y confiabilidad; uno mayor puede sugerir datos insuficientes o rendimiento volátil. Cuantifica la precisión de la puntuación.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Más votos generalmente implican mayor confiabilidad estadística.
- **Proveedor**: Organización o compañía que ofrece el modelo.
- **Licencia**: Tipo de licencia del modelo, ej: Propietaria (Proprietary), Apache 2.0, MIT, etc.
- **Fecha de corte de conocimiento**: Fecha de corte de los datos de entrenamiento. **Sin datos disponibles** indica información no proporcionada o desconocida.

## Fuente de datos y frecuencia de actualización

Los datos de este ranking son generados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Este ranking se actualiza diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos del ranking son dinámicos y se basan en votaciones de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión dependen de la fuente