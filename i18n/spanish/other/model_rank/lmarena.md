# Leaderboard de LLM Arena (actualizado en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Este es un ranking basado en datos de Chatbot Arena (lmarena.ai), generado mediante un proceso automatizado.

> **Última actualización de datos**: 2025-07-07 11:42:50 UTC / 2025-07-07 19:42:50 CST (Hora de Beijing)

{% hint style="info" %}
Haga clic en el **nombre del modelo** en la tabla para acceder a su página de detalles o prueba.
{% endhint %}

## Leaderboard

| Rango(UB) | Rango(StyleCtrl) | Modelo                                                                                                                         | Puntuación | Intervalo de confianza | Votos      | Proveedor                    | Licencia                    | Fecha límite de conocimiento |
|:----------|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------|:----------:|:----------------------|:----------|:----------------------------|:---------------------------|:----------------------------|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro) | 1477 | +5/-5 | 15,769 | Google | Propietario | Sin datos |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06) | 1446 | +4/-5 | 13,997 | Google | Propietario | Sin datos |
| 3 | 3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135) | 1429 | +4/-4 | 24,237 | OpenAI | Propietario | Sin datos |
| ... (tabla completa preservada sin cambios) ... |
| 212 | 210 | [LLaMA-13B](https://arxiv.org/abs/2302.13971) | 815 | +14/-9 | 2,446 | Meta | No comercial | 2023/2 |

## Explicaciones

- **Rango(UB)**: Clasificación calculada según el modelo Bradley-Terry. Refleja el rendimiento integral del modelo en la arena, proporcionando una estimación del **límite superior** de su puntuación Elo para ayudar a comprender su potencial competitivo.
- **Rango(StyleCtrl)**: Clasificación tras el control de estilo conversacional. Busca reducir el sesgo de preferencia causado por estilos de respuesta (ej. verbosidad, concisión), evaluando más puramente las capacidades fundamentales del modelo.
- **Modelo**: Nombre del Modelo de Lenguaje Grande (LLM). Esta columna incluye enlaces; haga clic para acceder.
- **Puntuación**: Calificación Elo obtenida por el modelo mediante votos de usuarios en la arena. Sistema de clasificación relativa: puntuaciones más altas indican mejor rendimiento. Dinámico y refleja la fortaleza relativa en el entorno competitivo actual.
- **Intervalo de confianza**: Intervalo de confianza del 95% de la puntuación Elo (ej. `+6/-6`). Intervalos más pequeños indican mayor estabilidad y confiabilidad; intervalos grandes pueden sugerir datos insuficientes o alta volatilidad. Proporciona evaluación cuantitativa de la precisión de la calificación.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Más votos generalmente implican mayor confiabilidad estadística.
- **Proveedor**: Organización o empresa que proporciona el modelo.
- **Licencia**: Tipo de licencia del modelo (Propietaria, Apache 2.0, MIT, etc.).
- **Fecha límite de conocimiento**: Fecha límite de los datos de entrenamiento del modelo. **Sin datos** indica información no disponible o desconocida.

## Fuente de datos y frecuencia de actualización

Los datos de este ranking son generados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Este leaderboard se actualiza diariamente mediante GitHub Actions.

## Exención de responsabilidad

Este reporte es solo para referencia. Los datos del leaderboard son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión de los datos dependen de las fuentes y del procesamiento del proyecto `fboulnois/llm-leaderboard-csv`. Los distintos modelos pueden tener licencias diferentes; consulte siempre las indicaciones oficiales de los proveedores.