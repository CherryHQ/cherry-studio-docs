---
description: Tools
icon: code
---
# Tutoriel d'utilisation de Code Tools


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




La version Cherry Studio v1.5.7 introduit une fonctionnalité puissante et simple d'utilisation : Code Agent, permettant de démarrer et gérer directement divers agents de programmation IA. Ce tutoriel vous guidera à travers le processus complet de configuration et de démarrage.

***

### Étapes opérationnelles

#### 1. Mettez à jour Cherry Studio

Assurez-vous d'abord que votre Cherry Studio est mis à jour vers la version **v1.5.7** ou supérieure. Vous pouvez télécharger la dernière version sur [GitHub Releases](https://github.com/CherryHQ/cherry-studio/releases) ou le site officiel.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### 2. Ajustez la position de la barre de navigation

Pour faciliter l'utilisation des onglets supérieurs, nous recommandons de positionner la barre de navigation en haut.

* Chemin d'accès : `Paramètres` -> `Paramètres d'affichage` -> `Configuration de la barre de navigation`
* Définissez l'option "Position de la barre de navigation" sur **`Haut`**.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 3. Créez un nouvel onglet

Cliquez sur l'icône "+" en haut de l'interface pour créer un nouvel onglet vierge.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

#### 4. Activez la fonction Code Agent

Dans le nouvel onglet, cliquez sur l'icône `Code` (ou `</>`) pour accéder à l'interface de configuration de Code Agent.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

#### 5. Sélectionnez un outil CLI

Choisissez un outil Code Agent selon vos besoins et votre clé API disponible. Actuellement pris en charge :

* **Claude Code**
* **Gemini CLI**
* **Qwen Code**
* **OpenAI Codex**

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 6. Sélectionnez le modèle pour l'Agent

Dans la liste déroulante des modèles, choisissez un modèle compatible avec l'outil CLI sélectionné. _(Consultez les "Remarques importantes" ci-dessous pour la compatibilité détaillée)_

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### 7. Spécifiez le répertoire de travail

Cliquez sur "Sélectionner un répertoire" pour définir un espace de travail pour l'Agent. Celui-ci aura accès à tous les fichiers et sous-répertoires pour comprendre le contexte du projet.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### 8. Configurez les variables d'environnement

* **Configuration automatique** : Vos choix aux étapes 6 (modèle) et 7 (répertoire) génèrent automatiquement les variables correspondantes.
* **Ajout personnalisé** : Ajoutez des variables spécifiques si nécessaire (ex: `PROXY_URL`).

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### 9. Options de mise à jour

* **Exécutables intégrés** : Cherry Studio inclut tous les exécutables Code Agent, utilisables hors connexion.
* **Mise à jour automatique** : Cochez **`Vérifier les mises à jour et installer la dernière version`** pour maintenir l'Agent à jour.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

#### 10. Lancez l'Agent

Après configuration, cliquez sur **`Démarrer`**. Cherry Studio ouvrira le Terminal système avec les variables chargées, exécutant le Code Agent sélectionné. Interagissez avec l'Agent IA dans la fenêtre de terminal.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

### Remarques importantes

1. **Compatibilité des modèles** :
   * **Claude Code** : Requiert des modèles supportant le format API Anthropic :
     * Modèles Claude
     * DeepSeek V3.1 (plateforme officielle)
     * Kimi K2 (plateforme officielle)
     * GLM 4.5 de Zhipu (plateforme officielle)
     * **Attention** : Les fournisseurs tiers (One API, New API...) utilisent souvent le format OpenAI pour DeepSeek/Kimi/GLM, incompatible avec Claude Code.
   * **Gemini CLI** : Requiert les modèles Gemini de Google.
   * **Qwen Code** : Supporte le format OpenAI Chat Completions. Recommandé : **`Qwen3 Coder`**.
   * **OpenAI Codex** : Supporte les modèles GPT (ex: `gpt-4o`, `gpt-5`).
   
2. **Conflits de dépendances** :
   * Cherry Studio intègre un environnement Node.js isolé pour éviter les conflits.
   * En cas d'erreurs, désinstallez les dépendances globales (Node.js, outils système).
   
3. **Consommation de tokens API** :
   * **Les Code Agents consomment énormément de tokens**. Les tâches complexes génèrent de nombreuses requêtes.
   * Surveillez votre quota API et budget pour éviter les dépassements.

Ce tutoriel vous aidera à maîtriser rapidement les puissantes fonctionnalités Code Agent de Cherry Studio !