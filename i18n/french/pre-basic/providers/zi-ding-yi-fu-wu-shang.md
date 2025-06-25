# Fournisseurs personnalisés

{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

## Fournisseurs Personnalisés

Cherry Studio intègre non seulement les principaux services de modèles d'IA, mais vous offre également une puissante capacité de personnalisation. Grâce à la fonctionnalité **Fournisseurs d'IA personnalisés**, vous pouvez facilement intégrer n'importe quel modèle d'IA dont vous avez besoin.

### Pourquoi avez-vous besoin d'un fournisseur d'IA personnalisé ?

* **Flexibilité :** Libérez-vous des limites des listes prédéfinies de fournisseurs, choisissez librement le modèle d'IA qui correspond le mieux à vos besoins.
* **Diversité :** Essayez divers modèles d'IA de différentes plateformes, découvrez leurs avantages uniques.
* **Contrôle :** Gérez directement vos clés API et adresses d'accès pour garantir la sécurité et la confidentialité.
* **Personnalisation :** Intégrez des modèles déployés en privé pour répondre aux besoins de scénarios métiers spécifiques.

### Comment ajouter un fournisseur d'IA personnalisé ?

En quelques étapes simples, vous pouvez ajouter votre fournisseur d'IA personnalisé à Cherry Studio :

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Ouvrir les paramètres :** Dans la barre de navigation de gauche de l'interface Cherry Studio, cliquez sur "Paramètres" (icône d'engrenage).
2. **Accéder aux services de modèles :** Dans la page des paramètres, sélectionnez l'onglet "Services de modèles".
3. **Ajouter un fournisseur :** Sur la page "Services de modèles", vous verrez la liste des fournisseurs existants. Cliquez sur le bouton "+ Ajouter" sous la liste pour ouvrir la fenêtre contextuelle "Ajouter un fournisseur".
4. **Remplir les informations :** Dans la fenêtre contextuelle, vous devez remplir les informations suivantes :
   * **Nom du fournisseur :** Attribuez un nom facilement identifiable à votre fournisseur personnalisé (exemple : MyCustomOpenAI).
   * **Type de fournisseur :** Sélectionnez le type de votre fournisseur dans la liste déroulante. Actuellement pris en charge :
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Enregistrer la configuration :** Après avoir rempli les informations, cliquez sur le bouton "Ajouter" pour sauvegarder votre configuration.

### Configurer un fournisseur d'IA personnalisé

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Après l'ajout, vous devez trouver le fournisseur que vous venez d'ajouter dans la liste et effectuer une configuration détaillée :

1. **État d'activation :** À l'extrémité droite de la liste des fournisseurs personnalisés se trouve un interrupteur d'activation. L'activer signifie que ce service personnalisé est activé.
2. **Clé API :**
   * Saisissez la clé API (API Key) fournie par votre fournisseur de services d'IA.
   * Cliquez sur le bouton "Vérifier" à droite pour vérifier la validité de la clé.
3. **Adresse API :**
   * Renseignez l'adresse d'accès API (Base URL) du service d'IA.
   * Veuillez consulter la documentation officielle de votre fournisseur d'IA pour obtenir l'adresse API correcte.
4.  **Gestion des modèles :**

    * Cliquez sur le bouton "+ Ajouter" pour ajouter manuellement l'ID du modèle que vous souhaitez utiliser sous ce fournisseur. Par exemple `gpt-3.5-turbo`, `gemini-pro`, etc.

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    \* Si vous n'êtes pas sûr du nom exact du modèle, référez-vous à la documentation officielle de votre fournisseur d'IA.\
    \* Cliquez sur le bouton "Gérer" pour modifier ou supprimer les modèles déjà ajoutés.

### Commencer à utiliser

Une fois la configuration ci-dessus terminée, vous pouvez sélectionner votre fournisseur d'IA personnalisé et votre modèle dans l'interface de chat de Cherry Studio pour commencer à dialoguer avec l'IA !

### Utiliser vLLM comme fournisseur d'IA personnalisé

vLLM est une bibliothèque d'inférence LLM rapide et facile à utiliser, similaire à Ollama. Voici comment l'intégrer à Cherry Studio :

1.  **Installer vLLM :** Suivez la documentation officielle de vLLM ([https://docs.vllm.ai/en/latest/getting\_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)) pour l'installer.

    ```sh
    pip install vllm # si vous utilisez pip
    uv pip install vllm # si vous utilisez uv
    ```
2.  **Lancer le service vLLM :** Démarrez le service en utilisant l'interface compatible OpenAI fournie par vLLM. Deux méthodes principales sont disponibles :

    * Lancer via `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Lancer via `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Assurez-vous que le service démarre avec succès et qu'il écoute sur le port par défaut `8000`. Vous pouvez également spécifier le port du service vLLM avec le paramètre `--port`.

3. **Ajouter le fournisseur vLLM dans Cherry Studio :**
   * Suivez les étapes décrites précédemment pour ajouter un nouveau fournisseur d'IA personnalisé.
   * **Nom du fournisseur :** `vLLM`
   * **Type de fournisseur :** Sélectionnez `OpenAI`.
4. **Configurer le fournisseur vLLM :**
   * **Clé API :** vLLM ne nécessitant pas de clé API, vous pouvez laisser ce champ vide ou saisir n'importe quel contenu.
   * **Adresse API :** Renseignez l'adresse API du service vLLM. Par défaut, l'adresse est : `http://localhost:8000/` (si un port différent est utilisé, modifiez-le en conséquence).
   * **Gestion des modèles :** Ajoutez le nom du modèle que vous avez chargé dans vLLM. Dans l'exemple `python -m vllm.entrypoints.openai.api_server --model gpt2`, vous devez saisir `gpt2`.
5. **Commencer à dialoguer :** Vous pouvez désormais sélectionner le fournisseur vLLM et le modèle `gpt2` dans Cherry Studio pour dialoguer avec le LLM alimenté par vLLM !

### Astuces et conseils

* **Lire attentivement la documentation :** Avant d'ajouter un fournisseur personnalisé, lisez attentivement la documentation officielle de votre fournisseur d'IA pour connaître les informations clés telles que la clé API, l'adresse d'accès et les noms de modèles.
* **Vérifier la clé API :** Utilisez le bouton "Vérifier" pour confirmer rapidement la validité de votre clé API et éviter les erreurs.
* **Attention à l'adresse API :** L'adresse API peut varier selon les fournisseurs et modèles d'IA, assurez-vous de saisir l'adresse correcte.
* **Ajouter les modèles selon les besoins :** N'ajoutez que les modèles que vous utiliserez réellement, évitez d'en ajouter trop inutilement.
