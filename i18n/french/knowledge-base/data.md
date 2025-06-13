---
icon: database
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Instructions de stockage des données

Toutes les données ajoutées dans la base de connaissances de Cherry Studio sont stockées localement. Lors de l'ajout, une copie du document est placée dans le répertoire de stockage des données de Cherry Studio.

<figure><img src="../.gitbook/assets/mermaid-diagram-1739241680067.png" alt=""><figcaption><p>Diagramme de traitement de la base de connaissances</p></figcaption></figure>

Base de données vectorielle : [https://turso.tech/libsql](https://turso.tech/libsql)

Après l'ajout d'un document à la base de connaissances de Cherry Studio, celui-ci est découpé en plusieurs fragments qui sont ensuite traités par le modèle d'incorporation.

Lors de l'utilisation d'un grand modèle linguistique pour les questions-réponses, les fragments de texte pertinents pour la question sont recherchés et transmis au modèle pour traitement.

Si vous avez des exigences en matière de confidentialité des données, il est recommandé d'utiliser une base de données d'incorporation locale et un grand modèle linguistique local.