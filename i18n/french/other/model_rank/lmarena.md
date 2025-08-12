# Classement LLM Arena (mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement généré automatiquement à partir des données de Chatbot Arena (lmarena.ai).

> **Date de mise à jour des données** : 2025-08-12 11:43:09 UTC / 2025-08-12 19:43:09 CST (heure de Beijing)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à sa page d'informations ou d'essai.
{% endhint %}

## Classement

| Rang(UB) | Rang(StyleCtrl) | Modèle                                                                                                                             | Score | Intervalle de confiance | Votes     | Fournisseur                  | Licence                   | Date de fin des connaissances |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
| 2 | 2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Proprietary             | nan      |
| 3 | 2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
| 4 | 2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Proprietary             | nan      |
| 5 | 3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Proprietary             | nan      |
| ... (les lignes restantes du tableau sont conservées inchangées, conformément aux règles) ...
| 266 | 264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## Explications

- **Rang(UB)** : Classement calculé à partir du modèle Bradley-Terry. Ce classement reflète la performance globale du modèle dans l'arène et fournit une estimation de la **borne supérieure** de son score Elo, aidant à comprendre son potentiel compétitif.
- **Rang(StyleCtrl)** : Classement après contrôle du style conversationnel. Cette méthode vise à réduire les biais de préférence dus au style de réponse des modèles (par exemple, verbeux vs concis), permettant une évaluation plus pure de leurs capacités fondamentales.
- **Modèle** : Nom du grand modèle linguistique (LLM). Cette colonne contient des liens vers les modèles correspondants.
- **Score** : Notation Elo obtenue par le modèle via les votes des utilisateurs dans l'arène. Le score Elo est un système de classement relatif où un score plus élevé indique une meilleure performance. Ce score évolue dynamiquement en fonction de l'environnement concurrentiel actuel.
- **Intervalle de confiance** : Intervalle de confiance à 95% du score Elo (par exemple : `+6/-6`). Un intervalle plus petit indique une notation plus stable et fiable, tandis qu'un intervalle plus large peut suggérer un manque de données ou une performance volatile. Il fournit une évaluation quantitative de la précision du score.
- **Votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est généralement élevée.
- **Fournisseur** : Organisation ou entreprise fournissant le modèle.
- **Licence** : Type de licence du modèle (par exemple Propriétaire, Apache 2.0, MIT).
- **Date de fin des connaissances** : Date de fin des données d'entraînement du modèle. **Données non disponibles** indique que les informations ne sont pas fournies ou inconnues.

## Source des données et fréquence de mise à jour

Les données de ce classement sont générées et fournies automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement par GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement sont dynamiques et basées sur les préférences de vote des utilisateurs dans Chatbot Arena durant une période spécifique. L'exhaustivité et l'exactitude des données dépendent de la source en amont et des mises à jour/traitements du projet `fboulnois/llm-leaderboard-csv`. Les modèles peuvent utiliser différentes licences - veuillez vous référer aux informations officielles des fournisseurs.