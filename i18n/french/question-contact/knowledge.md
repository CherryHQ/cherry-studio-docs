---
icon: book-bookmark
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Vulgarisation des connaissances

## Que sont les tokens ?

Les tokens sont l'unité fondamentale de traitement du texte par les modèles d'IA, on peut les comprendre comme les plus petites unités de "pensée" du modèle. Ils ne correspondent pas exactement aux caractères ou mots tels que nous les concevons, mais représentent plutôt une méthode particulière de segmentation du texte spécifique au modèle.

#### 1. Segmentation du chinois
* Un caractère chinois est généralement encodé en 1-2 tokens
* Par exemple : `"你好"` ≈ 2-4 tokens

#### 2. Segmentation de l'anglais
* Les mots courants représentent généralement 1 token
* Les mots longs ou peu courants sont décomposés en plusieurs tokens
* Par exemple :
  * `"hello"` = 1 token
  * `"indescribable"` = 4 tokens

#### 3. Caractères spéciaux
* Les espaces, signes de ponctuation occupent également des tokens
* Un saut de ligne représente généralement 1 token

{% hint style="info" %}
Les Tokenizers varient selon les fournisseurs de services, et peuvent même différer entre les modèles d'un même fournisseur. Ces explications visent uniquement à clarifier le concept de token.
{% endhint %}

***

## Qu'est-ce qu'un Tokenizer ?

Le Tokenizer (outil de segmentation) est l'outil qui permet aux modèles d'IA de convertir du texte en tokens. Il détermine comment découper le texte d'entrée en unités minimales compréhensibles par le modèle.

### Pourquoi les Tokenizers diffèrent-ils selon les modèles ?

#### 1. Données d'entraînement différentes
* Corpus différents entraînant des optimisations distinctes
* Prise en charge variable des langues multiples
* Optimisations spécifiques à certains domaines (médical, juridique, etc.)

#### 2. Algorithmes de segmentation différents
* BPE (Byte Pair Encoding) - Série GPT d'OpenAI
* WordPiece - Google BERT
* SentencePiece - Adapté aux scénarios multilingues

#### 3. Objectifs d'optimisation différents
* Certains privilégient la compression
* D'autres la préservation sémantique
* D'autres encore la vitesse de traitement

### Impact concret

Un même texte peut produire différents nombres de tokens selon les modèles :

```
Entrée : "Hello, world!"
GPT-3 : 4 tokens
BERT : 3 tokens
Claude : 3 tokens
```

***

## Qu'est-ce qu'un modèle d'embedding (Embedding Model) ?

**Concept de base :** Un modèle d'embedding est une technique convertissant des données discrètes dimensionnelles élevées (texte, images...) en vecteurs continus de basse dimension. Cette conversion permet aux machines de mieux comprendre et traiter des données complexes. Imaginez transformer un puzzle complexe en un simple point de coordonnées qui conserve les caractéristiques clés du puzzle. Dans l'écosystème des grands modèles, il agit comme un "traducteur", transformant des informations humainement compréhensibles en formes numériques calculables par l'IA.

**Mode de fonctionnement :** En traitement du langage naturel, le modèle d'embedding projette les mots dans un espace vectoriel où les termes sémantiquement proches se regroupent naturellement. Par exemple :
* Les vecteurs de "roi" et "reine" seront proches
* Les termes comme "chat" et "chien" formeront un autre groupe
* Des mots sans lien sémantique comme "voiture" et "pain" seront éloignés

**Principaux scénarios d'application :**
* Analyse de texte : classification documentaire, analyse des sentiments
* Systèmes de recommandation : suggestions de contenu personnalisées
* Traitement d'images : recherche d'images similaires
* Moteurs de recherche : optimisation de la recherche sémantique

**Avantages clés :**
1. Réduction dimensionnelle : simplification des données complexes
2. Cohérence sémantique : préservation des informations sémantiques essentielles
3. Efficacité computationnelle : accélération significative de l'entraînement et de l'inférence

**Valeur technique :** Les modèles d'embedding sont des composants fondamentaux des systèmes d'IA modernes. Ils fournissent des représentations de données de haute qualité pour les tâches d'apprentissage automatique, constituant une technologie clé dans le développement du traitement du langage naturel et de la vision par ordinateur.

***

## Fonctionnement du modèle d'Embedding dans la recherche de connaissances

**Flux de travail de base :**

1. **Phase de prétraitement de la base de connaissances**
* Segmentation des documents en chunks (blocs de texte) appropriés
* Conversion de chaque chunk en vecteur via le modèle d'embedding
* Stockage des vecteurs et du texte original dans une base de données vectorielle

2. **Phase de traitement des requêtes**
* Conversion de la question utilisateur en vecteur
* Recherche de contenu similaire dans la base vectorielle
* Fourniture des résultats pertinents comme contexte au LLM

***

## Qu'est-ce que MCP (Model Context Protocol) ?

MCP est un protocole open source visant à fournir des informations contextuelles aux grands modèles de langage (LLM) de manière standardisée.

* **Analogie :** Imaginez MCP comme une "clé USB" pour l'IA. De même qu'une clé USB stocke divers fichiers accessibles sur ordinateur, le serveur MCP peut "brancher" différents "plugins" contextuels. Les LLM peuvent ainsi accéder à ces composants selon leurs besoins, enrichissant leurs capacités par un contexte élargi.
* **Comparaison avec les outils fonctionnels :** Les outils fonctionnels traditionnels étendent les capacités des LLM, mais MCP propose une abstraction de niveau supérieur. Alors que les outils fonctionnels sont spécifiques à certaines tâches, MCP offre un mécanisme contextuel modulaire et universel.

### **Avantages clés de MCP**

1. **Standardisation :** Interface et format de données unifiés pour une collaboration transparente
2. **Modularité :** Décomposition de l'information contextuelle en modules indépendants (plugins)
3. **Flexibilité :** Sélection dynamique des plugins contextuels par les LLM
4. **Évolutivité :** Architecture ouverte à de nouveaux types de plugins contextuels

***