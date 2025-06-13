---
description: 数据设置→Obsidian配置
icon: gem
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Tutoriel de configuration d'Obsidian

Cherry Studio prend en charge l'intégration avec Obsidian, permettant d'exporter des conversations complètes ou des messages individuels vers votre base de connaissances Obsidian.

{% hint style="warning" %}
Cette procédure ne nécessite pas d'installation de plug-in Obsidian supplémentaire. Cependant, le mécanisme d'importation de Cherry Studio vers Obsidian étant similaire à Obsidian Web Clipper, nous recommandons de mettre à jour Obsidian vers sa dernière version (actuellement supérieure à **1.7.2**) pour éviter les [échecs d'importation dus aux conversations trop longues](https://github.com/obsidianmd/obsidian-clipper/releases/tag/0.7.0).
{% endhint %}

## Tutoriel récent

{% hint style="info" %}
Contrairement à l'ancienne version, la nouvelle fonction d'exportation vers Obsidian sélectionne automatiquement le chemin de la base de données, sans nécessiter la saisie manuelle du nom du coffre ou du dossier.
{% endhint %}

### Étape 1 : Configurer Cherry Studio

Ouvrez _Paramètres_ → _Paramètres des données_ → _Configuration Obsidian_ dans Cherry Studio. Les noms des coffres Obsidian ouverts localement apparaîtront automatiquement dans le menu déroulant. Sélectionnez votre coffre Obsidian cible :

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

### Étape 2 : Exporter les conversations

#### Exporter une conversation complète

Dans l'interface de conversation de Cherry Studio, cliquez droit sur une conversation, sélectionnez _Exporter_, puis _Exporter vers Obsidian_ :

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

Une fenêtre apparaît pour configurer les **Propriétés** de la note, son **emplacement** dans Obsidian et le **mode de traitement** :

* **Coffre** : Sélectionnez un autre coffre Obsidian via le menu déroulant
* **Chemin** : Choisissez le dossier de destination via le menu déroulant
* Propriétés de la note Obsidian :
  * Étiquettes (tags)
  * Date de création (created)
  * Source (source)
* **Modes de traitement** disponibles :
  * **Nouveau (remplace si existant)** : Crée une nouvelle note dans le dossier spécifié, écrasant toute note homonyme
  * **Préfixer** : Ajoute le contenu sélectionné au début de la note existante
  * **Ajouter** : Ajoute le contenu sélectionné à la fin de la note existante

{% hint style="info" %}
Seul le premier mode inclut les Propriétés. Les deux autres modes ne les incluent pas.
{% endhint %}

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption><p>Configurer les propriétés de la note</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption><p>Sélectionner le chemin</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption><p>Choisir le mode de traitement</p></figcaption></figure>

Après sélection des options, cliquez sur OK pour exporter la conversation complète vers le dossier correspondant de votre coffre Obsidian.

#### Exporter un message individuel

Cliquez sur le _menu à trois barres_ sous le message, sélectionnez _Exporter_ puis _Exporter vers Obsidian_ :

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption><p>Exporter un message individuel</p></figcaption></figure>

La même fenêtre de configuration que pour l'export complet apparaîtra. Suivez le [tutoriel ci-dessus](obsidian.md#dao-chu-wan-zheng-dui-hua) pour finaliser.

### Exportation réussie

🎉 Félicitations ! Vous avez terminé la configuration d'intégration Cherry Studio-Obsidian et effectué le processus complet d'exportation. Profitez-en !

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Exporter vers Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Voir le résultat de l'exportation</p></figcaption></figure>

***

## Ancien tutoriel (pour Cherry Studio \< v1.1.13)

### Étape 1 : Préparer Obsidian

Ouvrez votre coffre Obsidian et créez un dossier pour stocker les exports (exemple : dossier "Cherry Studio") :

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

Notez le texte encadré en bas à gauche : c'est votre nom de `coffre`.

### Étape 2 : Configurer Cherry Studio

Dans _Paramètres_ → _Paramètres des données_ → _Configuration Obsidian_ de Cherry Studio, saisissez le nom du `coffre` et du `dossier` obtenus à [l'étape 1](obsidian.md#di-yi-bu) :

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

Le champ `Étiquette globale` (optionnel) permet de définir un tag universel pour toutes les notes exportées.

### Étape 3 : Exporter les conversations

#### Exporter une conversation complète

Dans l'interface de conversation, cliquez droit sur une conversation, sélectionnez _Exporter_ puis _Exporter vers Obsidian_.

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption><p>Exporter une conversation complète</p></figcaption></figure>

Configurez les **Propriétés** de la note et le **mode de traitement** :
* **Nouveau (remplace si existant)** : Crée une note dans le dossier spécifié à l'étape 2
* **Préfixer** : Ajoute le contenu au début de la note existante
* **Ajouter** : Ajoute le contenu à la fin de la note existante

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption><p>Configurer les propriétés de la note</p></figcaption></figure>

{% hint style="info" %}
Seul le premier mode inclut les Propriétés. Les deux autres modes ne les incluent pas.
{% endhint %}

#### Exporter un message individuel

Cliquez sur le _menu à trois barres_ sous le message, sélectionnez _Exporter_ puis _Exporter vers Obsidian_.

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption><p>Exporter un message individuel</p></figcaption></figure>

Suivez le [tutoriel ci-dessus](obsidian.md#dao-chu-wan-zheng-dui-hua) pour finaliser la configuration.

### Exportation réussie

🎉 Félicitations ! Vous avez terminé la configuration d'intégration Cherry Studio-Obsidian et effectué le processus complet d'exportation. Profitez-en !

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption><p>Exporter vers Obsidian</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption><p>Voir le résultat de l'exportation</p></figcaption></figure>