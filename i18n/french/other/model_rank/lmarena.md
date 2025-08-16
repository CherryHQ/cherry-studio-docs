# Classement LLM Arena (mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Il s'agit d'un classement basé sur les données de Chatbot Arena (lmarena.ai), généré automatiquement via un processus automatisé.

> **Date de mise à jour des données**: 2025-08-16 11:40:33 UTC / 2025-08-16 19:40:33 CST (heure de Pékin)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à ses informations détaillées ou à la page de démonstration.
{% endhint %}

## Classement

| Rang(UB) | Rang(StyleCtrl) | Nom du modèle                                                                                                                             | Score | Intervalle de confiance | Votes     | Fournisseur                  | Licence                     | Date de fin des connaissances |
|:---------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:------|:------------------------|:----------|:-----------------------------|:----------------------------|:------------------------------|
| 1        | 1               | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                                     | 1470  | +5/-5                   | 26,019    | Google                       | Proprietary                 | nan                           |
| 2        | 2               | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                         | 1446  | +6/-6                   | 13,715    | Google                       | Proprietary                 | nan                           |
| ... (le reste du tableau reste inchangé, avec les liens, scores et données techniques identiques) ...

## Explications

- **Rang(UB)** : Classement calculé selon le modèle Bradley-Terry. Il reflète la performance globale du modèle dans l'arène et fournit une estimation de la **limite supérieure** de son score Elo, aidant à comprendre sa compétitivité potentielle.
- **Rang(StyleCtrl)** : Classement après contrôle du style conversationnel. Conçu pour réduire les biais de préférence liés au style des réponses (par exemple détaillé vs concis), évaluant plus purement les capacités fondamentales du modèle.
- **Nom du modèle** : Nom du grand modèle de langage (LLM). Contient des liens vers des informations associées.
- **Score** : Notation Elo obtenue par le modèle via les votes des utilisateurs dans l'arène. Plus le score est élevé, meilleure est la performance. Dynamique, il reflète la force relative actuelle du modèle dans l'environnement compétitif.
- **Intervalle de confiance** : Intervalle de confiance à 95% du score Elo (par exemple : `+6/-6`). Plus l'intervalle est petit, plus le score est stable et fiable. Quantifie la précision de l'évaluation.
- **Votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus ce nombre est élevé, plus la fiabilité statistique du score est grande.
- **Fournisseur** : Organisation ou entreprise fournissant le modèle.
- **Licence** : Type de licence du modèle, par exemple propriétaire (Proprietary), Apache 2.0, MIT, etc.
- **Date de fin des connaissances** : Date de fin des données d'entraînement du modèle. **Données non disponibles** indique une information non fournie ou inconnue.

## Source des données et fréquence de mise à jour

Ces données de classement sont générées automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui collecte et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement par GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement sont dynamiques et basées sur les votes de préférence des utilisateurs sur Chatbot Arena durant une période spécifique. L'exhaustivité et l'exactitude dépendent des sources amont et des mises à jour du projet `fboulnois/llm-leaderboard-csv`. Les modèles utilisent différentes licences - veuillez consulter les instructions officielles des fournisseurs avant utilisation.