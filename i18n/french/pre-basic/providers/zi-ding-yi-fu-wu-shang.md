
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Fournisseurs personnalisés

Cherry Studio intègre non seulement les principaux services de modèles IA, mais vous offre également une puissante capacité de personnalisation. Grâce à la fonctionnalité **Fournisseurs IA personnalisés**, vous pouvez facilement connecter tout modèle IA dont vous avez besoin.

## Pourquoi utiliser des fournisseurs IA personnalisés ?

* **Flexibilité :** Ne plus être limité par la liste préconfigurée des fournisseurs, choisissez librement le modèle IA le plus adapté à vos besoins.
* **Diversité :** Essayez divers modèles IA de différentes plateformes pour découvrir leurs avantages uniques.
* **Contrôle :** Gérez directement vos clés API et adresses d'accès, garantissant sécurité et confidentialité.
* **Personnalisation :** Intégrez des modèles déployés en privé pour répondre à des besoins métiers spécifiques.

## Comment ajouter un fournisseur IA personnalisé ?

En quelques étapes simples, ajoutez votre fournisseur IA personnalisé dans Cherry Studio :

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Ouvrir les paramètres :** Dans la barre de navigation gauche de Cherry Studio, cliquez sur "Paramètres" (icône d'engrenage).
2. **Accéder aux services de modèles :** Dans la page des paramètres, sélectionnez l'onglet "Services de modèles".
3. **Ajouter un fournisseur :** Sur la page "Services de modèles", vous verrez la liste des fournisseurs existants. Cliquez sur le bouton "+ Ajouter" en bas de liste pour ouvrir la fenêtre "Ajouter un fournisseur".
4. **Remplir les informations :** Dans la fenêtre, renseignez :
   * **Nom du fournisseur :** Donnez un nom reconnaissable à votre fournisseur (ex: MonOpenAIPersonnel).
   * **Type de fournisseur :** Sélectionnez le type dans la liste déroulante. Types actuellement pris en charge :
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Enregistrer la configuration :** Après remplissage, cliquez sur "Ajouter" pour sauvegarder.

## Configurer le fournisseur IA personnalisé

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Après l'ajout, trouvez votre fournisseur dans la liste et configurez-le en détail :

1. **Statut d'activation :** Sur l'extrême droite de la liste, un interrupteur active/désactive le service personnalisé.
2. **Clé API :**
   * Saisissez votre clé API fournie par le service IA.
   * Cliquez sur "Vérifier" à droite pour tester la validité de la clé.
3. **Adresse API :**
   * Entrez l'URL d'accès de base du service API.
   * Consultez toujours la documentation officielle pour obtenir l'URL correcte.
4. **Gestion des modèles :**
   * Cliquez sur "+ Ajouter" pour saisir manuellement les ID des modèles à utiliser (ex : `gpt-3.5-turbo`, `gemini-pro`).

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>

    * Si les noms exacts sont inconnus, reportez-vous à la documentation officielle.
    * Utilisez "Gérer" pour modifier ou supprimer les modèles ajoutés.

## Commencer à utiliser

Après configuration, sélectionnez votre fournisseur IA personnalisé et son modèle dans l'interface de discussion de Cherry Studio pour démarrer vos conversations !

## Utiliser vLLM comme fournisseur IA personnalisé

vLLM est une bibliothèque d'inférence LLM rapide et simple, similaire à Ollama. Voici comment l'intégrer :

1. **Installer vLLM :** Suivez la documentation officielle ([https://docs.vllm.ai/en/latest/getting\_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # avec pip
    uv pip install vllm # avec uv
    ```
2. **Démarrer vLLM :** Lancez le service avec l'API compatible OpenAI. Deux méthodes :

    * Avec `vllm.entrypoints.openai.api_server`:

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Avec `uvicorn`:

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

    Le service écoute par défaut sur le port `8000`. Utilisez `--port` pour changer le port.

3. **Ajouter vLLM dans Cherry Studio :**
   * Ajoutez un nouveau fournisseur comme précédemment.
   * **Nom :** `vLLM`
   * **Type :** Sélectionnez `OpenAI`.
4. **Configurer vLLM :**
   * **Clé API :** Laissez vide ou saisissez n'importe quelle valeur (inutilisée).
   * **Adresse API :** `http://localhost:8000/` (ou port personnalisé).
   * **Modèles :** Ajoutez le nom du modèle chargé (ex: `gpt2`).
5. **Démarrer les conversations :** Sélectionnez vLLM et son modèle (ex: `gpt2`) pour interagir !

## Astuces et conseils

* **Lisez la documentation :** Consultez toujours la documentation du fournisseur pour les clés API, URL et noms de modèles.
* **Vérifiez la clé API :** Utilisez le bouton de vérification pour éviter les erreurs.
* **Attention à l'URL API :** Vérifiez l'exactitude de l'adresse.
* **Ajout ciblé des modèles :** N'ajoutez que les modèles réellement utilisés pour optimiser les performances.