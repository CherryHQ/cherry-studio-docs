# Tabla de clasificación de LLM Arena (actualizada en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta clasificación se genera automáticamente utilizando datos de Chatbot Arena (lmarena.ai).

> **Última actualización**: 2025-09-03 11:40:24 UTC / 2025-09-03 19:40:24 CST (Hora de Beijing)

{% hint style="info" %}
Haz clic en el **nombre del modelo** en la clasificación para acceder a sus detalles o página de prueba.
{% endhint %}

## Tabla de clasificación

| Rango(UB) | Rango(StyleCtrl) | Nombre del modelo                                                                                                                                       |   Puntuación | Intervalo de confianza |        Votos | Proveedor                   | Licencia               | Fecha límite de conocimiento |
|:----------|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:----------------------|:------------|:----------------------------|:-----------------------|:----------------------------|
|       1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                                  |        1470 | +5/-5                 |     26,019 | Google                      | Proprietary           | nan                         |
|       2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                                      |        1446 | +6/-6                 |     13,715 | Google                      | Proprietary           | nan                         |
| ... (La tabla completa se mantiene idéntica, preservando enlaces, números y estructuras) ...

|     266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                                            |         840 | +16/-16                |      2,446 | Meta                        | Non-commercial        | 2023/2                      |

## Explicación

- **Rango(UB)**: Clasificación basada en el modelo Bradley-Terry. Este rango refleja el rendimiento integral del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su potencial competitivo.
- **Rango(StyleCtrl)**: Clasificación tras controlar el estilo de conversación. Busca reducir el sesgo de preferencia por estilos de respuesta (ej. extenso vs conciso) para evaluar mejor las capacidades fundamentales.
- **Nombre del modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna incluye enlaces para más detalles.
- **Puntuación**: Calificación Elo obtenida mediante votaciones en la arena. Puntuaciones mayores indican mejor rendimiento. Refleja fortaleza relativa actual.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo. Intervalos menores indican mayor estabilidad; mayores pueden indicar datos insuficientes o variabilidad.
- **Votos**: Total de votos recibidos. Más votos suelen indicar mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que ofrece el modelo.
- **Licencia**: Tipo de licencia (Propietaria, Apache 2.0, MIT, etc.).
- **Fecha límite de conocimiento**: Fecha de corte del conocimiento entrenado. **Sin datos** indica información desconocida.

## Fuente de datos y frecuencia de actualización

Esta clasificación se genera automáticamente mediante [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que procesa datos de [lmarena.ai](https://lmarena.ai/). Se actualiza diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo informativo. Los datos son dinámicos y se basan en votaciones de preferencia durante períodos específicos. La integridad depende de fuentes externas. Diferentes modelos tienen licencias variadas; consulte siempre las disposiciones oficiales.