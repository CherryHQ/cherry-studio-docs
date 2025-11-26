---
icon: database
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Notes sur le stockage des données

Toutes les données ajoutées à la base de connaissances de Cherry Studio sont stockées localement. Lors de l'ajout, une copie du document est placée dans le répertoire de stockage des données de Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Diagramme du processus de traitement de la base de connaissances</p></figcaption></figure>

Base de données vectorielle : [https://turso.tech/libsql](https://turso.tech/libsql)

Lorsqu'un document est ajouté à la base de connaissances de Cherry Studio, il est découpé en plusieurs segments. Ces segments sont ensuite traités par un modèle d'incorporation.

Lors de l'utilisation d'un grand modèle pour des questions-réponses, les segments de texte pertinents pour la question sont recherchés et transmis ensemble au grand modèle de langage pour traitement.

Si vous avez des exigences concernant la confidentialité des données, il est recommandé d'utiliser une base de données d'incorporation locale et un grand modèle de langage local.