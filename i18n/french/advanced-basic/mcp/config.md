
{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}

# Configuration et utilisation du MCP

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

1. Ouvrez les paramètres de Cherry Studio.
2. Trouvez l'option `MCP 服务器`.
3. Cliquez sur `添加服务器`.
4. Remplissez les paramètres du MCP Server ([lien de référence](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Les éléments à remplir peuvent inclure :
   * Nom : personnalisez un nom, par exemple `fetch-server`
   * Type : sélectionnez `STDIO`
   * Commande : remplissez `uvx`
   * Arguments : remplissez `mcp-server-fetch`
   * (Il peut y avoir d'autres paramètres selon le serveur spécifique)
5. Cliquez sur `保存`.

{% hint style="success" %}
Après cette configuration, Cherry Studio téléchargera automatiquement le MCP Server requis - `fetch server`. Une fois le téléchargement terminé, vous pouvez commencer à l'utiliser ! Note : si la configuration de mcp-server-fetch échoue, essayez de redémarrer votre ordinateur.
{% endhint %}

### Activation du service MCP dans la zone de discussion

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

* Ajout réussi d'un serveur MCP dans les paramètres `MCP 服务器`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Démonstration des effets**

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Comme le montre l'image ci-dessus, en combinant la fonction `fetch` du MCP, Cherry Studio comprend mieux l'intention de la requête utilisateur. Il récupère des informations pertinentes sur le Web et fournit des réponses plus précises et complètes.