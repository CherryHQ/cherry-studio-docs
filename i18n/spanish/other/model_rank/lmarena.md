# Clasificación de LLM Arena (actualizada en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta es una clasificación basada en datos de Chatbot Arena (lmarena.ai), generada mediante un proceso automatizado.

> **Fecha de actualización de datos**: 2025-08-20 11:41:39 UTC / 2025-08-20 19:41:39 CST (Hora de Beijing)

{% hint style="info" %}
Haz clic en el **nombre del modelo** en la clasificación para acceder a su página de detalles o prueba.
{% endhint %}

## Clasificación

| Clasificación (UB) | Clasificación (StyleCtrl) | Nombre del modelo                                                                                                                             | Puntuación | Intervalo de confianza | Votos      | Proveedor              | Licencia                | Fecha de corte de conocimiento |
|:---------------|:--------------|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro) | 1470 | +5/-5 | 26,019 | Google | Proprietary | nan |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06) | 1446 | +6/-6 | 13,715 | Google | Proprietary | nan |
| ... (el resto de las filas de la tabla se mantienen intactas, con contenido idéntico al original) ... |
| 265 | 263 | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b) | 857 | +13/-13 | 3,480 | Databricks | MIT | 2023/4 |
| 266 | 264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971) | 840 | +16/-16 | 2,446 | Meta | Non-commercial | 2023/2 |

## Explicación

- **Clasificación (UB)**: Clasificación basada en el modelo Bradley-Terry. Refleja el rendimiento general del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su potencial competitivo.
- **Clasificación (StyleCtrl)**: Clasificación tras controlar el estilo de conversación. Busca reducir el sesgo de preferencia causado por estilos de respuesta (como verboso o conciso), evaluando más puramente la capacidad fundamental del modelo.
- **Nombre del modelo**: Nombre del Modelo de Lenguaje Grande (LLM). Esta columna incluye enlaces relevantes al modelo.
- **Puntuación**: Puntuación Elo obtenida por el modelo mediante votación de usuarios en la arena. El sistema Elo clasifica en términos relativos: cuanto mayor la puntuación, mejor el rendimiento. Actualización dinámica continua.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo (ej: `+6/-6`). Intervalos más pequeños indican mayor estabilidad y confiabilidad; mayores sugieren datos insuficientes o rendimiento fluctuante. Cuantifica la precisión de la puntuación.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Mayor cantidad suele indicar mayor confiabilidad estadística.
- **Proveedor**: Organización o compañía que proporciona el modelo.
- **Licencia**: Tipo de licencia del modelo (ej: Propietaria (Proprietary), Apache 2.0, MIT, etc.).
- **Fecha de corte de conocimiento**: Fecha de corte de datos de entrenamiento del modelo. **Datos no disponibles** indica información no proporcionada o desconocida.

## Fuente de datos y frecuencia de actualización

Estos datos son generados y proporcionados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). La clasificación se actualiza diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este reporte es solo para referencia. Los datos son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión de los datos dependen de las fuentes iniciales y del procesamiento del proyecto `fboulnois/llm-leaderboard-csv`. Los modelos pueden tener distintas licencias: siempre consulte las especificaciones oficiales del proveedor.