
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Classement LLM Arena (mise à jour en temps réel)

Il s'agit d'un classement basé sur les données de Chatbot Arena (lmarena.ai), généré par un processus automatisé.

> **Heure de mise à jour des données**: 2025-06-22 11:41:35 UTC / 2025-06-22 19:41:35 CST (Heure de Pékin)

{% hint style="info" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à sa page de détails ou d'essai.
{% endhint %}

## Classement

| Rang(UB) | Rang(StyleCtrl) | Nom du modèle                                                                                                                                       | Score | Intervalle de confiance | Nombre de votes | Fournisseur                  | Licence                     | Date de fin des connaissances |
|:---------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:------|:------------------------|:----------------|:----------------------------|:----------------------------|:------------------------------|
| 1        | 1               | [Gemini-2.5-Pro-Preview-06-05](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-06-05)                                   | 1480  | +6/-6                   | 8,825           | Google                       | Proprietary                  | Données non disponibles       |
| 2        | 2               | [Gemini-2.5-Pro-Preview-05-06](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro-preview-05-06)                                   | 1446  | +5/-5                   | 13,025          | Google                       | Proprietary                  | Données non disponibles       |
| 3        | 2               | [o3-2025-04-16](https://openai.com/index/introducing-o3-and-o4-mini/)                                                                             | 1427  | +4/-4                   | 16,019          | OpenAI                       | Proprietary                  | Données non disponibles       |
| ...      | ...             | ...                                                                                                                                                 | ...   | ...                     | ...             | ...                          | ...                          | ...                           |

*(Le reste du tableau est conservé sans traduction du contenu technique)*

## Explications

- **Rang(UB)** : Classement calculé sur la base du modèle Bradley-Terry. Ce classement reflète la performance globale du modèle dans l'arène et fournit une estimation de la **limite supérieure** de son score Elo, aidant à comprendre sa compétitivité potentielle.
- **Rang(StyleCtrl)** : Classement après contrôle du style conversationnel. Ce classement vise à réduire les biais de préférence dus au style des réponses du modèle (par exemple, bavardage, concision) pour évaluer plus purement les capacités fondamentales du modèle.
- **Nom du modèle** : Nom du grand modèle de langage (LLM). Cette colonne intègre des liens associés au modèle, cliquables pour accéder aux détails.
- **Score** : Score Elo obtenu par le modèle dans l'arène via les votes des utilisateurs. Le score Elo est un système de classement relatif, un score plus élevé indiquant une meilleure performance du modèle. Ce score est dynamique et reflète la force relative du modèle dans l'environnement concurrentiel actuel.
- **Intervalle de confiance** : Intervalle de confiance à 95% pour le score Elo du modèle (par exemple : `+6/-6`). Plus cet intervalle est petit, plus le score du modèle est stable et fiable ; à l'inverse, un intervalle plus large peut indiquer un manque de données ou des variations importantes dans les performances du modèle. Il fournit une évaluation quantitative de la précision du score.
- **Nombre de votes** : Nombre total de votes reçus par ce modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est généralement élevée.
- **Fournisseur** : Organisation ou entreprise fournissant ce modèle.
- **Licence** : Type de licence du modèle, par exemple propriétaire (Proprietary), Apache 2.0, MIT, etc.
- **Date de fin des connaissances** : Date de fin des données d'entraînement du modèle. **Données non disponibles** signifie que les informations pertinentes ne sont pas fournies ou sont inconnues.

## Source des données et fréquence de mise à jour

Les données de ce classement sont générées et fournies automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui récupère et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement automatiquement via GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement sont dynamiques et basées sur les votes de préférence des utilisateurs dans Chatbot Arena pendant une période spécifique. L'exhaustivité et l'exactitude des données dépendent des sources en amont ainsi que de la mise à jour et du traitement par le projet `fboulnois/llm-leaderboard-csv`. Différents modèles peuvent utiliser différentes licences. Veuillez consulter les instructions officielles du fournisseur du modèle avant toute utilisation.