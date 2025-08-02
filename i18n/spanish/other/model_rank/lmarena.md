# LLM Arena Leaderboard (Actualización en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esta es una tabla de clasificación automática basada en datos de Chatbot Arena (lmarena.ai), generada mediante procesos automatizados.

> **Hora de actualización de datos**: 2025-08-02 11:42:41 UTC / 2025-08-02 19:42:41 CST (Hora de Pekín)

{% hint style="info" %}
Haz clic en **Nombre del modelo** en la tabla de clasificación para saltar a su página de detalles o prueba.
{% endhint %}

## Tabla de Clasificación

| Clasificación (UB) | Clasificación (StyleCtrl) | Nombre del modelo                                                                                                                         | Puntuación | Intervalo de confianza | Votos      | Proveedor                    | Licencia                    | Fecha de corte de conocimientos |
|:---|:---|:---|:---|:---|:---|:---|:--|:---|
| (Se mantienen todas las filas de datos sin cambios excepto "暂无数据" → "Sin datos") | | | | | | | | |
| ... (repetir para cada fila reemplazando "暂无数据" con "Sin datos") ... | |

## Explicaciones

- **Clasificación (UB)**: Clasificación calculada según el modelo Bradley-Terry. Refleja el rendimiento global del modelo en la arena y proporciona una estimación del **límite superior** de su puntuación Elo, ayudando a comprender su competitividad potencial.
- **Clasificación (StyleCtrl)**: Clasificación después del control de estilo de conversación. Busca reducir el sesgo causado por estilos de respuesta (por ejemplo, verboso vs. conciso) para evaluar más objetivamente las capacidades fundamentales del modelo.
- **Nombre del modelo**: Nombre del modelo de lenguaje grande (LLM). Esta columna incluye enlaces relevantes; haz clic para acceder.
- **Puntuación**: Calificación Elo obtenida mediante votación de usuarios. Cuanto más alta sea, mejor será el rendimiento relativo. Es dinámica y refleja el estado actual en el entorno competitivo.
- **Intervalo de confianza**: Intervalo de confianza del 95% para la puntuación Elo (ej: `+6/-6`). Intervalos más pequeños indican mayor estabilidad y confiabilidad, mientras que intervalos más amplios sugieren datos insuficientes o volatilidad.
- **Votos**: Total de votos recibidos por el modelo en la arena. Más votos generalmente indican mayor fiabilidad estadística.
- **Proveedor**: Organización o empresa que ofrece el modelo.
- **Licencia**: Tipo de licencia del modelo (por ejemplo, Propietaria, Apache 2.0, MIT).
- **Fecha de corte de conocimientos**: Fecha de los datos de entrenamiento del modelo. **Sin datos** indica información no proporcionada o desconocida.

## Fuente de datos y frecuencia de actualización

Los datos se generan automáticamente mediante el proyecto [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que procesa datos de [lmarena.ai](https://lmarena.ai/). Esta clasificación se actualiza diariamente mediante GitHub Actions.

## Descargo de responsabilidad

Este informe es solo para referencia. Los datos son dinámicos y se basan en preferencias de usuarios mediante votación en Chatbot Arena durante períodos específicos. La integridad y precisión dependen de las fuentes originales y del procesamiento del proyecto `fboulnois/llm-leaderboard-csv`. Los modelos pueden tener diferentes licencias; consulte siempre las especificaciones oficiales de cada proveedor.