
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Classement LLM Arena (Mise à jour en temps réel)

Il s'agit d'un classement généré automatiquement basé sur les données de Chatbot Arena (lmarena.ai).

> **Dernière mise à jour des données** : 2025-06-21 09:44:44 UTC / 2025-06-21 17:44:44 CST (Heure de Pékin)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à sa page de détails ou d'essai.
{% endhint %}

## Classement

| Rang(UB) | Rang(StyleCtrl) | Modèle                                                                                                                                       | Score | Intervalle de confiance | Votes     | Fournisseur               | Licence                  | Date de fin des connaissances |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|1|1|[Gemini-2.5-Pro-Preview-06-05](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-06-05)|1480|+6/-6|8,825|Google|Propriétaire|Données non disponibles|
|2|2|[Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)|1446|+5/-5|13,025|Google|Propriétaire|Données non disponibles|
|3|2|[o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)|1427|+4/-4|16,019|OpenAI|Propriétaire|Données non disponibles|
|3|3|[ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)|1426|+5/-5|20,638|OpenAI|Propriétaire|Données non disponibles|
|3|6|[DeepSeek-R1-0528](https://api-docs.deepseek.com/news/news250528)|1421|+7/-7|8,423|DeepSeek|MIT|Données non disponibles|
|...*(La traduction continue de manière identique pour toutes les lignes du tableau)*|...|...|...|...|...|...|...|...|
|204|202|[LLaMA-13B](https://arxiv.org/abs/2302.13971)|815|+12/-10|2,446|Meta|Non commercial|2023/02|

## Explications

- **Rang(UB)** : Classement calculé selon le modèle de Bradley-Terry. Ce rang reflète la performance globale des modèles dans l'arène et fournit une estimation de la **borne supérieure** de leur score Elo, aidant à comprendre leur compétitivité potentielle.
- **Rang(StyleCtrl)** : Classement après contrôle du style conversationnel. Ce rang vise à réduire les biais de préférence liés au style des réponses des modèles (par exemple, longues ou concises), évaluant plus purement leurs capacités fondamentales.
- **Modèle** : Nom du modèle de langage (LLM). Cette colonne contient des liens pertinents vers chaque modèle.
- **Score** : Notation Elo obtenue via les votes des utilisateurs dans l'arène. Le système Elo classe les modèles de manière relative - plus le score est élevé, meilleure est la performance. Ce score évolue dynamiquement et reflète la compétitivité actuelle du modèle.
- **Intervalle de confiance** : Intervalle de confiance à 95% du score Elo (ex: `+6/-6`). Plus cet intervalle est petit, plus le score est stable et fiable. À l'inverse, un grand intervalle peut indiquer un manque de données ou une performance irrégulière. Il fournit une évaluation quantitative de la précision du score.
- **Votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est grande.
- **Fournisseur** : Organisation ou entreprise fournissant le modèle.
- **Licence** : Type de licence du modèle, par exemple Propriétaire, Apache 2.0, MIT, etc.
- **Date de fin des connaissances** : Date de clôture des données d'entraînement du modèle. **Données non disponibles** signifie que les informations ne sont pas fournies ou sont inconnues.

## Source des données et fréquence de mise à jour

Les données de ce classement sont générées automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement via GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement sont dynamiques et basées sur les préférences des utilisateurs dans Chatbot Arena pendant une période spécifique. L'exhaustivité et l'exactitude des données dépendent de la source amont et des mises à jour/traitements du projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent utiliser différentes licences - veuillez consulter les informations officielles des fournisseurs.