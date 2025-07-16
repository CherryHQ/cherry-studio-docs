# Ranking LLM Arena (Actualización en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




{% hint style="info" %}
Este ranking se genera automáticamente basado en datos de Chatbot Arena (lmarena.ai) mediante un flujo automatizado.

> **Fecha de actualización de datos**: 2025-07-16 11:44:18 UTC / 2025-07-16 19:44:18 CST (Hora de Pekín)
{% endhint %}

{% hint style="tips" %}
Haga clic en los **nombres de los modelos** en el ranking para acceder a sus detalles o páginas de prueba.
{% endhint %}

## Leaderboard

| Rango(UB) | Rango(StyleCtrl) | Nombre del modelo                                                                                                          | Puntuación | Intervalo de confianza | Votos       | Proveedor              | Licencia                   | Fecha de corte de conocimientos |
|:----------|:-----------------|:---------------------------------------------------------------------------------------------------------------------------|:----------:|:-----------------------|:-----------|:-----------------------|:---------------------------|:-------------------------------|
| 1         | 1                | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                     | 1474       | +4/-4                 | 18,297     | Google                 | Propietaria             | Datos no disponibles      |
| ...       | ...              | ...                                                                                                                        | ...        | ...                    | ...        | ...                    | ...                        | ...                            |
| 216       | 214              | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                               | 815        | +15/-13               | 2,446      | Meta                   | No comercial            | 2023/2                    |

## Explicación

- **Rango(UB)**: Ranking calculado mediante el modelo Bradley-Terry que refleja el rendimiento global de los modelos en la arena. Proporciona una estimación del **límite superior** de los puntos Elo para entender su competitividad potencial.
- **Rango(StyleCtrl)**: Ranking ajustado con control de estilo conversacional para reducir sesgos de preferencia por estilos de respuestas (extensas/concisas), evaluando mejor las capacidades centrales.
- **Nombre del modelo**: Nombres de los LLM con enlaces incrustados a detalles o pruebas.
- **Puntuación**: Puntos Elo obtenidos mediante votaciones de usuarios. Sistema de clasificación relativa donde mayor puntuación = mejor rendimiento.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo. Intervalos pequeños indican mayor confiabilidad.
- **Votos**: Total de votos recibidos por el modelo. Más votos = mayor fiabilidad estadística.
- **Proveedor**: Organización que ofrece el modelo.
- **Licencia**: Tipo de licencia (Propietaria, Apache 2.0, MIT, etc).
- **Fecha de corte de conocimientos**: Fecha límite de los datos de entrenamiento. "Datos no disponibles" indica información desconocida.

## Fuente de datos y frecuencia de actualización

Los datos de este ranking son generados automáticamente por [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) usando datos procesados de [lmarena.ai](https://lmarena.ai/). El ranking se actualiza diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo de referencia. Los datos del ranking son dinámicos y se basan en votaciones de preferencia de usuarios en Chatbot Arena durante períodos específicos. La integridad y precisión dependen del proyecto `fboulnois/llm-leaderboard-csv`. Los modelos pueden tener diferentes licencias - consulte siempre los documentos oficiales de los proveedores.