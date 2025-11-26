---
hidden: True
icon: code
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Structure du Code

```yaml
...
├─ docs/ # Répertoire de documentation
├─ resources/ # Répertoire des fichiers de ressources
├─ scripts/ # Répertoire des fichiers de script
└─ src/ # Répertoire principal du code source
    ├─main/ # Code du processus principal
    ├─preload/ # Répertoire des scripts de préchargement
    └─renderer/ # Code du processus de rendu
        ├─src/ # Code source du processus de rendu
            ├─assets/ # Fichiers de ressources
                ├─fonts/ # Fichiers de polices
                ├─images/ # Avatars et autres fichiers image
                └─styles/ # Fichiers de style
            ├─components/ # Composants
            ├─config/ # Fichiers de configuration
            ├─context/ # Contexte
            ├─databases/ # Fichiers liés aux bases de données
            ├─hooks/ # Hooks personnalisés
            ├─i18n/ # Fichiers d'internationalisation
            ├─pages/ # Fichiers de pages
            ├─providers/ # Configuration liée aux fournisseurs de services
            ├─services/ # Fichiers de service
            ├─store/ # Fichiers de gestion d'état
            ├─types/ # Fichiers de définition de types TypeScript
            ├─utils/ # Fonctions utilitaires
            ...
        ...
    ...
...

```