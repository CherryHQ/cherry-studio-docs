---
icon: book-bookmark
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Science et Connaissances

## Que sont les tokens ?

Les tokens sont les unités fondamentales utilisées par les modèles d'IA pour traiter le texte. On peut les comprendre comme les plus petites unités de "pensée" du modèle. Ils ne correspondent pas exactement aux caractères ou mots tels que nous les concevons, mais représentent une méthode de segmentation textuelle propre au modèle.

#### 1. Segmentation du chinois
* Un caractère chinois est généralement encodé sur 1-2 tokens
* Exemple : `"你好"` ≈ 2-4 tokens

#### 2. Segmentation de l'anglais
* Les mots courants occupent généralement 1 token
* Les mots longs ou peu communs sont décomposés en plusieurs tokens
* Exemples :
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Caractères spéciaux
* Les espaces, signes de ponctuation consomment aussi des tokens
* Un saut de ligne correspond généralement à 1 token

{% hint style="info" %}
Les Tokenizer varient selon les fournisseurs de services, et même entre différents modèles d'un même fournisseur. Ces informations servent uniquement à clarifier le concept de token.
{% endhint %}

***

## Qu'est-ce qu'un Tokenizer ?

Le Tokenizer (système de segmentation) est l'outil qui permet aux modèles d'IA de convertir le texte en tokens. Il détermine comment découper le texte en unités minimales compréhensibles par le modèle.

### Pourquoi les Tokenizer diffèrent-ils selon les modèles ?

#### 1. Données d'entraînement différentes
* Corpus différents entraînent des optimisations distinctes
* Prise en charge multilingue variable
* Optimisations spécifiques à certains domaines (médical, juridique, etc.)

#### 2. Algorithmes de segmentation différents
* BPE (Byte Pair Encoding) - Série GPT d'OpenAI
* WordPiece - Google BERT
* SentencePiece - Adapté aux scénarios multilingues

#### 3. Objectifs d'optimisation différents
* Certains privilégient l'efficacité de compression
* D'autres la préservation sémantique
* D'autres encore la vitesse de traitement

### Impact pratique
Un même texte peut produire un nombre différent de tokens selon les modèles :
```
Entrée : "Hello, world!"
GPT-3: 4 tokens
BERT: 3 tokens
Claude: 3 tokens
```

***

## Qu'est-ce qu'un Modèle d'Incorporation (Embedding Model) ?

**Concept fondamental :** Un modèle d'incorporation transforme des données discrètes de haute dimension (texte, images) en vecteurs continus de basse dimension, permettant aux machines de mieux comprendre et traiter des données complexes. Imaginez simplifier un puzzle complexe en un point de coordonnées qui préserve les caractéristiques essentielles. Dans l'écosystème des grands modèles, il agit comme un "traducteur" convertissant des informations compréhensibles par l'homme en formes numériques utilisables par l'IA.

**Mode de fonctionnement :** Dans le traitement du langage naturel, les modèles d'incorporation mappent les mots vers des positions spécifiques dans un espace vectoriel. Les mots sémantiquement proches s'y regroupent naturellement :
* Les vecteurs de "roi" et "reine" seront proches
* Les termes comme "chat" et "chien" resteront voisins
* Des mots sans lien sémantique comme "voiture" et "pain" seront éloignés

**Applications principales :**
* Analyse textuelle : classification de documents, analyse des sentiments
* Systèmes de recommandation : suggestions de contenu personnalisé
* Traitement d'images : recherche d'images similaires
* Moteurs de recherche : optimisation de la recherche sémantique

**Avantages clés :**
1. Réduction dimensionnelle : simplification des données complexes
2. Préservation sémantique : conservation des informations essentielles
3. Efficacité computationnelle : accélération significative de l'entraînement et de l'inférence

**Valeur technique :** Les modèles d'incorporation sont des composants fondamentaux des systèmes d'IA modernes, fournissant des représentations de haute qualité qui alimentent les progrès en traitement du langage naturel et vision par ordinateur.

***

## Fonctionnement des modèles d'incorporation dans la recherche de connaissances

**Processus principal :**

1. **Prétraitement de la base de connaissances**
* Segmentation des documents en morceaux (chunks) appropriés
* Conversion de chaque morceau en vecteur via le modèle d'incorporation
* Stockage des vecteurs et textes originaux dans une base de données vectorielle

2. **Traitement des requêtes**
* Conversion de la question utilisateur en vecteur
* Recherche de contenu similaire dans la base vectorielle
* Fourniture du contenu pertinent comme contexte au LLM

***

## Qu'est-ce que le MCP (Model Context Protocol) ?

Le MCP est un protocole open source conçu pour fournir du contexte aux modèles de langage (LLM) de manière standardisée.

* **Analogie :** Imaginez le MCP comme une "clé USB" pour l'IA. De même qu'une clé USB stocke divers fichiers pour un accès immédiat sur ordinateur, un serveur MCP peut "brancher" des "plugins" contextuels que les LLM peuvent solliciter pour enrichir leurs capacités.
* **Comparaison avec les Function Tool :** Contrairement aux outils fonctionnels traditionnels qui répondent à des tâches spécifiques, le MCP offre une abstraction supérieure - un mécanisme modulaire et universel d'acquisition de contexte.

### Avantages clés du MCP
1. **Standardisation :** Interface et format de données unifiés pour une collaboration fluide
2. **Modularité :** Information contextuelle décomposable en modules (plugins) indépendants
3. **Flexibilité :** Sélection dynamique des plugins contextuels par les LLM
4. **Évolutivité :** Conception extensible pour de nouveaux types de plugins contextuels