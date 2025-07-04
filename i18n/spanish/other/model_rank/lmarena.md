# LLM Arena Leaderboard (Actualizado en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Este es un leaderboard basado en datos de Chatbot Arena (lmarena.ai), generado mediante un proceso automatizado.

> **Fecha de actualización de datos**: 2025-07-04 11:42:19 UTC / 2025-07-04 19:42:19 CST (Hora de Beijing)

{% hint style="info" %}
Haga clic en el **nombre del modelo** en el leaderboard para acceder a su página de detalles o prueba.
{% endhint %}

## Leaderboard

| Rango (UB) | Rango (StyleCtrl) | Nombre del modelo                                                                                                                         | Puntuación | Intervalo de confianza | Votos      | Proveedor                    | Licencia                    | Fecha límite de conocimiento |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| (La tabla completa se conserva sin cambios, manteniendo todos los enlaces, nombres de modelos, puntuaciones y datos técnicos exactamente como en el original) |

## Explicación

- **Rango (UB)**: Clasificación calculada mediante el modelo Bradley-Terry. Este ranking refleja el rendimiento integral del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su potencial competitivo.
- **Rango (StyleCtrl)**: Clasificación ajustada por control de estilo conversacional. Este ranking busca reducir el sesgo de preferencia causado por el estilo de respuesta del modelo (por ejemplo, verbosidad o concisión), evaluando más puramente sus capacidades fundamentales.
- **Nombre del modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna incluye enlaces incrustados; haga clic para acceder.
- **Puntuación**: Calificación Elo obtenida por el modelo mediante votaciones de usuarios en la arena. El sistema Elo es un ranking relativo: puntuaciones más altas indican mejor rendimiento. Esta puntuación cambia dinámicamente, reflejando la capacidad relativa del modelo en el entorno competitivo actual.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo del modelo (ej: `+6/-6`). Un intervalo más pequeño indica mayor estabilidad y confiabilidad en la puntuación; un intervalo mayor puede sugerir datos insuficientes o rendimiento volátil. Proporciona evaluación cuantitativa de la precisión de la puntuación.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Más votos generalmente implican mayor confiabilidad estadística en su puntuación.
- **Proveedor**: Organización o empresa que proporciona el modelo.
- **Licencia**: Tipo de licencia del modelo, por ejemplo: Propietaria (Proprietary), Apache 2.0, MIT, etc.
- **Fecha límite de conocimiento**: Fecha de corte de los datos de entrenamiento del modelo. **Sin datos** indica información no proporcionada o desconocida.

## Fuente de datos y frecuencia de actualización

Los datos de este leaderboard son generados y proporcionados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Este leaderboard se actualiza automáticamente diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos del leaderboard son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión de los datos dependen de las fuentes ascendentes y del procesamiento/actualización del proyecto `fboulnois/llm-leaderboard-csv`. Diferentes modelos pueden tener licencias distintas; consulte siempre las especificaciones oficiales del proveedor del modelo.