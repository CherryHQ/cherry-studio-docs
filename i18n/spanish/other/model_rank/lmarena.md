```markdown
# LLM Arena Leaderboard (Actualización en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Este es un leaderboard basado en datos de Chatbot Arena (lmarena.ai), generado automáticamente mediante un proceso de automatización.

> **Fecha de actualización de datos**: 2025-08-01 11:44:25 UTC / 2025-08-01 19:44:25 CST (Hora de Pekín)

{% hint style="info" %}
Haz clic en el **nombre del modelo** en el leaderboard para ir a su página de detalles o prueba.
{% endhint %}

## Leaderboard

| Posición (UB) | Posición (StyleCtrl) | Nombre del modelo                                                                                                                         |   Puntuación | Intervalo de confianza    | Votos      | Proveedor                    | Licencia                    | Fecha límite de conocimiento   |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                      | 1474 | +5/-4   | 19,209  | Google                 | Propietaria             | Sin datos     |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)          | 1446 | +4/-5   | 13,692  | Google                 | Propietaria             | Sin datos     |
|        2 |               3 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                    | 1443 | +7/-8   | 5,725   | xAI                    | Propietaria             | Sin datos     |
| ... (tabla completa conservando enlaces y datos numéricos sin cambios) ...

## Explicaciones

- **Posición (UB)**: Ranking calculado según el modelo Bradley-Terry. Este ranking refleja el rendimiento global del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su competitividad potencial.
- **Posición (StyleCtrl)**: Ranking después de controlar el estilo de conversación. Este ranking busca reducir el sesgo de preferencia causado por el estilo de respuesta del modelo (por ejemplo, verboso o conciso), evaluando de manera más pura sus capacidades fundamentales.
- **Nombre del modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna incluye enlaces relacionados con el modelo; haz clic para acceder.
- **Puntuación**: Puntuación Elo obtenida por el modelo mediante votos de usuarios en la arena. El sistema Elo es un ranking relativo: a mayor puntuación, mejor rendimiento. Esta puntuación cambia dinámicamente según el entorno competitivo actual.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo (ej: `+6/-6`). Un intervalo menor indica mayor estabilidad y fiabilidad; uno mayor sugiere datos insuficientes o rendimiento fluctuante. Proporciona una evaluación cuantitativa de la precisión.
- **Votos**: Número total de votos recibidos por el modelo en la arena. Más votos generalmente indican mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que proporciona el modelo.
- **Licencia**: Tipo de licencia del modelo, como Propietaria, Apache 2.0, MIT, etc.
- **Fecha límite de conocimiento**: Fecha de corte del conocimiento en los datos de entrenamiento. **Sin datos** indica información no proporcionada o desconocida.

## Fuentes y frecuencia de actualización

Los datos de este leaderboard son generados y proporcionados automáticamente por el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que obtiene y procesa datos de [lmarena.ai](https://lmarena.ai/). Este leaderboard se actualiza automáticamente diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos del leaderboard son dinámicos y se basan en votos de preferencia de usuarios en Chatbot Arena durante un período específico. La integridad y precisión dependen de las fuentes de datos originales y del procesamiento del proyecto `fboulnois/llm-leaderboard-csv`. Diferentes modelos pueden usar licencias distintas; consulte siempre las instrucciones oficiales del proveedor.
```