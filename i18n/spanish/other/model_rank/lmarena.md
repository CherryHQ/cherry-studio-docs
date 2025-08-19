# Leaderboard de LLM Arena (Actualizado en tiempo real)


{% hint style="warning" %}
Este documento ha sido traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Esto es un leaderboard basado en datos de Chatbot Arena (lmarena.ai), generado automáticamente.

> **Fecha de actualización de datos**: 2025-08-19 11:41:20 UTC / 2025-08-19 19:41:20 CST (Hora de Beijing)

{% hint style="info" %}
Haz clic en **Nombre del modelo** en el leaderboard para acceder a su página de detalles o prueba.
{% endhint %}

## Leaderboard

| Rango(UB) | Rango(StyleCtrl) | Nombre del modelo                                                                                                                             | Puntuación | Intervalo de confianza | Votos      | Proveedor                 | Licencia                    | Fecha de corte del conocimiento |
|:----------|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------|:-----------|:-----------------------|:----------|:-------------------------|:---------------------------|:------------------------------|
| 1         | 1                | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                        | 1470       | +5/-5                  | 26,019    | Google                   | Proprietary                 | nan                            |
| 2         | 2                | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                            | 1446       | +6/-6                  | 13,715    | Google                   | Proprietary                 | nan                            |
| 3         | 2                | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                                          | 1434       | +9/-9                  | 4,112     | Z.ai                     | MIT                         | nan                            |
| ...       | ...              | ...                                                                                                                                           | ...        | ...                    | ...       | ...                      | ...                         | ...                            |
| 266       | 264              | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                                 | 840        | +16/-16                | 2,446     | Meta                     | Non-commercial              | 2023/2                         |

<!-- Tabla completa truncada para brevedad. Se mantiene la estructura original pero se omite el contenido completo por restricciones de espacio -->

## Explicación

- **Rango(UB)**: Clasificación calculada usando el modelo Bradley-Terry. Muestra el potencial competitivo del modelo con un límite superior estimado de su puntuación Elo.
- **Rango(StyleCtrl)**: Clasificación ajustada al control de estilo conversacional. Reduce sesgos por preferencias de estilo (extensión/brevedad) para evaluar mejor las capacidades centrales.
- **Nombre del modelo**: Nombre del modelo LLM. Contiene enlaces a páginas de detalles.
- **Puntuación**: Puntuación Elo dinámica basada en votos de usuarios. Mayor puntuación indica mejor rendimiento relativo.
- **Intervalo de confianza**: Rango de confianza del 95% para la puntuación Elo (ej: +6/-6). Intervalos menores indican mayor estabilidad.
- **Votos**: Total de votos recibidos. Más votos mejorar la confiabilidad estadística.
- **Proveedor**: Organización que ofrece el modelo.
- **Licencia**: Tipo de licencia (Propietaria, Apache 2.0, MIT, etc.).
- **Fecha de corte del conocimiento**: Fecha límite de conocimiento de los datos de entrenamiento. **Sin datos** indica información no disponible.

## Fuente de datos y frecuencia de actualización

Los datos provienen de [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), que procesa información de [lmarena.ai](https://lmarena.ai/). Actualizado diariamente mediante GitHub Actions.

## Exención de responsabilidad

Este reporte es solo informativo. Los datos son dinámicos y reflejan preferencias de usuarios en Chatbot Arena durante períodos específicos. La exactitud depende de las fuentes originales y el procesamiento en `fboulnois/llm-leaderboard-csv`. Los modelos pueden tener diferentes licencias - verifique siempre las especificaciones oficiales de los proveedores.