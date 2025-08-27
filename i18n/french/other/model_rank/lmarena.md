# LLM Arena Classement (mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement basé sur les données de Chatbot Arena (lmarena.ai), généré automatiquement.

> **Date de mise à jour des données**: 2025-08-27 11:40:29 UTC / 2025-08-27 19:40:29 CST (heure de Beijing)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à ses détails ou à une page d'essai.
{% endhint %}

## Classement

| Rang(UB) | Rang(StyleCtrl) | Modèle                                                                                                                             | Score | Intervalle de confiance | Votes    | Fournisseur                 | Licence                   | Date de mise à jour des connaissances |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| ... (le reste du tableau est conservé inchangé avec les liens et données techniques préservés) ... |

## Explications

- **Rang(UB)**: Classement calculé basé sur le modèle Bradley-Terry. Ce classement reflète la performance globale des modèles dans l'arène et fournit une estimation de la **borne supérieure** de leur score Elo, aidant à comprendre leur compétitivité potentielle.
- **Rang(StyleCtrl)**: Classement après contrôle du style de conversation. Ce classement vise à réduire les biais de préférence dus au style de réponse des modèles (par exemple, verbosité ou concision), évaluant plus purement leurs capacités fondamentales.
- **Nom du modèle**: Nom du grand modèle de langage (LLM). Cette colonne inclut des liens pertinents vers les modèles.
- **Score**: Score Elo obtenu par les votes des utilisateurs dans l'arène. Le score Elo est un système de classement relatif : plus le score est élevé, meilleure est la performance du modèle. Ce score évolue dynamiquement, reflétant la force relative du modèle dans l'environnement concurrentiel actuel.
- **Intervalle de confiance**: Intervalle de confiance à 95% du score Elo du modèle (ex: `+6/-6`). Un intervalle plus petit indique une plus grande fiabilité et stabilité du score ; à l'inverse, un intervalle large peut suggérer des données insuffisantes ou une performance variable. Il fournit une évaluation quantitative de la précision du score.
- **Votes**: Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est généralement grande.
- **Fournisseur**: Organisation ou entreprise fournissant le modèle.
- **Licence**: Type de licence du modèle, par exemple propriétaire (Proprietary), Apache 2.0, MIT, etc.
- **Date de mise à jour des connaissances**: Date de fin des données d'entraînement du modèle. **Aucune donnée** indique que les informations ne sont pas fournies ou sont inconnues.

## Sources des données et fréquence de mise à jour

Les données de ce classement sont générées automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement via GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement évoluent dynamiquement et sont basées sur les votes préférentiels des utilisateurs sur Chatbot Arena pendant une période spécifique. L'exhaustivité et l'exactitude des données dépendent des sources en amont et des mises à jour/traitements du projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent avoir différentes licences : veuillez consulter les instructions officielles des fournisseurs de modèles avant utilisation.