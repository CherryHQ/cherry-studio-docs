# Configuration et utilisation du MCP


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Ouvrez les paramètres de Cherry Studio.
2. Trouvez l'option `Serveur MCP`.
3. Cliquez sur `Ajouter un serveur`.
4. Remplissez les paramètres du serveur MCP ([lien de référence](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Les informations à fournir peuvent inclure :
   * Nom : un nom personnalisé, par exemple `fetch-server`
   * Type : sélectionnez `STDIO`
   * Commande : entrez `uvx`
   * Arguments : entrez `mcp-server-fetch`
   * (d'autres paramètres peuvent exister selon le serveur spécifique)
5. Cliquez sur `Enregistrer`.

{% hint style="success" %}
Après cette configuration, Cherry Studio téléchargera automatiquement le serveur MCP requis - `fetch server`. Une fois le téléchargement terminé, vous pouvez commencer à l'utiliser ! Remarque : si la configuration de mcp-server-fetch échoue, essayez de redémarrer votre ordinateur.
{% endhint %}

### Activer le service MCP dans la boîte de discussion

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Le serveur MCP a été ajouté avec succès dans les paramètres

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Démonstration de l'effet d'utilisation**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Comme le montre l'image ci-dessus, grâce à la fonction `fetch` intégrée au MCP, Cherry Studio peut mieux comprendre l'intention des requêtes utilisateur, récupérer des informations pertinentes sur Internet et fournir des réponses plus précises et complètes.