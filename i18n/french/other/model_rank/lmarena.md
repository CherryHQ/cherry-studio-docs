# Classement LLM Arena (mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement généré automatiquement à partir des données de Chatbot Arena (lmarena.ai).

> **Date de mise à jour des données**: 2025-06-30 11:44:35 UTC / 2025-06-30 19:44:35 CST (heure de Pékin)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à ses informations détaillées ou à sa page d'essai.
{% endhint %}

## Classement

| Rang (UB) | Rang (StyleCtrl) | Modèle                                                                                                                      | Score | Intervalle de confiance | Votes     | Fournisseur              | Licence                 | Date limite des connaissances |
|:----------|:-----------------|:----------------------------------------------------------------------------------------------------------------------------|:------|:------------------------|:----------|:-------------------------|:------------------------|:------------------------------|
| 1         | 1                | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                      | 1477  | +5/-5                   | 12,327    | Google                   | Proprietary             | Non disponible                |
| 2         | 2                | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)          | 1446  | +4/-6                   | 14,040    | Google                   | Proprietary             | Non disponible                |
| 3         | 3                | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                           | 1428  | +5/-3                   | 22,488    | OpenAI                   | Proprietary             | Non disponible                |
| ...       | ...              | ...                                                                                                                         | ...   | ...                     | ...       | ...                      | ...                     | ...                           |
| 207       | 205              | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                              | 840   | +11/-12                 | 3,480     | Databricks               | MIT                     | 2023/4                        |
| 208       | 207              | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                               | 817   | +11/-12                 | 2,446     | Meta                     | Non-commercial          | 2023/2                        |

## Notes

- **Rang (UB)**: Classement calculé à partir du modèle Bradley-Terry. Ce rang reflète la performance globale du modèle dans l'arène et fournit une estimation de la **limite supérieure** de son score Elo, aidant à comprendre sa compétitivité potentielle.
- **Rang (StyleCtrl)**: Classement après contrôle du style conversationnel. Ce classement vise à réduire les biais de préférence dus au style de réponse des modèles (par exemple, prolixe vs concis), évaluant plus purement les capacités fondamentales.
- **Modèle**: Nom du grand modèle linguistique (LLM). Cette colonne intègre des liens associés au modèle - cliquez pour accéder.
- **Score**: Notation Elo obtenue par les votes des utilisateurs dans l'arène. Le système Elo est un classement relatif où des scores plus élevés indiquent de meilleures performances. Ce score est dynamique et reflète la force relative actuelle du modèle dans l'environnement compétitif.
- **Intervalle de confiance**: Intervalle de confiance à 95% du score Elo du modèle (par exemple: `+6/-6`). Plus cet intervalle est petit, plus le score est stable et fiable ; inversement, un intervalle large peut indiquer des données insuffisantes ou des performances volatiles. Il fournit une évaluation quantitative de la précision du score.
- **Votes**: Nombre total de votes reçus par ce modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique de son score est généralement élevée.
- **Fournisseur**: Organisation ou entreprise fournissant le modèle.
- **Licence**: Type de licence du modèle, par exemple propriétaire (Proprietary), Apache 2.0, MIT, etc.
- **Date limite des connaissances**: Date limite des données d'entraînement du modèle. **Non disponible** signifie que les informations ne sont pas fournies ou sont inconnues.

## Source des données et fréquence de mise à jour

Ce classement est généré automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv) qui récupère et traite les données depuis [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement par GitHub Actions automatiquement.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement sont dynamiques et basées sur les votes de préférence des utilisateurs dans Chatbot Arena pendant une période spécifique. L'exhaustivité et l'exactitude des données dépendent des sources en amont et des mises à jour/traitements du projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent utiliser différentes licences — veuillez toujours consulter les instructions officielles du fournisseur de modèles lors de leur utilisation.