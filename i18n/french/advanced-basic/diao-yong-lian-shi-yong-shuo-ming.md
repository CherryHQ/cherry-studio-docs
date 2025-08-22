---
icon: route
---
# Guide d'utilisation des traces


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Fonctionnalité

Les traces (également appelées "traces") offrent aux utilisateurs une capacité d'analyse des conversations, leur permettant d'observer les performances spécifiques des modèles, bases de connaissances, MCP, recherche web, etc., pendant le dialogue. Il s'agit d'un outil d'observabilité basé sur [OpenTelemetry](https://opentelemetry.io/docs/languages/js/), qui visualise les données collectées, stockées et traitées côté client, fournissant des mesures quantitatives pour identifier les problèmes et optimiser les performances.

Chaque conversation correspond à une trace. Une trace est composée de plusieurs spans, chaque span correspondant à une logique de traitement du Cherry Studio telle que : appel de session de modèle, appel MCP, interrogation de base de connaissances, recherche web, etc. La trace s'affiche sous forme d'arborescence où les spans sont des nœuds, montrant principalement le temps d'exécution et l'utilisation de tokens. Le détail d'une span permet également de consulter ses entrées/sorties spécifiques.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Activation des traces

Par défaut, après l'installation de Cherry Studio, les traces sont masquées. Activez-les dans "Paramètres" → "Paramètres généraux" → "Mode développeur" comme ci-dessous :

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Les conversations précédentes ne génèrent pas d'enregistrements de trace. Les traces ne sont créées qu'à partir des nouvelles questions. Les enregistrements sont stockés localement. Pour supprimer complètement les traces : 
- Via "Paramètres" → "Paramètres des données" → "Répertoire des données" → "Effacer le cache"
- Ou manuellement en supprimant les fichiers du dossier `~/.cherrystudio/trace`

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Cas d'utilisation

### Vue complète de la chaîne

Cliquez sur l'icône de trace dans la fenêtre de conversation pour voir l'ensemble de la chaîne d'appels. Vous visualisez toutes les interactions : modèles, recherche web, bases de connaissances ou MCP.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Détail des appels de modèles

Cliquez sur un nœud d'appel de modèle pour voir le détail de ses entrées/sorties.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Détail des recherches web

Cliquez sur un nœud de recherche web pour voir la requête envoyée et les résultats obtenus.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Détail des bases de connaissances

Cliquez sur un nœud de base de connaissances pour consulter la question posée et la réponse retournée.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Détail des appels MCP

Cliquez sur un nœud MCP pour voir les paramètres d'entrée du serveur d'outil et les données renvoyées.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Problèmes et suggestions

Cette fonctionnalité est fournie par l'équipe [EDAS](https://www.aliyun.com/product/edas) d'Alibaba Cloud. Pour toute question ou suggestion, rejoignez le groupe DingTalk (ID : 21958624) pour discuter directement avec les développeurs.

\