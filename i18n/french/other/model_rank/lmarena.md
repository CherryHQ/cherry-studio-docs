# Classement de l'Arena LLM (Mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement généré automatiquement à partir des données de Chatbot Arena (lmarena.ai).

> **Date de mise à jour des données** : 2025-09-07 11:39:47 UTC / 2025-09-07 19:39:47 CST (Heure de Beijing)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à sa page d'informations détaillées ou à son essai.
{% endhint %}

## Classement

|    Rang(UB) |    Rang(StyleCtrl) | Nom du modèle                                                                                                                             |   Score | Intervalle de confiance | Nombre de votes | Fournisseur                      | Licence                          | Date de fin de connaissances |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                            | Propriétaire                     | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                            | Propriétaire                     | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                              | MIT                              | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                               | Propriétaire                     | nan      |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                            | Propriétaire                     | nan      |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
|      262 |             258 | [OpenAssistant-Pythia-12B](https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5)                               |  923 | +10/-10 | 6,368   | OpenAssistant                     | Apache 2.0                       | 2023/4   |
|      263 |             260 | [FastChat-T5-3B](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)                                                              |  901 | +12/-12 | 4,288   | LMSYS                             | Apache 2.0                       | 2023/4   |
|      264 |             263 | [StableLM-Tuned-Alpha-7B](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)                                           |  873 | +12/-12 | 3,336   | Stability AI                      | CC-BY-NC-SA-4.0                  | 2023/4   |
|      265 |             263 | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                                  |  857 | +13/-13 | 3,480   | Databricks                        | MIT                              | 2023/4   |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                              | Non-commercial                   | 2023/2   |

## Explications

- **Rang(UB)** : Classement calculé selon le modèle Bradley-Terry. Ce classement reflète la performance globale du modèle dans l'arène et fournit une estimation de la **borne supérieure** de son score Elo, aidant à comprendre sa compétitivité potentielle.
- **Rang(StyleCtrl)** : Classement après contrôle du style conversationnel. Ce classement vise à réduire les biais de préférence liés au style de réponse des modèles (par exemple, verbosité ou concision), pour évaluer plus purement les capacités fondamentales.
- **Nom du modèle** : Nom du Grand Modèle de Langage (LLM). Cette colonne contient des liens vers les modèles ; cliquez pour accéder.
- **Score** : Score Elo obtenu par le modèle via les votes des utilisateurs dans l'arène. Elo est un système de classement relatif : un score plus élevé indique une meilleure performance. Ce score est dynamique et reflète la force relative du modèle dans l'environnement concurrentiel actuel.
- **Intervalle de confiance** : Intervalle de confiance à 95% du score Elo du modèle (par exemple : `+6/-6`). Plus cet intervalle est petit, plus le score est stable et fiable ; inversement, un intervalle plus large peut indiquer des données insuffisantes ou une performance variable. Il fournit une évaluation quantitative de la précision du score.
- **Nombre de votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est généralement importante.
- **Fournisseur** : Organisation ou entreprise fournissant le modèle.
- **Licence** : Type de licence du modèle, par exemple Propriétaire, Apache 2.0, MIT, etc.
- **Date de fin de connaissances** : Date de fin de connaissances des données d'entraînement du modèle. **Aucune donnée** signifie que les informations ne sont pas fournies ou sont inconnues.

## Source des données et fréquence de mise à jour

Les données de ce classement sont générées et fournies automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement par GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif seulement. Les données du classement sont dynamiques et basées sur les préférences de vote des utilisateurs dans Chatbot Arena pendant une période spécifique. L'exhaustivité et l'exactitude des données dépendent des sources en amont et des mises à jour/traitements du projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent utiliser différentes licences - consultez toujours les instructions officielles du fournisseur du modèle avant utilisation.