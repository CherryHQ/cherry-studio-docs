# Classement LLM Arena (mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement basé sur les données de Chatbot Arena (lmarena.ai), généré par un processus automatisé.

> **Date de mise à jour des données** : 2025-07-01 11:42:53 UTC / 2025-07-01 19:42:53 CST (Heure de Pékin)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à ses détails ou à une page d'essai.
{% endhint %}

## Classement

| Rang (UB) | Rang (StyleCtrl) | Nom du modèle                                                                                                                         | Score | Intervalle de confiance | Votes     | Fournisseur                | Licence                 | Date de clôture des connaissances |
|:----------|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------|:------|:------------------------|:----------|:---------------------------|:------------------------|:----------------------------------|
| 1         | 1                | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                 | 1473  | +5/-4                   | 14,062    | Google                     | Proprietary             | Aucune donnée                     |
| 2         | 2                | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                     | 1446  | +4/-5                   | 14,432    | Google                     | Proprietary             | Aucune donnée                     |
| 3         | 2                | [ChatGPT-4o-latest (2025-03-26)](https://x.com/OpenAI/status/1905331956856050135)                                                      | 1428  | +4/-3                   | 23,599    | OpenAI                     | Proprietary             | Aucune donnée                     |
| ... (le reste du tableau reste inchangé) ... |

## Explications

- **Rang (UB)** : Classement calculé à partir du modèle Bradley-Terry. Ce classement reflète la performance globale du modèle dans l'arène et fournit une estimation de la **borne supérieure** de son score Elo, aidant à comprendre sa compétitivité potentielle.
- **Rang (StyleCtrl)** : Classement après contrôle du style de conversation. Ce classement vise à réduire le biais de préférence dû au style des réponses du modèle (par exemple, verbeux ou concis), évaluant plus précisément les compétences fondamentales du modèle.
- **Nom du modèle** : Nom du grand modèle de langage (LLM). Cette colonne contient des liens vers les modèles, cliquables pour accéder directement.
- **Score** : Score Elo obtenu par le modèle via les votes des utilisateurs dans l'arène. Le score Elo est un système de classement relatif, où un score plus élevé indique une meilleure performance. Ce score évolue dynamiquement, reflétant la force relative du modèle dans l'environnement compétitif actuel.
- **Intervalle de confiance** : Intervalle de confiance à 95% pour le score Elo du modèle (par exemple : `+6/-6`). Plus cet intervalle est petit, plus le score est stable et fiable ; un intervalle plus large peut indiquer un manque de données ou une performance variable. Il fournit une évaluation quantitative de la précision du score.
- **Votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est généralement élevée.
- **Fournisseur** : Organisation ou entreprise fournissant le modèle.
- **Licence** : Type de licence du modèle, par exemple propriétaire (Proprietary), Apache 2.0, MIT, etc.
- **Date de clôture des connaissances** : Date de clôture des données de formation du modèle. **Aucune donnée** indique que les informations ne sont pas fournies ou sont inconnues.

## Source des données et fréquence de mise à jour

Les données de ce classement sont générées automatiquement et fournies par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement par GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement sont dynamiques et basées sur les votes de préférence des utilisateurs dans Chatbot Arena pendant une période spécifique. L'exhaustivité et l'exactitude des données dépendent des sources en amont et des mises à jour et traitements du projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent utiliser des licences différentes ; veuillez consulter les directives officielles des fournisseurs de modèles lors de leur utilisation.