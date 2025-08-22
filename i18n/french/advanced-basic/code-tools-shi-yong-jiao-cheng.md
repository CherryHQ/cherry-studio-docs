---
description: Tools
icon: code
---
# Tutoriel d'utilisation des outils de code


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




La version v1.5.7 de Cherry Studio introduit une fonctionnalité d'agent de code puissante et simple, permettant de démarrer et gérer divers agents de programmation IA. Ce tutoriel vous guide à travers l'intégralité du processus de configuration et de démarrage.

***

### Étapes opérationnelles

#### 1. Mise à jour de Cherry Studio

Assurez-vous d'abord que votre Cherry Studio est mis à jour en **v1.5.7** ou ultérieure. Vous pouvez télécharger la dernière version sur [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) ou depuis le site officiel.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### 2. Positionnement de la barre de navigation

Pour faciliter l'utilisation de l'onglet supérieur, nous recommandons de positionner la barre de navigation en haut de l'écran.

* Chemin : `Paramètres` → `Paramètres d'affichage` → `Configuration de la barre de navigation`
* Définissez l'option "Position de la barre de navigation" sur **`Haut`**.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Créer un nouvel onglet

Cliquez sur l'icône "＋" en haut de l'interface pour créer un nouvel onglet vierge.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 4. Activer la fonction Code Agent

Dans le nouvel onglet, cliquez sur l'icône `Code` (ou `</>`) pour accéder à l'interface de configuration de l'agent de code.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Sélection de l'outil CLI

Sélectionnez un outil Code Agent selon vos besoins et vos clés API disponibles. Les options actuellement supportées sont :

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Choix du modèle pour l'agent

Dans la liste déroulante des modèles, sélectionnez un modèle compatible avec l'outil CLI choisi. *(Voir les détails de compatibilité dans la section "Remarques importantes" ci-dessous)*

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Spécifier le répertoire de travail

Cliquez sur "Sélectionner un répertoire" pour définir l'emplacement de travail de l'agent. Celui-ci aura accès à tous les fichiers et sous-dossiers de ce répertoire afin de comprendre le contexte du projet.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Configuration des variables d'environnement

* **Configuration automatique** : Vos sélections à l'étape 6 (modèle) et 7 (répertoire) génèrent automatiquement les variables d'environnement.
* **Ajout personnalisé** : Ajoutez des variables spécifiques (ex : `PROXY_URL`) si nécessaire pour votre agent ou projet.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Options de mise à jour

* **Exécutables intégrés** : Tous les outils Code Agent sont pré-intégrés pour une utilisation hors ligne.
* **Mises à jour automatiques** : Cochez **`Vérifier les mises à jour et installer la dernière version`** pour maintenir l'agent à jour.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Démarrer l'agent

Après configuration complète, cliquez sur **`Démarrer`**. Cherry Studio lancera le terminal système avec les variables configurées et exécutera l'agent sélectionné. Interagissez ensuite avec l'agent dans la fenêtre du terminal.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Remarques importantes

1. **Compatibilité des modèles** :
   * **Claude Code** : Nécessite des modèles au format Anthropic API. Compatibilité actuelle :
     * Modèles Claude
     * DeepSeek V3.1 (API officielle)
     * Kimi K2 (API officielle)
     * GLM 4.5 de Zhipu (API officielle)
     * **Attention** : Nombreux fournisseurs tiers (ex : One API, New API) pour DeepSeek/Kimi/GLM utilisent actuellement le format OpenAI, pouvant causer des incompatibilités avec Claude Code.
   * **Gemini CLI** : Requiert des modèles Gemini de Google.
   * **Qwen Code** : Compatible avec les API au format OpenAI Chat Completions. Privilégiez **`Qwen3 Coder`** pour une génération de code optimale.
   * **OpenAI Codex** : Compatible avec les modèles GPT (ex : `gpt-4o`, `gpt-5`).
2. **Conflits de dépendances** :
   * Cherry Studio inclut un environnement Node.js isolé pour garantir un fonctionnement sans conflits.
   * En cas d'erreurs, déinstallez temporairement les dépendances globales (ex : Node.js) pour résoudre les conflits.
3. **Avertissement sur les tokens API** :
   * **Les agents de code consomment énormément de tokens**. Les tâches complexes peuvent entraîner une large sollicitation des API.
   * Contrôlez rigoureusement votre consommation en fonction de votre budget pour éviter les dépassements.

Ce tutoriel vous permettra de maîtriser rapidement la fonctionnalité puissante des agents de code de Cherry Studio !