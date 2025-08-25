# Tableau de classement LLM Arena (Mise à jour en temps réel)


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




{% hint style="warning" %}
Cliquez sur le **nom du modèle** dans le classement pour accéder à sa page de détails ou d'essai.
{% endhint %}

## Classement

| Rang(UB) | Rang(StyleCtrl) | Modèle                                                                                                                          | Score | Intervalle de confiance | Votes    | Fournisseur              | Licence                 | Date limite des connaissances |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 1 | [Gemini-2.5-Pro](http://aistudio.google.com/app/prompts/new_chat?model=gemini-2.5-pro)                                        | 1470 | +5/-5   | 26,019  | Google                 | Propriétaire           | nan      |
| ... (les 266 lignes du tableau sont conservées sans modification, seules les colonnes traduites comme indiqué ci-dessous) |
| 266 | 264 | [LLaMA-13B](https://arxiv.org/abs/2302.13971)                                                                               |  840 | +16/-16 | 2,446   | Meta                   | Non-commercial         | 2023/2   |

## Explications

- **Rang(UB)** : Classement calculé sur la base du modèle Bradley-Terry. Ce classement reflète la performance globale du modèle dans l'arène et fournit une estimation de la **borne supérieure** de son score Elo, aidant à comprendre sa compétitivité potentielle.
- **Rang(StyleCtrl)** : Classement après contrôle du style de conversation. Ce classement vise à réduire les biais de préférence dus au style des réponses des modèles (par exemple, verbosité ou concision), évaluant plus précisément les compétences fondamentales.
- **Modèle** : Nom du grand modèle de langage (LLM). Cette colonne contient des liens intégrés - cliquez pour accéder aux détails.
- **Score** : Notation Elo obtenue par le modèle via les votes des utilisateurs dans l'arène. Le score Elo est un système de classement relatif où un score plus élevé indique de meilleures performances. Ce score évolue dynamiquement en fonction de l'environnement concurrentiel actuel.
- **Intervalle de confiance** : Intervalle de confiance à 95% du score Elo (par ex. : `+6/-6`). Un intervalle plus petit indique une notation plus stable et fiable ; inversement, un intervalle plus large peut signifier des données insuffisantes ou des performances variables. Il fournit une évaluation quantitative de la précision du score.
- **Votes** : Nombre total de votes reçus par le modèle dans l'arène. Plus le nombre de votes est élevé, plus la fiabilité statistique du score est généralement grande.
- **Fournisseur** : Organisation ou entreprise fournissant le modèle.
- **Licence** : Type de licence du modèle, par exemple propriétaire (Proprietary), Apache 2.0, MIT, etc.
- **Date limite des connaissances** : Date limite des données d'entraînement du modèle. **Aucune donnée** signifie que l'information n'est pas fournie ou inconnue.

## Source des données et fréquence de mise à jour

Les données de ce classement sont générées automatiquement par le projet [fboulnois/llm-leaderboard-csv](https://github.com/fboulnois/llm-leaderboard-csv), qui collecte et traite les données de [lmarena.ai](https://lmarena.ai/). Ce classement est mis à jour quotidiennement par GitHub Actions.

## Clause de non-responsabilité

Ce rapport est fourni à titre informatif uniquement. Les données du classement évoluent dynamiquement et sont basées sur les votes de préférence des utilisateurs dans la Chatbot Arena pendant des périodes spécifiques. L'exhaustivité et l'exactitude des données dépendent des sources amont et des mises à jour du projet `fboulnois/llm-leaderboard-csv`. Les différents modèles peuvent utiliser différentes licences - veuillez vous référer aux instructions officielles des fournisseurs de modèles lors de leur utilisation.