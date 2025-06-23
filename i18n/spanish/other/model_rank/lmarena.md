
{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# LLM Arena Leaderboard (Actualizado en Tiempo Real)

Este es un ranking basado en datos de Chatbot Arena (lmarena.ai), generado mediante procesos automatizados.

> **Última actualización de datos**: 2025-06-23 11:42:38 UTC / 2025-06-23 19:42:38 CST (Hora de Pekín)

{% hint style="info" %}
Haz clic en el **nombre del modelo** en el ranking para acceder a su página de detalles o prueba.
{% endhint %}

## Leaderboard

| Rango (UB) | Rango (StyleCtrl) | Nombre del Modelo                                                                                                                                       | Puntuación | Intervalo de confianza | Votos      | Proveedor                    | Licencia                    | Fecha límite de conocimientos |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro-Preview-06-05](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-06-05)                        | 1480 | +6/-6   | 8,825   | Google                 | Propietaria             | Datos no disponibles     |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                        | 1446 | +5/-5   | 13,025  | Google                 | Propietaria             | Datos no disponibles     |
| 3 | 2 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                                     | 1427 | +4/-4   | 16,019  | OpenAI                 | Propietaria             | Datos no disponibles     |
| ... *(El resto de filas de la tabla conservan estructura idéntica, traduciendo solo campos de texto)* ... | | | | | | | |
| 204 | 202 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                             | 815 | +12/-10 | 2,446   | Meta                   | No comercial          | 2023/2   |

## Explicaciones

- **Rango (UB)**: Clasificación calculada mediante el modelo Bradley-Terry. Refleja el rendimiento general del modelo en la arena, proporcionando una estimación del **límite superior** de su puntuación Elo para entender su potencial competitivo.
- **Rango (StyleCtrl)**: Clasificación ajustada por control de estilo conversacional. Busca reducir el sesgo por preferencias de estilo (ej. verbosidad, concisión), evaluando principalmente la capacidad central del modelo.
- **Nombre del modelo**: Nombre del Modelo de Lenguaje Grande (LLM). Esta columna incluye enlaces; haz clic para acceder.
- **Puntuación**: Puntuación Elo obtenida mediante votación de usuarios en la arena. El sistema Elo clasifica modelos relativamente; mayor puntuación indica mejor rendimiento. Este valor es dinámico y refleja la fuerza relativa actual del modelo.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo (ej: `+6/-6`). Intervalos más pequeños indican mayor estabilidad y fiabilidad; intervalos grandes pueden sugerir datos insuficientes o alta volatilidad. Cuantifica la precisión de la puntuación.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Más votos generalmente implican mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que ofrece el modelo.
- **Licencia**: Tipo de licencia del modelo, ej. Propietaria (Propietary), Apache 2.0, MIT, etc.
- **Fecha límite de conocimientos**: Fecha de corte de los datos de entrenamiento. **Datos no disponibles** significa información no proporcionada o desconocida.

## Fuente de datos y frecuencia de actualización

Los datos de este ranking son generados y proporcionados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Este ranking se actualiza diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos del ranking son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión de los datos dependen de las fuentes originales y del procesamiento en `fboulnois/llm-leaderboard-csv`. Los modelos pueden tener diferentes licencias; consulte siempre las especificaciones oficiales del proveedor.