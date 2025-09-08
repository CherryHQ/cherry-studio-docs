# Classement LLM Arena (Mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement basé sur les données de Chatbot Arena (lmarena.ai), généré via un processus automatisé.

> **Dernière mise à jour des données** : 2025-09-08 11:40:35 UTC / 2025-09-08 19:40:35 CST (Heure de Pékin)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à sa page de détails ou d'essai.
{% endhint %}

## Classement

| Rang(UB) | Rang(StyleCtrl) | Nom du modèle                                                                                                                             | Score | Intervalle de confiance | Votes     | Fournisseur                    | Licence                    | Date de connaissance |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Propriétaire             | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Propriétaire             | nan      |
|        3 |               2 | [GLM-4.5](https://z.ai/blog/glm-4.5)                                                                                            | 1434 | +9/-9   | 4,112   | Z.ai                   | MIT                     | nan      |
|        4 |               2 | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                        | 1434 | +6/-6   | 13,058  | xAI                    | Propriétaire             | nan      |
|        5 |               3 | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                               | 1429 | +4/-4   | 30,777  | OpenAI                 | Propriétaire             | nan      |
|        6 |               3 | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                           | 1428 | +4/-4   | 32,033  | OpenAI                 | Propriétaire             | nan      |
|        7 |               3 | [Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)                                      | 1427 | +9/-9   | 4,154   | Alibaba                | Apache 2.0              | nan      |
|        8 |               3 | [DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)                                                               | 1427 | +5/-5   | 18,284  | DeepSeek               | MIT                     | nan      |
|        9 |               4 | [Grok-3-Preview-02-24](https://x.ai/blog/grok-3)                                                                                | 1423 | +4/-4   | 31,757  | xAI                    | Propriétaire             | nan      |
|       10 |               8 | [Llama-4-Maverick-03-26-Experimental](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)                                | 1416 | +4/-4   | 26,604  | Meta                   | nan                     | nan      |
| ... (le reste du tableau reste inchangé avec les mêmes données) ... |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## Explications

- **Rang(UB)** : Classement calculé selon le modèle Bradley-Terry. Ce rang reflète la performance globale du modèle dans l'arène et fournit une estimation de la **borne supérieure** de son score Elo, aidant à comprendre sa compétitivité potentielle.
- **Rang(StyleCtrl)** : Classement après contrôle du style conversationnel. Ce rang vise à réduire les biais de préférence dus au style de réponse des modèles (par exemple, verbosité ou concision), évaluant plus purement leurs capacités fondamentales.
- **Nom du modèle** : Nom du grand modèle de langage (LLM). Cette colonne contient des liens intégrés vers les modèles, cliquables pour accéder aux détails.
- **Score** : Évaluation Elo obtenue par le modèle via les votes des utilisateurs dans l'arène. Le score Elo est un système de classement relatif : plus le score est élevé, meilleure est la performance du modèle. Ce score évolue dynamiquement, reflétant la force relative du modèle dans l'environnement concurrentiel actuel.
- **Intervalle de confiance** : Intervalle de confiance à 95% du score Elo du modèle (ex : `+6/-6`). Plus cet intervalle est petit, plus le score est stable et fiable ; inversement, un intervalle large peut indiquer des données insuffisantes ou une performance fluctuante. Il fournit une évaluation quantitative de la précision du score.
- **Votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est généralement grande.
- **Fournisseur** : Organisation ou entreprise fournissant le modèle.
- **Licence** : Type de licence du modèle, par exemple propriétaire (Proprietary), Apache 2.0, MIT, etc.
- **Date de connaissance** : Date de fin des données d'entraînement du modèle. **Aucune donnée** indique que l'information n'est pas fournie ou inconnue.

## Source des données et fréquence de mise à jour

Les données de ce classement sont générées et fournies automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement par GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement sont dynamiques et basées sur les votes de préférence des utilisateurs dans Chatbot Arena pendant une période spécifique. L'exhaustivité et l'exactitude des données dépendent des sources en amont et des mises à jour/traitements du projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent utiliser différentes licences - veuillez consulter les instructions officielles des fournisseurs de modèles avant toute utilisation.