
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Ollama

Ollama est un excellent outil open source qui vous permet d'exécuter et de gérer facilement divers grands modèles de langage (LLM) localement. Cherry Studio prend désormais en charge l'intégration d'Ollama, vous permettant d'interagir directement avec des LLM déployés localement dans une interface familière, sans dépendre de services cloud !

## Qu'est-ce qu'Ollama ?

Ollama est un outil qui simplifie le déploiement et l'utilisation des grands modèles de langage (LLM). Il présente les caractéristiques suivantes :

* **Exécution locale :** Les modèles fonctionnent entièrement sur votre ordinateur local, sans nécessiter de connexion internet, protégeant ainsi votre vie privée et la sécurité des données.
* **Simplicité d'utilisation :** Téléchargez, exécutez et gérez divers LLM grâce à des simples commandes terminal.
* **Modèles variés :** Prend en charge de nombreux modèles open source populaires comme Llama 2, Deepseek, Mistral, Gemma et autres.
* **Multiplateforme :** Compatible avec macOS, Windows et Linux.
* **API ouverte :** Propose une interface compatible avec OpenAI, permettant une intégration avec d'autres outils.

## Pourquoi utiliser Ollama dans Cherry Studio ?

* **Sans service cloud :** Libérez-vous des quotas et frais des API cloud en profitant pleinement de la puissance des LLM locaux.
* **Confidentialité des données :** Toutes vos données de conversation restent locales, éliminant les risques de fuite d'informations.
* **Utilisation hors-ligne :** Continuez à interagir avec les LLM même sans connexion internet.
* **Personnalisation :** Choisissez et configurez le LLM le plus adapté à vos besoins spécifiques.

## Configuration d'Ollama dans Cherry Studio

### **1. Installation et exécution d'Ollama**

Commencez par installer et exécuter Ollama sur votre ordinateur :

* **Téléchargez Ollama :** Rendez-vous sur le site officiel d'Ollama ([https://ollama.com/](https://ollama.com/)) et téléchargez le package d'installation correspondant à votre système d'exploitation.
  
  Sur Linux, installez Ollama directement via la commande :

  ```sh
  curl -fsSL https://ollama.com/install.sh | sh
  ```
* **Installez Ollama :** Suivez les instructions de l'installateur.
* **Téléchargez un modèle :** Ouvrez le terminal (ou l'invite de commande), puis utilisez `ollama run` pour télécharger le modèle souhaité. Par exemple, pour Llama 2 :
  
  ```sh
  ollama run llama3.2
  ```
  
  Ollama téléchargera et exécutera automatiquement le modèle.
* **Maintenez Ollama actif :** Gardez Ollama en fonctionnement pendant vos interactions avec les modèles via Cherry Studio.

### **2. Ajout d'Ollama comme fournisseur de services dans Cherry Studio**

Ajoutez ensuite Ollama en tant que fournisseur d'IA personnalisé :

* **Ouvrez les paramètres :** Cliquez sur l'icône "Paramètres" (engrenage) dans la barre de navigation gauche.
* **Accédez aux services de modèles :** Sélectionnez l'onglet "Services de modèles".
* **Ajoutez un fournisseur :** Cliquez sur Ollama dans la liste.

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt=""><figcaption></figcaption></figure>

### **3. Configuration du fournisseur Ollama**

Configurez Ollama dans la liste des fournisseurs :

1. **Statut d'activation :**
   * Assurez-vous que l'interrupteur à droite est activé (position "ON").
2. **Clé API :**
   * Ollama ne nécessite généralement **pas** de clé API. Laissez ce champ vide ou saisissez n'importe quelle valeur.
3. **Adresse API :**
   *    Renseignez l'adresse API locale d'Ollama. L'adresse standard est :
        
        ```
        http://localhost:11434/
        ```
        
        (Modifiez si vous avez changé le port).
4. **Durée de maintien actif :** Durée d'inactivité (en minutes) avant que Cherry Studio ne ferme automatiquement la session Ollama pour libérer les ressources.
5. **Gestion des modèles :**
   * Cliquez sur "+ Ajouter" pour saisir manuellement les noms des modèles Ollama téléchargés.
   * Exemple : si vous avez exécuté `ollama run llama3.2`, saisissez `llama3.2`.
   * Utilisez le bouton "Gérer" pour modifier ou supprimer des modèles existants.

## Commencer à utiliser

Une fois configuré, sélectionnez Ollama dans l'interface de chat de Cherry Studio, choisissez votre modèle téléchargé, et démarrez votre conversation locale avec le LLM !

## Conseils pratiques

* **Premier lancement d'un modèle :** Le premier chargement nécessite un téléchargement initial qui peut être long (selon la taille du modèle).
* **Liste des modèles :** Exécutez `ollama list` dans le terminal pour voir vos modèles Ollama disponibles.
* **Configuration matérielle :** Les LLM exigent des ressources substantielles (CPU, RAM, GPU). Vérifiez la compatibilité de votre matériel.
* **Documentation d'Ollama :** Cliquez sur `Voir la documentation et modèles d'Ollama` dans la page de configuration pour accéder directement à la documentation officielle.