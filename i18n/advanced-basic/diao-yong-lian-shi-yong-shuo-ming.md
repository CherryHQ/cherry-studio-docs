---
icon: route
---
# Guide d'utilisation de la chaîne d'appel


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




## Fonctionnalités

La chaîne d'appel (également appelée "trace") offre aux utilisateurs une capacité d'analyse des conversations, leur permettant d'observer les performances spécifiques des modèles, des bases de connaissances, du MCP, des recherches Internet et d'autres composants pendant le dialogue. Il s'agit d'un outil d'observabilité basé sur [OpenTelemetry](https://opentelemetry.io/docs/languages/js/) qui collecte, stocke et traite les données côté client pour une visualisation, fournissant une base d'évaluation quantitative pour localiser les problèmes et optimiser les performances.

Chaque conversation correspond à une donnée de trace. Une trace est composée de plusieurs spans, chaque span correspondant à une logique de traitement de programme dans Cherry Studio, comme l'appel d'une session de modèle, l'appel du MCP, l'appel d'une base de connaissances ou l'appel d'une recherche Internet. La trace est présentée sous forme d'arborescence où les spans sont les nœuds, affichant les principales données telles que le temps d'exécution et la consommation de tokens. Dans le détail d'un span, vous pouvez également consulter ses entrées et sorties spécifiques.

<figure><img src="../.gitbook/assets/trace2.gif" alt=""><figcaption></figcaption></figure>

## Activer Trace

Par défaut, après l'installation de Cherry Studio, la fonction Trace est cachée. Vous devez l'activer dans "Paramètres" > "Paramètres généraux" > "Mode développeur", comme illustré ci-dessous :

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

Les conversations antérieures ne généreront pas d'enregistrements Trace. Les enregistrements ne sont créés qu'après de nouveaux échanges question-réponse. Les enregistrements générés sont stockés localement. Pour supprimer complètement les traces, vous pouvez utiliser "Paramètres" > "Paramètres des données" > "Répertoire de données" > "Effacer le cache", ou supprimer manuellement les fichiers dans ~/.cherrystudio/trace, comme montré ci-dessous :

<figure><img src="../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>

## Scénarios d'utilisation

### Visualisation complète de la chaîne

Cliquez sur la chaîne d'appel dans la boîte de dialogue Cherry Studio pour afficher les données complètes de la chaîne. Que des modèles, des recherches Internet, des bases de connaissances ou du MCP soient appelés pendant la conversation, toutes les données d'appel de la chaîne complète sont visibles dans la fenêtre de la chaîne d'appel.

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

### Visualisation des modèles dans la chaîne

Pour consulter les détails d'un modèle dans la chaîne d'appel, cliquez sur le nœud d'appel du modèle afin d'afficher ses entrées et sorties spécifiques.

<figure><img src="../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

### Visualisation des recherches Internet dans la chaîne

Pour consulter les détails d'une recherche Internet dans la chaîne d'appel, cliquez sur le nœud de recherche Internet afin d'afficher ses entrées et sorties spécifiques. Dans les détails, vous pouvez voir la requête envoyée et les résultats retournés.

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

### Visualisation des bases de connaissances dans la chaîne

Pour consulter les détails d'une base de connaissances dans la chaîne d'appel, cliquez sur le nœud de la base de connaissances afin d'afficher ses entrées et sorties spécifiques. Dans les détails, vous pouvez voir la requête envoyée et la réponse retournée.

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

### Visualisation des appels MCP dans la chaîne

Pour consulter les détails d'un appel MCP dans la chaîne d'appel, cliquez sur le nœud d'appel MCP afin d'afficher ses entrées et sorties spécifiques. Dans les détails, vous pouvez voir les paramètres d'entrée passés au tool du serveur MCP et la réponse du tool.

<figure><img src="../.gitbook/assets/image (153).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

## Problèmes et suggestions

Cette fonctionnalité est actuellement fournie par l'équipe [EDAS](https://www.aliyun.com/product/edas) d'Alibaba Cloud. Si vous rencontrez des problèmes ou avez des suggestions, veuillez rejoindre le groupe DingTalk (ID de groupe : 21958624) pour discuter en profondeur avec les développeurs.