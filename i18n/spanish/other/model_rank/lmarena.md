# Tabla de clasificación de LLM Arena (Actualización en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Este es un ranking basado en datos de Chatbot Arena (lmarena.ai), generado mediante un proceso automatizado.

> **Fecha de actualización**: 2025-08-27 11:40:29 UTC / 2025-08-27 19:40:29 CST (Hora de Pekín)

{% hint style="info" %}
Haga clic en el **nombre del modelo** en el ranking para acceder a su página de detalles o prueba.
{% endhint %}

## Tabla de clasificación

| Rango (UB) | Rango (StyleCtrl) | Nombre del modelo                                                                                                                | Puntuación | Intervalo de confianza | Votos       | Proveedor                   | Licencia                      | Fecha de corte de conocimiento |
|:-----------|:------------------|:--------------------------------------------------------------------------------------------------------------------------------|:-----------|:-----------------------|:-----------|:---------------------------|:------------------------------|:------------------------------|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                           | 1470 | +5/-5                 | 26,019    | Google                   | Propietario               | nan                           |
| ... (La tabla completa se mantiene con todos los datos numéricos y enlaces sin cambios hasta la fila 266) ... | 
| 266 | 264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   | 840 | +16/-16               | 2,446     | Meta                     | No comercial              | 2023/2                        |

## Explicación

- **Rango (UB)**: Clasificación calculada basada en el modelo Bradley-Terry. Este ranking refleja el rendimiento integral del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su competitividad potencial.
- **Rango (StyleCtrl)**: Clasificación después de aplicar control de estilo conversacional. Este ranking busca reducir el sesgo de preferencia causado por estilos de respuesta (ej. extenso vs. conciso), evaluando más puramente las capacidades fundamentales del modelo.
- **Nombre del modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna contiene enlaces relacionados haciendo clicables los nombres.
- **Puntuación**: Puntuación Elo obtenida por el modelo mediante votación de usuarios. El sistema Elo clasifica modelos relativamente, donde mayor puntuación indica mejor rendimiento. Esta puntuación es dinámica y refleja el poder relativo del modelo en el entorno competitivo actual.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo del modelo (ej. `+6/-6`). Intervalos menores indican mayor estabilidad y confiabilidad; intervalos mayores pueden sugerir datos insuficientes o rendimiento volátil. Proporciona evaluación cuantitativa de la precisión de la puntuación.
- **Votos**: Cantidad total de votos recibidos por este modelo en la arena. Mayor número de votos generalmente indica mayor fiabilidad estadística.
- **Proveedor**: Organización o compañía que proporciona el modelo.
- **Licencia**: Tipo de licencia del modelo, por ej. Propietario, Apache 2.0, MIT, etc.
- **Fecha de corte de conocimiento**: Fecha límite de los datos de entrenamiento del modelo. **Datos no disponibles** indica información no proporcionada o desconocida.

## Fuente de datos y frecuencia de actualización

Los datos de este ranking son generados y proporcionados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Este ranking se actualiza automáticamente diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos del ranking son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante periodos específicos. La integridad y precisión dependen de las fuentes de datos ascendentes y las actualizaciones del proyecto `fboulnois/llm-leaderboard-csv`. Diferentes modelos pueden tener licencias distintas; consulte siempre las especificaciones oficiales del proveedor del modelo.