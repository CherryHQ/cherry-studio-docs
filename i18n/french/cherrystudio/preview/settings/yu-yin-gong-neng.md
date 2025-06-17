---
hidden: True
icon: phone-arrow-up-right
---

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Fonctionnalités vocales

```
Guide d'utilisation des fonctionnalités vocales de Cherry Studio

I. Vue d'ensemble des fonctionnalités vocales

Cherry Studio propose trois modules vocaux principaux : TTS (synthèse vocale), ASR (reconnaissance vocale) et appels vocaux. Ces fonctionnalités vous permettent d'interagir naturellement avec l'IA par la voix, améliorant ainsi votre expérience.

- TTS (Text-to-Speech) : Convertit les réponses textuelles de l'IA en sortie audio
- ASR (Automatic Speech Recognition) : Convertit votre voix en texte d'entrée
- Appels vocaux : Combine TTS et ASR pour une expérience conversationnelle similaire à ChatGPT

II. Fonctionnalité TTS (Synthèse vocale)

1. Types de services pris en charge

Cherry Studio prend en charge quatre types de services TTS :

- OpenAI : Utilise l'API TTS d'OpenAI, nécessite une clé API
- TTS navigateur : Utilise la synthèse vocale intégrée au navigateur, gratuit sans configuration
- Siliconflow : Utilise le service TTS de Siliconflow, nécessite une clé API
- TTS en ligne gratuit : Service TTS gratuit, ne nécessite pas de clé API

2. Méthode de configuration

1) Accédez à la page des paramètres, sélectionnez l'onglet "Fonctionnalités vocales"
2) Dans le sous-onglet "TTS" :
   - Activez la fonction TTS (basculez l'interrupteur)
   - Sélectionnez le type de service TTS
   - Configurez les paramètres selon le service choisi :
     - OpenAI : Saisissez la clé API, l'URL API, sélectionnez la voix et le modèle
     - TTS navigateur : Sélectionnez la voix
     - Siliconflow : Saisissez la clé API, l'URL API, sélectionnez la voix, le modèle, le format de réponse et la vitesse
     - TTS en ligne gratuit : Sélectionnez la voix et le format de sortie
3) Configurez les options de filtrage TTS (optionnel) :
   - Filtrer le processus de réflexion
   - Filtrer les balises Markdown
   - Filtrer les blocs de code
4) Définissez l'affichage de la barre de progression TTS
5) Cliquez sur le bouton "Tester TTS" pour vérifier la configuration

3. Méthode d'utilisation

- Une fois le TTS activé, les réponses de l'IA sont automatiquement converties en audio
- Dans l'interface de chat, un bouton de lecture TTS apparaît sous chaque réponse
- Cliquez sur le bouton pour lire/mettre en pause l'audio
- Si la barre de progression est activée, elle s'affiche sous le texte
- Les textes longs sont synthétisés par segments et lus en continu

III. Fonctionnalité ASR (Reconnaissance vocale)

1. Types de services pris en charge

Cherry Studio prend en charge trois types de services ASR :

- OpenAI : Utilise le modèle Whisper d'OpenAI, nécessite une clé API
- Navigateur : Utilise la reconnaissance vocale intégrée au navigateur, gratuit sans configuration
- Serveur local : Se connecte à un serveur WebSocket local pour la reconnaissance vocale

2. Méthode de configuration

1) Accédez à la page des paramètres, sélectionnez l'onglet "Fonctionnalités vocales"
2) Dans le sous-onglet "ASR" :
   - Activez la fonction ASR (basculez l'interrupteur)
   - Sélectionnez le type de service ASR
   - Configurez les paramètres selon le service choisi :
     - OpenAI : Saisissez la clé API, l'URL API, sélectionnez le modèle
     - Navigateur : Aucune configuration supplémentaire nécessaire
     - Serveur local : Option de démarrage automatique du serveur ASR au lancement de l'application
   - Sélectionnez la langue de reconnaissance (par défaut : chinois)
3) Cliquez sur le bouton "Tester ASR" pour vérifier la configuration

3. Méthode d'utilisation

- Une fois l'ASR activé, un bouton de reconnaissance vocale apparaît à côté du champ de saisie
- Cliquez sur le bouton pour démarrer l'enregistrement
- Après avoir parlé, la voix est convertie en texte dans le champ de saisie
- Cliquez à nouveau sur le bouton pour arrêter l'enregistrement
- La reconnaissance prend en charge plusieurs phrases en mode accumulation continu

IV. Fonctionnalité d'appels vocaux

1. Caractéristiques

- Combine TTS et ASR pour une expérience conversationnelle type ChatGPT
- Interface flottante déplaçable
- Mode "Appuyer pour parler"
- Prise en charge des raccourcis personnalisés
- Fenêtre réductible
- Choix de modèles dédiés aux appels vocaux
- Messages contextuels personnalisables

2. Méthode de configuration

1) Accédez à la page des paramètres, sélectionnez l'onglet "Fonctionnalités vocales"
2) Dans le sous-onglet "Fonction d'appel" :
   - Activez la fonction d'appel vocal (basculez l'interrupteur)
   - Cliquez sur "Choisir un modèle" pour sélectionner le modèle IA utilisé
   - Personnalisez le message contextuel dans le champ dédié (optionnel)
   - Cliquez sur "Enregistrer" pour sauvegarder ou "Réinitialiser" pour restaurer le message par défaut

3. Méthode d'utilisation

1) Dans l'interface de chat, cliquez sur l'icône téléphone à droite du champ de saisie
2) La fenêtre d'appel vocal s'ouvre avec un message de bienvenue audio
3) Maintenez enfoncé le bouton "Appuyer pour parler" pour démarrer l'enregistrement (ou utilisez le raccourci)
4) Relâchez le bouton pour envoyer l'audio à l'IA
5) La réponse de l'IA est générée et lue via TTS
6) Utilisez les boutons de contrôle :
   - Bouton sourdine : contrôle la sortie audio
   - Bouton pause/reprise : interrompt ou continue la conversation
   - Bouton paramètres : configure les raccourcis
   - Bouton réduction : réduit la fenêtre à la ligne "Appuyer pour parler"
7) Cliquez sur le bouton de fermeture pour terminer l'appel

4. Configuration des raccourcis

1) Dans la fenêtre d'appel vocal, cliquez sur le bouton paramètres
2) Dans le panneau des paramètres, cliquez sur "Raccourcis"
3) Appuyez sur la touche souhaitée (espace, Maj, etc.)
4) Cliquez sur "Enregistrer"
5) Pour utiliser : maintenez la touche pour enregistrer, relâchez pour envoyer

V. Problèmes courants et solutions

1. Problèmes liés au TTS

- Problème : Aucun son produit
  Solution : Vérifiez l'activation du TTS, le type de service et les paramètres requis

- Problème : Mauvaise qualité audio
  Solution : Essayez différents services TTS ou voix

- Problème : Message d'erreur pendant la lecture
  Solution : Vérifiez la clé API et la connexion réseau

2. Problèmes liés à l'ASR

- Problème : La voix n'est pas reconnue
  Solution : Vérifiez l'activation de l'ASR, le type de service et les paramètres

- Problème : Faible précision de reconnaissance
  Solution : Changez de service ASR ou ajustez la position/volume du microphone

- Problème : Échec de connexion au serveur ASR
  Solution : Vérifiez l'état du serveur local ou redémarrez l'application

3. Problèmes liés aux appels vocaux

- Problème : Fenêtre d'appel ne s'ouvre pas
  Solution : Vérifiez l'activation de la fonction, et la configuration TTS/ASR

- Problème : Pas de réponse au "Appuyer pour parler"
  Solution : Vérifiez les autorisations du microphone ou redémarrez l'appel

- Problème : Pas de sortie audio des réponses IA
  Solution : Vérifiez l'activation du TTS et l'état de sourdine

VI. Paramètres avancés et options personnalisées

1. Paramètres TTS avancés

- Options de filtrage : Filtrez les processus de réflexion, les marqueurs Markdown et les blocs de code
- Affichage de la barre de progression
- Voix et modèles personnalisés : Ajoutez des voix et modèles personnalisés

2. Paramètres ASR avancés

- Démarrage automatique du serveur : Démarre le serveur ASR au lancement de l'application
- Sélection de la langue : Choix parmi différentes langues de reconnaissance

3. Paramètres d'appel vocal avancés

- Messages contextuels personnalisés : Guidez les réponses de l'IA pendant les appels
- Modèle dédié : Sélectionnez un modèle IA spécifique pour les appels
- Raccourcis personnalisés : Définissez vos propres raccourcis d'enregistrement

VII. Recommandations d'utilisation

1. Choix du service TTS :
   - Pour une haute qualité : OpenAI ou Siliconflow
   - Sans configuration API : TTS navigateur ou TTS en ligne gratuit

2. Choix du service ASR :
   - Pour une haute précision : OpenAI
   - Sans configuration API : Reconnaissance vocale du navigateur

3. Optimisez les appels vocaux :
   - Utilisez un casque pour éviter l'écho audio
   - Privilégiez les environnements calmes pour une meilleure reconnaissance
   - Personnalisez les messages contextuels pour adapter les réponses au format audio

4. Ajustez les paramètres selon vos besoins :
   - Communication textuelle principale : Activez uniquement le TTS
   - Saisie vocale principale : Activez uniquement l'ASR
   - Expérience conversationnelle complète : Activez les appels vocaux

Nous espérons que ce guide vous aidera à exploiter pleinement les fonctionnalités vocales de Cherry Studio pour une interaction IA plus naturelle et intuitive !
```