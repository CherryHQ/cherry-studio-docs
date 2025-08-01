---
icon: route
---
# Guide d'utilisation des traces


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Fonctionnalités

Les traces (« trace ») offrent aux utilisateurs une capacité d'analyse des conversations, permettant d'observer les performances spécifiques des modèles, bases de connaissances, MCP, recherches web, etc. pendant les dialogues. Il s'agit d'un outil d'observabilité basé sur [OpenTelemetry](https://opentelemetry.io/docs/languages/js/). Grâce à la collecte, au stockage et au traitement des données côté client, il permet une visualisation qui sert de base quantitative pour la résolution de problèmes et l'optimisation des résultats.

Chaque conversation correspond à une trace, composée de plusieurs spans. Chaque span représente une logique de traitement de Cherry Studio, telle qu'un appel à un modèle conversationnel, un appel MCP, une requête en base de connaissances ou une recherche web. La trace s'affiche en structure arborescente, les spans étant les nœuds. Les principales données incluent le temps d'exécution et la consommation de tokens, tandis que les détails d'un span montrent les entrées/sorties spécifiques.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Activation des traces

Par défaut, les traces sont cachées après l'installation de Cherry Studio. Pour les activer, accédez à "Paramètres" → "Paramètres généraux" → "Mode développeur", comme illustré ci-dessous :

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Les conversations antérieures ne génèrent pas de traces : seules les nouvelles interactions créent des enregistrements. Ceux-ci sont stockés localement. Pour effacer complètement les traces : 
1. Via l'interface : "Paramètres" → "Paramètres des données" → "Répertoire des données" → "Effacer le cache"
2. Manuellement : supprimez les fichiers du dossier `~/.cherrystudio/trace`

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Scénarios d'utilisation

### Consultation de la chaîne complète

Cliquez sur l'icône de trace dans l'interface de conversation pour visualiser l'intégralité du flux. Appels de modèles, recherches web, bases de connaissances ou MCP sont tous affichés dans la fenêtre de traces.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Analyse des modèles dans la trace

Pour examiner les détails d'un modèle, cliquez sur son nœud d'appel pour consulter les entrées/sorties.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Analyse des recherches web dans la trace

Cliquez sur le nœud de recherche web pour voir la requête lancée et les résultats retournés.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Analyse des bases de connaissances dans la trace

Cliquez sur le nœud de base de connaissances pour inspecter la question posée et la réponse générée.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Analyse des appels MCP dans la trace

Cliquez sur le nœud MCP pour visualiser les paramètres d'entrée et les retours du tool côté serveur.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Problèmes et suggestions

Cette fonctionnalité est fournie par l'équipe [EDAS](https://www.aliyun.com/product/edas) d'Alibaba Cloud. Pour toute question ou suggestion, rejoignez le groupe DingTalk (ID : 21958624) pour échanger avec les développeurs.

\