# Classement de l'Arena LLM (mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement généré automatiquement à partir des données de Chatbot Arena (lmarena.ai).

> **Dernière mise à jour des données** : 2025-08-24 11:40:18 UTC / 2025-08-24 19:40:18 CST (Heure de Pékin)

{% hint style="info" %}
Cliquez sur les **noms de modèles** dans le classement pour accéder à leurs pages d'informations ou d'essai.
{% endhint %}

## Classement

|   Classement (UB) |   Classement (StyleCtrl) | Nom du modèle                                                                                                                   |   Score | Intervalle de confiance | Votes      | Fournisseur              | Licence                  | Date de fin des connaissances |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| (Le contenu du tableau reste inchangé conformément aux règles de traduction) | | | | | | | | |
|        1 |               1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                          | 1470 | +5/-5   | 26,019  | Google                 | Proprietary             | nan      |
|        2 |               2 | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)              | 1446 | +6/-6   | 13,715  | Google                 | Proprietary             | nan      |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
|      266 |             264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                                   |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial          | 2023/2   |

## Explications

- **Classement (UB)** : Classement calculé selon le modèle Bradley-Terry. Ce classement reflète la performance globale des modèles dans l'arène et fournit une estimation de la **borne supérieure** de leur score Elo, aidant à comprendre leur compétitivité potentielle.
- **Classement (StyleCtrl)** : Classement après contrôle du style conversationnel. Il vise à réduire les biais de préférence liés au style des réponses (par exemple, longueur, concision) pour évaluer plus purement les capacités fondamentales des modèles.
- **Nom du modèle** : Nom du grand modèle de langage (LLM). Cette colonne contient des liens vers les modèles correspondants.
- **Score** : Score Elo obtenu par le modèle à partir des votes des utilisateurs dans l'arène. Le score Elo est un système de classement relatif - plus le score est élevé, meilleure est la performance. Ce score évolue dynamiquement et reflète la force relative du modèle dans l'environnement concurrentiel actuel.
- **Intervalle de confiance** : Intervalle de confiance à 95% du score Elo (par exemple : `+6/-6`). Plus cet intervalle est petit, plus le score est stable et fiable. À l'inverse, un intervalle plus large peut indiquer un manque de données ou des performances volatiles. Il fournit une évaluation quantitative de la précision du score.
- **Votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est grande.
- **Fournisseur** : Organisation ou entreprise proposant le modèle.
- **Licence** : Type de licence du modèle (Propriétaire, Apache 2.0, MIT, etc.).
- **Date de fin des connaissances** : Date limite des données d'entraînement du modèle. **Aucune donnée** indique que les informations ne sont pas fournies ou sont inconnues.

## Source des données et fréquence de mise à jour

Ce classement est généré et fourni automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement via GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre indicatif. Les données du classement sont dynamiques et basées sur les votes de préférence des utilisateurs dans Chatbot Arena pendant une période spécifique. L'exhaustivité et l'exactitude des données dépendent des sources en amont et des mises à jour/traitements du projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent utiliser différentes licences - veuillez consulter les indications officielles des fournisseurs de modèles.