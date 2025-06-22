
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuration et utilisation de MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Ouvrez les paramètres de Cherry Studio.
2. Trouvez l'option `Serveur MCP`.
3. Cliquez sur `Ajouter un serveur`.
4. Remplissez les paramètres du serveur MCP ([lien de référence](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Les éléments à remplir peuvent inclure :
   * **Nom** : Un nom personnalisé, par exemple `fetch-server`
   * **Type** : Sélectionnez `STDIO`
   * **Commande** : Saisissez `uvx`
   * **Paramètres** : Saisissez `mcp-server-fetch`
   * (Peut inclure d'autres paramètres selon le serveur spécifique)
5. Cliquez sur `Sauvegarder`.

{% hint style="success" %}
Après avoir effectué cette configuration, Cherry Studio téléchargera automatiquement le serveur MCP requis - `fetch server`. Une fois le téléchargement terminé, vous pourrez commencer à l'utiliser ! Remarque : Si la configuration de mcp-server-fetch échoue, essayez de redémarrer votre ordinateur.
{% endhint %}

### Activer le service MCP dans la zone de discussion

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Le serveur MCP a été ajouté avec succès dans les paramètres `Serveur MCP`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Démonstration de l'effet**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Comme le montre l'image ci-dessus, après avoir intégré la fonction `fetch` de MCP, Cherry Studio peut mieux comprendre l'intention de la requête de l'utilisateur, obtenir des informations pertinentes sur Internet et fournir des réponses plus précises et complètes.