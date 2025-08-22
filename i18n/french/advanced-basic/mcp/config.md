# Configuration et utilisation du MCP


{% hint style="warning" %}
Ce document a été traducido del chino por IA y aún no ha sido revisado.
{% endhint %}




<figure><img src="../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1.  Ouvrez les paramètres de Cherry Studio.
2.  Trouvez l'option `MCP 服务器`.
3.  Cliquez sur `添加服务器`.
4.  Remplissez les paramètres correspondants du MCP Server ([lien de référence](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)). Les éléments à remplir peuvent inclure :
    *   Nom : personnalisez un nom, par exemple `fetch-server`
    *   Type : sélectionnez `STDIO`
    *   Commande : entrez `uvx`
    *   Arguments : entrez `mcp-server-fetch`
    *   (Il peut y avoir d'autres paramètres selon le serveur spécifique)
5.  Cliquez sur `保存`.

{% hint style="success" %}
Après avoir terminé cette configuration, Cherry Studio téléchargera automatiquement le MCP Server requis - `fetch server`. Une fois le téléchargement terminé, vous pourrez commencer à l'utiliser ! Remarque : en cas d'échec de la configuration de mcp-server-fetch, essayez de redémarrer votre ordinateur.
{% endhint %}

### Activer le service MCP dans la boîte de discussion

<figure><img src="../../.gitbook/assets/MCP-输入框按钮示例.png" alt=""><figcaption></figcaption></figure>

*   Un serveur MCP a été ajouté avec succès dans les paramètres `MCP 服务器`

<figure><img src="../../.gitbook/assets/MCP服务器示例.png" alt=""><figcaption></figcaption></figure>

### **Démonstration des effets d'utilisation**

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Comme le montre l'image ci-dessus, en combinant la fonction `fetch` du MCP, Cherry Studio peut mieux comprendre l'intention de la requête utilisateur, récupérer des informations pertinentes sur Internet et fournir des réponses plus précises et complètes.