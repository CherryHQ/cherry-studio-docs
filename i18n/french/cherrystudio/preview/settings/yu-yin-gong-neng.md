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

1. Présentation des fonctionnalités vocales

Cherry Studio propose trois modules vocaux principaux : TTS (Synthèse vocale), ASR (Reconnaissance vocale) et Appel vocal. Ces fonctionnalités vous permettent d'interagir naturellement avec l'IA par la voix, améliorant ainsi votre expérience utilisateur.

- TTS (Text-to-Speech) : Convertit les réponses textuelles de l'IA en sortie vocale
- ASR (Automatic Speech Recognition) : Convertit votre voix en saisie texte
- Appel vocal : Combine TTS et ASR pour une expérience conversationnelle similaire à ChatGPT

2. Fonction TTS (Synthèse vocale)

1. Types de services pris en charge

Cherry Studio prend en charge quatre types de services TTS :

- OpenAI : Utilise l'API TTS d'OpenAI (nécessite une clé API)
- TTS navigateur : Utilise la synthèse vocale intégrée au navigateur (gratuit, aucune configuration)
- Siliconflow : Utilise le service TTS de Siliconflow (nécessite une clé API)
- TTS en ligne gratuit : Service TTS gratuit sans clé API

2. Méthode de configuration

1) Accédez à la page des paramètres et sélectionnez l'onglet "Fonctions vocales"
2) Dans le sous-onglet "TTS" :
   - Activez la fonction TTS (activez le commutateur)
   - Sélectionnez le type de service TTS
   - Configurez les paramètres en fonction du service choisi :
     - OpenAI : Saisissez la clé API, l'adresse API, sélectionnez la voix et le modèle
     - TTS navigateur : Sélectionnez la voix
     - Siliconflow : Saisissez la clé API, l'adresse API, sélectionnez la voix, le modèle, le format de réponse et la vitesse
     - TTS en ligne gratuit : Sélectionnez la voix et le format de sortie
3) Configurez les options de filtrage TTS (optionnel) :
   - Filtrer les processus de réflexion
   - Filtrer les balises Markdown
   - Filtrer les blocs de code
4) Définissez l'affichage ou non de la barre de progression TTS
5) Cliquez sur le bouton "Tester TTS" pour vérifier la configuration

3. Mode d'utilisation

- Une fois activé, les réponses de l'IA sont automatiquement converties en sortie vocale
- Un bouton de lecture TTS apparaît sous chaque réponse de l'IA dans l'interface de chat
- Cliquez sur le bouton pour lire/mettre en pause la voix
- Si activée, la barre de progression TTS s'affiche sous le texte
- Les textes longs sont synthétisés et lus en segments continus

3. Fonction ASR (Reconnaissance vocale)

1. Types de services pris en charge

Cherry Studio prend en charge trois types de services ASR :

- OpenAI : Utilise le modèle Whisper d'OpenAI (nécessite une clé API)
- Navigateur : Utilise la reconnaissance vocale intégrée au navigateur (gratuit, aucune configuration)
- Serveur local : Se connecte à un serveur WebSocket local pour la reconnaissance vocale

2. Méthode de configuration

1) Accédez à la page des paramètres et sélectionnez l'onglet "Fonctions vocales"
2) Dans le sous-onglet "ASR" :
   - Activez la fonction ASR (activez le commutateur)
   - Sélectionnez le type de service ASR
   - Configurez les paramètres en fonction du service choisi :
     - OpenAI : Saisissez la clé API, l'adresse API, sélectionnez le modèle
     - Navigateur : Aucune configuration supplémentaire
     - Serveur local : Option pour démarrer automatiquement le serveur ASR au lancement
   - Sélectionnez la langue de reconnaissance vocale (par défaut : chinois)
3) Cliquez sur le bouton "Tester ASR" pour vérifier la configuration

3. Mode d'utilisation

- Une fois activé, un bouton de reconnaissance vocale apparaît à côté de la zone de saisie
- Cliquez sur le bouton pour démarrer l'enregistrement
- Après avoir parlé, votre voix est convertie en texte dans la zone de saisie
- Cliquez à nouveau pour arrêter l'enregistrement
- Prise en charge de la reconnaissance continue de plusieurs phrases en mode cumulatif

4. Appel vocal

1. Caractéristiques

- Combine TTS et ASR pour une expérience conversationnelle similaire à ChatGPT
- Interface fenêtrée flottante et déplaçable
- Prise en charge du mode "Appuyer pour parler"
- Prise en charge des raccourcis personnalisés
- Fenêtre pliable
- Sélection d'un modèle dédié aux appels vocaux
- Personnalisation des instructions contextuelles

2. Méthode de configuration

1) Accédez à la page des paramètres et sélectionnez l'onglet "Fonctions vocales"
2) Dans le sous-onglet "Appel vocal" :
   - Activez la fonction d'appel vocal (activez le commutateur)
   - Cliquez sur "Choisir modèle" pour sélectionner l'IA dédiée aux appels
   - Personnalisez l'instruction contextuelle dans la zone de texte (optionnel)
   - Cliquez sur "Enregistrer" pour sauvegarder ou "Réinitialiser" pour restaurer l'instruction par défaut

3. Mode d'utilisation

1) Dans l'interface de chat, cliquez sur l'icône d'appel vocal à droite de la zone de saisie
2) La fenêtre d'appel vocal s'ouvre avec un message vocal de bienvenue
3) Maintenez enfoncé le bouton "Appuyer pour parler" (ou utilisez le raccourci)
4) Relâchez pour envoyer l'enregistrement à l'IA
5) L'IA génère une réponse jouée via TTS
6) Commandes disponibles :
   - Bouton Muet : Contrôle la sortie TTS
   - Bouton Pause/Reprendre : Interrompt ou continue la conversation
   - Bouton Paramètres : Configure les raccourcis
   - Bouton Réduire : Réduit la fenêtre à la ligne "Appuyer pour parler"
7) Cliquez sur Fermer pour terminer l'appel

4. Configuration des raccourcis

1) Dans la fenêtre d'appel vocal, cliquez sur Paramètres
2) Cliquez sur le bouton Raccourci
3) Appuyez sur la touche désirée (espace, Maj, etc.)
4) Cliquez sur "Enregistrer" pour valider
5) Utilisation : maintenez la touche pour enregistrer, relâchez pour envoyer

5. Problèmes courants et solutions

1. Problèmes liés au TTS

- Problème : Pas de sortie audio
  Solution : Vérifiez l'activation du TTS, le service sélectionné et les paramètres requis

- Problème : Mauvaise qualité audio
  Solution : Essayez un autre service TTS ou une autre voix

- Problème : Message d'erreur pendant la lecture
  Solution : Vérifiez la clé API et la connexion internet

2. Problèmes liés à l'ASR

- Problème : Aucune reconnaissance vocale
  Solution : Vérifiez l'activation de l'ASR, le service sélectionné et les paramètres requis

- Problème : Mauvaise précision de reconnaissance
  Solution : Essayez un autre service ASR ou ajustez la position du microphone

- Problème : Échec de connexion au serveur
  Solution : Vérifiez l'état du serveur local ou redémarrez l'application

3. Problèmes d'appel vocal

- Problème : Impossible d'ouvrir la fenêtre
  Solution : Vérifiez l'activation et la configuration correcte du TTS/ASR

- Problème : Pas de réponse au mode "Appuyer pour parler"
  Solution : Vérifiez les autorisations microphone ou relancez l'appel

- Problème : Aucune réponse vocale de l'IA
  Solution : Vérifiez l'activation du TTS et l'état du muet

6. Paramètres avancés

1. Paramètres TTS avancés

- Filtrage : Exclut processus de réflexion, Markdown et blocs de code
- Barre de progression : Active/désactive son affichage
- Voix et modèles personnalisés : Ajout d'options supplémentaires

2. Paramètres ASR avancés

- Démarrage automatique : Lance le serveur ASR au démarrage
- Sélection de langue : Choisit la langue de reconnaissance

3. Paramètres d'appel vocal avancés

- Instructions contextuelles personnalisées : Guide le comportement de l'IA
- Modèle dédié : Sélectionne une IA spécifique pour les appels
- Raccourcis personnalisés : Personnalise les touches d'enregistrement

7. Recommandations d'utilisation

1. Choisissez un service TTS adapté :
   - Haute qualité : OpenAI ou Siliconflow
   - Simplicité : TTS navigateur ou TTS en ligne gratuit

2. Choisissez un service ASR adapté :
   - Haute précision : OpenAI
   - Simplicité : Reconnaissance navigateur

3. Optimisez l'expérience d'appel :
   - Utilisez un casque pour éviter l'écho
   - Privilégiez les environnements calmes
   - Personnalisez les instructions contextuelles pour des réponses vocales optimales

4. Adaptez la configuration à vos besoins :
   - Communication textuelle : Activez uniquement TTS
   - Saisie vocale : Activez uniquement ASR
   - Conversation complète : Activez la fonction d'appel vocal

Nous espérons que ce guide vous aidera à exploiter pleinement les fonctionnalités vocales de Cherry Studio pour une interaction IA fluide et naturelle !
```