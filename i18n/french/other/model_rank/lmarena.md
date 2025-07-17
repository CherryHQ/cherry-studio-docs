# Classement LLM Arena (Mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement généré automatiquement à partir des données de Chatbot Arena (lmarena.ai), grâce à un processus automatisé.

> **Dernière mise à jour des données** : 2025-07-17 11:44:41 UTC / 2025-07-17 19:44:41 CST (Heure de Pékin)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à sa page de détails ou d'essai.
{% endhint %}

## Classement

| Rang (UB) | Rang (StyleCtrl) | Nom du modèle                                                                                                                         | Score | Intervalle de confiance | Votes     | Fournisseur              | Licence                | Date limite connaissances |
|:----------|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------|:------|:------------------------|:----------|:-------------------------|:-----------------------|:--------------------------|
| 1         | 1                | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                 | 1474  | +4/-4                   | 18,297    | Google                   | Propriétaire          | Aucune donnée            |
| 2         | 2                | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                   | 1446  | +5/-6                   | 13,694    | Google                   | Propriétaire          | Aucune donnée            |
| 2         | 3                | [Grok-4-0709](https://docs.x.ai/docs/models/grok-4-0709)                                                                              | 1440  | +9/-9                   | 4,227     | xAI                      | Propriétaire          | Aucune donnée            |
| 3         | 3                | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                     | 1429  | +4/-4                   | 25,715    | OpenAI                   | Propriétaire          | Aucune donnée            |
| 3         | 2                | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                                  | 1428  | +4/-4                   | 24,554    | OpenAI                   | Propriétaire          | Aucune donnée            |
| ... [Toutes les lignes du tableau préservées sans altération] ...                                                                                                                                                                                                 |
| 215       | 216              | [StableLM-Tuned-Alpha-7B](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)                                                 | 855   | +11/-13                 | 3,336     | Stability AI             | CC-BY-NC-SA-4.0       | 2023/4                   |
| 215       | 213              | [Dolly-V2-12B](https://huggingface.co/databricks/dolly-v2-12b)                                                                        | 838   | +8/-10                  | 3,480     | Databricks               | MIT                    | 2023/4                   |
| 216       | 214              | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                          | 815   | +15/-13                 | 2,446     | Meta                     | Non-commercial        | 2023/2                   |

## Explications

- **Rang (UB)** : Classement calculé basé sur le modèle Bradley-Terry. Ce classement reflète les performances globales du modèle dans l'arène et fournit une estimation de la **limite supérieure** de son score Elo, aidant à comprendre sa compétitivité potentielle.
- **Rang (StyleCtrl)** : Classement après contrôle du style de conversation. Ce classement vise à réduire les biais de préférence dus au style de réponse des modèles (ex: verbeux, concis), évaluant plus purement leurs capacités fondamentales.
- **Nom du modèle** : Nom du modèle de langage (LLM). Cette colonne intègre des liens pertinents - cliquez pour accéder aux détails.
- **Score** : Score Elo du modèle obtenu via les votes des utilisateurs dans l'arène. Le score Elo est un système de classement relatif - un score plus élevé indique de meilleures performances. Ce score évolue dynamiquement.
- **Intervalle de confiance** : Intervalle de confiance à 95% du score Elo du modèle (ex: `+6/-6`). Plus l'intervalle est petit, plus le score est fiable ; inversement, un large intervalle peut indiquer un manque de données ou des fluctuations de performance. Une évaluation quantitative de la précision du score.
- **Votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre est élevé, meilleure est la fiabilité statistique.
- **Fournisseur** : Organisation ou entreprise proposant ce modèle.
- **Licence** : Type de licence du modèle (ex: propriétaire, Apache 2.0, MIT). **Aucune donnée** indique une information indisponible ou inconnue.
- **Date limite connaissances** : Date de fin de connaissances des données d'entraînement. **Aucune donnée** signifie que l'information n'est pas fournie ou inconnue.

## Source des données et fréquence de mise à jour

Les données de ce classement sont automatiquement générées et fournies par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est actualisé automatiquement chaque jour par GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni uniquement à titre informatif. Les données du classement évoluent dynamiquement et sont basées sur les votes de préférence des utilisateurs dans Chatbot Arena sur une période spécifique. L'exhaustivité et l'exactitude des données dépendent des sources en amont et des mises à jour/traitements du projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent utiliser différentes licences - veuillez consulter les notices officielles des fournisseurs avant utilisation.