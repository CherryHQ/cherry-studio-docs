# Fournisseurs Personnalisés


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




Cherry Studio intègre non seulement les principaux services de modèles IA, mais vous offre également une puissante capacité de personnalisation. Grâce à la fonctionnalité **Fournisseurs IA personnalisés**, vous pouvez facilement connecter n'importe quel modèle IA dont vous avez besoin.

## Pourquoi utiliser des fournisseurs IA personnalisés ?

* **Flexibilité :** Libérez-vous des listes prédéfinies de fournisseurs et choisissez librement les modèles IA les mieux adaptés à vos besoins.
* **Diversité :** Expérimentez avec divers modèles IA de différentes plateformes pour découvrir leurs avantages uniques.
* **Contrôle :** Gérez directement vos clés API et adresses d'accès pour garantir sécurité et confidentialité.
* **Personnalisation :** Intégrez des modèles déployés en privé pour répondre à des besoins métiers spécifiques.

## Comment ajouter un fournisseur IA personnalisé ?

En quelques étapes simples, ajoutez votre fournisseur IA personnalisé dans Cherry Studio :

<figure><img src="../../.gitbook/assets/image (2) (5).png" alt=""><figcaption></figcaption></figure>

1. **Ouvrez les paramètres :** Dans la barre de navigation gauche de Cherry Studio, cliquez sur "Paramètres" (icône d'engrenage).
2. **Accédez aux services de modèles :** Dans la page des paramètres, sélectionnez l'onglet "Services de modèles".
3. **Ajoutez un fournisseur :** Sur la page "Services de modèles", vous verrez la liste des fournisseurs existants. Cliquez sur le bouton "+ Ajouter" en bas de la liste pour ouvrir la fenêtre modale "Ajouter un fournisseur".
4. **Renseignez les informations :** Dans la fenêtre modale, fournissez les détails suivants :
   * **Nom du fournisseur :** Attribuez un nom identifiable (ex : MyCustomOpenAI).
   * **Type de fournisseur :** Sélectionnez le type dans la liste déroulante. Options actuelles :
     * OpenAI
     * Gemini
     * Anthropic
     * Azure OpenAI
5. **Enregistrez la configuration :** Après renseignement, cliquez sur "Ajouter" pour sauvegarder.

## Configuration d'un fournisseur IA personnalisé

<figure><img src="../../.gitbook/assets/image (3) (5) (1).png" alt=""><figcaption></figcaption></figure>

Après l'ajout, localisez votre fournisseur dans la liste et configurez-le en détail :

1. **Statut d'activation :** Un interrupteur à droite de la liste active/désactive le service.
2. **Clé API :**
   * Saisissez la clé API fournie par votre service IA.
   * Cliquez sur "Vérifier" pour valider la clé.
3. **Adresse API :**
   * Indiquez l'URL de base d'accès à l'API.
   * Consultez impérativement la documentation officielle pour l'URL correcte.
4. **Gestion des modèles :**
   * Cliquez sur "+ Ajouter" pour saisir manuellement les ID de modèles (ex: `gpt-3.5-turbo`, `gemini-pro`).

    <figure><img src="../../.gitbook/assets/image (4) (5).png" alt=""><figcaption></figcaption></figure>
   * Référez-vous à la documentation officielle pour les noms exacts.
   * Utilisez "Gérer" pour modifier ou supprimer des modèles existants.

## Commencer à utiliser

Après configuration, sélectionnez votre fournisseur IA personnalisé dans l'interface de chat de Cherry Studio pour dialoguer avec l'IA !

## Utiliser vLLM comme fournisseur IA personnalisé

vLLM est une bibliothèque d'inférence LLM rapide et simple, similaire à Ollama. Voici comment l'intégrer à Cherry Studio :

1. **Installez vLLM :** Suivez la documentation officielle ([https://docs.vllm.ai/en/latest/getting_started/quickstart.html](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)).

    ```sh
    pip install vllm # avec pip
    uv pip install vllm # avec uv
    ```
2. **Démarrez le service vLLM :** Lancez le service via l'API compatible OpenAI. Deux méthodes principales :

    * Via `vllm.entrypoints.openai.api_server`

    ```sh
    python -m vllm.entrypoints.openai.api_server --model gpt2
    ```

    * Via `uvicorn`

    ```sh
    vllm --model gpt2 --served-model-name gpt2
    ```

Le service écoute par défaut sur le port `8000`. Utilisez `--port` pour spécifier un autre port.

3. **Ajoutez vLLM dans Cherry Studio :**
   * Ajoutez un nouveau fournisseur IA personnalisé.
   * **Nom :** `vLLM`
   * **Type :** Sélectionnez `OpenAI`.
4. **Configurez vLLM :**
   * **Clé API :** Laissez vide ou saisissez n'importe quoi (non requise).
   * **Adresse API :** `http://localhost:8000/` (ajustez le port si nécessaire).
   * **Gestion des modèles :** Saisissez le nom du modèle chargé (ex: `gpt2`).
5. **Démarrez les conversations :** Sélectionnez vLLM et le modèle (ex: `gpt2`) pour dialoguer !

## Conseils et astuces

* **Documentation :** Consultez toujours la documentation officielle pour les clés API, URL et noms de modèles.
* **Vérifiez les clés :** Utilisez le bouton "Vérifier" pour valider les clés API.
* **URL précises :** Les adresses API varient selon les services - soyez rigoureux.
* **Modèles ciblés :** Ajoutez uniquement les modèles utiles pour éviter l'encombrement.