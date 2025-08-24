---
hidden: True
icon: phone-arrow-up-right
---
# Fonctionnalités vocales


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




{% hint style="warning" %}
Cette fonctionnalité est mise en suspens car le développeur concerné n'a pas poursuivi la maintenance de la PR.
{% endhint %}

Guide d'utilisation des fonctionnalités vocales de Cherry Studio

## I. Aperçu des fonctionnalités vocales

Cherry Studio propose trois modules vocaux principaux : TTS (synthèse vocale), ASR (reconnaissance vocale) et appel vocal. Ces options vous permettent d'interagir naturellement avec l'IA via la voix, améliorant ainsi votre expérience utilisateur.

- **TTS (Text-to-Speech)** : Convertit les réponses textuelles de l'IA en sortie vocale
- **ASR (Automatic Speech Recognition)** : Convertit votre voix en saisie textuelle
- **Appel vocal** : Combine TTS et ASR pour une expérience de conversation similaire à ChatGPT

## II. Fonction TTS (Synthèse vocale)

### 1. Services pris en charge

Cherry Studio prend en charge quatre types de services TTS :

- **OpenAI** : Utilise l'API TTS d'OpenAI, nécessite une clé API
- **TTS navigateur** : Utilise la synthèse vocale intégrée au navigateur, gratuit sans configuration
- **Siliconflow** : Utilise le service TTS de Siliconflow, nécessite une clé API
- **TTS en ligne gratuit** : Service TTS gratuit, ne nécessite pas de clé API

### 2. Configuration

1. Accédez à la page Paramètres, onglet "Fonctionnalités vocales"
2. Sous l'onglet "TTS" :
   - Activez la fonction TTS (bascule ON)
   - Sélectionnez le type de service TTS
   - Configurez les paramètres selon le service choisi :
     - **OpenAI** : Saisissez la clé API, l'adresse API, choisissez la voix et le modèle
     - **TTS navigateur** : Sélectionnez la voix
     - **Siliconflow** : Saisissez la clé API, l'adresse API, choisissez la voix, le modèle, le format de réponse et la vitesse
     - **TTS en ligne gratuit** : Sélectionnez la voix et le format de sortie
3. Configurez les options de filtrage TTS (optionnel) :
   - Filtrer les processus de réflexion
   - Filtrer le balisage Markdown
   - Filtrer les blocs de code
4. Définissez si vous souhaitez afficher la barre de progression TTS
5. Cliquez sur "Tester TTS" pour vérifier la configuration

### 3. Utilisation

- Une fois activé, les réponses de l'IA sont automatiquement converties en parole
- Sous chaque réponse IA dans l'interface de chat, un bouton de lecture TTS apparaît
- Cliquez pour lire/mettre en pause
- Si activée, la barre de progression s'affiche sous le texte
- Les textes longs sont synthétisés en segments et lus en continu

## III. Fonction ASR (Reconnaissance vocale)

### 1. Services pris en charge

- **OpenAI** : Utilise le modèle Whisper d'OpenAI, nécessite une clé API
- **Navigateur** : Reconnaissance vocale intégrée, gratuit sans configuration
- **Serveur local** : Connexion à un serveur WebSocket local

### 2. Configuration

1. Page Paramètres > Onglet "Fonctionnalités vocales"
2. Sous l'onglet "ASR" :
   - Activez l'ASR (bascule ON)
   - Sélectionnez le type de service
   - Configurez selon le service :
     - **OpenAI** : Clé API, adresse API, modèle
     - **Navigateur** : Aucune configuration supplémentaire
     - **Serveur local** : Option de démarrage automatique au lancement
   - Sélectionnez la langue de reconnaissance (par défaut : chinois)
3. Cliquez sur "Tester ASR" pour vérifier

### 3. Utilisation

- Bouton microphone apparaît près de la zone de saisie
- Cliquez pour démarrer l'enregistrement
- La parole est convertie en texte dans la zone de saisie
- Re-cliquez pour terminer
- Prise en charge de la reconnaissance continue multi-phrases

## IV. Fonction d'appel vocal

### 1. Caractéristiques

- Interface fenêtrée déplaçable
- Mode "Maintenir pour parler"
- Raccourcis personnalisables
- Fenêtre pliable
- Modèle dédié sélectionnable
- Instructions personnalisables

### 2. Configuration

1. Page Paramètres > Onglet "Fonctionnalités vocales"
2. Sous l'onglet "Appel vocal" :
   - Activez la fonction (bascule ON)
   - Cliquez "Choisir modèle" pour sélectionner le modèle IA
   - Personnalisez les instructions (optionnel)
   - Cliquez "Enregistrer" ou "Réinitialiser"

### 3. Utilisation

1. Cliquez l'icône téléphone dans l'interface de chat
2. La fenêtre d'appel s'ouvre avec un message vocal de bienvenue
3. Maintenez le bouton "Maintenir pour parler" (ou utilisez le raccourci)
4. Relâchez pour envoyer
5. L'IA répond via TTS
6. Boutons de contrôle :
   - **Muet** : Contrôle la sortie TTS
   - **Pause/Reprendre** : Interrompt la conversation
   - **Paramètres** : Configure les raccourcis
   - **Réduire** : Minimise la fenêtre
7. Fermez avec le bouton ×

### 4. Configuration des raccourcis

1. Dans la fenêtre d'appel, cliquez ⚙️ > Bouton Raccourcis
2. Appuyez sur la touche souhaitée (espace, maj, etc.)
3. Cliquez "Enregistrer"
4. Maintenez la touche pour parler, relâchez pour envoyer

## V. FAQ et solutions

### 1. Problèmes TTS

- **Aucun son** : Vérifiez l'activation, le service et les paramètres
- **Mauvaise qualité** : Essayez un autre service ou voix
- **Messages d'erreur** : Vérifiez clé API et connexion internet

### 2. Problèmes ASR

- **Aucune reconnaissance** : Vérifiez activation, service et paramètres
- **Faible précision** : Essayez un autre service ou ajustez le microphone
- **Échec connexion serveur** : Vérifiez le serveur local ou redémarrez

### 3. Problèmes d'appel vocal

- **Fenêtre ne s'ouvre pas** : Vérifiez activation, configuration TTS/ASR
- **Pas de réponse au maintien** : Vérifiez permissions micro ou redémarrez
- **Pas de sortie vocale** : Vérifiez activation TTS et option muet

## VI. Paramètres avancés

### 1. Options TTS avancées
- Filtres : processus de réflexion, Markdown, blocs de code
- Barre de progression
- Voix et modèles personnalisables

### 2. Options ASR avancées
- Démarrage automatique du serveur
- Sélection de la langue

### 3. Options d'appel vocal avancées
- Instructions personnalisées
- Modèle dédié sélectionnable
- Raccourcis personnalisables

## VII. Conseils d'utilisation

1. **Choisir un service TTS** :
   - Qualité élevée : OpenAI ou Siliconflow
   - Sans configuration : TTS navigateur ou en ligne gratuit

2. **Choisir un service ASR** :
   - Haute précision : OpenAI
   - Sans configuration : navigateur

3. **Optimiser l'appel vocal** :
   - Utilisez un casque pour éviter la rétroaction
   - Environnement calme pour une meilleure reconnaissance
   - Instructions personnalisées pour des réponses adaptées

4. **Ajustements selon les besoins** :
   - Principalement texte : activez uniquement TTS
   - Principalement voix : activez uniquement ASR
   - Dialogue complet : activez l'appel vocal

Profitez de l'expérience d'interaction naturelle avec les fonctionnalités vocales de Cherry Studio !